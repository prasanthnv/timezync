from flask_restful import Resource

class UserHandler(Resource):
    def get(self):
        return {'hello': 'world'}
