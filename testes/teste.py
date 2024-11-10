from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text='Olá, Kivy!')
        self.layout.add_widget(self.label)
        
        self.button = Button(text='Clique aqui!')
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        return self.layout

    def on_button_press(self, instance):
        self.label.text = 'Você clicou no botão!'

if __name__ == '__main__':
    MyApp().run()