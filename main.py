import sys
from processInput import read_input
from processInput import create_objects
from galeShapley import gale_shapley

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    hospitals_prefs = []
    applicants_prefs = []
    try:
        n = read_input(input_file, hospitals_prefs, applicants_prefs)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    hospitals, applicants = create_objects(n, hospitals_prefs, applicants_prefs)
    gale_shapley(hospitals)


if __name__ == "__main__":
    main()