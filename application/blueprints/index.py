from flask import Blueprint
from .urls import urls

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>', methods=("GET",))
def catch_all(path):
    path_address = path.split("/")
    print(path_address)
    if len(path_address) > 1:
        address = urls["/" + path_address[0]]["/" + path_address[1]]

    else:
        if path_address[0] == '':
            path_address[0] = 'home'

        address = urls['/main']['/' + path_address[0]]

    return address
