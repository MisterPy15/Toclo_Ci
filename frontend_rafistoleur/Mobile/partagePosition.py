from flet import *

class GeoLocalisation:
    
    def __init__(self, page: Page):
        self.page = page
        self.page.adaptive = True
        self.container = self.GeoLocal()
    
    def GeoLocal(self):
        return Column(
            controls=[
                Container(height=50),
                Image(src="https://i.postimg.cc/qM9RmW00/CO-TE-D-IVOIR-removebg-preview.png",
                      height=150, 
                      width=150
                ),
                Text('PARTAGEZ VOTRE POSITION POUR QU\'ON VOUS PROPOSE LES MEILLEURS TOCLOS À PROXIMITÉ'),
                ElevatedButton("Obtenir ma position", on_click=self.get_location),  # Ajouter un bouton
                Text("", key="location_text")  # Utiliser key pour identifier
            ]
        )
    
    async def get_location(self, e):
        try:
            position = await Geolocator.get_current_position(
                accuracy=GeolocatorPositionAccuracy.LOWEST  # Utiliser une précision valide
            )
            location_text = self.page.get_control("location_text")  # Accéder au contrôle par sa clé
            if location_text:  # Vérifier si le contrôle existe
                location_text.value = f"Latitude: {position.latitude}, Longitude: {position.longitude}"
                self.page.update()
            else:
                print(f"Erreur: le contrôle 'location_text' n'a pas été trouvé.")
        except Exception as ex:
            # Afficher une erreur si la localisation échoue
            location_text = self.page.get_control("location_text")  # Accéder au contrôle par sa clé
            if location_text:  # Vérifier si le contrôle existe
                location_text.value = f"Erreur: {str(ex)}"
                self.page.update()
            else:
                print("Erreur: le contrôle 'location_text' n'a pas été trouvé.")
    
    def run(self):
        self.page.add(self.container)
     
def main(page: Page):
    app = GeoLocalisation(page)
    app.run()
    
app(target=main)
