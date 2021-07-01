from django import forms
from django.core import paginator
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm #입력받는 공간
# Create your views here.
# all /  get/ order_by/filter/exclude 를 배움!

def home(request):
    blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('-pub_date') 글 최신순으로 정렬
    search = request.GET.get('search') #get방식으로 서치가 들어올때
    if search == 'true': #뭐라도 들어오면
        author = request.GET.get('writer') #라이터라는 변수에 겟방식으로 어터를 받아
        blogs = Blog.objects.filter(writer=author).order_by('-pub_date') # 제외하고 가져와
        #blogs = Blog.objects.exclude(writer=author) # 받은게 같은 것만 불러와
        #blogs = Blog.objects.exclude(writer=author).order_by('') 끝에 order_by된다~~
        return render(request, 'home.html', {'blogs': blogs})

    paginator = Paginator(blogs, 3) #3개씩 쪼개서 보낼게 !~ get방식으로
    page = request.GET.get('page') #정보가 오지 않아도 넘어가도록 /  페이지가 몇번째인지 page가 정보받음
    blogs = paginator.get_page(page) #페이지를 가져와서 몇번쨰인지 블로그스에 넘겨서 보내는 형식/page에 해당하는 글들을 보여주는 코드
    return render(request, 'home.html', {'blogs': blogs})

def detail(request,id):#view.py에서 매개변수를 받고싶을때는 url.py에서 <str:id>(패쓰컨버터라고 함)이걸 해줘야함+html에서는 blog.id해줘야함
    blog = get_object_or_404(Blog, pk = id) #프라이머리 키(기본키),ID값이래
    return render(request,'detail.html', {'blog':blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form' : form}) #form 객체를 그대로 넘겨줌

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail',new_blog.id) #id값을 보내줘야함
    return redirect('home')
    

def edit(request,id):
    edit_blog = Blog.objects.get(id = id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id): #update는 creat이랑 비슷함. 하지만 매개변수라는 id값을 받고 수정해야할 데이터를 데이터 베이스에서 부르고 덮어씌우는 것
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save() #세이브 안하면 데이터베이스에 적용이 안됨
    return redirect('detail', update_blog.id) #수정한 글의 detail페이지로 가는 것

def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home', )