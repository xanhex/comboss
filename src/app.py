"""
Comboss app.

The app provides the user with combo lists of characters from fighting games.
"""
from flask import Flask, render_template

from models import Character, Combo, db  # type: ignore


def create_app() -> Flask:
    """
    App runner.

    Usage:
        For local testing with Debug:
        `python app.py`

        For normal run defined with config:
        `flask run`
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config_default')

    # Loads the private config from instance folder if exist
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)

    @app.route('/')
    def characters_list() -> str:
        """View function for characters list."""
        return render_template(
            'characters_list.html',
            characters=db.session.execute(
                db.select(Character).order_by(Character.name),
            ).scalars(),
        )

    @app.route('/<character_slug>')
    def character(character_slug) -> str:
        """View function for a character combo list."""
        character = db.one_or_404(
            db.select(Character).where(Character.slug == character_slug),
        )
        combos = db.session.execute(
            db.select(Combo)
            .where(Combo.character == character)
            .order_by(Combo.game_version, Combo.damage.desc()),
        ).scalars()
        context = {
            'character': character,
            'combos': combos,
        }
        return render_template('character.html', **context)

    return app


if __name__ == '__main__':
    # Debug mode ON and port is set to 8000 for local testing
    create_app().run(debug=True, port=8000)
