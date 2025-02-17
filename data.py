import ast


with open("data/qwerty_graph.txt", "r") as f1:
    content = f1.read()
    data = ast.literal_eval(content)

    kyb_k = {}

    for x, y in data.items():
        tmp = [n for (_, n) in y.items()]
        kyb_k[x] = tmp


with open("data/dictionnaire_fr.txt", "r") as f2:
    content = f2.read()
    dict = content.split("\n")
    # print(dict)
