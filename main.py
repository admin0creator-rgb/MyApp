from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window

class ClickerGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=30, spacing=20, **kwargs)
        self.score = 0
        self.time_left = 10

        self.score_label = Label(text="Счёт: 0", font_size=40)
        self.time_label = Label(text="Время: 10", font_size=30)
        self.click_btn = Button(text="ЖМИ!", font_size=50, background_color=(0, 1, 0, 1))
        self.click_btn.bind(on_press=self.on_click)

        self.add_widget(self.score_label)
        self.add_widget(self.time_label)
        self.add_widget(self.click_btn)

        Clock.schedule_interval(self.tick, 1)

    def on_click(self, instance):
        if self.time_left > 0:
            self.score += 1
            self.score_label.text = f"Счёт: {self.score}"

    def tick(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.text = f"Время: {self.time_left}"
        else:
            Clock.unschedule(self.tick)
            self.click_btn.disabled = True
            self.click_btn.text = f"Игра окончена! Счёт: {self.score}"

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.2, 1)
        return ClickerGame()

if __name__ == "__main__":
    MyApp().run()