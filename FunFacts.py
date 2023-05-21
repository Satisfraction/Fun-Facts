import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', 0)

class FunFacts(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        self.background_color = (1, 0.5, 0.5, 1)
        self.add_widget(Label(text='FunFacts', font_size=30, color=(1, 1, 1, 1)))
        self.fact_button = Button(text='Zeige mir einen FunFact!', font_size=20, background_color=(1, 1, 1, 1), size_hint=(1, 0.5))
        self.fact_button.bind(on_release=self.show_fact)
        self.add_widget(self.fact_button)
        self.fact_text = Label(text='', font_size=20, color=(1, 1, 1, 1))
        self.add_widget(self.fact_text)

    def show_fact(self, button):
        response = requests.get('https://uselessfacts.jsph.pl/random.json?language=de')
        if response.status_code == 200:
            fact = response.json()['text']
            self.fact_text.text = fact
        else:
            self.fact_text.text = 'Konnte keinen Fakt abrufen'

class FunFactsApp(App):
    def build(self):
        return FunFacts()

if __name__ == '__main__':
    FunFactsApp().run()
