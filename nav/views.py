from django.shortcuts import render

# Create your views here.
def about(req):
    info = {'name':'Alice', 'age':25, 'courses':['Java','Python','C++','JavaScript']}
    return render(req, 'nav/about.html', context=info)

def contact(req):
    return render(req,'nav/contact.html')