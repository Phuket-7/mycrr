from django.shortcuts import render

from django.forms import Form,fields,widgets
from django.http import JsonResponse
import datetime

from app01 import models

class LoginForm(Form):
    name = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名', 'id': 'name'})
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空'},
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码', 'id': 'password'})
    )

# 登录
def login(request) :
    pass

# 主页
def index(request) :
    time_list = models.Relationship.time_list
    room_list = models.Room.objects.all()
    return render(request,"index.html",{"time_list":time_list,"room_list":room_list})

# 数据请求
def booking(request) :
    response = {'stuta':True,'msg': None,'data':None}
    try :
        fetch_date = request.GET.get('date')
        fetch_date = datetime.datetime.strptime(fetch_date, '%Y-%m-%d').date()
        booking_list = models.Relationship.objects.filter(date=fetch_date)
        booking_dict = {}
        for item in booking_list:
            if item.room_id not in booking_dict:
                booking_dict[item.room_id] = {item.time_select: {'name': item.user.name, 'id': item.user.id}}
            else:
                if item.booking_time not in booking_dict[item.room_id]:
                    booking_dict[item.room_id][item.time_select] = {'name': item.user.name, 'id': item.user.id}

        room_list = models.Room.objects.all()
        data = []
        for room in room_list :
            tr = []
            tr.append({'text':room.title,'attrs':{}})
            for tm in models.Relationship.time_list :
                if room.id in booking_dict and tm[0] in booking_dict[room.id] :
                    td = {'text':booking_dict[room.id][tm[0]]['name'],'attrs':{'room_id':room.id,'time_id':tm[0],'class':'chosen'}}
                else :
                    td = {'text':'','attrs':{'room_id':room.id,'time_id':tm[0]}}
                tr.append(td)
            data.append(tr)
        response['data'] = data
        print(response['data'])
    except Exception as e:
        response['stuta'] = False
        response['msg'] = str(e)
    return JsonResponse(response)
