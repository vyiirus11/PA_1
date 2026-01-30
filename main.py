import sys
import importlib.util
import time
import random
from collections import deque

# --- load modules from filenames with hyphens (read-input.py, gale-shapley.py) ---
def _load_module(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

processInput = _load_module("./read-input.py", "processInput")
galeShapley  = _load_module("./gale-shapley.py", "galeShapley")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python main.py match <input_file>")
        print("  python main.py verify <input_file> <matching_file>")
        print("  python main.py verify <input_file>")
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]

    hospitals_prefs = []
    applicants_prefs = []

    # maybe// n = processInput.read_input(input_file, hospitals_prefs, applicants_prefs)

    try:
        n = processInput.read_input(input_file, hospitals_prefs, applicants_prefs)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    if mode == "match":
        hospitals, applicants = processInput.create_objects(n, hospitals_prefs, applicants_prefs)
        matching, proposals = galeShapley.gale_shapley(hospitals)

        # Output format: n lines, hospital i matched to student j
        for i in range(1, n + 1):
            print(i, matching[i])

        # optional: proposals count (comment out if autograder hates extra output)
        # print("PROPOSALS", proposals)

    elif mode == "verify":
        # read proposed matching either from a file or from stdin
        proposed = None

        if len(sys.argv) >= 4:
            match_file = sys.argv[3]
            try:
                proposed = processInput.read_matching_file(match_file, n)
            except Exception as e:
                print(f"INVALID: {e}")
                sys.exit(1)
        else:
            # stdin mode: user pastes n lines of "i j"
            lines = [ln.strip() for ln in sys.stdin if ln.strip() != ""]
            proposed = {}
            for ln in lines:
                parts = ln.split()
                if len(parts) != 2:
                    print("INVALID: each line must be 'i j'")
                    sys.exit(1)
                h = int(parts[0]); a = int(parts[1])
                proposed[h] = a

        # IMPORTANT: create FRESH objects so hospital.preferences are full (not popped)
        hospitals, applicants = processInput.create_objects(n, hospitals_prefs, applicants_prefs)

        is_valid, is_stable, msg = galeShapley.verify_matching(n, hospitals, applicants, proposed)
        print(msg)
    
    elif mode == "scale":
        run_scalability()

    else:
        print("Invalid mode. Use 'match' or 'verify'.")
        sys.exit(1)

def run_scalability():
    ns = [1,2,4,8,16,32,64,128,256,512]
    engine_times = []
    verifier_times = []

    for n in ns:
        hp = [random.sample(range(1,n+1), n) for _ in range(n)]
        ap = [random.sample(range(1,n+1), n) for _ in range(n)]

        hospitals, applicants = processInput.create_objects(n, hp, ap)

        t0 = time.perf_counter()
        matching, _ = galeShapley.gale_shapley(hospitals)
        t1 = time.perf_counter()
        engine_times.append(t1 - t0)

        hospitals, applicants = processInput.create_objects(n, hp, ap)
        v0 = time.perf_counter()
        galeShapley.verify_matching(n, hospitals, applicants, matching)
        v1 = time.perf_counter()
        verifier_times.append(v1 - v0)

        print(n, engine_times[-1], verifier_times[-1])

if __name__ == "__main__":
    main()
