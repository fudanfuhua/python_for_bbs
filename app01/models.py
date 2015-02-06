from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('Bbs_User')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.title
    
class Bbs_User(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy is too lazy to leaving anything here')
    photo = models.ImageField(upload_to='upload_imgs/',default='upload_imgs/hehe.img')
   
    def __unicode__(self):
        return self.user.username
    