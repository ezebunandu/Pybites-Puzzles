def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError

    if len(sports) > 5:
        raise ValueError

    result = {"name": name, "age": age}
    if sports:
        result["sports"] = sorted(list(sports))
    if awards:
        result["awards"] = awards
    return result
