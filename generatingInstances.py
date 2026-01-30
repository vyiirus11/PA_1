import random

def generate_prefs(n):
    prefs = []
    for i in range(1, n+1):
        lst = list(range(1, n+1))
        random.shuffle(lst)
        prefs.append(lst)
    return prefs

def generate_instance(n):
    hospitals_prefs = generate_prefs(n)
    applicants_prefs = generate_prefs(n)
    return hospitals_prefs, applicants_prefs