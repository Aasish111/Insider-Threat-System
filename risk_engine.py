def compute_risk(row):

    score = 0

    # Suspicious printing behavior
    if row["total_printed_pages"] > 100:
        score += 20

    # Suspicious file burning
    if row["total_files_burned"] > 10:
        score += 30

    # Late exit behavior
    if row["late_exit_flag"] == 1:
        score += 20

    # Weekend entry
    if row["entry_during_weekend"] == 1:
        score += 20

    # Model anomaly
    if row["anomaly"] == -1:
        score += 50

    return min(score, 100)