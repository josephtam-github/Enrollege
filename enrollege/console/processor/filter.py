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


def save_ranked_data(final_data):
    f = open('cleaned_data.tsv', 'w')
    for (k, v) in final_data.items():
        f.write(k + '\t' + v.to_string() + '\n')
    f.close()


def filter_ranked_result(user_profile, data):
    result = {}
    count = 0
    for (k, v) in data.items():
        if user_profile.sat_score >= v.sat and user_profile.max_tuition >= v.tuition:
            count += 1
            result[k] = v

    return result
