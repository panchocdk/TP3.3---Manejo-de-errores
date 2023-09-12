from flask import Blueprint
from ..models.exceptions import FilmNotFound, InvalidDataError

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(FilmNotFound)
def handle_film_not_found(error):
    return error.get_response()

@errors.app_errorhandler(InvalidDataError)
def handle_validate_data(error):
    return error.get_response()