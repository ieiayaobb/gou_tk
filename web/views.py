from django.shortcuts import render_to_response
from django.template import RequestContext

from web.models import Shop
from web.parser import parse_taobao


def get_index(request):
    shops = Shop.objects.all()
    shop_groups = []
    each_shops_group = []
    for shop in shops:
        shop.goods = parse_taobao(shop)[0:4]
        if each_shops_group.__len__() >= 3:
            shop_groups.append(each_shops_group)
            each_shops_group = []
        each_shops_group.append(shop)
    if each_shops_group.__len__() > 0:
        shop_groups.append(each_shops_group)

    return render_to_response('index.html', locals(),
                              context_instance = RequestContext(request))


def get_shop(request, shop_id):
    return render_to_response('shop.html', locals(),
                              context_instance=RequestContext(request))


def get_good(request, shop_id):
    return render_to_response('good.html', locals(),
                              context_instance=RequestContext(request))