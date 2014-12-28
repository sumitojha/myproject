from django.shortcuts import render

from models import Question

def latest_books(request):
    book_list = Question.objects.order_by('pub_date')
    return render(request, 'index.html', {'book_list': book_list})