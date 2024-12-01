from flet import *

class Confirmation:
    def __init__(self, page: Page):
        self.page = page
        self.container = self.AllLoginR()
    
    def AllLoginR(self):
        return Column(
            controls=[
                self.Form(),
            ],
        )
    
    def Form(self):
        return Container(
            content=Column(
                alignment='center',
                horizontal_alignment="center",
                controls=[
                    Container(height=40),
                    Image(src="https://i.postimg.cc/qM9RmW00/CO-TE-D-IVOIR-removebg-preview.png", 
                          height=150, width=150),
                    Container(height=20),
                    Text("SAISISSEZ LE CODE A 6 CHIFFRES", 
                         size=20, color="orange", weight='bold'),
                    Container(height=30),
                    Text("Nous avons envoyé un code au +225 {} \npar SMS", 
                         size=16),
                    Container(height=10),
                    TextField(
                        label="Code ",
                        border_radius=15,
                        border_width=3,
                        border_color="black",
                        keyboard_type="number"
                    ),
                    Container(height=180),
                    Text("Vous n'avez pas reçu ?",
                        spans=[TextSpan(text="00:00")]),
                    Container(height=10),
                    Row(
                        alignment='center',
                        controls=[
                            TextButton(
                                text="Renvoyer le code",
                                width=190,
                                icon=icons.SEND,
                                on_click=lambda e: print("Renvoyer"),
                                style=ButtonStyle(color='white', bgcolor='#808080')
                            ),
                            TextButton(
                                text="Envoyer Par SMS",
                                width=190,
                                icon=icons.MESSAGE,
                                on_click=lambda e : print("Envoyer par SMS"),
                                style=ButtonStyle(color='white', bgcolor='#808080')
                            ),
                        ]
                    ) 
                ]
            ),
        )


    def run(self):
        self.page.add(self.container)


def main(page : Page):
         app = Confirmation(page)
         app.run()
    
app(target=main)