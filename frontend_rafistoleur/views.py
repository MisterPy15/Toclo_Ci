from flet import *
from .Web.homePage import Home


def Views_handler(page):
    
    return{
        '/':View(
            route='/',
            controls=[
                Home(page)
            ]
            
        )
        
    }