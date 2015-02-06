from django.contrib import admin
from app01 import models 
# Register your models here.
class BBS_admin(admin.ModelAdmin):
    list_display = ('title','summary','author','signature','created_at','user_photo')
    list_filter = ('created_at',)
    search_fields = ('title','author__user__username',)
    def signature(self,obj):
        return obj. author.signature    
    def  user_photo(self,obj):
        return obj.author.photo
    signature.short_description = ''
    
    
class user_display(admin.ModelAdmin):
    list_display = ('user','signature','photo')
    
    
admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Bbs_User,user_display    )    
