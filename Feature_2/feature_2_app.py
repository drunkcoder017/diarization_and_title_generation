

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from feature_2_view import suggest_titles


def generate_titles_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content', '')

            if not content.strip():
                return JsonResponse({'error': 'Content cannot be empty.'}, status=400)

            titles = suggest_titles(content)
            return JsonResponse({'suggested_titles': titles}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid HTTP method. Use POST.'}, status=405)
