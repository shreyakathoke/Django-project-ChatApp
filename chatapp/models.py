from django.db import models
from django.contrib.auth.models import User

# -----------------------------
# User Profile (Optional)
# -----------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png")
    status = models.CharField(max_length=255, default="Hey there! I am using ChatApp.")

    def __str__(self):
        return self.user.username


# -----------------------------
# Message Model
# -----------------------------
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=True)

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender} → {self.receiver}: {self.content[:30]}"


# -----------------------------
# (Optional) Chat/Conversation
# -----------------------------
# This is useful if you want group chats or multiple participants
class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name="chats")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Chat between: " + ", ".join([user.username for user in self.participants.all()])
