from datetime import date, time
import datetime
import re
from sqlalchemy.sql import exists
from sqlalchemy import create_engine, engine, Column, Integer, String, ForeignKey, Table,TIMESTAMP
from sqlalchemy.log import echo_property
from sqlalchemy.orm import relationship, sessionmaker, relationships
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import column
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from numpy import savetxt


engine = create_engine('postgres://postgres:postgres@localhost:5432/examDB', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

START_DATE = '2020-12-10'
end_date_temp = datetime.now() - timedelta(days=1)
END_DATE = end_date_temp.strftime('%Y-%m-%d')

Base = declarative_base()




class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String(10), primary_key=True)
    name = Column(String(50))
    children = relationship('Price_Records')
    

class Price_Records(Base):
    __tablename__ = 'price_records'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    stock_ticker = Column(String(10), ForeignKey('stocks.ticker'))
    date_id = Column(Integer, ForeignKey('dates.id'))
    child = relationship("Date")


class Date(Base):
    __tablename__ = 'dates'
    id = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP)



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Names = ['AMC', 'PLTR', 'FORD', 'RIDE', 'SPCE', 'AI', 'TSLA','GameStop Corp.', 'Apple Inc.', 'General Electric Company', 'Nokia Corporation']
Stocks = ['AMC', 'PLTR', 'FORD', 'RIDE', 'SPCE', 'AI', 'TSLA', 'GME', 'AAPL', 'GE', 'NOK']


def get_data(ticker, name):
    try:
        stock_data = data.DataReader(ticker,'yahoo', START_DATE, END_DATE)
        stock = clean_data(stock_data, 'Adj Close')
        save_data(stock, name, ticker)
        
    except KeyError:
        print('Key Error in {t}'.format(t=ticker))
    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))


def clean_data(stock_data, col):
    weekdays = pd.date_range(start=START_DATE, end= END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    print(clean_data.fillna(method='ffill'))
    return clean_data.fillna(method='ffill')

def save_data(stockprices, stock_name ,stock_ticker):
    stock = Stock(ticker=stock_ticker, name=stock_name)
    for i in range(0, len(stockprices)):
        #if stockprices[i] > 0:
        record = Price_Records(price=stockprices[i])
        if session.query(exists().where(Date.date == stockprices.index[i])).scalar() == False:
            date = Date(date=stockprices.index[i])
            record.child = date
        else:
            record = Price_Records(price=stockprices[i],date_id = i+1)
        stock.children.append(record)

        session.add(stock)
        session.commit()
            



    

for i in range(0, len(Stocks)):

    get_data(Stocks[i], Names[i])


