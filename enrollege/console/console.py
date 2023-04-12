from .processor.scraper import get_uni_ranking, get_ranking_field
from .models.user_profile import UserProfile
from .processor.filter import normalize_data, filter_ranked_uni, filter_ranked_result, get_top_n, save_ranked_data


def recommend(user_sat, user_tuition):
    """Generates a short list of universities based on user's SAT and tuition budget """

    university_data = get_ranking_field('dataset.csv',
                                        ['INSTNM', 'CITY', 'STABBR', 'TUITIONFEE_OUT', 'SAT_AVG_ALL',
                                         'ADM_RATE_ALL', 'UGDS_MEN'])
    college_rank = get_uni_ranking()
    final_data = filter_ranked_uni(university_data, college_rank)
    # save_ranked_data(final_data)
    user_profile = UserProfile(sat_score=user_sat, max_tuition=user_tuition)
    filter_data = filter_ranked_result(user_profile, final_data)

    result = []
    if len(filter_data) == 0:
        return result
    else:
        names = []
        sat_score = []
        tuition = []
        ranks = []
        male_ratio = []
        accept_rates = []

        for (k, v) in filter_data.items():
            names.append(k)
            tuition.append(v.tuition)
            sat_score.append(v.sat)
            accept_rates.append(v.accept_rate)
            ranks.append(v.rank)
            male_ratio.append(v.male_ratio)
        tuition = normalize_data(tuition)
        ranks = normalize_data(ranks)
        sat_score = normalize_data(sat_score)
        male_ratio = normalize_data(male_ratio)

        score = {}
        for i in range(len(names)):
            score[names[i]] = 0.35 * (1 - tuition[i]) + 0.1 * (1 - sat_score[i]) + 0.1 * (1 - accept_rates[i]) \
                              + 0.35 * (1 - ranks[i]) + 0.1 * (1 - male_ratio[i])
        recommendation = get_top_n(score, 5)

        result = recommendation
        return result
