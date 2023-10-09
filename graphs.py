from ib_insync import *
from optiondata import OptionData
import matplotlib.pyplot as plt

class Graphs():

    _data: list[OptionData]

    def __init__(self, option_set: list[Option]):
        _data = [OptionData(option) for option in option_set]

    def plot_delta(self):
        x = [option.getstrike() for option in self._data]
        y = [option.getgreeks[0] for option in self._data]

        plot = plt.plot(x,y)

        plt.show()
