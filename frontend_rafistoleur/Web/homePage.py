from flet import *

class Home:
    def __init__(self, page: Page):
        self.page = page
        self.page.bgcolor = "white"
        self.container = self.HomePageContainer()
      
      
        
    def HomePageContainer(self):
        return Column(
            controls=[
                self.navBar(),
                self.Header(),
                self.ServicePresentation(),
                self.Partenariats(),
                self.Categories(),
                self.LieuxPresences(),
                self.DevenirMembre(),
                self.Footer(),
            ]
        )
    
    
    
    def navBar(self):
        return  Container(height=50, bgcolor='orange',
                            content =
                                    Row(
                                        controls = [
                                                    Container(width=20),
                                                    Image(src = "https://i.postimg.cc/9QDCd0Zf/Rafisto-Ci.png", 
                                                        height=40, 
                                                        width=40, 
                                                        border_radius=30),
                                                    
                                                    self.menuOption("Client"),
                                                    self.menuOption("Toclo"),
                                                    self.menuOption("À Propos"),
                                                    self.menuOption("Ouvrir dans le navigateur"),
                            ],
                            spacing='50',
                            alignment="center"
                            
                        )
                    )
        
    
    
    def menuOption(self, text):
        return Container(
            Text(
            text,
            color="white",
            size=20,
            font_family='poppins',
            weight='bold',
        ),
            on_click =lambda e: self.navigate(text)
        )


    def navigate(self, destination):
        print(f"Navigation vers {destination}")

   
   
   
        
    def Header(self):
        return Row(
            controls=[
                # Text("Bienvenue à Rafistoleur", size=24, weight="bold")
            ]
        )
    
    
    
    def ServicePresentation(self):
        return Row(
            controls=[
                # Text("Présentation des services")
            ]
        )
    
    
    
    def Partenariats(self):
        return Row(
            controls=[
                # Text("Nos Partenariats")
            ]
        )
    
    
    
    def Categories(self):
        return Row(
            controls=[
                # Text("Catégories")
            ]
        )
    
    
    
    def LieuxPresences(self):
        return Row(
            controls=[
                # Text("Présence géographique")
            ]
        )
    
    
    
    
    def DevenirMembre(self):
        return Row(
            controls=[
                # Text("Devenez membre")
            ]
        )
    
    
    
    def Footer(self):
        return Row(
            controls=[
                # Text("Pied de page")
            ]
        )



    # Méthode Déclencheur
    def run(self):
        self.page.add(self.container)
    
     
# Ma fonction principale qui crée une instance pour
# Home et fait appel à run pour afficher le contenu de la page      
def main(page: Page):
    app = Home(page)
    app.run()

app(target=main)
