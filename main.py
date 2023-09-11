from ib_insync import *
util.startLoop()

class Data():
    def __init__(self) -> None:
        self.ib = IB()
        self.ib.connect('127.0.0.1', 7496, clientId=1)


    def create_chain(self, symbol :str, date: str, strike_range: tuple, right: str):
        stock = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(stock)
        chains = self.ib.reqSecDefOptParams(stock.symbol, '', stock.secType, stock.conId)
        chain = next(c for c in chains if c.exchange == 'SMART')
        price = self.get_stock_price(stock)
        strikes = [strike for strike in chain.strikes
            if strike_range[0] < strike < strike_range[1]]
        contracts = [Option(stock, date, strike, right, 'SMART')
            for strike in strikes]
        return contracts

        
    def get_stock_price(self, stock: Contract):
        data1 = self.ib.reqMktData(stock)
        self.ib.sleep(0.5)
        price = data1.marketPrice()
        self.ib.cancelMktData(stock)
        return price
        
        
test = Data()
print(util.df(test.create_chain('SPY', '20230911', (400, 500), 'C')))