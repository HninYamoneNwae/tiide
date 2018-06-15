from flask import Flask

app=Flask(_name_)

@myapp.route("/")
def hello():
    return "Hello World"

@myapp.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
