from django.db import models

# Create your models here.
class Note(models.Model):
    phrase = models.TextField()
    category = models.CharField(max_length=200, blank=True)
    creat_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.phrase[:30]}... ({self.category})"


    class Meta:
        ordering = ['-creat_at']
        verbose_name = "Note"
        verbose_name_plural = "Notes"