from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='media_folder_products')
def media_folder_products(path_img):
    if not path_img:
        path_img = "products/default.jpg"
    return f"{settings.MEDIA_URL}{path_img}"

@register.filter(name='media_folder_users')
def media_folder_users(path_img):
    if not path_img:
        path_img = "users_avatars/default.jpg"
    return f"{settings.MEDIA_URL}{path_img}"