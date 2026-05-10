from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from pathlib import Path
font_path = str(Path(__file__).parent / "fonts" / "NotoSansCJK-Regular.ttc")
LabelBase.register(name='Chinese', fn_regular=font_path)
sector = ["生物和细胞", "生物的类群", "植物的生活", "人体生理与健康", "生物与环境", "生命的延续和发展"]
class MyApp(App):
    def build(self):
        # 创建 3 行 2 列的网格
        layout = GridLayout(cols=3, rows=2, spacing=10, padding=10)
        # 添加 6 个按钮
        for i in range(6):
            btn = Button(text=sector[i], font_name='Chinese')
            layout.add_widget(btn)
        return layout

MyApp().run()
