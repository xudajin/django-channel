from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'room.html', {"room_name": room_name})


from channels.layers import get_channel_layer  # 后去
from asgiref.sync import async_to_sync
import json

dict = {
    'username': 'proxy1',
    'token': 'fdaffddfagf'
}


def channel_message(id):  # 在消费者外通过 get_channel_layer() 调用消费者通道
    channel_layer = get_channel_layer()
    group_name = 'test_' + id  # group_name 必须和Consumer类中的 group_name 相同 才能连接到相同组中
    async_to_sync(channel_layer.group_send)(group_name, {
        "type": "chat_message",
        "message": json.dumps(dict),  # 序列化成json
    })


def test(request, id):
    channel_message(id)
    return HttpResponse('success')
