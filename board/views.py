from email import message
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from .models import *
from .forms import *

# Create your views here.


def home(request):
    boards = Board.objects.all()
    context = {"boards": boards}
    return render(request, "home.html", context)


def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    context = {"board": board}
    return render(request, "topics.html", context)


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        form = NewTopicForm(request.Post)
        if form.is_valid():
            form.save()

        return redirect("board_topics", pk=board.pk)
    else:
        form = NewTopicForm()

    context = {"board": board, "form": form}
    return render(request, "new_topic.html", context)
