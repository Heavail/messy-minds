import random
import os
import time
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivy.clock import Clock
import string
let = ''
for i in string.printable:
    let += i
print(let)
string.printable = '!1"#$%&2()*z0+ya,x-b.4w/cv:9;d<ue=tf3>g?@h8[i\j6]k^_l5m`n{o|p7q}r~s'
class Screen1(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0.2,0.2,0.2,)
        # self.bck = Image(source = 'background.PNG',size_hint = (1,1),allow_stretch = True,keep_ratio = False)
        self.App_name = MDLabel(
            text = 'Messy Minds',
            halign = 'center',
            pos_hint = {'center_x': 0.5,'center_y' : 0.9},
            font_style = 'H2',
            italic = True,
            theme_text_color = 'Custom',
            text_color = 'gold'
        )
        self.help = MDRaisedButton(
            text = 'How to Play ?',
            pos_hint = {'center_x': 0.9,'center_y': 0.9},
            md_bg_color = (0,0,0,1),
            text_color = 'white',
            on_press = self.help_dialogue
        )
        easy = MDFillRoundFlatButton(
            text = 'EASY',
            pos_hint = {'center_x':0.5,'center_y':0.7},
            md_bg_color = (0,1,0,0.7),
            theme_text_color = 'Custom',
            text_color = 'black',
            on_press = self.switch
        )
        medium = MDFillRoundFlatButton(
            text = 'MEDIUM',
            pos_hint = {'center_x':0.5,'center_y':0.6},
            md_bg_color = (1,1,0,0.7),
            theme_text_color = 'Custom',
            text_color = 'black',
            on_press = self.switch1
        )
        hard = MDFillRoundFlatButton(
            text = 'HARD',
            pos_hint = {'center_x':0.5,'center_y':0.5},
            md_bg_color = (1,0.6,0,0.7),
            theme_text_color = 'Custom',
            text_color = 'black',
            on_press = self.switch2
        )
        extreme = MDFillRoundFlatButton(
            text = 'EXTREME',
            pos_hint = {'center_x':0.5,'center_y':0.4},
            md_bg_color = (1,0,0,0.7),
            theme_text_color = 'Custom',
            text_color = 'black',
            on_press = self.switch3
        )
        self.num = 0
        # self.add_widget(self.bck)
        self.add_widget(self.help)
        self.add_widget(easy)
        self.add_widget(medium)
        self.add_widget(hard)
        self.add_widget(extreme)
        self.add_widget(self.App_name)
    def help_dialogue(self,instance):
        self.dialog = MDDialog(
            title = 'How to Play ?',
            text = '''This is a memory based game. Once you select the difficulty level you will be shown few texts in white after a timer. You have to remember those texts and write them down in the input box. Correct text will increase your score. So play and increase your memory.
            
            Note:- THE GAME IS CASE SENSITIVE SO TREAT CAPITAL AND SMALL LETTERS DIFFERENTLY... ''',
            pos_hint = {'center_x':0.5,'center_y':0.5},
            buttons=[
                MDRaisedButton(
                    text="CLOSE",
                    on_release=lambda x: self.dialog.dismiss()
                ),
            ],
        )
        self.dialog.open()
        pass
    def switch(self,instance):
        self.level = Screen2(string.digits,name = 'Screen2')
        self.manager.add_widget(self.level)
        self.manager.current = 'Screen2'
    def switch1(self,instance):
        self.level = Screen2(string.ascii_letters,name = 'Screen2')
        self.manager.add_widget(self.level)
        self.manager.current = 'Screen2'
    def switch2(self,instance):
        self.level = Screen2(string.ascii_letters+string.digits,name = 'Screen2')
        self.manager.add_widget(self.level)
        self.manager.current = 'Screen2'
    def switch3(self,instance):
        self.level = Screen2(string.printable,name = 'Screen2')
        self.manager.add_widget(self.level)
        self.manager.current = 'Screen2'
