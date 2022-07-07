def clamp(val: int, min: int, max: int) -> int:
    if val < min:
        return min
    elif val > max:
        return max

    return val