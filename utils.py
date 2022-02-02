import math

def are_parallel(r1, r2):
    if r1.m is None or r2.m is None:
        print("Non hai inserito una retta valida")
        return
    return r1.m == r2.m


def are_perpendicular(r1, r2):
    if r1.m is None or r2.m is None:
        print("Non hai inserito una retta valida")
        return
    if(r1.m == 0 and r2.m == math.inf) or (r1.m == 0 and r2.m == math.inf):
        return True
    elif r1.m != math.inf and r2.m != math.inf:
        return r1.m * r2.m == -1
    else:
        return False
