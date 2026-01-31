from collections import deque

# Initialize each person and hospital to be free.
# hospital: object with preference list and matched applicant
# applicant: object with preference list and matched hospital
# -----------------------------
# Task A: Matching Engine
# -----------------------------

def gale_shapley(hospitals):
    """
    hospitals: deque of Hospital objects.
    Mutates objects to set matched_hospital / matched_applicant.
    Returns (matching_dict, proposals_count)
    """
    free_hospitals = deque(hospitals)  # start with all hospitals free
    proposals = 0

    while free_hospitals:
        curr_hospital = free_hospitals.popleft()

        # If this hospital ran out of people to propose to, skip (shouldn't happen with valid complete rankings)
        if not curr_hospital.preferences: # UNDO// len(curr_hospital.preferences) == 0
            continue

        # propose to next applicant on its list
        fav_app = curr_hospital.preferences.popleft()
        proposals += 1

        if fav_app.matched_hospital is None:
            # match hospital and applicant
            curr_hospital.matched_applicant = fav_app
            fav_app.matched_hospital = curr_hospital

        else:
            # applicant compares curr_hospital vs current matched hospital
            current_hospital = fav_app.matched_hospital

            if fav_app.rank[curr_hospital.id] < fav_app.rank[current_hospital.id]:
                # applicant prefers new hospital
                current_hospital.matched_applicant = None

                curr_hospital.matched_applicant = fav_app
                fav_app.matched_hospital = curr_hospital

                # old hospital becomes free again
                free_hospitals.append(current_hospital)
            else:
                # applicant rejects curr_hospital, hospital remains free if it can still propose
                # UNDO// curr_hospital.matched_applicant = None
                if curr_hospital.preferences: # UNDO// len(curr_hospital.preferences) > 0:
                    free_hospitals.append(curr_hospital)

    matching = {}
    for curr_hospital in hospitals:
        matching[curr_hospital.id] = (curr_hospital.matched_applicant.id if curr_hospital.matched_applicant is not None else None)

    return matching, proposals
