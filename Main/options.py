from ib_insync import *

class OptionData():

    _dte: str
    _price: int
    _strike: int
    _iv: int
    _delta: int
    _gamma: int
    _vega: int

    def __init__(self, ib: IB, option: Option) -> None:
       ticker = ib.reqTickers(option)[0]
       self._dte = option.lastTradeDateOrContractMonth
       self._price = ticker.markPrice
       self._strike = option.strike
       self._iv = ticker.impliedVolatility
       self._delta = ticker.modelGreeks.delta
       self._gamma = ticker.modelGreeks.gamma
       self._vega = ticker.modelGreeks.vega 

    def get_dte(self):
        return self._dte
    
    def get_price(self):
        return self._price
    
    def get_strike(self):
        return self._strike
    
    def get_iv(self):
        return self._iv
    
    def get_greeks(self):
        return [self._delta, self._gamma, self._vega]

    