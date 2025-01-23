from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class ProductPageView(TemplateView):
    template_name = "pages/product.html"


@method_decorator(csrf_protect, name='dispatch')
@require_http_methods(["POST"])
def upload_file(request):
    try:
        files = request.FILES.getlist('files')
        # Here you would process the files
        # For example, save them to the server or process their contents
        
        return JsonResponse({
            'message': 'Files uploaded successfully',
            'files': [f.name for f in files]
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)
