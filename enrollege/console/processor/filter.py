from models.college import CollegeInfo, float_nan
# Notice I imported as 'models.college' instead of '..models.college' to avoid relative imports

def filter_ranked_uni(university_data: dict, college_rank: dict):
    """Filters the universities  from extracted CSV file that are included in list of ranked universities

    :param university_data: A dictionary containing data of universities
    :param college_rank: A dictionary containing array of colleges and their ranks

    :returns result: a dictionary containing the data of universities that have been ranked.
    """
    size = len(university_data['INSTNM'])
    result = {}
    for i in range(size):
        name = university_data['INSTNM'][i]
        if name not in college_rank:
            continue
        rank = college_rank[name]
        city = university_data['CITY'][i]
        state = university_data['STABBR'][i]
        try:
            sat = float_nan(university_data['SAT_AVG_ALL'][i])
            accept_rate = float_nan(university_data['ADM_RATE_ALL'][i])
            tuition = float_nan(university_data['TUITIONFEE_OUT'][i])
            male_ratio = float_nan(university_data['UGDS_MEN'][i])
        except Exception as exc:
            pass

        result[name] = CollegeInfo(rank, city, state, tuition, sat, accept_rate, male_ratio)

    return result
