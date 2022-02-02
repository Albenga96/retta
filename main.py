from line import Line
from utils import are_parallel, are_perpendicular

r1 = Line()
r2 = Line()
r1.implicit_form(3, 1, -4)
r2.from_two_points([-1, 3], [2, -2])

print(are_parallel(r1, r2))
print(are_perpendicular(r1, r2))
