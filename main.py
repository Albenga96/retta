from retta import Retta

r1 = Retta()
r2 = Retta()
r1.implicit_form(3, 10, 1)
r2.retta_from_two_points([-3, 2], [66, 6])
print(r1.m)
print(r2.m)

