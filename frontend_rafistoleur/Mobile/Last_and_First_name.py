from flet import *
import time



class InfoUser:
    
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
                        content = Column(
                                        alignment='center',
                                        horizontal_alignment="center",
                                        controls=[
                                                Container(height=40),
                                                
                                                Image(src="https://i.postimg.cc/qM9RmW00/CO-TE-D-IVOIR-removebg-preview.png", 
                                                    height=150,
                                                    width=150),
                                                
                                                Container(height=20),
                                                
                                                Text(" SAISISSEZ VOTRE NOM", 
                                                    size=20, 
                                                    color="orange",
                                                    weight='bold',
                                                    ),
                                                
                                                Container(height=30),
                                                
                                                
                                                Text("""Veuillez utiliser votre véritable nom afin que  
                                                        les rafistoleurs puissent vous plus facilement 
                                                        augmentant ainsi la sécurité de vos commandes.""", 
                                                    size=14),
                                                
                                                Container(height=10),
                                                
                                                
                                                TextField(label="Prénom",
                                                        
                                                        border_radius=15,
                                                        border_width=3,
                                                        border_color="black",
                                                        keyboard_type="number"),
                                                
                                                
                                                
                                                TextField(label="Nom",
                                                        
                                                        border_radius=15,
                                                        border_width=3,
                                                        border_color="black",
                                                        keyboard_type="number"),
                                                
                                                
                                                Container(height=150),
                        
                        Container(height=10),
                                                
                        Row(
                            alignment='center',
                            # horizontal_alignment="center",
                            controls=[
                                                        
                                    TextButton(text="Renvoyer le code",
                                                adaptive=True, 
                                                width=190,
                                                icon=icons.SEND, 
                                                on_click=lambda e: print("Renvoyer"),
                                                style=ButtonStyle(
                                                                    color='white', 
                                                                    bgcolor='#808080',
                                                    )
                                                ),
                                                            
                                    TextButton("Envoyer Par SMS",
                                                adaptive=True, 
                                                width=190,
                                                icon = icons.MESSAGE,
                                                on_click=lambda e : print("Envoyer par SMS"),
                                                style=ButtonStyle(
                                                        color='white', 
                                                        bgcolor='#808080',
                            )
                        ),
                    ]
                ) 
            ]
        ),
    )
    
    
    

    def run(self):
        self.page.add(self.container)
  
      

def main(page : Page):
    app = InfoUser(page)
    app.run()
    
app(target=main)