from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This was a project where I built out my portfolio'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Awesome open source project I am still working'
    }
]

def projects(request):
   page = 'projects'
   number = 11
   context = {'page':page}
   return render(request, 'projects/projects.html', {'page':page, 'number':number,'projects':projectsList})

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-projects.html', {'project':projectObj})

