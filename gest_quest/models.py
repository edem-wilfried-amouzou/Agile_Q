from django.db import models
from django.utils.text import slugify

class Admin(models.Model):

    LEVEL = [
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
    ]
    first_name = models.CharField(max_length=150, unique=True)
    last_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150, unique=True, null=False)
    level = models.CharField(max_length=20, choices=LEVEL, default='admin')
    
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
        db_table = 'Admin'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Question(models.Model):

    author = models.CharField(max_length=150, null=False, blank=True, default='Anonymous')
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'Question'

    def __str__(self):
        return f"{self.text[:50]}..."
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.author} {self.text[:30]}")
            self.slug = base_slug
            counter = 1
            while Question.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)