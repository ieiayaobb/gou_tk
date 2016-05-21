from django.shortcuts import render_to_response
from django.template import RequestContext

from web.models import Shop, Good


def get_index(request):
    shops = Shop.objects.all()
    shop_groups = []
    each_shops_group = []
    for shop in shops:
        shop.goods = Good.objects.filter(shop=shop)
        if each_shops_group.__len__() >= 3:
            shop_groups.append(each_shops_group)
            each_shops_group = []
        each_shops_group.append(shop)
    if each_shops_group.__len__() > 0:
        shop_groups.append(each_shops_group)

    return render_to_response('index.html', locals(),
                              context_instance = RequestContext(request))
