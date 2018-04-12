from django.shortcuts import render
import csv
import json


def read_csv(path):
    csvfile = open(path, 'r')
    reader = csv.reader(csvfile, delimiter=',')
    datas = [row for row in reader]

    return datas


def create_node(father):
    actors = read_csv('/Users/liyuan/Documents/商务智能/Directors-Actors-Relation-Map/web/static/actor.csv')
    directors = read_csv('/Users/liyuan/Documents/商务智能/Directors-Actors-Relation-Map/web/static/director.csv')

    # print(actors[0][0])
    nodes = []
    links = []
    level = [father]

    for flag in range(1, 4):
        print(flag)
        tmp = level[:]
        while level:
            name = level.pop()
            nodes.append({"id": name, "group": flag})

        while tmp:
            name = tmp.pop()
            for actor in actors:
                if actor[0] == name:

                    dirs = actor[4].split(',')
                    values = actor[5].split(',')

                    for (dir, value) in zip(dirs, values):

                        links.append({"source": name, "target": dir, "value": int(value)})
                        level.append(dir)

            for director in directors:
                if director[0] == name:
                    acts = director[4].split(',')
                    values = director[5].split(',')

                    for (act, value) in zip(acts, values):
                        links.append({"source": name, "target": act, "value": int(value)})
                        level.append(act)
    print(level)
    while level:
        name = level.pop()
        nodes.append({"id": name, "group": 4})
    res = {"nodes": nodes, "links": links}

    return res


# Create your views here.
def detail(request):
    res = create_node("James Flavin")
    return render(request, 'relation1.html', {'relation1_list': json.dumps(res)})


def search(request):
    q = request.GET.get('q')
    res = create_node(q)
    return render(request, 'relation1.html', {'relation1_list': json.dumps(res)})
