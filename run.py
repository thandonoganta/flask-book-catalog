from app import create_app,db
from app.auth.models import User
from sqlalchemy import exc

# if __name__ == '__main__':
# #     flask_app = create_app('prod')
# #     with flask_app.app_context():
# #         db.create_all()
# #     flask_app.run()

# flask_app = create_app('prod')
# with flask_app.app_context():
#     db.create_all()
#     if not User.query.filter_by(user_name = 'Thando').first():
#         User.create_user(user='Thando', email='ngntha001@myuct.ac.za', password='PanxuPanxu7671$')
#         flask_app.run()

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name = 'Thando').first():
            User.create_user(user='Thando', email='ngntha001@myuct.ac.za'
                             ,password='PanxuPanxu7671$')
    except: exc.IntegrityError

            flask_app.run()