from django.shortcuts import render

# Create your views here.


def draw_number_view(request):
    return render(request, 'quiz/draw_number.html')
