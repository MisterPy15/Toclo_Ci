from flet import *
import asyncio



class Login:
    
    def __init__(self, page: Page):
        self.page = page
        self.page.adaptive = True
        self.container = self.AllLoginR()


    def AllLoginR(self):
        return Container(
            content=Column(
                scroll=ScrollMode.ALWAYS,
                controls=[
                    Container(height=20),
                    self.back_interface(),
                    self.Form(),
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )


    def back_interface(self):
        return Container(
            content=Row(
                controls=[
                    IconButton(icon=icons.ARROW_BACK,
                               icon_color="white",
                               icon_size=30, on_click=self.quit_app_for_back_interface),
                ]
            )
        )


    def quit_app_for_back_interface(self, e):
        self.page.window_close()


    def Form(self):
        return Container(
            content=Column(
                scroll="auto",
                alignment='center',
                horizontal_alignment="center",
                controls=[
                    Container(height=40),
                    Image(src="https://i.postimg.cc/qM9RmW00/CO-TE-D-IVOIR-removebg-preview.png",
                          height=150,
                          width=150),
                    Container(height=20),
                    Text(" Entrez Votre Numéro de \n             Téléphone",
                         size=28,
                         color="orange",
                         weight='bold',
                         ),
                    Container(height=30),
                    Text("Nous enverrons un code de Confirmation à ce \n                            numéro",
                         size=16),
                    Container(height=10),
                    TextField(label="Tel ",
                              border_radius=15,
                              border_width=3,
                              border_color="black",
                              keyboard_type="number"),
                    Container(height=100),
                    FilledButton(text="Continuer",
                                 width=210,
                                 on_click=None,
                                 style=ButtonStyle(
                                     color='white',
                                     bgcolor='green',
                                 ))
                ]
            ),
        )

    # async def nextPage(self, e):
    #     self.page.add(self.container)
    #     self.page.clean()
    #     self.page.update()
    #     await Confirmation(self.page).run()

    def run(self, ):
        self.page.add(self.container)
       
  
  
  
# def main(page : Page):
#         app = Confirmation(page)
#         app.run()
    
# app(target=main)