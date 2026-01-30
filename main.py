import sys
from processInput import read_input
from processInput import create_objects
from galeShapley import gale_shapley, output
from runningTime import run_experiment

def main():
    if sys.argv[1] == "--time":
        run_experiment()
        return

    input_file = sys.argv[1]
    hospitals_prefs = []
    applicants_prefs = []
    try:
        n = read_input(input_file, hospitals_prefs, applicants_prefs)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    hospital_list, hospitals_deque, applicants = create_objects(n, hospitals_prefs, applicants_prefs)
    gale_shapley(hospitals_deque, hospital_list)
    output(hospital_list)



if __name__ == "__main__":
    main()