"""A simple script for creating the database of the app."""
import csv
from pathlib import Path

from flask import Flask

from models import Character, Combo, Game, db  # type: ignore

app = Flask(__name__)
app.config.from_object('config_default')

CSV_FILES = Path(app.root_path) / 'data'
DATABASE = Path(app.instance_path) / 'comboss.db'


def create_db():
    """Create the database from data.csv located in the instance folder."""
    # Delete old database file before create new one (only for SQLite)
    DATABASE.unlink(missing_ok=True)
    data = (
        ('games.csv', Game, 'Game'),
        ('characters.csv', Character, 'Character'),
        ('combo.csv', Combo, 'Combo'),
    )
    with app.app_context():
        db.init_app(app)
        db.create_all()
        if not list(CSV_FILES.glob('*.csv')):
            print('CSV files not found.')
            return
        for file, model, title in data:
            with open(
                (CSV_FILES / file),
                encoding='utf-8',
                errors=None,
            ) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    instance = model(**row)
                    db.session.add(instance)
                    print(f'{title} `{instance}` has been created.')
                db.session.commit()


if __name__ == '__main__':
    create_db()
