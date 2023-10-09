from ib_insync import *
import optiondata
import grpahs
import matplotlib.pyplot as plt


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

def __main__():
    util.startLoop()

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)
    ib.reqMarketDataType(4)

def test():
    util.startLoop()

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)
    ib.reqMarketDataType(4)

    chain = create_chain(ib, 'SPY', '20231009', (420,440), "C")
    graph = grpahs.Graphs(chain)
    graph.plot_delta()
    print("here")


test()  
    