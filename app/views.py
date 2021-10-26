from django.shortcuts import render
from django.views.generic import View
from .forms import SearchForm
import json
import requests

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&applicationId='

class IndexView(View):
  def get(self, request, *args, **kwargs):
    form = SearchForm(request.POST or None)

    return render(request, 'app/index.html', {
      'form': form,

    })
