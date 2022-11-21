from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def suresh(request):
    return HttpResponse(' <marque>suresh most innocent guy</marque><style>marque{border: 10px solid limegreen;color:red;text-align:center;font-size:30px;')
