from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field

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
