from click import pass_context
from user import User

users = [
    User(1,'Famba', 'Fans123')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authentication(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(playload):
    user_id = playload['identity']
    return userid_mapping.get(user_id,None)