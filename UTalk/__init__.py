from flask import Flask

#from flask import Module

app = Flask(__name__)
#app.register_module(users)
import UTalk.routes.views
import UTalk.routes.users