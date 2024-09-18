# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .settings import redis_instance

def submit_message(request):
    if request.method == "POST":
        user = request.POST.get("user")
        content = request.POST.get("content")

        # Find urgent messages
        if "#" in content:
            urgent_parts = [word[1:] for word in content.split() if word.startswith("#")]
            for part in urgent_parts:
                # Increment count in Redis and set expiration to 24 hours (86400 seconds)
                redis_instance.hincrby(user, part, 1)
                redis_instance.expire(user, 86400)  # Set expiration to 24 hours

        return JsonResponse({"status": "success"})
    return render(request, "submit_message.html")

def get_trends(request):
    trends = {}

    # Get all user keys and aggregate trends
    for key in redis_instance.keys():
        user_trends = redis_instance.hgetall(key)
        for part, count in user_trends.items():
            part = part.decode("utf-8")
            count = int(count)
            if part in trends:
                trends[part] += count
            else:
                trends[part] = count

    # Sort trends by count in ascending order
    sorted_trends = sorted(trends.items(), key=lambda item: item[1])

    return JsonResponse({"trends": sorted_trends})
