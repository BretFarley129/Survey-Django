# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    context = {
        'word': get_random_string(4)
    }
    if not 'name' in request.session:
        request.session['name'] = "test"
    if not 'location' in request.session:
        request.session['location'] = "test"
    if not 'language' in request.session:
        request.session['language'] = "test"
    if not 'comment' in request.session:
        request.session['comment'] = "test"
    if not 'count' in request.session:
        request.session['count'] = 0
    
    return render(request,'getSurved/index.html', context)

def process(request):
    request.session['count'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    
    return redirect('/result')
    
def result(request):
    return render(request,'getSurved/results.html')

def refresh(request):
    return redirect('/')


