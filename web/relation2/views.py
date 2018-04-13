from django.shortcuts import render
import csv
import json
# Create your views here.

def read_csv(path):
    csvfile = open(path, 'r')
    reader = csv.reader(csvfile, delimiter=',')
    datas = [row for row in reader]

    return datas


def create_node(father):
    actors = read_csv('/Users/liyuan/Documents/商务智能/Directors-Actors-Relation-Map/web/static/actor.csv')
    directors = read_csv('/Users/liyuan/Documents/商务智能/Directors-Actors-Relation-Map/web/static/director.csv')


    res = []
    links = []
    level = [father]

    # res.append({"id": father, "children": []})
    for flag in range(1, 4):
        tmp = level[:]
        while tmp:
            name = tmp.pop()
            for actor in actors:
                if actor[0] == name:

                    dirs = actor[4].split(',')
                    for dir in dirs:
                        links.append({"source": name, "target": dir, "value": flag})
                        level.append(dir)

            for director in directors:
                if director[0] == name:
                    acts = director[4].split(',')
                    for act in acts:
                        links.append({"source": name, "target": act, "value": flag})
                        level.append(act)

    # nodes.append({"id": father, "children": [], "group": 0})
    #
    # nodes[0]['children'].append({"id": father, "children": [], "group": 0})
    # print(links)
    round_1 = []
    for i in range(len(links)):
        if links[i]['value'] == 1:
            name = links[i]['source']
            if name not in round_1:
                round_1.append(name)
                node = {"name": name, "children": []}
                res.append(node)

    round_2 = []
    for i in range(len(links)):
        if links[i]['value'] == 1:
            name1 = links[i]['source']
            name2 = links[i]['target']
            if name2 not in round_2:
                round_2.append(name2)
                node = {"name": name2, "children": []}
                for i in res:
                    if i["name"] == name1:
                        i["children"].append(node)
                        break

    round_3 = []
    for i in range(len(links)):
        if links[i]['value'] == 2:
            name1 = links[i]['source']
            name2 = links[i]['target']
            if name2 not in round_3:
                round_3.append(name2)
                node = {"name": name2, "children": []}
                for i in res:
                    for j in i["children"]:
                        if j["name"] == name1:
                            j["children"].append(node)
                            break

    round_4 = []
    for i in range(len(links)):
        if links[i]['value'] == 3:
            name1 = links[i]['source']
            name2 = links[i]['target']
            if name2 not in round_4:
                round_4.append(name2)
                node = {"name": name2}
                for i in res:
                    for j in i["children"]:
                        for k in j["children"]:
                            if k["name"] == name1:
                                k["children"].append(node)
                                break

    # print(res)
    return res[0]


def relation2(request):
    res = create_node("James Flavin")
    return render(request, 'relation2.html', {'relation2_list': json.dumps(res)})


def search2(request):
    q = request.GET.get('q')
    print(q)
    res = create_node(q)
    return render(request, 'relation2.html', {'relation2_list': json.dumps(res)})
# if __name__ == '__main__':
#     create_node('James Flavin')
