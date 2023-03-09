from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from survey.models import Test, Question, Choice, User, Color


def get_page(tests, request, count=3):
    """Пагинатор."""
    paginator = Paginator(tests, count)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


@login_required
def index(request):
    """Главная страница."""
    user = get_object_or_404(User, id=request.user.id)
    test_list = Test.objects.all()
    page_obj = get_page(test_list, request)
    context = {
        'page_obj': page_obj,
        'user': user,
    }
    return render(request, 'survey/index.html', context)


@login_required
def start_survey(request, slug):
    """Функция тестирования."""
    user = get_object_or_404(User, id=request.user.id)
    test_object = get_object_or_404(Test, slug=slug)
    questions = Question.objects.filter(test=test_object)
    context = {
        'questions': questions,
        'user': user,
    }
    if request.method == 'POST':
        score, correct, wrong = 0, 0, 0
        for q in questions:
            if q.correct_answer == request.POST.get(q.text):
                score += 5
                correct += 1
                user.currency += 5
                user.save()
            else:
                wrong += 1
        context['score'] = score
        context['correct'] = correct
        context['wrong'] = wrong
        user.count_test += 1
        user.save()
        return render(request, 'survey/result.html', context)
    else:
        return render(request, 'survey/questions.html', context)


@login_required
def get_user_list(request):
    """Список пользователей."""
    users = User.objects.all()
    page_obj = get_page(users, request, count=5)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'survey/all_users.html', context)


@login_required
def profile(request):
    """Профиль, покупка цветов. Не реализовано."""
    user = get_object_or_404(User, id=request.user.id)
    user_color_active = user.color.get(is_active=True)
    colors = Color.objects.all()
    context = {
        'colors': colors,
        'user_color_active': user_color_active,
    }
    if request.method == 'POST':
        balance = user.currency
        cost = Color.objects.get(name=list(request.POST.values())[-1]).price
        user.currency -= cost
        print(balance)
        user.color.is_active = True
        user.color.is_available = True
        user.save()
        return redirect('survey:get_user_list')
    return render(request, 'survey/profile.html', context)
