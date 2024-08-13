from kivy.app import App
from kivy.uix.widget import Widget
import pytmx


class MapWidget(Widget):
    pass



if __name__ == "__main__":
    class MapApp(App):
        def build(self):
            return MapWidget()

    MapApp().run()