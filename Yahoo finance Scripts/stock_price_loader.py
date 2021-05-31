from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, engine, Column, Integer, String, ForeignKey, Table,TIMESTAMP, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, relationships
from types import MethodType
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql.expression import join
from datetime import datetime, timedelta

engine = create_engine('postgresql://postgres:password@localhost:5432/examDB', echo=False)

Session = sessionmaker(bind=engine)
session = Session()




Base = declarative_base()

class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String(10), primary_key=True)
    name = Column(String(50))
    children = relationship('Price_Records')
    def __init__(self, ticker, name):
        self.name = name
        self.ticker = ticker

        


class Price_Records(Base):
    __tablename__ = 'price_records'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    stock_ticker = Column(String(10), ForeignKey('stocks.ticker'))
    date = Column(Date)
    def __init__(self, stock_ticker, price, date):
        self.stock_ticker = stock_ticker
        self.date = date
        self.price = price





app = Flask(__name__)
ma = Marshmallow(app)

class PriceSchema(ma.Schema):
    class Meta:
        fields = (['stock_ticker', 'price', 'date'])

prices_schema = PriceSchema(many = True)

@app.route('/prices/<string:ticker>/<string:date>')
def index(ticker, date):

    all_prices = session.query(Price_Records.price, Price_Records.date).filter(Price_Records.stock_ticker == 'GME', Price_Records.date == date).all()
    #session.query(Price_Records.price, Date.date).join(Price_Records, Date.id == Price_Records.date_id).filter(Price_Records.stock_ticker == ticker)
    #all_prices  = session.query(func.public.get_stock("GME")).all()
    print(all_prices)
    result = prices_schema.dump(all_prices)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


