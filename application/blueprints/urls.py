from .website.app_main.urls import urls_main
from .website.app_register.urls import urls_register

urls = {
    "/main": urls_main,
    "/register": urls_register,
}
