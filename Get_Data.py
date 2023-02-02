import yfinance as yf
import json

#Return the current majority consensus for target stock
def getFirmMajority (ticker) :
    grades = {}
    numberFirms = 0
    tickerData = yf.Ticker(ticker);
    summaries = tickerData.recommendations_summary
    for index, row in summaries.iterrows():
        if row["To Grade"] in grades:
            grades[row["To Grade"]] += 1
        else:
            grades[row["To Grade"]] = 1
        numberFirms+= 1
    max_key, max_value = max(grades.items(), key=lambda item: item[1])
    output = {"Firm Majority": "Majority Of Firms Give a Grade Of : " + str(max_key) + "| Results: " + str(max_value) + " out of " + str(numberFirms) }
    return json.dumps(output)



#Return complete list of firm recommendations for target stock
def getRecommendations (ticker) :
    tickerData = yf.Ticker(ticker);
    summaries = tickerData.recommendations_summary
    hash = {}
    for index, row in summaries.iterrows():
        hash[row["Firm"]] = (row["From Grade"] or "N/A", row["To Grade"])
    return hash

#Get trend of recommendation changes amongst firms
def getFirmTrend (ticker):
    actions = {}
    numberFirms = 0
    tickerData = yf.Ticker(ticker);
    summaries = tickerData.recommendations_summary
    for index, row in summaries.iterrows():
        if row["Action"] in actions and row["Action"] != "main" and row["Action"] != "init" :
            actions[row["Action"]] += 1
        elif row["Action"] != "main" and row["Action"] != "init":
             actions[row["Action"]] = 1
        numberFirms += 1
    max_key, max_value = max(actions.items(), key=lambda item: item[1])
    output = {"Trend": "Changes in firm recommendations suggests expectations for " + ticker + " has gone "+ max_key +"."}
    return json.dumps(output)

#Get basic ticker information
def getInfo(ticker):
    tickerData = yf.Ticker(ticker);
    output = {"Information" : str(tickerData.info)}
    return json.dumps(output)

#Get basic ticker information
def getFastInfo(ticker):
    tickerData = yf.Ticker(ticker);
    output = {"Information" : str(tickerData.fast_info)}
    return json.dumps(output)

#Get PE Ratio
def getPE(ticker) :
    tickerData = yf.Ticker(ticker);
    # Get the current stock price and earnings per share (EPS)
    price = tickerData.fast_info['last_price']
    eps = tickerData.info['trailingEps']
    pe = round(price/eps,2)
    output = {'PE Ratio': pe}
    return json.dumps(output)


#Calculate Future PE Ratio
def getFuturePE(ticker) :
    tickerData = yf.Ticker(ticker);
    # Get the current stock price and earnings per share (EPS)
    price = tickerData.fast_info['last_price']
    eps = tickerData.info['forwardEps']
    pe = round(price / eps, 2)
    output = {"Future PE": pe}
    return json.dumps(output)

def getMarketCap(ticker) :
    tickerData = yf.Ticker(ticker);
    output = {"Market Cap":"$" + "{:,}".format(tickerData.fast_info["market_cap"])}
    return json.dumps(output)


def getIncome(ticker):
    tickerData = yf.Ticker(ticker);
    output = {"Information" : str(tickerData.info['netIncomeToCommon'])}
    return json.dumps(output)










