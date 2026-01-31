import time
import random
import matplotlib.pyplot as plt

# --- OPTION 1: normal imports (if your files are importable like this) ---
# from read_input import create_objects
# from gale_shapley import gale_shapley
# from verifier import verify_matching

# --- OPTION 2: load hyphen filenames like your main.py (recommended for your setup) ---
import importlib.util

def _load_module(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

processInput = _load_module("./read-input.py", "processInput")
matcher      = _load_module("./gale_shapley.py", "matcher")
verifier     = _load_module("./verifier.py", "verifier")


def generate_prefs(n):
    prefs = []
    for _ in range(n):
        lst = list(range(1, n + 1))
        random.shuffle(lst)
        prefs.append(lst)
    return prefs


def generate_instance(n):
    hospitals_prefs = generate_prefs(n)
    applicants_prefs = generate_prefs(n)
    return hospitals_prefs, applicants_prefs


def run_experiment():
    ns = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    matcher_times = []
    verifier_times = []

    for n in ns:
        hospitals_prefs, applicants_prefs = generate_instance(n)

        # -------------------------
        # time matcher
        # -------------------------
        hospitals, applicants = processInput.create_objects(n, hospitals_prefs, applicants_prefs)

        t0 = time.perf_counter()
        matching, _ = matcher.gale_shapley(hospitals)
        t1 = time.perf_counter()

        matcher_elapsed = t1 - t0
        matcher_times.append(matcher_elapsed)

        # -------------------------
        # time verifier
        # IMPORTANT: fresh objects so hospital.preferences are not popped
        # -------------------------
        hospitals2, applicants2 = processInput.create_objects(n, hospitals_prefs, applicants_prefs)

        v0 = time.perf_counter()
        verifier.verify_matching(n, hospitals2, applicants2, matching)
        v1 = time.perf_counter()

        verifier_elapsed = v1 - v0
        verifier_times.append(verifier_elapsed)

        print(f"n={n}, matcher={matcher_elapsed:.6f}s, verifier={verifier_elapsed:.6f}s")

    # -------------------------
    # plot both lines
    # -------------------------
    plt.plot(ns, matcher_times, marker="o", label="Matcher (Gale–Shapley)")
    plt.plot(ns, verifier_times, marker="o", label="Verifier")
    plt.xlabel("Number of Hospitals/Students (n)")
    plt.ylabel("Running Time (seconds)")
    plt.title("Runtime vs n (Matcher + Verifier)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_experiment()
