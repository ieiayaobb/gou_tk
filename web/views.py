from django.shortcuts import render_to_response
from django.template import RequestContext

from pyquery import PyQuery as pyq

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



prefix='https://yzcfs.tmall.com/category.htm?spm=a220o.1000855.w5001-13085558540.8.P5dAW2'
prefix='https://turnsignal.tmall.com/category.htm?spm=a1z10.1-b.w5001-3604573288.3.K1YgfR'
def parse_taobao():
    doc = pyq(url=prefix)
    cts = doc('.J_TGoldData')
    for i in cts:
        print pyq(i).find('img').attr('srd')

parse_taobao()


def get_shop(request, shop_id):
    return render_to_response('shop.html', locals(),
                              context_instance=RequestContext(request))


def get_good(request, shop_id):
    return render_to_response('good.html', locals(),
                              context_instance=RequestContext(request))