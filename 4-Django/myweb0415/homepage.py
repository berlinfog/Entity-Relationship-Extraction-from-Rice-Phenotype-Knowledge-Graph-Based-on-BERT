# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from toolkit.pre_load import neo_con
from django.http import JsonResponse
import os
import json
def homepage(request):
    return render(request,"homepage.html")