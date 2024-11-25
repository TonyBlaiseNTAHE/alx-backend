#!/usr/bin/env python3
"""5. Mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)


class Config:
    """Config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """get_user
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """before_request
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """get_locale
    """
    user = get_user()
    if user is not None and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
