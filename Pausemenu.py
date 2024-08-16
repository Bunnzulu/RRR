from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button


class PauseWidgets(RelativeLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

class HoverButtons(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_hover)

    def on_hover(self, window, pos):
        if self.collide_point(*pos):
            self.background_normal = ""
            self.background_color = (1.0,1.0,1.0,1)
            self.color = (0,0,0,1)
        else:
            self.background_color = (0,0,0,0)
            self.color = (1,1,1,1)
            self.background_normal = ""


if __name__ == "__main__":
    class PMenuApp(App):
        pass
    PMenuApp().run()