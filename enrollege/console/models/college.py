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

