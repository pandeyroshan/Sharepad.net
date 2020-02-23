from django.db import models

# Create your models here.


class ChatRoom(models.Model):
    ip_address = models.GenericIPAddressField(null=False)
    chatroom_id = models.CharField(max_length=200)
    users = models.IntegerField(default=1)
    max_limit = models.IntegerField(default=3)

    def __str__(self):
        return self.chatroom_id
    
    class Meta:
        verbose_name = 'ChatRoom'
        verbose_name_plural = 'ChatRoom'

class TextBook(models.Model):
    chatroom = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200,blank=True)
    content = models.TextField()

    def __str__(self):
        return self.book_name
    
    class Meta:
        verbose_name = 'Textbook'
        verbose_name_plural = 'Textbook'