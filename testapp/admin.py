from django.contrib import admin
from testapp.models import HydJobs,BanJobs,MumbJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)
class BanJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(BanJobs,BanJobsAdmin)
class MumbJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(MumbJobs,MumbJobsAdmin)