# -*- coding: utf-8 -*-
#
# Importation of render and the function from the main file
#
from __future__ import unicode_literals
from blog.projet_1 import get_name, get_change_since_close, get_change_since_open, get_last_price
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import dataItemForm
from blog.models import DataItem


#
# Function for the views
#


#     isin = 'FR0003500008', 'FR0000036675', 'FR0013252186', 'FR0013283108', 'FR0013176526'


def add_row(request):
    isin = request.POST.get("add-isin")  # isin inputed by user
    place = request.POST.get("add-place")
    form = dataItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Form submission successful')

    # retrieve data from isin
    row = get_row(isin, place)
    context = {
        'row': row,
        'form': form
    }
    return render(request, 'home.html', context)


def get_row(isin, place):
    name = get_name(isin=isin, place=place)
    lastprice = get_last_price(isin=isin, place=place)
    sinceclose = get_change_since_close(isin=isin, place=place)
    sinceopen = get_change_since_open(isin=isin, place=place)
    isin = isin
    place = place

    row = {
        'name': name, 'lastprice': lastprice, 'sinceclose': sinceclose, 'sinceopen': sinceopen, 'isin': isin,
        'place': place
    }
    data = DataItem(
        name=name,
        lastprice=lastprice,
        sinceclose=sinceclose,
        sinceopen=sinceopen,
        isin=isin,
        place=place
    )
    data.save()
    return row


def get_data_db(request):
    mydata = DataItem.objects.all()
    return render(request, 'mydatahistory.html', {'mydata': mydata})


def delete_row(request):
    mydata = DataItem.objects.all()
    isin_to_delete = request.POST.get('delete')
    mydata.filter(isin=isin_to_delete).delete()
    return render(request, 'datahistoryrefreshed.html', {'mydata': mydata})


def refresh_quotes(request):
    mydata = DataItem.objects.all()
    for stock in mydata.values('isin', 'place'):
        stock_isin = stock['isin']
        stock_place = stock['place']
        lastprice = get_last_price(isin=stock_isin, place=stock_place)
        mydata.values('isin', 'place').filter(isin=stock_isin, place=stock_place).update(lastprice=lastprice)
    return render(request, 'datahistoryrefreshed.html', {'mydata': mydata})

