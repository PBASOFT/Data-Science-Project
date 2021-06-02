from datetime import date, time
import datetime
import re
from sqlalchemy.sql import exists
from sqlalchemy import create_engine, engine, Column, Integer, String, ForeignKey, Table, Date, Float
from sqlalchemy.log import echo_property
from sqlalchemy.orm import relationship, sessionmaker, relationships
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import column, true
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from numpy import savetxt


engine = create_engine('postgres://postgres:password@localhost:5432/examDB', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

START_DATE = '2021-12-10'
end_date_temp = datetime.now() - timedelta(days=1)
END_DATE = end_date_temp.strftime('%Y-%m-%d')

Base = declarative_base()




class Stock(Base):
    __tablename__ = 'stock'
    ticker = Column(String(10), primary_key=True)
    name = Column(String(50))
    children = relationship('Price_Records')
    

class Price_Record(Base):
    __tablename__ = 'price_record'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    stock_ticker = Column(String(10), ForeignKey('stock.ticker'), index = true)
    date = Column(Date)
    



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
    #print(clean_data.fillna(method='ffill'))
    return clean_data.fillna(method='ffill')

def save_data(stockprices, stock_name ,stock_ticker):
    stock = Stock(ticker=stock_ticker, name=stock_name)
    for i in range(0, len(stockprices)):
        record = Price_Record(price = stockprices[i], date=stockprices.index[i])
        stock.children.append(record)
    session.add(stock)
    session.commit()

for i in range(0, len(Stocks)):

    get_data(Stocks[i], Names[i])


