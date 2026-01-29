from collections import deque

# Initialize each person and hospital to be free.
# ideally hospital is an object with a preference list and matched applicants
# applicants are objects with preference lists and matched hospitals

class Hospital:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.matched_applicant = None

class Applicant:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.matched_hospital = None

# assume we are passing in n (number of hospitals/applicants),
# a queue of hospital objects and a list of applicant objects
def gale_shapley(hospitals):

    while (hospitals.empty() is False):
        curr_hospital = hospitals[0]
        fav_app = curr_hospital.preferences[0]

        if (fav_app.matched_hospital is None):
            # match hospital and applicant
            curr_hospital.matched_applicant = fav_app
            fav_app.matched_hospital = curr_hospital
            hospitals.popleft()

        elif (fav_app.preferences.index(curr_hospital) <
              fav_app.preferences.index(fav_app.matched_hospital)):
            
            # match H and a
            curr_hospital.matched_applicant = fav_app
            old_hospital = fav_app.matched_hospital
            old_hospital.matched_applicant = None
            fav_app.matched_hospital = curr_hospital

            hospitals.popleft()
            # add old hospital back to queue
            hospitals.append(old_hospital)

        else:
            # a rejects H so H gets added back to the queue
            curr_hospital.preferences.popleft() # remove fav_app from curr_hospital's list

# while (some hospital is free and hasn't been match/assigned
# to every applicant) {
#     Choose such a hospital H
#     a = 1st applicant on H's list to whom H has not been matched
#    if (a is free) 
#        Match H and a
#    else if (a prefers H to its current assignment H')
#        Match H and a
#        Free H'
#    else
#        a rejects H
# }