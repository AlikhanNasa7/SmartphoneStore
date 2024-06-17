from .models import Basket


def baskets(request):
    user = request.user
    context = {
        'baskets': Basket.objects.filter(user=user) if user.is_authenticated else [],
    }
    return context
