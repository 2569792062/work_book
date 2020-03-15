from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse
import json
import time, datetime

def get(request):
    queryset=Book.objects.all()
    book_list=[]
    for book in queryset:
        timeArray = time.localtime(book.times)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        title = str(book.title)
        book_list.append({
            'id':book.id,
            'title':title,
            'times':otherStyleTime,
            'author':book.author,
            'brief':book.brief,

        })
    return HttpResponse(book_list)

def delete(request,pk):
    try:
        book=Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    book.delete()
    return HttpResponse("删除成功")

def products(request,pk):
    try:
        book = Book.objects.get(id=pk)
    except Exception:
        return HttpResponse('此id不存在')
    books = []
    timeArray = time.localtime(book.times)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    books.append({
    'id':book.id,
    'title':book.title,
    'times':otherStyleTime,
    'author':book.author,
    'brief':book.brief,})


    return HttpResponse(books)