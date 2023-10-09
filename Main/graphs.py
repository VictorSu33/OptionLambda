from ib_insync import *
import options
import matplotlib.pyplot as plt

class Graphs():

    _data: list[OptionData]

    def __init__(self, option_set: list[Option]):
        _data = [options.OptionData(option) for option in option_set]