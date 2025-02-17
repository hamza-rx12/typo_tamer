from data import kyb_k, dict
from min_edit_dist import min_dist

source = "las"
y = []

for x in dict:
    y.append(
        {
            x: (
                min_dist(source, x, rep_cost=1).dist()
                if x[0] == source[0] or x[0] in kyb_k[x[0]]
                else min_dist(source, x).dist()
            )
        }
    )
y = sorted(y, key=lambda k: list(k.values()))

t = 0
for i in y:
    print(i)
    t += 1
    if t == 30:
        break
