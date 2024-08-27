from django.contrib import admin
from .models import ChaiVarity , ChaiReview , Store , ChaiCertificate

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2
    

class ChaiVarityAdmine(admin.ModelAdmin):
    list_display = ('name' , 'type' , 'date_added')
    inlines = [ChaiReviewInline]
    
    
class StoreAdmine(admin.ModelAdmin):
    list_display = ('name' , 'location')
    filter_horizontal = ('chai_varieties',)
    
    
class ChaiCertificateAdmine(admin.ModelAdmin):
    list_display = ('chai' , 'certificate_number')
    
    

admin.site.register(ChaiVarity , ChaiVarityAdmine)
admin.site.register(Store , StoreAdmine)
admin.site.register(ChaiCertificate , ChaiCertificateAdmine)
