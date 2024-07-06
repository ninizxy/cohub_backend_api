from django.db import models

class Note(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='N/A')  # 设置默认值为 'N/A'
    description = models.TextField(default='No description')  # 设置默认值为 'No description'
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(default='N/A')

    def __str__(self):
        return self.title
