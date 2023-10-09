from ib_insync import *
#from optiondata import OptionData
import matplotlib.pyplot as plt

class OptionData():

    _dte: str
    _price: float
    _strike: float
    _iv: float
    _delta: float
    _gamma: float
    _vega: float

    def __init__(self, ticker: Ticker, option: Option) -> None:

        self._dte = option.lastTradeDateOrContractMonth
        self._price = ticker.last
        self._strike = option.strike
        self._iv = ticker.impliedVolatility
        self._delta = ticker.modelGreeks.delta
        self._gamma = ticker.modelGreeks.gamma
        self._vega = ticker.modelGreeks.vega

    def getdte(self):
        return self._dte
    
    def getprice(self):
        return self._price
    
    def getstrike(self):
        return self._strike
    
    def getiv(self):
        return self._iv
    
    def getgreeks(self):
        return [self._delta, self._gamma, self._delta]
    
class Graphs():

    _data: list[OptionData]

    def __init__(self, option_set: list[Option]):
        options = IB.qualifyContracts(option_set)
        tickers = IB.reqTickers(*options)
        
        self._data = [OptionData(tickers[i], options[i]) for i in range(0,len(options))]

    def plot_delta(self):
        x = [option.getstrike() for option in self._data]
        y = [option.getgreeks[0] for option in self._data]

        plot = plt.plot(x,y)

        plt.show()
        
        
def get_stock_price(ib: IB, stock: Contract):
    data1 = ib.reqMktData(stock)
    ib.sleep(0.5)
    price = data1.marketPrice()
    ib.cancelMktData(stock)
    return price

def create_chain(ib: IB, symbol :str, date: str, strike_range: tuple, right: str):
    stock = Stock(symbol, 'SMART', 'USD')
    ib.qualifyContracts(stock)
    chains = ib.reqSecDefOptParams(stock.symbol, '', stock.secType, stock.conId)
    chain = next(c for c in chains if c.exchange == 'SMART')
    strikes = [strike for strike in chain.strikes
        if strike_range[0] < strike < strike_range[1]]
    contracts = [Option(stock, date, strike, right, 'SMART')
        for strike in strikes]
    return contracts

def test():
    util.startLoop()

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)
    ib.reqMarketDataType(4)

    chain = create_chain(ib, 'SPY', '20231009', (420,440), "C")
    graph = Graphs( chain)
    graph.plot_delta()
    print("here")


test()  