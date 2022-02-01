class Retta:
    def __init__(self):
        self.m = 0
        self.q = 0

    def retta_from_two_points(self, p1, p2):
        if(p1[0] == p2[0] and p1[1] == p2[1]):
            return
        elif(p1[0] == p2[0] and p1[1] != p2[1]):
            self.m = None
            self.q = None
        elif(p1[0] != p2[0] and p1[1] == p2[1]):
            self.m = 0
            self.q = p1[1]
        else:
            print((p1[1]-p2[1]))
            print((p1[0]-p2[0]))
            self.m = (p1[1]-p2[1])/(p1[0]-p2[0])
            self.q = p1[1] - (p1[1]-p2[1])/(p1[0]-p2[0])*p1[0]   

    def explicit_form(self, m, q):
        self.m = m
        self.q = q

    def implicit_form(self, a, b, c):
        if(b!=0):
            self.m = -a/b
            self.q = -c/b
        else:
            self.m = None
            self.q = None

