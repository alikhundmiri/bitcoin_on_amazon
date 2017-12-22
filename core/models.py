from django.db import models

LINK_TYPE = (
	(1, "Books"),
	(2, "Group"),
	(3, "Recommended"),
	(4, "Grow"),
	)

# Create your models here.
class price(models.Model):	
	timestamp		=		models.DateTimeField(auto_now=False, auto_now_add=True)
	updated			=		models.DateTimeField(auto_now=True, auto_now_add=False)
	current_price	=		models.CharField(default=0, max_length=10)
	cp_int			=		models.IntegerField(default=0)

	def __str__(self):
		return (self.current_price)

	class Meta:
		ordering 				=		["-timestamp", "-updated"]
		verbose_name 			=		"Price"
		verbose_name_plural		=		"Prices"

class affiliated_links(models.Model):
	linktype		=		models.IntegerField(choices=LINK_TYPE, default=1)
	href_one		=		models.CharField(max_length=1000, null=True, blank=True, help_text='enter the image with a tag')
	src_one			=		models.CharField(max_length=1000, null=True, blank=True, help_text='enter the text  with a tag')
	src_two			=		models.CharField(max_length=1000, null=True, blank=True, help_text="enter the item's amazon link url")
	name			=		models.CharField(max_length=1000, null=True, blank=True, help_text="The name you want to call")
	purchase_rate	=		models.IntegerField(default=0, null=True, blank=True)
	quantity		=		models.IntegerField(default=0, null=True, blank=True) 

	timestamp		=		models.DateTimeField(auto_now=False, auto_now_add=True)
	updated			=		models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return (self.name)

	class Meta:
		ordering				=		['-timestamp', '-updated', 'name', 'linktype']
		verbose_name 			=		"Affiliated Link"
		verbose_name_plural		=		"Affiliated Links"



