from timezync.core.router import Router
from timezync.handlers.admin import user as User

# 
router = Router('user', prefix='/api/v1/admin', children=[
    (User.UserHandler, '/'),
    # (User.UserInstanceHandler, '/user/<int:user_id>')
])
# user_router.add_route(UserHandler, '/user')
# user_router.add_route(UserInstanceHandler, '/user/<int:user_id>')



