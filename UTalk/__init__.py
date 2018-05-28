from flask import Flask
from flask import Flask,render_template
from UTalk.routes.users import users

app = Flask(__name__)
#app.register_module(users)
import UTalk.routes.views