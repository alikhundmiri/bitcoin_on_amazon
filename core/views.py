from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils.timezone import datetime

from .models import price, affiliated_links
import decimal
import requests
from math import log10

def index(request):	
	rate = price.objects.order_by("-id").first()
	books = affiliated_links.objects.filter(linktype=1)
	group = affiliated_links.objects.filter(linktype=2)
	recommended = affiliated_links.objects.filter(linktype=3)
	grow = affiliated_links.objects.filter(linktype=4)
	

	context = {
		"rate" : rate,
		"books" : books,
		"recommended" : recommended,
		"grow" : grow,
		"groups" : group,
	}
	return render(request, "btcprice.html", context)

@user_passes_test(lambda u: u.is_superuser)
def refresh(request):
	rate_f, rate_s = fetch_price()
	# save to price database
	print(type(rate_f))
	new = price()
	new.cp_int = (rate_f) #for calculation
	new.current_price = (rate_s) # for display
	new.save()

	save_qualtity(rate_f)
	return HttpResponseRedirect('/')


def fetch_price():
	URL = 'https://api.coindesk.com/v1/bpi/currentprice/INR.json'
	print("fetching from :" + URL)
	r = requests.get(URL)
	print(r.json())
	result_f = r.json()['bpi']['INR']['rate_float']
	result_s = r.json()['bpi']['INR']['rate']
	# print(result_f)
	return int(result_f), result_s

def save_qualtity(rate):
	group = affiliated_links.objects.filter(linktype=2)

	for item in group:
		item.quantity = (rate/item.purchase_rate)
		item.save()

