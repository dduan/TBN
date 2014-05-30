from kivy.app import App
from kivy.uix.widget import Widget

class MyPaintWidigt(Widget):
    pass

class MyPaintApp(App):
    def build(self):
        return MyPaintWidigt()

if __name__ == '__main__':
    MyPaintApp().run()