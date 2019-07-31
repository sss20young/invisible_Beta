from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def result(request):
    if request.method == 'GET':
        subject = request.GET['subject']
        grade = request.GET['grade']
        study = request.GET['study']
        teacher = request.GET['teacher']
    return render(request, 'best_lecture_result.html', {'subject':subject, 'grade':grade, 'study':study, 'teacher':teacher})