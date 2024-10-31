from flet import *


class AcceuilService:
    
    def __init__(self, page: Page):
        self.page=page
        self.page.adaptive = True
        self.container = self.AllHome()
        
        
        
        
    def AllHome(self):
        return Column(
                    controls=[
                        
                    ]
            
        )
            
        
    
    
    
    def run(self):
        self.page.add(self.container)
        


def main(page: Page):
    app = AcceuilService(page)
    app.run()
    
app(target=main)
    
    
        