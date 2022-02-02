from line import Line
from utils import are_parallel, are_perpendicular

r1 = Line()
r2 = Line()
r1.explicit_form(1, 20)
r2.from_two_points([2, 2], [4, 4])

print(are_parallel(r1, r2))
print(are_perpendicular(r1, r2))
