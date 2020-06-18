from django.urls import path

from . import views

urlpatterns=[
	path('index',views.index,name='index'),
	path('<int:question_id>/',views.detail,name='detail'),
	path('api',views.api_call,name='api'),
	path('incOne',views.incOne,name='incOne')
]