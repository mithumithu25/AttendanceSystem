from  kivy.app import App
from kivy.uix.button import Button
#python3  kivy==2.0.0 kivymd,pillow
class Main_App(App):
    def build(self):
        btn=Button(text="Click Me",size_hint=(0.2,0.3),pos_hint={"center_x":0.5,"center_y":0.5})
        return btn
Main_App().run()
#https://youtu.be/Saa35hSATNo?si=nEsfF9M0cSmFHSce
