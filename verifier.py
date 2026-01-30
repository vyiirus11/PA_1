# -----------------------------
# Task B: Verifier
# -----------------------------

def verify_matching(n, hospitals, applicants, proposed_matching):
    """
    proposed_matching: dict hospital_id -> applicant_id

    Returns (is_valid, is_stable, message)
    """
    # (a) validity checks
    valid, reason = _check_validity(n, proposed_matching)
    if not valid:
        return False, False, f"INVALID: {reason}"

    # apply the proposed matching to objects (so stability check can use matched fields)
    _apply_matching(hospitals, applicants, proposed_matching)

    # (b) stability check
    stable, info = _check_stability(n, hospitals, applicants)
    if not stable:
        curr_hospital, fav_app = info
        return True, False, f"UNSTABLE: blocking pair ({curr_hospital}, {fav_app})"

    return True, True, "VALID STABLE"


def _check_validity(n, proposed_matching):
    # must have exactly one match per hospital
    if len(proposed_matching) != n:
        return False, f"expected {n} hospital lines, got {len(proposed_matching)}"

    seen_applicants = set()

    for curr_hospital in range(1, n + 1):
        if curr_hospital not in proposed_matching:
            return False, f"hospital {curr_hospital} missing from matching"

        fav_app = proposed_matching[curr_hospital]
        if not (1 <= fav_app <= n):
            return False, f"hospital {curr_hospital} matched to invalid applicant id {fav_app}"

        if fav_app in seen_applicants:
            return False, f"duplicate applicant {fav_app}"

        seen_applicants.add(fav_app)

    # also implies each applicant matched exactly once because we have n unique applicants in 1..n
    return True, "ok"


def _apply_matching(hospitals, applicants, proposed_matching):
    # reset
    for curr_hospital in hospitals:
        curr_hospital.matched_applicant = None
    for fav_app in applicants:
        fav_app.matched_hospital = None

    # build quick lookup
    j_map = {curr_hospital.id: curr_hospital for curr_hospital in hospitals}    # Hospital (j)
    i_map = {fav_app.id: fav_app for fav_app in applicants}         # Applicants (i)

    for j, i in proposed_matching.items():
        curr_hospital = j_map[j]
        fav_app = i_map[i]
        curr_hospital.matched_applicant = fav_app
        fav_app.matched_hospital = curr_hospital


def _check_stability(hospitals, applicants):
    """
    Looks for any blocking pair.
    Returns (True, None) if stable
    or (False, (h_id, a_id)) if unstable with example blocking pair.
    """
    # precompute hospital ranking of applicants (for "prefers" test)
    # hospital_rank[h_id][a_id] = rank (smaller is better)
    hospital_rank = {
        curr_hospital.id: {fav_app.id: i for i, fav_app in enumerate(list(h.preferences))}
        for h in hospitals
    }

    for curr_hospital in hospitals:
        curr_a = curr_hospital.matched_applicant
        curr_rank = hospital_rank[curr_hospital.id][curr_a.id]

        for i, r in hospital_rank[curr_hospital.id].items():
            if r < curr_rank:
                fav_app = applicants[i - 1]
                if fav_app.rank[curr_hospital.id] < fav_app.rank[fav_app.matched_hospital.id]:
                    return False, (curr_hospital.id, fav_app.id)

    return True, None
