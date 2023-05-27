from django.contrib import admin


from .models import *

class Admin(admin.ModelAdmin):
    list_display=['job','employee','work','user','feed_back']
    
    

admin.site.register(job)
admin.site.register(employee)
admin.site.register(work)
admin.site.register(user)
admin.site.register(feed_back)