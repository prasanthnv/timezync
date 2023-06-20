from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for

class Router:
    def __init__(self, name, prefix='/api/v1', children=[]):
        self.name = name
        self.prefix = prefix
        self.blueprint = Blueprint(self.name, __name__, url_prefix=self.prefix)
        self.api = Api(self.blueprint)
        if len(children) > 0:
            for child in children:
                self.add_child(child)

    def add_child(self, child):
        self.api.add_resource(child[0], child[1], endpoint=child[2])

    def add_route(self, handler, route, endpoint=None):
        self.api.add_resource(handler, route, endpoint=endpoint)
    
    def get_blueprint(self):
        return self.blueprint
    
    def get_api(self):
        return self.api
    
    def register(self, app):
        app.register_blueprint(self.blueprint)
    




