from collections import deque
# get input and make objects and lists
class Hospital:
    def __init__(self, id, prefs):
        self.id = id
        self.prefs = deque(prefs)
        self.matched_applicant = None

class Applicant:
    def __init__(self, id, prefs):
        self.id = id
        self.prefs = prefs
        self.rank = {h: i for i , h in enumerate(prefs)}
        self.matched_hospital = None


def read_input(filename, hospitals_prefs, applicants_prefs):
    with open(filename, "r") as f:
        n = int(f.readline().strip())
        # hospital_prefs = []
        # applicant_prefs = []

        for i in range(n):
            hospitals_prefs.append(list(map(int, f.readline().strip().split())))

        for j in range(n):
            applicants_prefs.append(list(map(int, f.readline().strip().split())))

    print( "Read input successfully." )
    print("\nhospital prefs: ")
    print(hospitals_prefs)
    print("\napplicant prefs: ")
    print(applicants_prefs)
    return n

def create_objects(n, hospital_prefs, applicant_prefs):
    applicants = []
    for i in range(1, n+1):
        applicants.append(Applicant(i, applicant_prefs[i-1]))
    
    print("Created applicant objects.")
    for app in applicants:
        print(f"Applicant {app.id} prefs: {app.prefs}, rank: {app.rank}")

    hospitals = deque()
    for j in range(1, n+1):
        prefs_as_objs = [applicants[k-1] for k in hospital_prefs[j-1]]
        hospitals.append(Hospital(j, prefs_as_objs))

    print("Created hospital objects.")
    for h in hospitals:
        print(f"Hospital {h.id} prefs: {[app.id for app in h.prefs]}")

    return hospitals, applicants
