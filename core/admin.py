from django.contrib import admin

# Register your models here.
from .models import price, affiliated_links

class PriceAdmin(admin.ModelAdmin):
	list_display = ['current_price', 'timestamp']
	list_filter = ['current_price', 'timestamp']
	search_fields = ['current_price', 'timestamp']

class LinksAdmin(admin.ModelAdmin):
	list_display = ["name", "linktype"]
	list_filter = ["name", "linktype"]
	search_fields = ["name", "linktype"]


admin.site.register(price, PriceAdmin)
admin.site.register(affiliated_links, LinksAdmin)
