from django.db.models import Q #追加
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm
from .forms import QuestionFormSet

# Create your views here.
from django.http import HttpResponse
from .models import Question,Category
from django.views.decorators.http import require_POST
from django.views.generic import DeleteView

# 一覧画面
def index(request):
    posts = Question.objects.order_by('id')
    hists = Question.objects.order_by('-id')[:10]
    new_orders = Question.objects.filter(status='新規')
    form = QuestionForm(request.GET or None)
    try:
        len(posts)
    except:
        posts = 0

    if posts != "":
        for p in posts:
            p.tags = p.tags.split(",")
    count = Question.objects.filter(status='新規')
    try:
        count = len(count)
    except:
        count = 0
    d = {
        'posts':posts,
        'count':count,
        'hists':hists,
        'form':form,
        'new_orders':new_orders,
    }

    return render(request, 'index.html', d)

# 質問詳細画面
def detail(request, pk):
    posts = get_object_or_404(Question, pk=pk)
    post_answer = Question.objects.order_by('id')
    posts.tags = posts.tags.split(",")
    count = Question.objects.filter(status='新規')
    hists = Question.objects.order_by('-id')[:10]
    new_orders = Question.objects.filter(status='新規')
    try:
        count = len(count)
    except:
        count = 0
    d = {
        'posts':posts,
        'count':count,
        'hists':hists,
        'new_orders':new_orders,
        'post_answer':post_answer,
    }

    return render(request, 'detail.html', d)
    
# 質問詳細編集画面
def edit(request, pk):

    form = QuestionForm(request.GET or None)
    posts = Question.objects.get( pk=pk)
    hists = Question.objects.order_by('-id')[:10]
    new_orders = Question.objects.filter(status='新規')

    form.is_valid()
    if len(request.GET) != 0:
    # if request.method == 'GET':
        posts.status=form.cleaned_data['status']
        posts.category_system=form.cleaned_data['category_system']
        posts.category_detail=form.cleaned_data['category_detail']
        posts.questioner=form.cleaned_data['questioner']
        posts.question_contents=form.cleaned_data['question_contents']
        posts.tags=form.cleaned_data['tags']
        posts.save()
        posts.tags = posts.tags.split(",")
        count = Question.objects.filter(status='新規')
        new_orders = Question.objects.filter(status='新規')
        try:
            count = len(count)
        except:
            count = 0

        d = {
            'posts':posts,
            'form':form,
            'count':count,
            'hists':hists,
            'new_orders':new_orders,
        }

        return render(request, 'detail.html',d)
        
    form['status'].initial=posts.status
    form['category_system'].initial=posts.category_system
    form['category_detail'].initial=posts.category_detail
    form['questioner'].initial=posts.questioner
    form['question_contents'].initial=posts.question_contents
    form['tags'].initial=posts.tags
    count = Question.objects.filter(status='新規')
    try:
        count = len(count)
    except:
        count = 0
    
    d = {
        'posts':posts,
        'form':form,
        'count':count,
        'hists':hists,
        'new_orders':new_orders,
    }

    return render(request, 'edit.html', d)
    
# 質問追加画面
def add(request):
    posts = Question.objects.all()
    form = QuestionForm(request.GET or None)
    count = Question.objects.filter(status='新規')
    hists = Question.objects.order_by('-id')[:10]
    new_orders = Question.objects.filter(status='新規')
    try:
        count = len(count)
    except:
        count = 0
    context = {
        'posts':posts,
        'form':form,
        'count':count,
        'hists':hists,
        'new_orders':new_orders,
    }
    if len(request.GET) != 0:
    # if request.method == 'GET':
        form.is_valid()
        
        # create()の場合
        Question.objects.create(**form.cleaned_data)

        posts = Question.objects.order_by('id')
        if posts != "":
            for p in posts:
                p.tags = p.tags.split(",")
        d = {
            'form':form,
            'posts':posts,
            'count':count,
            'hists':hists,
            'new_orders':new_orders,
        }

        return render(request, 'index.html',d)
    return render(request, 'add.html', context)

# 回答画面    
def answer(request, pk):
    form = QuestionForm(request.GET or None)
    posts = Question.objects.get( pk=pk)
    count = Question.objects.filter(status='新規')
    hists = Question.objects.order_by('-id')[:10]
    new_orders = Question.objects.filter(status='新規')
    try:
        count = len(count)
    except:
        count = 0
    form['answer'].initial=posts.answer
    d = {
        'posts':posts,
        'form':form,
        'count':count,
        'hists':hists,
        'new_orders':new_orders,
    }

    if len(request.GET) != 0:
    # if request.method == 'GET':
        form.is_valid()
        posts.answer=form.cleaned_data['answer']
        posts.status="完了"
        posts.save()

        posts = Question.objects.order_by('id')
        count = Question.objects.filter(status='新規')
        try:
            count = len(count)
        except:
            count = 0
        if posts != "":
            for p in posts:
                p.tags = p.tags.split(",")
        d = {
            'posts':posts,
            'count':count, 
            'hists':hists,
            'form':form,
            'new_orders':new_orders,
        }

        return render(request, 'index.html',d)
        
    return render(request, 'answer.html', d)

# 質問削除
def delete(request, pk):
    record = Question.objects.get(id = pk)
    record.delete()
    
    posts = Question.objects.order_by('id')
    count = Question.objects.filter(status='新規')
    hists = Question.objects.order_by('-id')[:10]
    new_orders = Question.objects.filter(status='新規')
    try:
        count = len(count)
    except:
        count = 0
    if posts != "":
        for p in posts:
            p.tags = p.tags.split(",")
    d = {
        'posts':posts,
        'count':count,
        'hists':hists,
        'new_orders':new_orders,
    }

    return render(request, 'index.html', d)

# 検索
def find(request):       
    # pdb.set_trace()

    profile_list = Question.objects.all()
    count = Question.objects.filter(status='新規')
    formset = QuestionForm(request.POST or None)
    hists = Question.objects.order_by('-id')[:10]
    new_orders = Question.objects.filter(status='新規')
    try:
        count = len(count)
    except:
        count = 0

    if request.method == 'POST':
        # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
        formset.is_valid()

        # Qオブジェクトを格納するリスト
        queries = []

        # 各フォームの入力をもとに、Qオブジェクトとして検索条件を作っていく
        for form in formset:
            # Qオブジェクトの引数になる。
            q_kwargs = {}
            category_system = request.POST['category_system']
            if category_system:
                profile_list = profile_list.filter(category_system__contains=category_system)

            category_detail = request.POST['category_detail']
            if category_detail:
                profile_list = profile_list.filter(category_detail__contains=category_detail)

            question_contents = request.POST['question_contents']
            if question_contents:
                profile_list = profile_list.filter(question_contents__contains=question_contents)

            answer = request.POST['answer']
            if answer:
                profile_list = profile_list.filter(answer__contains=answer)
                    
    for p in profile_list:
        p.tags = p.tags.split(",")
        
    context = {
        'posts': profile_list,
        'form': formset,
        'count':count,
        'hists':hists,
        'new_orders':new_orders,
    }
    return render(request, 'index.html', context)