from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog")
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to="blogs")
