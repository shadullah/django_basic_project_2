from django.shortcuts import render

# Create your views here.
def about(req):
    data = {'author': 'tabid', 'age': 20, 'list': [1,2,3]}
    return render(req, 'navigation/about.html', data)

def contact(req):
        return render(req, 'navigation/contact.html')
