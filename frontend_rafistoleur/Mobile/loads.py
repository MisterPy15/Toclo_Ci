from flet import *
import asyncio
from login import Login





class Loading:
    def __init__(self, page: Page):
        self.page = page
        self.page.adaptive=True
        self.container = self.allLoads()
    
    def allLoads(self):
        return Column(
            controls=[
                Container(height=200),
                ProgressRing(color="orange"),
                Container(height=50),
                
                Image(src="https://i.postimg.cc/qM9RmW00/CO-TE-D-IVOIR-removebg-preview.png",
                      height=200, width=200)
                
            ],
            alignment="center",
            horizontal_alignment="center"
        )
    
    
    
    async def start_loading(self):
        self.page.add(self.container)
        await asyncio.sleep(5)
        self.page.clean()
        self.page.update()
        Login(self.page).run()
    
    
   
    def run(self):
        asyncio.run(self.start_loading())


def main(page: Page):
    app = Loading(page)
    app.run()


app(target=main)
