from django.http import HttpResponse
from django.shortcuts import render


# https://www.w3schools.com/tags/tag_textarea.asp
# https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_textarea

def about(request):
    return HttpResponse("This is about page!")


def home(request):
    return render(request, 'home.html')


def viseverse(request):
    return render(request, 'viseverse.html')


def reverse(request):
    user_text = request.GET['usertext']
    return render(request, 'reverse.html',
                  {'usertext': user_text, 'reversed': user_text[::-1], 'word_count': len(user_text.split(" "))})
