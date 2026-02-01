from django.db import models

class GeneratedText(models.Model):
    seed_text = models.CharField(max_length=200)
    output_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.seed_text
