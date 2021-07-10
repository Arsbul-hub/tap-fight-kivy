from kivy.config import Config
from kivy.config import Config

# 0 выключен 1 включен как true / false
# Вы можете использовать 0 или 1 && True или False
x = 640
y = 480
Config.set('graphics', 'resizable', True)
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
class Open_popup(Popup):
    def __init__(self):
        super().__init__()
        t = Widget()
        t.add_widget(Label(text="4", size_hint=(None,None), pos=(0,0)))
from kivy.lang import Builder


#В этом приложении будет несколько экранов
#на каждом из экранов будет свой способ позиционирования элементов

#Загружаю разметку
#Builder.load_string()
class Menu(FloatLayout):
    def __init__(self):
        super().__init__()
        #self.f1 = Widget()
        self.size=(x,y)
        #f2 = BoxLayout()
        #self.orientation = "horizontal"
        self.size = (x,y)
        #print(self.size)
        self.nsize = (.3, .2)
        self.poses = {"fight":{"x": .5 - self.nsize[0]/2, "y": .5 - self.nsize[1]/2 + .2},
                      "you":{"x": .5 - self.nsize[0]/2, "y": .5 - self.nsize[1]/2},
                      "store":{"x": .5 - self.nsize[0]/2, "y": .5 - self.nsize[1]/2 - .2},
                      "tap1":{"x":0,"y":.4},
                      "tap2":{"x":.8,"y":.4},
                      "db":{"x":.5 - 0.7/2,"y": .8},
                      "edit_name": {"x": .5 - self.nsize[0]/2 / 2, "y": .5 - self.nsize[1]/2 / 2},
                      "enter_name":{"x": .5 - .2, "y": .7 - .2 / 2},
                      "ok":{"x": .5 - 0.3 / 2, "y": .4 - 0.2 / 2},
                      "your_name":{"x": .5 - 0.2 / 2, "y": .9 - 0.1 / 2},
                      "vs": {"x": .5 - 0.2 / 2, "y": .7 - 0.1 / 2},
                      }
        self.fight = Button(text="В бой", on_press=self.to_fight,size_hint=self.nsize,
                             pos_hint=self.poses.get("fight")
                             )
        self.add_widget(self.fight)
        self.you = Button(text="Вы", on_press=self.to_you,size_hint=self.nsize,
                             pos_hint=self.poses.get("you")
                             )
        self.add_widget(self.you)
        self.store = Button(text="Магазин", on_press=self.to_store,size_hint=self.nsize,
                             pos_hint=self.poses.get("store")
                             )
        self.add_widget(self.store)
        self.tap1 = Button(text="В бой", on_press=self.c1, size_hint=(.2, .2),
                                  pos_hint={"x":2,"y":2})
        self.add_widget(self.tap1)

        self.db = ProgressBar(max=100, size_hint=(.7, .1), value=50, pos_hint={"x":2,"y":2})
        self.add_widget(self.db)
        self.tap2 = Button(text="В бой", on_press=self.c2, size_hint=(.2, .2),
                                  pos_hint={"x":2,"y":2})
        self.add_widget(self.tap2)
        #self.to_main_menu()
        self.edit_name = Button(text="Изменить имя", on_press=self.to_edit_name, size_hint=(.2, .2),
                                  pos_hint={"x":2,"y":2})
        self.add_widget(self.edit_name)
        self.ok = Button(text="Ок", on_press=self.to_ok, size_hint=(.3, .2),
                                  pos_hint={"x":2,"y":2})
        self.add_widget(self.ok)
        self.enter_name = TextInput(text='',pos_hint={"x":2,"y":2},size_hint=(.4,.2), multiline=False)
        self.add_widget(self.enter_name)
        self.your_name = Label(text="", size_hint=(.2, .1), pos_hint=self.poses.get("your_name"))
        self.add_widget(self.your_name)
        self.vs = Label(text="", size_hint=(.2, .1), pos_hint=self.poses.get("vs"))
        self.add_widget(self.vs)

        self.tik = 0
        self.win_flag = False
        try:
            with open('player_data.pickle', 'rb') as f:
                data = pickle.load(f)
                self.name = data
                self.your_name.text = f"Ваше имя: {self.name}"

        except:
            self.you.pos_hint = {"x": 2, "y": 2}
            self.store.pos_hint = {"x": 2, "y": 2}
            self.fight.pos_hint = {"x": 2, "y": 2}
            self.your_name.pos_hint = {"x": 2, "y": 2}

            self.to_edit_name("r")
        #self.add_widget(self.pb)
    def to_you(self,t):
        self.your_name.pos_hint = {"x":2,"y":2}
        self.you.pos_hint= {"x":2,"y":2}
        self.store.pos_hint = {"x": 2, "y": 2}
        self.fight.pos_hint = {"x": 2, "y": 2}

        self.edit_name.pos_hint= self.poses.get("edit_name")
    def to_edit_name(self,t):

        self.edit_name.pos_hint= {"x":2,"y":2}
        self.enter_name.pos_hint  = self.poses.get("enter_name")
        self.ok.pos_hint = self.poses.get("ok")
    def to_ok(self,t):
        self.save_name()

        self.you.pos_hint = self.poses.get("you")
        self.store.pos_hint = self.poses.get("store")
        self.fight.pos_hint = self.poses.get("fight")
        self.ok.pos_hint = {"x":2,"y":2}
        self.enter_name.pos_hint = {"x":2,"y":2}
        self.your_name.pos_hint = self.poses.get("your_name")
        self.your_name.text = f"Ваше имя: {self.name}"
        #self.to_you("1")
    def save_name(self):
        self.name = self.enter_name.text[:8]
        with open('player_data.pickle', 'wb') as f:
                pickle.dump(self.name,f)
    def to_store(self, t):
        pass
    def to_fight(self,t):
        self.fight.pos_hint={"x":2,"y":2}
        self.you.pos_hint = {"x": 2, "y": 2}
        self.store.pos_hint = {"x": 2, "y": 2}
        self.your_name.pos_hint = {"x": 2, "y": 2}
        self.vs.pos_hint = self.poses.get("vs")
        self.vs.text = f"{self.name} против Наглеца"
        self.tap2.pos_hint =self.poses.get("tap2")
        self.tap1.pos_hint=self.poses.get("tap1")
        self.db.pos_hint=self.poses.get("db")


    def c1(self, t):

        self.db.value += 3
        if self.db.value == 100:
            self.win_name = self.name
            self.win_flag = True

    def c2(self, t):
        self.db.value -= 3
        if self.db.value == 0:
            self.win_name = "Наглец"
            self.win_flag = True

    #def start(self):
        # return btn1
    def to_main_menu(self,t):
        self.info_dialog.dismiss()
        self.vs.pos_hint = {"x": 2, "y": 2}
        self.your_name.pos_hint = self.poses.get("your_name")
        self.fight.pos_hint=self.poses.get("fight")
        self.you.pos_hint = self.poses.get("you")
        self.store.pos_hint = self.poses.get("store")
        self.tap2.pos_hint = {"x": 2, "y": 2}
        self.tap1.pos_hint={"x":2,"y":2}
        self.db.pos_hint={"x":2,"y": 2}



        self.db.value = 50
    def loop(self,dt):
        if self.win_flag:
            #self.tik += 1
            #if self.tik == 3
                # open popup
            w = GridLayout(cols=1, padding=10)

            info_dialog_text = Label(text=f'Выиграл {self.win_name}!!!')
            w.add_widget(info_dialog_text)

            info_dialog_button = Button(text='Ок')
            w.add_widget(info_dialog_button)

            self.info_dialog = Popup(title="Итог", content=w, auto_dismiss=False, size_hint=(.9, .9))
            self.info_dialog.open()
            info_dialog_button.bind(on_press=self.to_main_menu)
            #self.tik = 0
            self.win_flag = False

class TapFight(App):


    def build(self):
        game = Menu()
        self.title = "Tap-Fight"
        Clock.schedule_interval(game.loop, 1.0/60)

    #self.background_color=(1,0.1,0.1)
        return game

# Запуск проекта
if __name__ == "__main__":
    TapFight().run()