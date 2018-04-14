from django.shortcuts import render
import csv
import json
# Create your views here.


def read_csv(path):
    csvfile = open(path, 'r')
    reader = csv.reader(csvfile, delimiter=',')
    datas = [row for row in reader]

    return datas


def read_movie():
    csvfile = open('static/movies.csv', 'r')
    reader = csv.reader(csvfile)
    values = [row for row in reader]

    return values


def create_node(father):
    actors = read_csv('static/actor.csv')
    directors = read_csv('static/director.csv')

    res = []
    level = [father]
    for flag in range(1, 4):
        tmp = level[:]
        while tmp:
            name = tmp.pop()
            for actor in actors:
                if actor[0] == name:
                    dirs = actor[4].split(',')
                    movies = actor[2].split(',')
                    res.extend(movies)
                    for dir in dirs:
                        level.append(dir)

            for director in directors:
                if director[0] == name:
                    acts = director[4].split(',')
                    movies = director[2].split(',')
                    res.extend(movies)
                    for act in acts:
                        level.append(act)

    print(res)
    nodes = []
    movies_list = read_movie()
    removelist = ["n/a", "*", "·", "Various", ".", "-", "na", "None"]
    tmp = []
    for m in movies_list:
        if m[0] in res:
            t = m[4].split(',')[0]
            if t not in removelist:
                if t not in tmp:
                    tmp.append(t)
                    nodes.append({"age": t, "population": 1})
                else:
                    for n in nodes:
                        if n['age'] == t:
                            n["population"] += 1

    print(nodes)
    return nodes


def relation3(request):
    res = create_node("James Flavin")
    return render(request, 'relation3.html', {'relation3_list': json.dumps(res)})

# if __name__ == '__main__':
#     create_node('James Flavin')



