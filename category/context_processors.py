from .models import *


def menu_links(request):
    categories = Category.objects.all()
    return dict(categories=categories)