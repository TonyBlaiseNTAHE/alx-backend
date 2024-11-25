#!/usr/bin/env python3
"""4. Force locale with URL parameter
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get_locale
    """
    user_locale = request.args.get('locale')
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
