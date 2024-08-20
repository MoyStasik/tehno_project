from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app import views
from app.views import like_async

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('settings/', views.settings, name='settings'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    path('logout/', views.logout, name='logout'),
    path('question/<int:question_id>', views.question, name='question'),
    path('<question_id>/like', views.like, name='like'),
    path('<question_id>/like_async', views.like_async, name='like_async')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)