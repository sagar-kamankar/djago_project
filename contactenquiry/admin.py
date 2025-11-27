from django.contrib import admin
from contactenquiry.models import contactEnquiry

# Register your models here.
class contactenquiryAdmin(admin.ModelAdmin):
    list_diplay=('name','phone','email','message')

admin.site.register(contactEnquiry,contactenquiryAdmin)    