from ib_insync import *

class OptionData():

    _dte: str
    _price: float
    _strike: float
    _iv: float
    _delta: float
    _gamma: float
    _vega: float

    def __init__(self, option: Option) -> None:
        ticker = IB.reqTickers(option)[0]

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