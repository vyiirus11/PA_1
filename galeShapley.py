from collections import deque

def gale_shapley(hospitals_deque, hospital_list):

    while (len(hospitals_deque) > 0):
        curr_hospital = hospitals_deque[0]
        fav_app = curr_hospital.prefs[0]

        if (fav_app.matched_hospital is None):
            # match hospital and applicant
            curr_hospital.matched_applicant = fav_app
            fav_app.matched_hospital = curr_hospital
            hospitals_deque.popleft()

        elif (fav_app.rank[curr_hospital.id] <
              fav_app.rank[fav_app.matched_hospital.id]):
            
            # match H and a
            curr_hospital.matched_applicant = fav_app
            old_hospital = fav_app.matched_hospital
            old_hospital.matched_applicant = None
            fav_app.matched_hospital = curr_hospital

            hospitals_deque.append(old_hospital)
            hospitals_deque.popleft()
            # add old hospital back to queue

        else:
            # a rejects H so H gets added back to the queue
            curr_hospital.prefs.popleft() # remove fav_app from curr_hospital's list

    output(hospital_list)

# we need a list of all hospitals in order to print the output matches 
def output(hospitals_list):
    for hospital in hospitals_list:
        print(f"{hospital.id} {hospital.matched_applicant.id}")