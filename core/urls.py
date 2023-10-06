from django.contrib import admin
from django.urls import path
# from views import StudentList
from API import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('listapi/', views.StudentList.as_view()),
    # path('createapi/', views.StudentCreate.as_view()),
    # path('retrieveapi/<int:pk>/', views.StudentRetrieveAPIView.as_view()),
    # path('updateapi/<int:pk>/', views.StudentUpdateAPIView.as_view()),
    # path('destroy/<int:pk>/', views.StudentDestroyAPIView.as_view()),
    path('list createapi/', views.StudentListcreateAPIView.as_view()),
    path('retrieve update destroy/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),
]
