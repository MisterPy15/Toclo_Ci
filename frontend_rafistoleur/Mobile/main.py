from flet import *
from loads import Loading
from login import Login
from SmsConfirm import Confirmation
import loads


def main(page:Page):
    def route_change(route):
        page.views.clear()
        
        if page.route == "/":
            loadin_app = Loading(page)
            
            page.views.append(
                View(
                    route="/",
                    controls=[loadin_app.container]
                )
            )
        
        
        
        elif page.route == "/confirmation":
            confirmation_app = Confirmation(page)
            
            page.views.append(
                
                View(
                    route="/",
                    controls=[confirmation_app.container]
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

app(target=loads.main)