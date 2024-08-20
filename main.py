from typing import Annotated

from fastapi import FastAPI, HTTPException, Body, Query, Depends
from pydantic import BaseModel, Field
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()


# 主页
@app.get("/")
def index():
    return {"message": "Hello, World!!!"}


@app.get('/403')
def not_found():
    # 返回状态码为403
    raise HTTPException(status_code=403, detail="Forbidden")


class Login(BaseModel):
    # 可选参数
    username: str = Field(None, title="用户名", max_length=50)
    password: str = Field(None, title="密码", max_length=50)
    type: str = Field(None, title="登录类型", max_length=50)
    mobile: str = Field(None, title="手机号", max_length=11)
    code: str = Field(None, title="验证码", max_length=6)


@app.post('/user/login')
def login(item: Login = Body(...)):
    if item.type == 'mobile':
        print('手机号登录', f"{item.mobile}--{item.code}")
    else:
        pass
    return {
        "code": 200,
        "data": {
            "token": "121111"
        },
        "msg": "登录成功"
    }


@app.post('/user/send-code')
def send_code():
    return {"code": "123456"}


@app.get('/user/info')
def user_info():
    return {
        "code": 200,
        "data": {
            "name": "张三",
            "avatar": "https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png",
            "roles": ["admin"]
        },
        "msg": "获取用户信息成功"
    }


@app.get('/user/menus')
def user_menu():
    return {
        "code": 200,
        "data": [
            {
                "id": 1,
                "pid": None,
                "name": "Home",
                "component": "RouteView",
                "path": "/",
                "redirect": "/home",
                "title": '首页',
                'icon': 'AccountBookFilled'

            },
            {
                "id": 2,
                "pid": 1,
                "name": "Home",
                "component": "Home",
                "path": "/home",
                "title": 'home',
                'icon': 'AlibabaOutlined'

            },

            {
                "id": 3,
                "pid": 1,
                "name": "Workspace",
                "component": "Workspace",
                "path": "/workspace",
                "title": 'workspace',
                'icon': 'AlipayOutlined'

            }
        ],
        "msg": "获取菜单成功"
    }


@app.get("/menu")
def menu(page: int = Query(default=1, description='页码'), pageSize: int = Query(default=10, description='每页数量')):
    def get_fake_date(no: int):
        return {
            "id": no,
            "pid": None,
            "path": '/dashboard',
            "name": 'Dashboard',
            "component": 'RouteView',
            "redirect": '/dashboard/analysis',
            "title": f'仪表板{no}',
            "icon": 'DashboardOutlined'
        }

    temp_data = []
    for i in range(100):
        temp_data.append(get_fake_date(i))
    start = (page - 1) * pageSize
    end = start + pageSize
    total_page = len(temp_data) // pageSize
    print({"total": total_page})
    print(100 // 20)

    return {
        "code": 200,
        "data": {"data": temp_data[start:end + 1], "total": total_page},
        "msg": "获取数据成功",

    }
