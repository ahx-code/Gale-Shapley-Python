def get_rank(female_name, male_name):
    try:
        return [choice.split(sep=':')[0] for person, choices in females.items() for choice in choices
                if person == female_name if male_name == choice.split(sep=':')[1]][0]
    except IndexError as error:
        print("[Error]: {}".format(error))


if __name__ == '__main__':

    males = {'A': ['1:O', '2:M', '3:N', '4:L', '5:P'],
             'B': ['1:P', '2:N', '3:M', '4:L', '5:O'],
             'C': ['1:M', '2:P', '3:L', '4:O', '5:N'],
             'D': ['1:P', '2:M', '3:O', '4:N', '5:L'],
             'E': ['1:O', '2:L', '3:M', '4:N', '5:P']}

    females = {'L': ['1:D', '2:B', '3:E', '4:C', '5:A'],
               'M': ['1:B', '2:A', '3:D', '4:C', '5:E'],
               'N': ['1:A', '2:C', '3:E', '4:D', '5:B'],
               'O': ['1:D', '2:A', '3:C', '4:B', '5:E'],
               'P': ['1:B', '2:E', '3:A', '4:C', '5:D']}

    result = {}

    while len(males.keys()) != len(result.keys()):
        # Male proposes
        for male, preferences in males.items():

            # If the male is not already engaged.
            if not next((True for key, _ in result.items() if key == male), None):

                for ranking in preferences:
                    rank, female = ranking.split(sep=':')

                    # Has female proposed before?
                    female_proposed = True if female in result.values() else False

                    if not female_proposed:
                        result[male] = female
                        break
                    else:
                        # Who is the current female darling?
                        darling = [boy_friend for boy_friend, girl_friend in result.items() if girl_friend == female][0]

                        # What are the darling and the candidate rankings?
                        darling_rank = get_rank(female_name=female, male_name=darling)
                        candidate_rank = get_rank(female_name=female, male_name=male)

                        # If candidate is superior
                        if candidate_rank < darling_rank:
                            # Leave darling
                            del result[darling]

                            # Get candidate
                            result[male] = female
                            break

    print(result)
