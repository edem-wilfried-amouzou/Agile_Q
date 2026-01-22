from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required as authentication_required
from .forms import AskQuestionForm
from .models import Question

# @authentication_required
def questions_list(request):
    questions = Question.objects.all().order_by("created_at")
    return render(request, 'gest_quest/list.html', {'qest': questions})

def askQuestion(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST or None)
        if form.is_valid():
            form.save()
            # return render(request, 'agl_quest/thank_you.html')
        redirect('ask')
    return render(request, 'gest_quest/ask.html', {'form': AskQuestionForm()})

def deleteQuestion(request, slug):
    question = Question.objects.get(slug=slug)
    action = request.POST.get('action')
    if action == 'delete':
        question.delete()
        return redirect('list')
    return render(request, 'gest_quest/list.html', {'question': question})
