from django.contrib import admin
from .models import Users

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('user_id','name','phone', 'role')
    list_editable=('name','phone', 'role')
    search_fields=('name',)
    
    
admin.site.register(Users,UserAdmin)