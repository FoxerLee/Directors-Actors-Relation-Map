# -*- coding: utf-8 -*-

from django.shortcuts import render
import json
import collections
import csv


def read_csv(path):

    csvfile = open(path, 'r')
    reader = csv.reader(csvfile)
    names = [row[0] for row in reader]

    csvfile = open(path, 'r')
    reader = csv.reader(csvfile)
    values = [int(row[1]) for row in reader]

    return names, values


def linear_scale(inputmin, inputmax, outputmin, outputmax, item):
    a = float(outputmax-outputmin)/float(inputmax-inputmin)
    b = outputmax - a*inputmax
    output = a*item +b
    return output


def word_counter(type, n=25):
    names = []
    values = []
    if type == 'actor':
        names, values = read_csv('static/actor.csv')
    elif type == 'director':
        names, values = read_csv('static/director.csv')

    wordDict = dict(zip(names, values))
    removelist = ["n/a", "*", "·", "Various", ".", "-", "na"]
    for word in removelist:
        try:
            del wordDict[word]

        except Exception:
            pass

    count = collections.Counter(wordDict)
    rank = count.most_common()[:n]
    countmax = rank[1][1]
    countmin = rank[-1][1]

    diclist = []

    for item in rank:
        rankdic = {}
        rankdic['text'] = item[0]
        rankdic['size'] = linear_scale(countmin, countmax, 10, 80, item[1])
        diclist.append(rankdic)
    diclist[0]['size'] = 90

    return diclist


def index(request):
    frequency_list_a = word_counter('actor')
    frequency_list_d = word_counter('director')

    return render(request, 'index1.html', {'frequency_list_a': json.dumps(frequency_list_a),
                                           'frequency_list_d': json.dumps(frequency_list_d)})
