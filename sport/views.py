from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

def foot(req):
    return render(req,'football.html')

def sportsmen(req,sport,id):
    footballs = [
        {'name':'Sergio Rames','pic':'img/f1.jpg','picsport':'img/fball.jpg',
         'desc':'Играет за Спартак, забил 10 голов'},
        {'name': 'Hulio Servantes', 'pic': 'img/f2.jpg', 'picsport': 'img/fball.jpg',
         'desc': 'Играет за Динамо, забил 20 голов'},
        {'name': 'Ivan Denisov', 'pic': 'img/f3.jpg', 'picsport': 'img/fball.jpg',
         'desc': 'Играет за Зенит, забил 30 голов'},
    ]
    data={}
    if sport=='football':
        data={'name':footballs[id]['name'],
              'pic':footballs[id]['pic'],
              'picsport':footballs[id]['picsport'],
              'desc':footballs[id]['desc']}

    return render(req,'sportsmen.html', data)

