import numpy as np


def float_nan(arg):
    """Converts non-integer values into float points"""
    if arg == 'NULL':
        arg.replace('NULL', float(0))
    else:
        np.nan_to_num(arg)
        return float(arg)


class CollegeInfo:
    rank = 0
    city = ''
    state = ''
    tuition = 0
    sat = 0
    accept_rate = 0
    debt = 0
    male_ratio = 0

    def __init__(self, rank, city, state, tuition, sat, accept_rate, male_ratio):
        self.rank = rank
        self.city = city
        self.state = state
        self.tuition = tuition
        self.sat = sat
        self.accept_rate = accept_rate
        self.male_ratio = male_ratio

    def to_string(self):
        return self.city + '\t' + self.state + '\t' + str(self.rank) + '\t' + str(self.tuition) + '\t' + str(self.sat) \
               + '\t' + str(self.accept_rate) + '\t' + '\t' + str(self.male_ratio)

    def to_string_with_name(self):
        return 'city:' + self.city + '\tstate:' + self.state + '\trank:' + str(self.rank) + '\ttuition:' + str(
            self.tuition) + '\tsat:' + str(self.sat) + '\tAC:' + str(self.accept_rate) + '\tMal:' + str(self.male_ratio)
