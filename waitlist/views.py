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
                product_category=data.get('product_category'),
                business_duration=data.get('business_duration'),
                order_volume=data.get('order_volume'),
                sales_channels=data.get('sales_channels', []),
                current_tools=data.get('current_tools'),
                time_drains=data.get('time_drains', []),
                frustrations=data.get('frustrations', []),
                lost_money=data.get('lost_money'),
                lost_money_details=data.get('lost_money_details'),
                desired_automation=data.get('desired_automation'),
                worst_task=data.get('worst_task'),
                two_hours_saved=data.get('two_hours_saved'),
                interest_level=data.get('interest_level'),
                biggest_slowdown=data.get('biggest_slowdown')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return render(request, 'waitlist/uru-waitlist.html')
