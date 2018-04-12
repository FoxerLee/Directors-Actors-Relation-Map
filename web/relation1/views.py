from django.shortcuts import render
import csv
import json

def read_csv(path):

    csvfile = open(path, 'r')
    reader = csv.reader(csvfile)
    names = [row[0] for row in reader]

    csvfile = open(path, 'r')
    reader = csv.reader(csvfile)
    values = [int(row[1]) for row in reader]

    return names, values


# Create your views here.
def detail(request):
    return render(request, 'relation1.html')