class Screen2(MDScreen):
    def __init__(self,lis,**kwargs):
        super().__init__(**kwargs)
        # self.bck = Image(source = 'background.PNG',size_hint = (1,1),allow_stretch = True,keep_ratio = False)
        self.lis = lis
        self.setup()
    def setup(self):
        self.md_bg_color = (0.2,0.2,0.2,1)
        self.variables()
        self.asked = False
        self.App_name = MDLabel(
            text = str(self.num),
            halign = 'center',
            pos_hint = {'center_x': 0.5,'center_y' : 0.5},
            font_style = 'H2',
            italic = True,
            theme_text_color = 'Custom',
            text_color = 'gold'
        )
        # self.add_widget(self.bck)
        self.add_widget(self.App_name)
    def on_enter(self):
        self.clear_widgets()
        self.setup()
        Clock.schedule_interval(self.timer, 1)
    def variables(self):
        self.word = ''
        self.digits = 0
        self.num = 3
        self.run = True
        self.dig = 0
        self.ask = False
        self.number = ''

    def timer(self,time):
        if self.num > 0:
            self.num -= 1
            self.App_name.text = str(self.num)
        else:
            Clock.unschedule(self.timer)
            self.on_num()
    def on_num(self):
        Clock.schedule_interval(self.generate_num,0.5)
    def working(self,instance):
        # self.input_text.text = ''
        if self.input_text.text == self.word:
            self.App_name.text_color = 'green'
            self.App_name.text = 'Correct!'
            self.digits += 1
        else:
            Clock.unschedule(self.generate_num)
            self.switchs()
        self.ask = False
    def switchs(self):
        self.output = Screen3(self,self.word,self.input_text.text,self.digits,name = 'screen3')
        self.output.word = self.word
        self.output.typed = self.input_text.text
        self.output.digits = self.digits
        self.manager.add_widget(self.output)
        self.manager.current = 'screen3'
    def generate_num (self,instance):
        if self.run == True and self.ask == False:
            self.App_name.text_color = 'white'
            char = random.choice(self.lis)
            self.word += str(char)
            self.dig = 0
            self.dis = ''
        if self.dig < len(self.word):
            self.run = False
            self.dis = self.word[:self.dig + 1]
            self.dig += 1
        else:
            self.run = True
        if self.ask == True:
            if self.asked == False:
                self.input_text = MDTextField(
                hint_text = 'Enter the text: ',
                hint_text_color = (1,0,0,1),
                pos_hint = {'center_x': 0.5,'center_y': 0.2},
                size_hint = (0.5,0.5)
                )
                self.add_widget(self.input_text)
                self.asked = True
            self.input_text.focus = True
            self.input_text.bind(on_text_validate = self.working)
        else:
            try:
                self.input_text.text = ''
    
            except:
                pass
            self.App_name.text = self.dis

            if self.run == True:
                self.App_name.text = ''
                self.ask = True
class Screen3(MDScreen):
    def __init__(self,screen,word,typed,digits,**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.word = word
        self.typed = typed
        self.digits = digits
        # self.bck = Image(source = 'background.PNG',size_hint = (1,1),allow_stretch = True,keep_ratio = False)
        self.main()
    def main(self):
        self.md_bg_color = (0,0,0,1)
        self.game_over = MDLabel(text = 'GAME OVER',
        halign = 'center',
        pos_hint = {'center_x':0.5,'center_y':0.9},
        font_style = 'H1',
        italic = True,
        theme_text_color = 'Custom',
        text_color = 'white'
        )
        self.your_text = MDLabel(text = f'Incorrect: {self.typed}',
        halign = 'center',
        pos_hint = {'center_x':0.5,'center_y':0.4},
        font_style = 'H3',
        italic = True,
        theme_text_color = 'Custom',
        text_color = 'red'
        )
        self.correct_text = MDLabel(text = f'Correct: {self.word}',
        halign = 'center',
        pos_hint = {'center_x':0.5,'center_y':0.5},
        font_style = 'H3',
        italic = True,
        theme_text_color = 'Custom',
        text_color = 'green'
        )
        self.score = MDLabel(text = f'Score: {self.digits}',
        halign = 'center',
        pos_hint = {'center_x':0.5,'center_y':0.6},
        font_style = 'H3',
        italic = True,
        theme_text_color = 'Custom',
        text_color = 'white'
        )
        self.play_again = MDFillRoundFlatButton(
            text = 'continue',
            pos_hint = {'center_x':0.4,'center_y':0.2},
            md_bg_color = (0,1,0,1),
            theme_text_color = 'Custom',
            text_color = 'white',
            on_press = self.switch1
        )
        self.quit = MDFillRoundFlatButton(
            text = 'exit',
            pos_hint = {'center_x':0.6,'center_y':0.2},
            md_bg_color = (1,1,1,0.2),
            theme_text_color = 'Custom',
            text_color = 'white',
            on_press = self.switch2
        )
        # self.add_widget(self.bck)
        self.add_widget(self.play_again)
        self.add_widget(self.quit)
        self.add_widget(self.score)
        self.add_widget(self.correct_text)
        self.add_widget(self.game_over)
        self.add_widget(self.your_text)
    def on_enter(self):
        self.clear_widgets()
        self.main()
    def switch1(self,instance):
        self.manager.current = 'Screen2'
        self.manager.remove_widget(self)
    def switch2(self,instance):
        self.manager.remove_widget(self.screen)
        self.manager.current = 'Screen1'
        self.manager.remove_widget(self)
class Messy_MindsApp(MDApp):
    def build(self):
        self.main_screen = Screen()
        self.manager = ScreenManager()
        scr1 = Screen1(name = 'Screen1')
        self.manager.add_widget(scr1)
        # self.manager.add_widget(Screen2(name = 'Screen3'))
        return self.manager
        pass
class Assets:
    def __init__(self):
        pass
    def main():
        self.word = ''
        self.digits = 0
        run = True
        while run:
            char = random.randint(0,9)
            self.word += str(char)
            self.dis = ''
            for i in self.word:
                self.dis += i
    
                time.sleep(0.5)
                os.system('cls')
            answer = input("Enter the self.word : ")
            if answer == self.word:
    
                self.digits += 1
    
            else:
    
                dec = input("Do you want to continue ? y/n: ")
                if dec == 'y':
                    self.word = ''
                    self.digits = 0
                else:
                    run = False
            time.sleep(0.5)
            os.system('cls')
Messy_MindsApp().run()
