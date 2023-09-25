# Comboss

A microservice that provides the user with lists of fighting game character
combo.

## Technologies

- Python
- Flask
- Pytest
- SQLAlchemy
- Sqlite
- Jinja2
- Bootstrap 5
- CSS
- Gunicorn
- Docker

## Standards

- pep8
- flake8
- black
- pymarkdown
- mypy

## How to run

1. Clone the repository
2. Edit `csv` files from `src/data` folder if you need
3. Inside `src` folder run:

    ```bash
    docker build -t comboss .
    docker run --name comboss --rm -p 8000:8000 comboss
    ```

## Local development and testing

1. After cloning the project activate virtual environment and install
dependencies from `src/requirements.txt` file
2. To test the current functionality run `pytest` command
3. Add your models or edit existing in `models` file
4. Edit `config_default.py` to configure the app or put your private
`config.py` in `project_root/instance` folder
1. Edit `app.py` to add new functionality to the project.
2. To test the app work in Docker container switch comments in two last
lines in `src/Dokerfile`.

## Demo

![screenshot](https://github.com/xanhex/comboss/blob/master/demo_1.png)
![screenshot](https://github.com/xanhex/comboss/blob/master/demo_2.png)
