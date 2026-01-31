from collections import deque

# get input and make objects and lists
class Hospital:
    def __init__(self, id, prefs):
        self.id = id
        self.preferences = deque(prefs)  # deque of Applicant objects
        self.matched_applicant = None    # Applicant object or None

class Applicant:
    def __init__(self, id, prefs):
        self.id = id
        self.prefs = prefs               # list of hospital IDs (ints)
        self.rank = {h: i for i, h in enumerate(prefs)}  # hospital_id -> rank
        self.matched_hospital = None     # Hospital object or None


def _parse_pref_line(line, n):
    nums = list(map(int, line.strip().split())) #(int, line.split())
    if len(nums) != n:
        raise ValueError("INVALID INPUT: each preference line must contain n integers")
    if sorted(nums) != list(range(1, n + 1)):
        raise ValueError("INVALID INPUT: each preference line must be a permutation of 1..n")
    return nums


def read_input(input_file, hospitals_prefs, applicants_prefs):
    """
    Fills hospitals_prefs and applicants_prefs with list[list[int]].
    Returns n.
    """
    with open(input_file, "r") as f:
        # keep non-empty lines only
        lines = [ln.strip() for ln in f if ln.strip() != ""]

    if not lines:
        raise ValueError("EMPTY INPUT FILE")

    n = int(lines[0])
    if n <= 0:
        raise ValueError("INVALID INPUT: n must be a positive")

    expected = 1 + 2 * n
    if len(lines) != expected:
        raise ValueError(f"INVALID INPUT: expected {expected} lines, got {len(lines)}")

    # next n are hospital prefs, next n are applicant prefs
    for i in range(1, 1 + n):
        hospitals_prefs.append(_parse_pref_line(lines[i], n))

    for i in range(1 + n, 1 + 2 * n):
        applicants_prefs.append(_parse_pref_line(lines[i], n))

    return n


def create_objects(n, hospitals_prefs, applicants_prefs):
    """
    Converts raw preference lists into Hospital/Applicant objects.
    Hospital preferences become deques of Applicant objects.
    """
    applicants = []
    for i in range(1, n + 1):
        applicants.append(Applicant(i, applicants_prefs[i - 1]))

    hospitals = deque()
    for j in range(1, n + 1):
        # hospital_prefs list has applicant IDs (1..n) -> convert to Applicant objects
        prefs_as_objs = [applicants[i - 1] for i in hospitals_prefs[j - 1]]
        hospitals.append(Hospital(j, prefs_as_objs))

    return hospitals, applicants


def read_matching_file(path, n):
    """
    Reads matching file with lines 'i j'.
    Returns dict hospital_id -> applicant_id.
    """
    with open(path, "r") as f:
        lines = [ln.strip() for ln in f if ln.strip() != ""]

    if not lines:
        raise ValueError("INVALID MATCHING: empty file")

    matching = {}
    for ln in lines:
        parts = ln.split()
        if len(parts) != 2:
            raise ValueError("INVALID MATCHING: each line must be 'i j'")
        h = int(parts[0])
        a = int(parts[1])
        matching[h] = a

    # We don't force exactly n lines here, because we want verifier to report reason cleanly.
    return matching
