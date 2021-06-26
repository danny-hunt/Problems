"""
The stable marriage problem is defined as follows:

Suppose you have N men and N women, and each person has ranked their prospective
opposite-sex partners in order of preference.

For example, if N = 3, the input could be something like this:

guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
Write an algorithm that pairs the men and women together in such a way that no two
people of opposite sex would both rather be with each other than with their current partners.
"""

guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}


for key, value in guy_preferences.items():
    value.append(0)
    value.append(0)
    # name name ... name is_matched? index_for_proposal

for key, value in gal_preferences.items():
    value.append(value[-1])
    value.append([])
    # name name ... name fiance list_of_suitors


def marriage(guy_preferences, gal_preferences):
    proposals = [2]
    while proposals != []:
        proposals = [
            [guy, value[value[-1]]]
            for guy, value in guy_preferences.items()
            if guy_preferences[guy][-2] == 0
        ]


        if proposals == []:
            return 0

        for proposal in proposals:
            gal_preferences[proposal[1]][-1].append(proposal[0])

        for gal, value in gal_preferences.items():
            for suitor in value[-1]:
                current_fiance = value[-2]
                current_fiance_index = value.index(value[-2])
                if value.index(suitor) < current_fiance_index:
                    guy_preferences[current_fiance][-2] = 0
                    guy_preferences[current_fiance][-1] += 1
                    guy_preferences[suitor][-2] = 1
                    value[-2] = suitor
                elif value.index(suitor) == current_fiance_index:
                    guy_preferences[current_fiance][-2] = 1
                else:
                    guy_preferences[suitor][-1] += 1

        print( [[gal, gal_preferences[gal][-2]] for gal in gal_preferences] )

marriage(guy_preferences, gal_preferences)





