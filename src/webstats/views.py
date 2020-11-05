from django.shortcuts import render
import time

# Create your views here.
def HomePageView(request):
    context = {
        "title": "webstats",
        "time": time.strftime("%H:%M:%S - %d/%m/%Y"),
        "tz": time.tzname
    }

    # print(dir(request))
    return render(request, "home.html", context)
