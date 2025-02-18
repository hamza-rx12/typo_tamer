from data import kyb_k, dict
from min_edit_dist import min_dist
import jellyfish

source = input("Type a french word: ")
y = []

for x in dict:

    reverse_cost = round(jellyfish.jaro_winkler_similarity(source, x) / 2, 1)
    if x[0] == source[0]:
        reverse_cost += 0.3
    elif x[0] in kyb_k[x[0]]:
        reverse_cost += 0.2
    elif len(x) == len(source):
        reverse_cost += 0.4

    y.append({x: (min_dist(source, x, rep_cost=2 - reverse_cost).dist())})


y = sorted(y, key=lambda k: list(k.values()))
if list(y[0].values())[0] == 0:
    print("You typed it right, that's impressive!")
else:
    print("Broo, no way you're this bad at typing!\nLet me help you, did you mean:")

    t = 0
    for i in y:
        print(i)
        t += 1
        if t == 15:
            break
