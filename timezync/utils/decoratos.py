from functools import wraps
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def catch_db_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IntegrityError as e:
            # Handle the IntegrityError exception with a specific error message
            error_message = 'An integrity constraint violation occurred.'
            if e.orig.args:
                error_message = e.orig.args[0]
            return {'message': error_message}, 400
        except SQLAlchemyError as e:
            # Handle other SQLAlchemy exceptions with a generic error message
            return {'message': 'An error occurred with the database operation.'}, 500
    return wrapper