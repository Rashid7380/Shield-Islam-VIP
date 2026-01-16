from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ShieldApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.add_widget(Label(text='🛡️ درع الاســـــــــــلام 𝑽𝑰𝑷_1', font_size='24sp', color=(0, 1, 0, 1)))
        
        # أزرار المهام الدفاعية
        btn1 = Button(text='تطهير الصور (Exif)', background_color=(0, 0.7, 0, 1))
        self.add_widget(btn1)
        
        btn2 = Button(text='فحص الشبكة (Nmap)', background_color=(0, 0.7, 0, 1))
        self.add_widget(btn2)
        
        btn3 = Button(text='توليد كلمة سر VIP', background_color=(0, 0.7, 0, 1))
        self.add_widget(btn3)

class VIPApp(App):
    def build(self):
        return ShieldApp()

if __name__ == '__main__':
    VIPApp().run()
