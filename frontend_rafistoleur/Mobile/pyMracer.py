from py_mini_racer import py_mini_racer

class Page:
    def __init__(self):
        self.context = py_mini_racer.MiniRacer()

    def eval_js(self, js_code):
        try:
            result = self.context.eval(js_code)
            return result
        except Exception as e:
            return str(e)

# Exemple d'utilisation
page = Page()
js_code = "2 + 2"
print(page.eval_js(js_code))  # Affiche 4
