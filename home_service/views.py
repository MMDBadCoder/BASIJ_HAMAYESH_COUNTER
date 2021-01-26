from django.shortcuts import render


# Create your views here.

def home_service_request(request):
    from datetime import datetime
    then = datetime(2021, 2, 6, 18, 0, 0)
    now = datetime.now()
    duration = then - now
    duration_in_s = duration.total_seconds()
    data = {
        'reminded_seconds': int(duration_in_s)
    }
    return render(request, 'index.html', data)
