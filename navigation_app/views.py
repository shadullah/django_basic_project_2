from django.shortcuts import render

# Create your views here.
def about(req):
    data = {'author': 'tabid', 'age': 20, 'list': [1,2,3],
            'courses':[
                  
                  {
                        'id':1,
                        'name': 'Python',
                        'fee': 5000
                  },
                  {
                        'id':2,
                        'name': 'Django',
                        'fee': 600
                  }
            ]
            
            }
    return render(req, 'navigation/about.html', data)

def contact(req):
        return render(req, 'navigation/contact.html')
