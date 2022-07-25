from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):

    if backend.name != 'vk-oauth2':
        return

    url_method = 'https://api.vk.com/method/'
    fields = ','.join(['bdate', 'sex', 'about', 'has_photo', 'photo_100'])
    access_token = response['access_token']

    api_url = f'{url_method}users.get?fields={fields}&access_token={access_token}&v=5.131'

    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.about_me = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.age = age

    if data['has_photo'] == 1:
        user.url_avatar = data['photo_100']

    if response['email']:
        user.email = response['email']

    user.save()