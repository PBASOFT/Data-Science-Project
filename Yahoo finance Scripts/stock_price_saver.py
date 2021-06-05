from datetime import date, time
import datetime
import re
from sqlalchemy.sql import exists
from sqlalchemy import create_engine, engine, Column, Integer, String, ForeignKey, Table, Date, Float
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


engine = create_engine('postgres://postgres:password@localhost:5432/examDB', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

START_DATE = '2020-5-10'
end_date_temp = datetime.now() - timedelta(days=1)
#END_DATE = end_date_temp.strftime('%Y-%m-%d')
END_DATE = '2020-5-30'

Base = declarative_base()




class Stock(Base):
    __tablename__ = 'stock'
    ticker = Column(String(10), primary_key=True)
    name = Column(String(50))
    children = relationship('Price_Records')
    

class Price_Records(Base):
    __tablename__ = 'price_record'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    stock_ticker = Column(String(10), ForeignKey('stock.ticker'),index = True)
    date = Column(Date)
    



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Names = ['AMC Entertainment Holdings Inc','Gamestop','Palantir Technologies Inc','Apple','Virgin Galactic','Amazon.com','Ford Motor Company','Advanced Micro Devices','Tesla','Athabasca Oil Corp','Nokia','ITM Power plc','C3Ai Inc','Coinbase Global Inc','BlackBerry','Roblox Corp']
Stocks = ['AMC','GME','PLTR','AAPL','SPCE','AMZN','FORD','AMD','TSLA','ATH','NOK','ITM','AI','COIN','BB','RBLX']

def saveToCSV(stockprices, stock_ticker):
    stockprices.to_csv("data/" + stock_ticker + ".csv")

def get_data(ticker, name):
    try:
        stock_data = data.DataReader(ticker,'yahoo', START_DATE, END_DATE)
        stock = clean_data(stock_data, 'Adj Close')
        #save_data(stock, name, ticker)
        saveToCSV(stock, ticker)
        
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
        record = Price_Records(price = stockprices[i], date=stockprices.index[i])
        stock.children.append(record)
    session.add(stock)
    session.commit()

for i in range(0, len(Stocks)):

    get_data(Stocks[i], Names[i])





