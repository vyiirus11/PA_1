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


with open("examplein.txt", "r") as f:
    n = int(f.readline().strip())
    hospital_prefs = []
    applicant_prefs = []

    for i in range(n):
        hospital_prefs.append(list(map(int, f.readline().strip().split())))

    for j in range(n):
        applicant_prefs.append(list(map(int, f.readline().strip().split())))

applicants = []
for i in range(1, n+1):
    applicants.append(Applicant(i, applicant_prefs[i]))

hospitals = deque()
for j in range(1, n+1):
    prefs_as_objs = [applicants[k] for k in hospital_prefs[j-1]]
    hospitals.append(Hospital(j, prefs_as_objs))