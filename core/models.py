from django.db import models

# Create your models here.


class ChatRoom(models.Model):
    ip_address = models.GenericIPAddressField()
    chatroom_id = models.CharField(max_length=200)
    users = models.IntegerField()
    max_limit = models.IntegerField()

    def __str__(self):
        return self.chatroom_id
    
    class Meta:
        verbose_name = 'ChatRoom'
        verbose_name_plural = 'ChatRoom'

class TextBook(models.Model):
    chatroom = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.book_name
    
    class Meta:
        verbose_name = 'Textbook'
        verbose_name_plural = 'Textbook'