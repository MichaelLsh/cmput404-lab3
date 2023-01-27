#! usr/bin/env python3 

# localhost:8080/hello.py
import os,json
print("Content-Type: text/html") #HTML is following
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")
