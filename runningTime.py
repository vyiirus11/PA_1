import time
from generatingInstances import generate_instance
from processInput import create_objects
from galeShapley import gale_shapley 

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