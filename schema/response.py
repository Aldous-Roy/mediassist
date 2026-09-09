from typing import Any


def _response(code: int, message: str, body: Any = None):
    return {
        "status": {
            "success": 200 <= code < 300,
            "code": code,
            "message": message
        },
        "body": body if body is not None else {}
    }


def success(body: Any = None, message: str = "Request successful"):
    return _response(200, message, body)


def created(body: Any = None, message: str = "Created successfully"):
    return _response(201, message, body)


def bad_request(message: str = "Bad request"):
    return _response(400, message)


def unauthorized(message: str = "Unauthorized"):
    return _response(401, message)


def forbidden(message: str = "Forbidden"):
    return _response(403, message)


def not_found(message: str = "Resource not found"):
    return _response(404, message)


def server_error(message: str = "Internal server error"):
    return _response(500, message)