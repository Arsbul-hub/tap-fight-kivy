from kivy.config import Config
from kivy.config import Config

# 0 выключен 1 включен как true / false
# Вы можете использовать 0 или 1 && True или False
x,y = (640,480)
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', str(x))
Config.set('graphics', 'height', str(y))
# Импорт всех классов
from kivy.uix.gridlayout import GridLayout
import pickle
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
#Window.clearcolor = (1, 1, 1, 1)

# Глобальные настройки
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button

from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

class Menu(FloatLayout):
    def __init__(self):
        super().__init__()
        #self.f1 = Widget()
        self.size = (x,y)
        self.startb = Button(text="В бой", on_press=self.to_fight, size_hint=(.4,.2),
                                  pos_hint={"x":.5-.4/2,"y":.5-.2/2+.1})
        self.add_widget(self.startb)
        self.my_character_button = Button(text="Мой персонаж", on_press=self.my_character, size_hint=(.4,.2),
                                  pos_hint={"x":.5-.4/2,"y":.5-.2/2})
        self.add_widget(self.my_character_button)

        self.magasine = Button(text="Магазин", on_press=self.no_working, size_hint=(.4,.2),
                                  pos_hint={"x":.5-.4/2,"y":.5-.2/2})
        self.add_widget(self.magasine)
        self.edit_name_button = Button(text="Изменить имя", on_press=self.edit_name, size=(300, 100),
                                  pos=(5000, 5000))
        self.add_widget(self.edit_name_button)

        self.tap1 = Button(text="В бой", on_press=self.c1, size=(200, 200),
                                  pos=(5000,5000))
        self.add_widget(self.tap1)
        self.tap2 = Button(text="В бой", on_press=self.c2, size=(200, 200),
                                  pos=(5000,5000))
        self.add_widget(self.tap2)
        self.pb = ProgressBar(max=100, size=(600, 30), value=50, pos=(5000,5000))
        self.add_widget(self.pb)

        self.enter_name = TextInput(text='',size=(300,50),pos=(5000,5000), multiline=False)
        self.add_widget(self.enter_name)
        self.ok = Button(text="Ок", on_press=self.save_name, size=(50, 50),
                                  pos=(5000,5000))
        self.add_widget(self.ok)
        # create content and add to the popup
        self.iters = 0
        self.name_message = Label(text="Если ваше имя больше 8 симбволов, то сохранено будет только превые 8", size=(200, 100), pos=(5000,5000))
        self.add_widget(self.name_message)
        self.name = ""
        self.coins = 0
        self.name_label = Label(text="",size = (200,100),pos=(640 / 2 - (200/2),400))
        self.add_widget(self.name_label)
        self.coins_num = Label(text="", size=(200, 100), pos=(640 / 2 - (200/2)+200,400))
        self.add_widget(self.coins_num)
        self.add_widget(Label(text="Внимание! Это бета-версия игры Tap-Fight!",color=(1,0,0), size=(200, 100), pos=(640 / 2 - (200/2),0))
        )
        w = GridLayout(cols=1, padding=10)

        self.win_name = ""
        info_dialog_text = Label(text="")
        w.add_widget(info_dialog_text)

        info_dialog_button = Button(text='')
        w.add_widget(info_dialog_button)

        self.info_dialog = Popup(title="Итог", content=w, size_hint=(None, None), size=(400, 400))
        try:
            with open('player_data.pickle', 'rb') as f:
                data = pickle.load(f)
                self.name = data.get("name")
                self.coins = data.get("coins")
                self.name_label.text = f"Ваше имя: {self.name}"
                self.coins_num.text = f"Кол-во tap-коинов: {str(self.coins)}"
        except FileNotFoundError:
            self.edit_name("r")
            self.startb.pos = (5000,5000)
            self.my_character_button.pos = (5000, 5000)



        self.win_text = Label(text="", size=(500, 500), pos=(5000,5000))
        self.add_widget(self.win_text)

        self.win_flag = False



        #self.add_widget(self.pb)
        #f2.add_widget(self.f1)
        #return f2
    def no_working(self,t):
        w = GridLayout(cols=1, padding=10)

        info_dialog_text = Label(text='Пока это не работает.\nСпасибо за понимание.')
        w.add_widget(info_dialog_text)

        info_dialog_button = Button(text='Ок')
        w.add_widget(info_dialog_button)

        info_dialog = Popup(title="Извените", content=w, size_hint=(None, None), size=(400, 400))
        info_dialog.open()
        info_dialog_button.bind(on_press=info_dialog.dismiss)
    def my_character(self,t):
        self.my_character_button.pos = (5000, 5000)
        self.startb.pos = (5000,5000)
        self.magasine.pos = (5000,5000)
        self.edit_name_button.pos = (640 / 2 - (300/2), 480 / 2 - (100/ 2))


    def edit_name(self,t):
        self.magasine.pos = (5000,5000)
        self.name_message.pos = (640 / 2 - (300/2), 400)
        self.enter_name.pos = (640 / 2 - (300/2), 480 / 2 - (100/ 2)+100)
        self.ok.pos = (640 / 2 - (50 / 2), 480 / 2 - (50 / 2)-100)
        self.edit_name_button.pos = (5000,5000)
        self.name_label.pos = (5000, 5000)
    def save_name(self,t):

        self.name = self.enter_name.text[:8]


        with open('player_data.pickle', 'wb') as f:
                pickle.dump({"name":self.name,"coins":self.coins},f)
                self.name_label.text = self.name
                self.coins_num.text = str(self.coins)
        self.to_main_menu("t")

    def to_fight(self,t):
        self.startb.pos = (5000,5000)
        self.magasine.pos = (5000, 5000)
        self.my_character_button.pos = (5000, 5000)
        self.tap1.pos = (640 / 2 - (200 / 2) - 200, 480 / 2 - (480 / 2 / 2))
        self.tap2.pos = (640 / 2 - (200 / 2) + 200, 480 / 2 - (480 / 2 / 2))
        self.pb.pos = (640 / 2 - 600 / 2, 430)
        self.name_label.text = f"{self.name} против Наглеца"
        self.name_label.pos = (640 / 2 - (200/2),350)
        self.coins_num.pos = (5000,5000)

    def c1(self, t):


        if self.pb.value == 100:
            self.win_text.pos = (640 / 2 - (500/2), 480 / 2 - (500/ 2))
            self.win_text.text = f"Победил {self.name}!"
            self.win_name = self.name
            if self.win_flag == False:
                self.win_flag = True
        if self.win_flag == False:
            self.pb.value += 3
    def c2(self, t):

        if self.pb.value == 0:
            self.win_text.pos = (640 / 2 - (500 / 2), 480 / 2 - (500 / 2))
            self.win_text.text = "Победил Наглец!"
            self.win_name = "Наглец"
            if self.win_flag == False:
                self.win_flag = True
        if self.win_flag == False:
            self.pb.value -= 3
    #def start(self):
        # return btn1
    def to_main_menu(self,t):
        with open('player_data.pickle', 'wb') as f:
                pickle.dump({"name":self.name,"coins":self.coins},f)
                #self.name_label.text = self.name
                #self.coins_num.text = str(self.coins)
        self.info_dialog.dismiss()
        self.win_text.pos = (5000,5000)
        self.magasine.pos = (640 / 2 - (300/2), 480 / 2 - (100/ 2)-100)
        self.my_character_button.pos = (640 / 2 - (300 / 2), 480 / 2 - (100 / 2))
        self.startb.pos = (640 / 2 - (300/2), 480 / 2 - (100 / 2)+100)
        self.name_label.text = f"Ваше имя: {self.name}"
        self.name_label.pos = (640 / 2 - (200/2),400)
        self.coins_num.text = f"Кол-во коинов: {str(self.coins)}"
        self.coins_num.pos = (640 / 2 - (200 / 2) + 200, 400)
        self.tap1.pos = (5000, 5000)
        self.tap2.pos = (5000, 5000)
        self.pb.pos = (5000, 5000)
        self.enter_name.pos = (5000, 5000)
        self.ok.pos = (5000, 5000)

        self.name_message.pos = (5000,5000)
        self.pb.value = 50
    def loop(self,dt):
        if self.win_flag:
            self.iters += 1

            if self.iters > 3:
                if self.win_name == self.name:
                    k = "Вы получаете 1 tap-коин"
                    self.coins += 1
                else:
                    self.coins -= 1
                    k = "Вы теряете 1 tap-коин"
                #
                self.iters = 0
                w = GridLayout(cols=1, padding=10)

                info_dialog_text = Label(text=f'Выиграл {self.win_name}!!!\n{k}')
                w.add_widget(info_dialog_text)

                info_dialog_button = Button(text='Ок')
                w.add_widget(info_dialog_button)


                self.info_dialog = Popup(title="Итог", content=w, auto_dismiss=False, size_hint=(None, None),size=(400, 400))
                self.info_dialog.open()
                info_dialog_button.bind(on_press=self.to_main_menu)
                #self.to_main_menu("T")
                self.win_flag = False

class TapFight(App):


    def build(self):
        game = Menu()
        self.title = "Tap-Fight"
        Clock.schedule_interval(game.loop,1.0)
    #self.background_color=(1,0.1,0.1)
        return game

# Запуск проекта
if __name__ == "__main__":
    TapFight().run()