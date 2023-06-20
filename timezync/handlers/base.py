from timezync import db

class BaseHandler:
    model = None
   
    def create(self, data):
        instance = self.model(**data)
        db.session.add(instance)
        db.session.commit()
        return instance

    def get(self, id):
        return self.model.query.get(id)

    def update(self, instance, data):
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance

    def delete(self, instance):
        db.session.delete(instance)
        db.session.commit()