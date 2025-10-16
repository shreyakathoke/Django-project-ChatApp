from django.urls import path
from . import views

app_name = 'chatapp'  # Namespacing

urlpatterns = [
    # Home / Welcome pages
    path('', views.welcome_page, name='welcome'),
    path('base/', views.base_page, name='base_page'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Chat functionality
    path('chat/', views.chat_home, name='chat_home'), 
    path('chat/<int:user_id>/', views.chat_view, name='chat_view'),  # open chat with a specific user
    path('send-message/', views.send_message, name='send_message'),   # ajax send message
    path('get-messages/<int:user_id>/', views.get_messages, name='get_messages'), # ajax get messages
]
