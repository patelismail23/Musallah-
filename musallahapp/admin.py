from django.contrib import admin

# Register your models here.


from .models import Musallah ,  Users , NamazTiming , Facilities , HasBeen , RamzanTiming 
class AdminMusallah (admin.ModelAdmin):
	list_display = ( 'musallah_name' ,'area' , 'contact_no' , 'is_verified')
	search_fields = (  'musallah_name' , 'area' , 'contact_no' , 'is_verified') 
admin.site.register (Musallah,AdminMusallah)
admin.site.register (Users)
admin.site.register  (NamazTiming) 
admin.site.register  (HasBeen )
admin.site.register  (RamzanTiming)






