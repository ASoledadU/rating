from django.shortcuts import render
from app.forms import AddForm
from app.forms import AddForms


def add(request):
    if request.method == "GET":
        return render(request, "add.html")
    elif request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data["x"]
            y = form.cleaned_data["y"]
            answer = x + y
            return render(request, "add.html", {"x": x, "y": y, "answer": answer})
        else:
            return render(request, "add.html", {"error": form.errors})


def subtract(request):
    if request.method == "GET":
        return render(request, "subtract.html")
    elif request.method == "POST":
        x = request.POST["x"]
        y = request.POST["y"]
        answer = int(x) - int(y)
        return render(request, "subtract.html", {"x": x, "y": y, "answer": answer})


def name(request):
    if request.method == "GET":
        return render(request, "name.html")
    elif request.method == "POST":
        name = request.POST["name"]
        return render(request, "name.html", {"name": name})


def movies(request):
    if request.method == "GET":
        return render(request, "movies.html")
    elif request.method == "POST":
        a = request.POST["a"]
        a1 = request.POST["a1"]
        b = request.POST["b"]
        b1 = request.POST["b1"]
        c = request.POST["c"]
        c1 = request.POST["c1"]
        answer = (int(a) * int(a1)) + (int(b) * int(b1)) + (int(c) * int(c1))
        return render(request, "movies.html", {"answer": answer})


def rating(request):
    if request.method == "GET":
        return render(request, "rating.html")
    elif request.method == "POST":
        form = AddForms(request.POST)
        if form.is_valid():
            points = form.cleaned_data["points"]
            return render(request, "rating.html", {"points": points})
        else:
            return render(request, "rating.html", {"error": form.errors})
