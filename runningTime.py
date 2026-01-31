import time
import matplotlib.pyplot as plt
from processInput import create_objects
from galeShapley import gale_shapley 

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

def run_experiment():
    ns = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    times = []

    for n in ns:
        # Generate random preferences
        hospitals_prefs, applicants_prefs = generate_instance(n)

        # Create objects
        hospital_list, hospitals_deque, applicants = create_objects(n, hospitals_prefs, applicants_prefs)

        # Measure time taken by Gale-Shapley algorithm
        start_time = time.time()
        gale_shapley(hospitals_deque, hospital_list)
        end_time = time.time()

        elapsed_time = end_time - start_time
        times.append((n, elapsed_time))
        print(f"n={n}, time={elapsed_time:.6f} seconds")

    # Plotting the results
    plt.plot(ns, [t[1] for t in times], marker='o')
    plt.xlabel('Number of Hospitals/Applicants (n)')
    plt.ylabel('Running Time (seconds)')
    plt.title('Gale-Shapley Algorithm Running Time')
    plt.show()