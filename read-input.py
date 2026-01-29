from collections import deque
# get input and make objects and lists
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


with open("examplein.txt", "r") as f:
    n = int(f.readline().strip())
    hospital_prefs = []
    applicant_prefs = []

    for i in range(n):
        hospital_prefs.append(list(map(int, f.readline().strip().split())))

    for j in range(n):
        applicant_prefs.append(f.readline().strip().split())


