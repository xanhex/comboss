# type: ignore
"""Contains all database models of the app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Character(db.Model):
    """
    Character ORM.

    Relationships:
        many-to-one: Game
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(100))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    game = db.relationship('Game', backref=db.backref('characters', lazy=True))

    def __init__(self, *args, **kwargs) -> None:
        """Set the default image if not provided."""
        super().__init__(*args, **kwargs)
        if not self.image:
            self.image = 'default.png'

    def __repr__(self) -> str:
        """To representation."""
        return self.slug


class Game(db.Model):
    """
    Game ORM.

    Relationships:
        one-to-many: Character
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self) -> str:
        """To representation."""
        return self.name


class Combo(db.Model):
    """
    Combo ORM.

    Relationships:
        many-to-one: Character
    """

    id = db.Column(db.Integer, primary_key=True)
    inputs = db.Column(db.String(30), nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    game_version = db.Column(db.String(100), nullable=False)
    character_id = db.Column(
        db.Integer,
        db.ForeignKey('character.id'),
        nullable=False,
    )
    character = db.relationship('Character', backref='combo', lazy=True)

    def __repr__(self) -> str:
        """To representation."""
        return self.inputs
