from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'personal/home.html')
    
def awards(request):
    return render(request,'personal/awards.html',{'awards':['FIFA World Player of the Year 2009',
                                                            'UEFA Club Footballer of the Year 2009',
'UEFA Club Forward of the Year 2009',
'UEFA Best Player in Europe 2011, 2015',
]})
