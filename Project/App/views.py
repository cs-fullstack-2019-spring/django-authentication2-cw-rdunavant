from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_titles(request):
    return render(request, 'App/blog_title.html')

def blog_entries(request):
    return render(request, 'App/blog_entry.html')