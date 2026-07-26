import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import WaitlistEntry

@ensure_csrf_cookie
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            WaitlistEntry.objects.create(
                name=data.get('name'),
                business_name=data.get('business'),
                contact=data.get('whatsapp'),
                platform=data.get('platform')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return render(request, 'waitlist/uru-waitlist.html')
