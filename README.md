[Assignment description](https://github.com/datsoftlyngby/soft2021spring-ds/blob/main/BigProject.pdf)

*CPH Business Spring 2021*, *Sebastian Harvej* & *Malene Hansen*

# Stocks: Hype vs Market

## Stage 1: Business Case Foundation

In recent years investing has grown popular among young people. They are known to be risk seeking and to gain and share knowledge and tips online.

It seems to be common knowledge that a stock can be hyped. Meaning that the price on a stock can go up solely (or mainly) because of hype. 

We have recently seen how these investors could cause a stock to go up, against any logic, when a group of people on the social media platform Reddit decided to buy GameStop shares, for the sake of punishing hedge funds, causing the stock to skyrocket.

This is an extra ordinary example, but it makes us wonder if smaller scaled hype actually has an effect on stock prices. And if so; is that something we can predict?


### Focus of interest
Our focus is to detect **hype on social media** and to compare it to stock prices.
As our social media source for this prototype we use the online forum reddit.com, as they are known to be a popular place to discuss investing. And equally important; reddit.com provides an extensive API to access data from their website.

The correlation between hype and stock prices is interesting to investigate, not only because it might reveal a whole new dimension to stock trading evolving around social media. And posibly the overall availability of knowledge sharing made possible by the www and maybe even more by social media entering the scene. But also because that revealing a correlation also opens up for the possibility of predicting stock priceses.


#### Detecting hype

To identify hype we first have to agree on the definition of hype. We therefore looked up the meaning of hype on Cambridge Dictionary and concluded the following meaning of hype:

> "Hype: to **advertise** or praise something **a lot** in newspapers, on television, online, etc. in order to **make people excited** about it **and want to buy** or try it."
>
> -- <cite>[source](https://dictionary.cambridge.org/dictionary/english/hype)</cite>

Based on that, we decided to measure hype by the quantity of mentions combined with the sentiment of their context.



### Hyphothesis

#### Null Hypotheses
Stock prices can not be affected by hype on social media.

#### Alternative Hypotheses
There is a correlation between stock prices and hype on social media.

### Expected outcome of research
We expect to see some correlation between at least some stocks going up and how much they are mentioned/discussed on social media. 

### Who will be the user of the results
Knowledge is money. We our selves will be the users of the results and hopefully we'll discover something new and exiting. And we will then be on the path to becoming the richest people on earth.


## Stage 2: Business Data Storytelling

### Data Sources


#### Yahoo Finance

We get stock prices using Yajoo finance to price data for stocks, we are then cleaning the close price for null vales by giving them the value of the the day before, the date and close price of the stock is saved to a database.![image](https://user-images.githubusercontent.com/16530705/120631424-27e69d80-c468-11eb-8978-d0b1b457dbd6.png)

#### Reddit.com

We are collecting post and comments from the following subreddit forums:

  - r/wallstreetbets (10.1 million users)
  - r/Stocks (2.6 million users)
  - r/Investing (1.8 million users)
  - r/pennystocks (1.6 million users)
  - r/StockMarket (1.5 million users)
  - r/algotrading (1.2 million users)
  - r/Robinhood (742.000 users)
 

  
  *The subreddit "wallstreetbets" became world famous following the gamestop surge initiated by its users. With the fame it grew tremendously and counts more than 10 million users as of today. The jargon is juvenile and rebellious and it has become infamous for encouraging aggressive trading strategies.
  The other subreddits consider seem to consider themselves to be of a "more serious" character than wallstreet bets. 
  All subreddits were chosen because they discuss investing and hold a great amount of users.*

We have collected the data over a period of 10 days and saved it in batches into csv files.




 #### Our Reddit data sets can be found [here](/Data_Collecting/data_files/all_data_streams/)
  
 #### Our scripts for collecting the  Reddit data can be found [here](/Data_Collecting/)


### Data Processing

To attempt to reject our Null Hypotheses we first need to measure hype our reddit data. 
The first leg of identifying stock hype is knowing the quantity of stock mentions. We therefore start by identifying stock mentions.

To do that we use Named Entity Recognition. We apply it to all comments and submissions by using a python library called spaCy, that has a pretrained pipeline that we can apply.





3.    Design a data story or data processing scenario (can be done manually on paper, but the use of software platforms is recommended).
      ****
      
      - Apple vs AAPL, GME vs GameStop
      -  bobles with orgs, visualizing most freg mentioned/most talked about orgs.
      - taking the most talked about and hold them up againtst stock prices
      ****
      
a.    decide on data processing parameters and methods

b.   choose data visualisation techniques

c.    create visual representations

d.   create dashboards

e.    create a first prototype of data story

2.    Export your solution in a file and upload it to your git repository.


#### Sentiment analyses
- Determine if contributions are positive, neutral or negative. // Buy, hold or sell?



#### Notes for further investigation

**Understanding the data:**

WSB slang: https://www.investopedia.com/wallstreetbets-slang-and-memes-5111311

**Challenges:**
- *"Only 100,000% away. Just need 10x the low point to the high point of GME squeeze to make it happen.*
   - Is not about the GME stock. It is "GME" beeing used to describe some other.
- *"GME 🚀🚀🚀 bought more this morning thanks kenny G"*
  - Is certainly about the GME stock.
- *"... Comparing it to Apple is not really a like for like comparison. If you don't understand crypto, as an investor at this point-- that's on you."*
  - Is not about Apple. Maybe it is valueable to look analyse the entities or context sorrounding the collected named entity.
- *Sentences like "den skal under 180-200" must me understood at "don't by" recommendation/negative. And "den skal op på 300 før jeg sælger" must be interpreted as a positive comment.
  - especially hard to cats, as comments like that come without a contex. Or the context must be retrieved from parent posts or parent comments.
- * Going red or going green also has a positive/negative measure


**Future improvements:**
- Maybe correlation gets better over time, when comparing several weeks or even months, to discover trends rather than each peak on the graph.
