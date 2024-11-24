from flet import *



class Login:
    
    def __init__(self, page: Page):
        self.page = page
        self.page.adaptive=True
        self.container = self.AllLoginR()
       
        
    
    def AllLoginR(self):
        return Column(scroll="auto",
                    controls=[
                            self.Form(),
            ],alignment="center",
            horizontal_alignment="center"
        )
        
        
        
    def Form(self):
        return Container(
            content = Column(
                # scroll="auto",
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
                                    
                                    
                                    Container(height=180),
                    
                                    
                                    FilledButton(text="Conitnuer",
                                                 adaptive=True, 
                                                 width=150, 
                                                 style=ButtonStyle(
                                                                    color='white', 
                                                                    bgcolor='green',
                                                                    ))
                                    
                    ]
                ),
        )
    
    
    

    def run(self):
        self.page.add(self.container)
  
      

# def main(page : Page):
#     app = Login(page)
#     app.run()
    
# app(target=main)