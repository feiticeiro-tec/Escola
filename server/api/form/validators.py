from flask import request
from flask_restx import inputs

class Validators():
    def match_value(field) -> callable:
        def match(value) -> str:
            if not value == request.values[field]:
                raise ValueError(f'{field} não deu match!')
            return value
        return match
    
    def match_value_optional(field) -> callable:
        def match(value) -> str:
            if not request.values[field]:
                return ''
            if not value == request.values[field]:
                raise ValueError(f'{field} não deu match!')
            return value
        return match

    def email() -> inputs.regex:
        return inputs.regex(r'[\W|\D]+@[\W|\D]+.[\W|\D]+')