from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


#http://127.0.0.1:8000
def home(request):
    #return HttpResponse("Hello World")
    data = [
        {"image": 'django.jpg', "card_title": 'Django card', "description": ' is a free, open-source, high-level Python web framework that allows developers to build safe, scalable, and maintainable web applications quickly.'},
        {"image": 'cpp.png', "card_title": 'C++ card', "description": 'C++ is a compiled, high-performance, general-purpose programming language that supports multiple paradigms, including object-oriented, procedural, and generic programming. Developed by Danish computer scientist Bjarne Stroustrup at Bell Labs in the early 1980s as an extension of the C language ("C with Classes"), it combines the raw speed of low-level programming with powerful high-level abstractions.'},
        {"image": 'csharp.png', "card_title": 'Csharp card', "description": 'C# (C-Sharp) is a modern, object-oriented, and type-safe programming language developed by Microsoft in the early 2000s. Led by Anders Hejlsberg as part of the .NET initiative, C# was designed to combine the computing power of C++ with the simplicity and developer productivity of languages like Java.'}
    ]
    return render(request, 'main/index.html', {'data': data})

def about(request):
    #return HttpResponse("Hello World")
    return render(request, 'main/about.html')