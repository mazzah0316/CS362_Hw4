def volume(x):
    if x <= 0:
        return 0
    elif type(x) == float:
        return x*x*x
    elif type(x) == int:
        return float(x)*float(x)*float(x)