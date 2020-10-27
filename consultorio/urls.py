from django.urls import path
from . import views

urlpatterns = [
	path('',views.CuidadPortatil,name='cuidad-portatil'),
	path('login/',views.signUp,name='login'),
	path('logout/', views.signOut, name='logout'),
	path('main/',views.main,name='main'),
	path('calendario/',views.calendario,name='calendario'),
	path('registro/',views.registro,name='registro'),
	path('historias/',views.historias,name='historias'),
]