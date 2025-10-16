from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message

# -----------------------------
# Welcome Page
# -----------------------------
def welcome_page(request):
    return render(request, 'chatapp/welcome.html')


def base_page(request):
    return render(request, 'chatapp/base.html')

# -----------------------------
# Register View
# -----------------------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("chatapp:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("chatapp:register")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful! Please login.")
        return redirect("chatapp:login")

    return render(request, "chatapp/register.html")

# -----------------------------
# Login View
# -----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("chatapp:chat_home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("chatapp:login")

    return render(request, "chatapp/login.html")

# -----------------------------
# Logout View
# -----------------------------
def logout_view(request):
    logout(request)
    return redirect("chatapp:login")

# -----------------------------
# Chat Home (Sidebar + Empty Chat Area)
# -----------------------------
@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "chatapp/chatpage.html", {"users": users})

# -----------------------------
# Load Chat with a User
# -----------------------------
@login_required
def chat_with_user(request, username):
    other_user = get_object_or_404(User, username=username)
    messages_qs = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("timestamp")
    return render(request, "chatapp/chat_detail.html", {
        "other_user": other_user,
        "messages": messages_qs,
    })

# -----------------------------
# Send Message (AJAX)
# -----------------------------
@login_required
def send_message(request):
    if request.method == "POST":
        receiver_id = request.POST.get("receiver_id")
        content = request.POST.get("content")

        if receiver_id and content.strip():
            receiver = User.objects.get(id=receiver_id)
            msg = Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return JsonResponse({"success": True, "message": msg.content, "timestamp": msg.timestamp.strftime("%H:%M")})

    return JsonResponse({"success": False})



from django.http import JsonResponse
from .models import Message
from django.contrib.auth.models import User

def get_messages(request, user_id):
    other_user = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("timestamp")

    return JsonResponse({
        "messages": [
            {"sender": msg.sender.username, "content": msg.content}
            for msg in messages
        ]
    })


@login_required
def chat_view(request, user_id):
    """
    Open chat between logged-in user and another user (user_id).
    """
    other_user = get_object_or_404(User, id=user_id)

    # Get all messages between the logged-in user and the other user
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')

    # Pass all registered users for sidebar
    users = User.objects.exclude(id=request.user.id)

    return render(request, 'chatapp/chat_detail.html', {
        'other_user': other_user,
        'messages': messages,
        'users': users,
    })
