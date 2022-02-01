from numpy import true_divide


def are_parallel(r1, r2):
    return r1.m == r2.m

def are_perpendicular(r1, r2):
    if((r1.m == 0 and r2.m == None) or ((r1.m == 0 and r2.m == None))):
        return True
    elif(r1.m != None and r2.m != None):
        return r1.m * r2.m == -1
    else:
        return False