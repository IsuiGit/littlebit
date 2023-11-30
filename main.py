from fastapi import FastAPI, Request, status, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import settings

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

'''Main section'''

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('includes/index.html', {'request': request})

'''Login section'''

@app.post("/login")
async def login(request: Request, login: Annotated[str, Form()], llbid: Annotated[str, Form()]):
    data = settings.loadUsers()
    if login in data.keys() and data[login]['llb-id'] == llbid:
        user = data[login]
        user['logged'] = True
        data[login] = user
        settings.saveUsers(data)
        return RedirectResponse(f"/user/{login}", status_code=status.HTTP_303_SEE_OTHER)
    else:
        pass

'''User page section'''

@app.get("/user/{login}")
async def user(request: Request, login: str, firstLogOn: bool = Query(default=True)):
    data = settings.loadUsers()
    user = data[login]
    if user['logged'] == True:
        if firstLogOn == False:
            user['firstLogOn'] = False
            data[login] = user
            settings.saveUsers(data)
            return RedirectResponse(f"/user/{login}", status_code=status.HTTP_303_SEE_OTHER)
        return templates.TemplateResponse('includes/user.html', {'request': request, 'user': user, 'login': login})
    else:
        return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/user/{login}/logout")
async def user(request: Request, login: str):
    data = settings.loadUsers()
    user = data[login]
    user['logged'] = False
    data[login] = user
    settings.saveUsers(data)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

'''User registration section'''

@app.get("/registration", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse('includes/registration.html', {'request': request})

@app.post("/registration")
async def register(request: Request, name: Annotated[str, Form()], login: Annotated[str, Form()]):
    data = settings.loadUsers()
    if data != None and login not in data.keys():
        data[login] = {'name':name, 'llb-id':str(hash(name))[-6:], 'firstLogOn': True, 'logged': True}
        settings.saveUsers(data)
        return RedirectResponse(f"/user/{login}", status_code=status.HTTP_303_SEE_OTHER)
    else:
        pass
