from django.db import models
from django.contrib.auth.models import User
import spacy

nlp = spacy.load('en_core_web_sm')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=20)
    last_reset = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    vector = models.BinaryField(null=True, blank=True)

    def save(self, *args, **kwargs):
        doc_nlp = nlp(self.content)
        self.vector = doc_nlp.vector.tobytes()
        super().save(*args, **kwargs)

class CreditRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_credits = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)