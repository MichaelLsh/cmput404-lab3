import cgi 
import cgitb

cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import json
import secret
from http.cookies import SimpleCookie

# Q
s = cgi.FieldStorage()
username = s.getfirst("username")
password  =s.getfirst("password")

form_ok = username == secret.username and password == secret.password
# print("Content-Type: text/html")
print("Content-Type: application/json")

if form_ok:
    print(f"Set-Cookie: username = {username}")
    print(f"Set-Cookie: password = {password}")


print()

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None 
if cookie.get("username"):
    cookie_username = cookie.get("username")
if cookie.get("password"):
    cookie_password = cookie.get("password")

cookie_ok = cookie_username == secret.username and cookie_password == secret.password
if cookie_ok:
    username = cookie_username
    password = cookie_password

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(login_page())
    print("username & password: ", username, password)


