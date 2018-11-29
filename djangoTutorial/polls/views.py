from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Question, Choice

from .forms import QuestionForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def all_questions(request):
    print("all_questions" + str(request.POST))
    #Creamos el cuestionario para poder crear questions
    form = QuestionForm(request.POST or None)

    questions = Question.objects.all()
    #Mandamos los objetos creados a la vista
    return render(request, 'polls/question-form.html', {'questions': questions, 'form': form})


def create(request):
    print("create" + str(request.POST))
    form = QuestionForm(request.POST or None)

    return render(request, 'polls/question-form.html', {'form': form})

#El acceso directo peta porque no devuelve nada (es correcto)
def nuevoObjeto(request):
    print("nuevoObjeto" + str(request.POST))
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return all_questions(request)


def update(request, question_id):
    question = Question.objects.get(id=question_id)
    form = QuestionForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'polls/question-form.html', {'form': form, 'question': question})


def delete(request, question_id):
    question = Question.objects.get(id=question_id)

    question.delete()

    return redirect('index')
