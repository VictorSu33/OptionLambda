from ib_insync import *
util.startLoop()

class Data():
    def __init__(self) -> None:
        self.ib = IB()
        self.ib.connect('127.0.0.1', 7496, clientId=1)


    def create_contract(self, symbol :str):
        stock = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(stock)
        data1 = self.ib.reqMktData(stock)
        self.ib.sleep(0.5)
        price = data1.marketPrice()
        self.ib.cancelMktData(stock)
        return price
        
test = Data()
print(test.create_contract('SPY'))
