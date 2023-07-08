from django.db import models
from user.models import User
import datetime


class Blog(models.Model):
    title=models.CharField(max_length=255)
    creator=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    seen_qty=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class New(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    seen_qty=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(blank=True, null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title

    def get_first_image(self):
        return Image.objects.filter(new_id=self.id).first().image
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.date.today()
        super().save(*args, **kwargs)


class LikeDislike(models.Model):
    like=models.PositiveIntegerField(default=0)
    dislike=models.PositiveIntegerField(default=0)
    blog=models.ForeignKey(Blog,on_delete=models.SET_NULL, null=True)
    new=models.ForeignKey(New,on_delete=models.SET_NULL, null=True)
    author=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.author.phone


class Comment(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    blog=models.ForeignKey(Blog,on_delete=models.SET_NULL, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    new=models.ForeignKey(New,on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.SET_NULL, null=True, blank=True)
    new=models.ForeignKey(New,on_delete=models.SET_NULL, null=True, blank=True)
    image=models.ImageField(upload_to='blog/avatar/')

    # def __str__(self) -> str:
    #     return self.blog.title if self.blog else self.new.title