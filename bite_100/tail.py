def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
    strip newlines and return a list of the last n lines"""
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines[-n:]]
