[Assignment description](https://github.com/datsoftlyngby/soft2021spring-ds/blob/main/BigProject.pdf)

*CPH Business Spring 2021*, *Sebastian Harvej* & *Malene Hansen*

# Stocks: Hype vs Market

## Stage 1: Business Case Foundation

In recent years investing has grown popular among young people. They are known to be risk seeking and to gain and share knowledge and tips online.

It seems to be common knowledge that a stock can be hyped. Meaning that the price on a stock can go up solely (or mainly) because of hype. 

We have recently seen how these investors can cause a stock to go up, against any logic, when a group of people on the social media platform Reddit decided to buy GameStop shares, for the sake of punishing hedge funds, causing the stock to skyrocket.

This is an extra ordinary example, but it makes us wonder if smaller scaled hype actually has an effect on stock prices. And if so; is that something we can predict?

### Focus of interest
We wan't to focus on scandinavian **small cap** stocks and **hype on social media**.

Small cap stocks are known to be volatile but also to have great growth potential. They are considered "High risk/High reward", which we think is a good match to the kind of investors we expect to meet on social media platforms. We stick to scandinavian small cap stocks both to narrow the field for this project, and because that we know first hand that the culture we're looking for exists here.

> "A small cap is generally a company with a market capitalization of between $300 million and $2 billion. The advantage of investing in small cap stocks is the opportunity to beat institutional investors through growth opportunities."
>
> -- <cite>[source](https://www.investopedia.com/terms/s/small-cap.asp)</cite>


> "hype: to advertise or praise something a lot in newspapers, on television, online, etc. in order to make people excited about it and want to buy or try it."
>
> -- <cite>[source](https://dictionary.cambridge.org/dictionary/english/hype)</cite>



It is interesting to investigate the correlation between hype and stock prices, not only because it might reveal a whole new dimension to stock trading evolving around social media, and posibly the overall availability of knowledge sharing made possible by the www and maybe even more by social media entering the scene. But also because that revealing a correlation also opens up for the possibility of predicting stock priceses and with that: endless wealth!

### Hyphothesis

#### Null Hypotheses
Stock prices can not be affected by hype on social media.

#### Alternative Hypotheses
It is possible to predict future stock prices by analysing stock hype on social media

### Expected outcome of research
We expect to see some correlation between at least some stocks going up and how much they are mentioned/discussed on social media. 

### Who will be the user of the results
Knowledge is money. We our selves will be the users of the results and hopefully we'll discover something new and exiting. And we will then be on the path to becoming the richest persons on earth.



## Stage 2: Business Data Storytelling

### Data Sources

We are collecting post and comments from the following three subreddit forums:
  - r/wallstreetbets (10.1 million users)
  - r/Stocks (2.6 million users)
  - r/Investing (1.8 million users)
  - r/Robinhood (742.000 users)
  
  *The subreddit "wallstreetbets" became world famous following the gamestop surge initiated by its users. With the fame it grew tremendously and counts more than 10 million users as of today. The jargon is juvenile and rebellious and it has become infamous for encouraging aggressive trading strategies.
  The subreddits "Stocks", "Investing" and "Robinhood" are considered more serious than wallstreet bets. They hold a great amount of users and are as interesting as their main purpuse is discussions and reccomendations about stock trading.*
  
  
 #### Our four sample data sets can be found [here](/DATA)
  
 #### Our script for collecting the data can be found [here](/Reddit_mine.ipynb)


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
- Sentences like "den skal under 180-200" must me understood at "don't by" recommendation/negative. And "den skal op på 300 før jeg sælger" must be interpreted as a positive comment.
  - especially hard to cats, as comments like that come without a contex. Or the context must be retrieved from parent posts or parent comments.
