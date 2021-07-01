from django.db import models
from django.db.models.fields import CharField
from django.shortcuts import render

class Blog(models.Model): #여긴 데이터베이스 칼럼(기둥)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField() #이건 사용자가 따로 입력하는게 아니어서 form 아님
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank = True, null = True) #이미지 필드에는 실제로 사진이 저장이 아니라 사진의 url이 저장되는 것, 트루 안해주면 왜 사진 안올리냐고 에러남
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

