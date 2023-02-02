import json
from flask import *
import yfinance as yf
import Get_Data


app = Flask(__name__)



@app.route('/',methods=['GET'])
def home():
    data_set = {'Page':'Home'}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/PE/',methods=['GET'])
def peRatio():
    ticker_query = str(request.args.get('ticker')) #/pe/?ticker=
    return Get_Data.getPE(ticker_query)

@app.route('/futurePE/',methods=['GET'])
def futurepeRatio():
    ticker_query = str(request.args.get('ticker')) #/futurePE/?ticker=
    return Get_Data.getFuturePE(ticker_query)

@app.route('/firmMajority/',methods=['GET'])
def firmMajority():
    ticker_query = str(request.args.get('ticker'))  # /firmMajority/?ticker=
    return Get_Data.getFirmMajority(ticker_query)

@app.route('/marketCap/',methods=['GET'])
def marketCap():
    ticker_query = str(request.args.get('ticker'))  # /marketCap/?ticker=
    return Get_Data.getMarketCap(ticker_query)

@app.route('/getInfo/',methods=['GET'])
def getInfo():
    ticker_query = str(request.args.get('ticker')) #/getInfo/?ticker=
    return Get_Data.getInfo(ticker_query)

@app.route('/getFastInfo/',methods=['GET'])
def getFastInfo():
    ticker_query = str(request.args.get('ticker')) #/getFastInfo/?ticker=
    return Get_Data.getFastInfo(ticker_query)

@app.route('/firmTrend/',methods=['GET'])
def getFirmTrends():
    ticker_query = str(request.args.get('ticker')) #/firmTrends/?ticker=
    return Get_Data.getFirmTrend(ticker_query)

@app.route('/income/',methods=['GET'])
def getStockIncome():
    ticker_query = str(request.args.get('ticker')) #/firmTrends/?ticker=
    return Get_Data.getIncome(ticker_query)






if __name__=='__main__':
    app.run(port=7777)