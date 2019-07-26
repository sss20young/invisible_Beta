from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def result(request):
    return render(request, 'best_lecture_result.html')