from flet import *



class Login:
    def __init__(self, page: Page):
        self.page = page
        self.Noir = "#000"
        self.Blanc = "#FFF"
        self.Bleu = "#1E90FF"
        
        self.page.title = "Rafistoleur"
        self.page.theme_mode = ThemeMode.LIGHT
        self.page.padding = 20
        self.container = self.loginAll()
        
    
    
    def loginAll(self):
            return Column(
                        controls=[
                            self.login_screen()
                            
                        ]
            )


    def login_screen(self):
        return Column(
            controls=[
                Container(
                    content=Text(
                        "Login",
                        size=30,
                        weight="bold",
                        color=self.Bleu,
                    ),
                    alignment=alignment.center,
                ),
                TextField(
                    label="Email",
                    width=300,
                    border_color=self.Bleu,
                ),
                TextField(
                    label="Mot de passe",
                    width=300,
                    password=True,
                    can_reveal_password=True,
                    border_color=self.Bleu,
                ),
                ElevatedButton(
                    text="Se connecter",
                    width=300,
                    bgcolor=self.Bleu,
                    color=self.Blanc,
                    on_click=self.on_login_click,
                ),
                TextButton(
                    text="Créer un compte",
                    on_click=self.on_create_account_click,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            spacing=20,
        )



    def on_login_click(self, e):
        # Logique pour se connecter
        print("Connexion réussie")



    def on_create_account_click(self, e):
        print("Créer un compte")
        
        
        
    def run(self):
        self.page.add()



def main(page: Page):
    app = Login(page)

app(target=main)
