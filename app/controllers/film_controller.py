from ..models.film_model import Film
from flask import request
from decimal import Decimal
from ..models.exceptions import FilmNotFound, InvalidDataError

class FilmController:
    """Film controller class"""

    @classmethod
    def get(cls, film_id):
        """Get a film by id"""
        film = Film(film_id=film_id)
        result = Film.get(film)
        if result is not None:
            return result.serialize(), 200
        else:
            raise FilmNotFound()
        
    @classmethod
    def get_all(cls):
        """Get all films"""
        film_objects = Film.get_all()
        films = []
        for film in film_objects:
            films.append(film.serialize())
        return films, 200
    
    @classmethod
    def create(cls):
        """Create a new film"""
        data = request.json
        # TODO: Validate data

        if data.get('title') is not None and len(data.get('title'))>=3:
            if isinstance(data.get('title'), str):
                data['title'] = data.get('title').strip()
            else:
                raise InvalidDataError('El titulo debe ser una cadena con al menos 3 caracteres')
        else:
            raise InvalidDataError('El titulo es obligatorio y debe tener almenos 3 caracteres')
        
        if data.get('language_id') is not None:
            if isinstance(data.get('language_id'), int):
                data['language_id'] = data.get('language_id')
            else:
                raise InvalidDataError('El campo language_id debe ser un numero entero')
        else:
            raise InvalidDataError('El campo language_id es obligatorio')
        
        if data.get('rental_duration') is not None:
            if isinstance(data.get('rental_duration'), int):
                data['rental_duration'] = data.get('rental_duration')
            else:
                raise InvalidDataError('El campo rental_duration debe ser un numero entero')
        else:
            raise InvalidDataError('El campo rental_duration es obligatorio')

        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
            else:
                raise InvalidDataError('El campo rental_rate debe ser un numero entero')
        else:
            raise InvalidDataError('El campo rental_rate es obligatorio')
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
            else:
                raise InvalidDataError('El campo replacement_cost debe ser un numero entero')
        else:
            raise InvalidDataError('El campo replacement_cost es obligatorio')
        
        if data.get('special_features') is not None:
            valid_features = ['Trailers','Commentaries', 'Deleted Scenes', 'Behind the Scenes']
            if isinstance(data.get('special_features'), list):
                data['special_features'] = data.get('special_features')
                for item in data['special_features']:
                    if not item in valid_features:
                        raise InvalidDataError('Solo se permiten features validas')
            else:
                raise InvalidDataError('El campo special_feature debe ser una lista de features')
        else:
            raise InvalidDataError('El campo special_features es obligatorio')
        
        film = Film(**data)
        Film.create(film)
        return {'message': 'Film created successfully'}, 201

    @classmethod
    def update(cls, film_id):
        """Update a film"""
        data = request.json
        # TODO: Validate data

        if data.get('title') is not None and len(data.get('title'))>=3:
            if isinstance(data.get('title'), str):
                data['title'] = data.get('title').strip()
            else:
                raise InvalidDataError('El titulo debe ser una cadena con al menos 3 caracteres')
        else:
            raise InvalidDataError('El titulo es obligatorio')
        
        if data.get('language_id') is not None:
            if isinstance(data.get('language_id'), int):
                data['language_id'] = data.get('language_id')
            else:
                raise InvalidDataError('El campo language_id debe ser un numero entero')
        else:
            raise InvalidDataError('El campo language_id es obligatorio')
        
        if data.get('rental_duration') is not None:
            if isinstance(data.get('rental_duration'), int):
                data['rental_duration'] = data.get('rental_duration')
            else:
                raise InvalidDataError('El campo rental_duration debe ser un numero entero')
        else:
            raise InvalidDataError('El campo rental_duration es obligatorio')

        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
            else:
                raise InvalidDataError('El campo rental_rate debe ser un numero entero')
        else:
            raise InvalidDataError('El campo rental_rate es obligatorio')
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
            else:
                raise InvalidDataError('El campo replacement_cost debe ser un numero entero')
        else:
            raise InvalidDataError('El campo replacement_cost es obligatorio')
        
        if data.get('special_features') is not None:
            valid_features = ['Trailers','Commentaries', 'Deleted Scenes', 'Behind the Scenes']
            if isinstance(data.get('special_features'), list):
                data['special_features'] = data.get('special_features')
                for item in data['special_features']:
                    if not item in valid_features:
                        raise InvalidDataError('Solo se permiten features validas')
            else:
                raise InvalidDataError('El campo special_feature debe ser una lista de features')
        else:
            raise InvalidDataError('El campo special_features es obligatorio')

        data['film_id'] = film_id

        film = Film(**data)

        # TODO: Validate film exists
        if cls.exists(cls, film_id):
            Film.update(film)
            return {'message': 'Film updated successfully'}, 200
        else:
            raise FilmNotFound()
    
    def exists(self, film_id):
        film = Film(film_id=film_id)
        result = Film.get(film)
        if result is not None:
            return True
        else:
            return False

    @classmethod
    def delete(cls, film_id):
        """Delete a film"""
        film = Film(film_id=film_id)

        # TODO: Validate film exists
        if cls.exists(cls, film_id):
            Film.delete(film)
            return {'message': 'Film deleted successfully'}, 204
        else:
            raise FilmNotFound()