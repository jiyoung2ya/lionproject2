from django.urls import path
from .views import *

urlpatterns = [ #view에 함수가 추가할때마다 적기
    path('<str:id>',detail, name="detail"), #str은 자료형 데이터베이스에 따른(혹은views) id는 매개변수 이름,views의 매개변수,html에서 접근을 할 수 이쓴ㄴ 네임스페이스
    path('new/',new, name="new"),
    path('create/',create,name="create"),
    path('edit/<str:id>',edit,name="edit"), #path컨버터를 만들어줘야함, 페쓰컨버터로 받은 id를, 수정하는 창을 보여주는 기능
    path('update/<str:id>', update, name="update"), #view.py에서 매개변수를 받고싶을때는 url.py에서 <str:id>(패쓰컨버터라고 함)이걸 해줘야함+html에서는 blog.id해줘야함
    path('delete/<str:id>',delete,name="delete"),
]