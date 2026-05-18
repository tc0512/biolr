from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from pathlib import Path

# 字体
font_path = str(Path(__file__).parent / "fonts" / "NotoSansCJK-Regular.ttc")
if Path(font_path).exists():
    LabelBase.register(name='Chinese', fn_regular=font_path)
    font_name = 'Chinese'
else:
    font_name = 'Roboto'

sector = ["生物和细胞", "生物的类群", "植物的生活", "人体生理与健康", "生物与环境", "生命的延续和发展"]

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=3, rows=2, spacing=10, padding=10)
        for i in range(6):
            btn = Button(text=sector[i], font_name=font_name)
            btn.bind(on_press=lambda x, num=i: self.show_popup(num))
            layout.add_widget(btn)
        return layout

    def show_popup(self, button_num):
        if button_num==0:
            content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            close_btn = Button(text='返回', size_hint_y=None, height=50, font_name=font_name)
            action_btn1 = Button(text='认识生物', size_hint_y=None, height=50, font_name=font_name)
            action_btn2 = Button(text='认识细胞', size_hint_y=None, height=50, font_name=font_name)
            content.add_widget(action_btn1)
            content.add_widget(action_btn2)
            content.add_widget(close_btn)
            popup = Popup(title=sector[button_num], content=content, size_hint=(0.7, 0.5))
            popup.title_font = font_name
            close_btn.bind(on_press=popup.dismiss)
            action_btn1.bind(on_press=lambda x: self.btn_action(popup, button_num))
            action_btn2.bind(on_press=lambda x: self.btn_action(popup, button_num))
            popup.open()
        elif button_num==1:
            content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            close_btn = Button(text='返回', size_hint_y=None, height=50, font_name=font_name)
            action_btn1 = Button(text='藻类与植物的类群', size_hint_y=None, height=50, font_name=font_name)
            action_btn2 = Button(text='动物的类群', size_hint_y=None, height=50, font_name=font_name)
            content.add_widget(action_btn1)
            content.add_widget(action_btn2)
            content.add_widget(close_btn)
            popup = Popup(title=sector[button_num], content=content, size_hint=(0.7, 0.5))
            popup.title_font = font_name
            close_btn.bind(on_press=popup.dismiss)
            action_btn1.bind(on_press=lambda x: self.btn_action(popup, button_num))
            action_btn2.bind(on_press=lambda x: self.btn_action(popup, button_num))
            popup.open()
        elif button_num==2:
            content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            close_btn = Button(text='返回', size_hint_y=None, height=50, font_name=font_name)
            action_btn = Button(text='被子植物的一生', size_hint_y=None, height=50, font_name=font_name)
            content.add_widget(action_btn)
            content.add_widget(close_btn)
            popup = Popup(title=sector[button_num], content=content, size_hint=(0.7, 0.4))
            popup.title_font = font_name
            close_btn.bind(on_press=popup.dismiss)
            action_btn.bind(on_press=lambda x: self.btn_action(popup, button_num))
            #action_btn.bind(on_press=lambda x: self.btn_action(popup, button_num))
            popup.open()
        elif button_num==3:
            content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            close_btn = Button(text='返回', size_hint_y=None, height=50, font_name=font_name)
            action_btn = Button(text='人的生殖和发育', size_hint_y=None, height=50, font_name=font_name)
            content.add_widget(action_btn)
            content.add_widget(close_btn)
            popup = Popup(title=sector[button_num], content=content, size_hint=(0.7, 0.4))
            popup.title_font = font_name
            close_btn.bind(on_press=popup.dismiss)
            action_btn.bind(on_press=lambda x: self.btn_action(popup, button_num))
            popup.open()
        elif button_num==4:
            content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            close_btn = Button(text='返回', size_hint_y=None, height=50, font_name=font_name)
            action_btn = Button(text='生态系统', size_hint_y=None, height=50, font_name=font_name)
            content.add_widget(action_btn)
            content.add_widget(close_btn)
            popup = Popup(title=sector[button_num], content=content, size_hint=(0.7, 0.4))
            popup.title_font = font_name
            close_btn.bind(on_press=popup.dismiss)
            action_btn.bind(on_press=lambda x: self.btn_action(popup, button_num))
            popup.open()
        elif button_num==5:
            content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            close_btn = Button(text='返回', size_hint_y=None, height=50, font_name=font_name)
            action_btn = Button(text='无性生殖', size_hint_y=None, height=50, font_name=font_name)
            content.add_widget(action_btn)
            content.add_widget(close_btn)
            popup = Popup(title=sector[button_num], content=content, size_hint=(0.7, 0.4))
            popup.title_font = font_name
            close_btn.bind(on_press=popup.dismiss)
            action_btn.bind(on_press=lambda x: self.btn_action(popup, button_num))
            popup.open()
    def btn_action(self, popup, button_num):
        popup.dismiss()

if __name__ == "__main__":
    MyApp().run()
