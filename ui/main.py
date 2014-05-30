from kivy.app import App
from kivy.uix.widget import Widget

class TbnWidget(Widget):
    pass

class TbnApp(App):
    def build(self):
        return TbnWidget()

if __name__ == '__main__':
    TbnApp().run()