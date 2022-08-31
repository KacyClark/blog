from django.shortcuts import render
from django.views.generic import TemplateView

from bs4 import BeautifulSoup
import requests

URL = "https://wttr.in"

HEADERS = {
    "user-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
        "104.0.0.0 Safari/537.36"
    )
}


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        resp = requests.get(URL, headers=HEADERS)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            weather_pre = soup.find("pre")
        else:
            weather_pre = "%s" % resp.text
        context["weather"] = str(weather_pre)
        return self.render_to_response(context)


class AboutPageView(TemplateView):
    template_name = "pages/about.html"    
 