# I have created this file - jamu

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpose2 = ""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose2 = purpose2 + "Removed Punctuation" + ", "
        params = {'purpose': purpose2, 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose2 = purpose2 + "change to upper case" + ", "
        params = {'purpose': purpose2, 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose2 = purpose2 + "New Line Remover" + ", "
        params = {'purpose': purpose2, 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index2, char in enumerate(djtext):
            if not(djtext[index2] == " " and djtext[index2+1] == " "):
                analyzed = analyzed + char
        purpose2 = purpose2 + "Extra Space Remover" + ", "
        params = {'purpose': purpose2, 'analyzed_text': analyzed}
        djtext = analyzed

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on":
        return HttpResponse("Please, Select any Operation...")

    return render(request, 'analyze.html', params)










