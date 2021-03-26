from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'todo'

urlpatterns = [
    path('admin/', admin.site.urls),


    # Auth
    path('signup/', views.signup, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #Todos
    path('', views.todohome, name='todohome'),
    path('create/', views.createtodo, name='createtodo'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]