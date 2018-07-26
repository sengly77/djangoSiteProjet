from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Game
from .forms import GameForm


def showAllGame(request):
    """ Show all video games """
    games = Game.objects.all()
    return render(request, "showAllGames.html", {'games': games})


def deleteGame(request, id):
    """ Delete a video game """
    game = Game.objects.get(id=id)
    game.delete()
    return redirect("showAllGame")


def addGame(request):
    """ Add a video game """
    form = GameForm(request.POST or None)
    if form.is_valid():
        game = form.save()
        game.save()
        return redirect("showAllGame")

    return render(request, 'addGame.html', locals())


def updateGame(request, id):
    """ Update a video game """
    game = Game.objects.get(id=id)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect("showAllGame")

    return render(request, 'updateGame.html', locals())