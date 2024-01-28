from django.urls import path
from . import views

urlpatterns = [
    path('exams/',views.allExamsView, name='get_exams'),

    path('authors/',views.allAthoursView, name= 'get_authors'),


    path('signup/',views.userRegistrationView, name='registeration')
    # path('exam/<str:exam_number>', views.exam, name="exam"),
]