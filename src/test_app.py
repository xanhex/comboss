"""Tests for Comboss app."""
import pytest

from app import create_app, db


@pytest.fixture()
def app():
    """App startup."""
    app = create_app()
    app.config.update(
        {
            'TESTING': True,
        },
    )

    return app


@pytest.fixture()
def database(app):
    """Fixture for creating database."""
    from models import Character, Game

    with app.app_context():
        db.create_all()
        test_game = Game(name='Test Game')
        test_character = Character(
            name='Test Character',
            slug='test_character',
            description='Test description.',
            game_id=1,
        )
        db.session.add(test_game)
        db.session.add(test_character)
        db.session.commit()

        yield db

        db.drop_all()


@pytest.fixture()
def client(app):
    """Fixture for creating test client."""
    return app.test_client()


def test_characters_list(client, database):
    """Test home page with characters list."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Characters</title>' in response.data


def test_character(client, database):
    """Test character page."""
    response = client.get('/test_character')
    assert response.status_code == 200
