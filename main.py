from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = "templates")
# @-annotation 'get and post methods' of http protocol 
#root url:http://127.0.0.1:8000/
@app.get('/')
def home():
    '''
    home page
    '''
    return "hello World"

@app.get('/greet')
def greet_user(name):
    '''
    checking username and password
    '''
    
    name = input("Enter your Username: ")
    password = int(input("Enter your Password: "))
    if( password == 12345):
        
        
        return "Successfully sign_in: " +name 


@app.get("/showGreetPage", response_class=HTMLResponse )
def show_greet_page(request:Request):
    return templates.TemplateResponse("greet.html", context={"request":Request})