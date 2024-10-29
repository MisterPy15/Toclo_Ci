from flet import *


class Login:
    
    def __init__(self, page: Page):
        self.page = page
        self.page.adaptive = True
        self.container = self.AllLoginR()
       
        
    
    def AllLoginR(self):
        return Column(
                    controls=[
                            self.Form(),
            ]
        )
        
        
    def Form(self):
        return Container(
            content = Column( 
                              controls=[
                                    TextField(border_radius=30),
                                    
                                    TextField(border_radius=30),
                                    
                                    TextField(border_radius=30),
                                    
                                    TextField(border_radius=30),
                                    
                                    TextField(border_radius=30),
                    ]
                ),
        )
    
    
    
    
    def run(self):
        self.page.add(self.container)
        

def main(page : Page):
    app = Login(page)
    app.run()
    
app(target=main)