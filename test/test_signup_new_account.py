import random
import string


def random_username(prefix, maxlen):
    symbol = string.ascii_letters
    return prefix + ''.join([random.choice(symbol) for i in range(random.randrange(maxlen))])

def test_signup_new_account(app):
    username = random_username('username_', 10)
    password = "test"
    email = username +'@localhost'
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.soap.can_login(username, email, password)
    assert app.soap.can_login(username, password)