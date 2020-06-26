from django.urls import path

from . import views

urlpatterns=[
	path('index',views.index,name='index'),
	path('<int:question_id>/',views.detail,name='detail'),
	path('api',views.api_call,name='api'),
	path('incOne',views.incOne,name='incOne'),
	path('decOne',views.decOne,name='decOne'),
	path('bookingRequests',views.bookingRequests,name='bookingRequests'),
	path('reject',views.reject,name='reject'),
	path('accept',views.accept,name='accept'),
	path('blockedUsers',views.blockedUsers,name='blockedUsers'),
	path('unblock',views.unblock,name='unblock'),
	path('bookingHistory',views.bookingHistory,name='bookingHistory'),
	path('acceptResource',views.acceptResource,name='acceptResource'),
	path('timetable',views.timetable,name='timetable')

]