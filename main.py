from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.scrollview import ScrollView
import re
from kivy.uix.image import Image





Config.set('graphics', 'resizable', True)



class MyApp(App):


    def build(self):


        self.sm=ScreenManager()

        LogoScr= Screen(name='Logo Screen')
        MainScr= Screen(name='Main Screen')


        img = Image(source='icon.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})
        scr1 = Screen(name='First Screen')
        scr2 = Screen(name='Second Screen')
        scr3 = Screen(name='Third Screen')
        scr4 = Screen(name='Fourth Screen')
        scr5 = Screen(name='Fifth Screen')
        scr6 = Screen(name='Sixth Screen')
        scr7 = Screen(name='Seventh Screen')
        scr8 = Screen(name='Eighth Screen')
        scr9 = Screen(name='Ninth Screen')
        scr10 = Screen(name='Tenth Screen')
        scrStory = Screen(name='Story')
        FeedBackScr = Screen(name='Feedback')

        blMS = BoxLayout(orientation='vertical', padding=50, spacing=10, size_hint_y=1.5)
        scrollMS=ScrollView()
        blscr1 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr2 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr3 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr4 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr5 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr6 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr7 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr8 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr9 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr10 = BoxLayout(orientation='vertical', padding=50, spacing=10)
        blscrStory = BoxLayout(orientation='vertical', padding=50, spacing=10, size_hint_y=1.5)
        blFBS = BoxLayout(orientation='vertical', padding=50, spacing=10)

        mainlb=Label(text='Percent helper', halign='center', size_hint=(1,.1),font_size='20dp') # ???????? ?????????????????? ????????????
        mainbut1=Button(text='?????????? ?????????????? ???? ??????????', size_hint= (1, 0.1))
        mainbut1.bind(on_release=self.toset1)
        mainbut2 = Button(text='?????????????? ?????????????????? ???????????????????? ?????????? ???? ??????????', size_hint= (1, 0.1))
        mainbut2.bind(on_release=self.toset2)
        mainbut3 = Button(text='?????????????????? ?????????? ???? ??????????????', size_hint= (1, 0.1))
        mainbut3.bind(on_release=self.toset3)
        mainbut4 = Button(text='?????????????????? ?????????? ???? ??????????????', size_hint= (1, 0.1))
        mainbut4.bind(on_release=self.toset4)
        mainbut5 = Button(text='???????????? ????????????, ???????????? ??????????, ?????? ???????', size_hint=(1, 0.1))
        mainbut5.bind(on_release=self.toset5)
        mainbut6 = Button(text='?????????? ???? ??????????, ?????? ??????????????? \n(???????????? ??????????, ????????????, ????????????????)', size_hint=(1, 0.1))
        mainbut6.bind(on_release=self.toset6)
        mainbut7 = Button(text='?????????? ???? ?????????? (?????????????????? ?????????? ???? ??????????)', size_hint=(1, 0.1))
        mainbut7.bind(on_release=self.toset7)
        mainbut8 = Button(text='?????????????? ?????????? ???? ??????????', size_hint=(1, 0.1))
        mainbut8.bind(on_release=self.toset8)
        mainbut9 = Button(text='?????? (???????? ?????????? ???????? ?????????? ?? ??????)', size_hint=(1, 0.1))
        mainbut9.bind(on_release=self.toset9)
        mainbut10 = Button(text='???????????????????? ?????????? ?? ??????????????', size_hint=(1, 0.1))
        mainbut10.bind(on_release=self.toset10)
        mainbutStory = Button(text='?????????????? ???????????????? (????????????????????)', size_hint=(1, 0.1))
        mainbutStory.bind(on_release=self.tosetStory)
        mainbutFB = Button(text='???????????????? ??????????', size_hint=(1, 0.1))
        mainbutFB.bind(on_release=self.tosetFB)
        blMS.add_widget(mainlb)
        blMS.add_widget(mainbut1)
        blMS.add_widget(mainbut2)
        blMS.add_widget(mainbut3)
        blMS.add_widget(mainbut4)
        blMS.add_widget(mainbut5)
        blMS.add_widget(mainbut6)
        blMS.add_widget(mainbut7)
        blMS.add_widget(mainbut8)
        blMS.add_widget(mainbut9)
        blMS.add_widget(mainbut10)
        blMS.add_widget(mainbutStory)
        blMS.add_widget(mainbutFB)
        scrollMS.add_widget(blMS)
        MainScr.add_widget(scrollMS)
        LogoScr.add_widget(img)



        scr1but=Button(text='?????????????? ?? ????????', size_hint=(1,.2)) # ???????? ???????????? 1 - ?????????????? ???? ??????????
        scr1but.bind(on_release=self.tomain)
        self.scr1lb=Label(text="???????? ?????? ???????????????????? ?????????? ?????????????? ???? \n??????????, ?????????????? ?? ???????????? ?????????? ??????????, \n???? ???????????????? ???????????????????? ?????????? ??????????????,\n ???? ???????????? ?????????? ??????????????, ?????????????? \n???????? ?????????? ?? ?????????????? ???????????? ????????????????????. \n(????????????: ???? ?????????? 100 ?????????? ?????????????? 30)", halign='center', size_hint= (1, 1), underline=True)
        self.scr1inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr1inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        scr1but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr1but1.bind(on_press=self.scr1count)
        self.scr1rez = Label(text="??????????????????: ")
        blscr1.add_widget(scr1but)

        blscr1.add_widget(self.scr1lb)
        blscr1.add_widget(self.scr1inp1)
        blscr1.add_widget(self.scr1inp2)
        blscr1.add_widget(self.scr1rez)
        blscr1.add_widget(scr1but1)

        scr1.add_widget(blscr1)


        scr2but = Button(text='?????????????? ?? ????????', size_hint=(1,.2)) # ???????? ???????????? 2 -?????????????? ?????????????????? ???????????????????? ?????????? ???? ??????????
        scr2but.bind(on_release=self.tomain)
        self.scr2lb = Label(text="???????? ?????? ???????????????????? ??????????, ?????????????? \n?????????????????? ???????? ?????????? ???????????????????? ???? \n??????????????, ?????????????? ?? ???????????? ?????????? ??????????, \n???? ???????????????? ?????????? ?????????? ??????????????, \n???? ???????????? ?????????? ??????????, ???? ???????????????? ???????????? \n?????????????? ?? ?????????????? ???????????? ????????????????????. \n(????????????: \n?????????????? ?????????????????? 25 ???????????????????? ???? 200)", halign='center', size_hint= (1, 1), underline=True)
        self.scr2inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ???????????? ??????????", input_type="number")
        self.scr2inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ?????????? ???? ???????????????? ???????? ??????????????", input_type="number")
        self.scr2rez = Label(text="??????????????????: ")
        scr2but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr2but1.bind(on_press=self.scr2count)
        blscr2.add_widget(scr2but)
        blscr2.add_widget(self.scr2lb)
        blscr2.add_widget(self.scr2inp1)
        blscr2.add_widget(self.scr2inp2)
        blscr2.add_widget(self.scr2rez)
        blscr2.add_widget(scr2but1)
        scr2.add_widget(blscr2)


        scr3but = Button(text='?????????????? ?? ????????', size_hint=(1,.2))  # ???????? ???????????? 3 - ?????????????????? ?????????? ???? ??????????????
        scr3but.bind(on_release=self.tomain)
        scr3lb = Label(
            text="???????? ?????? ???????????????????? ?????????????????? ?????????? ????\n???????????????????????? ?????????????? ?????????????? ?? ???????????? ??????????\n??????????, ?????????????? ???????? ??????????????????,\n ???? ???????????? ?????????? ??????????????, ???? ????????????????\n?????????????????????????? ?????????? ?? \n?????????????? ???????????? ????????????????????. \n(????????????: ?????????????????? ?????????? 120 ???? 30%)",
            halign='center', size_hint= (1, 1), underline=True)
        self.scr3inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr3inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ?????????????? ???? ?????????????? ??????????????????????", input_type="number")
        self.scr3rez = Label(text="??????????????????: ")
        scr3but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr3but1.bind(on_press=self.scr3count)
        blscr3.add_widget(scr3but)
        blscr3.add_widget(scr3lb)
        blscr3.add_widget(self.scr3inp1)
        blscr3.add_widget(self.scr3inp2)
        blscr3.add_widget(self.scr3rez)
        blscr3.add_widget(scr3but1)
        scr3.add_widget(blscr3)


        scr4but = Button(text='?????????????? ?? ????????', size_hint=(1,.2))  # ???????? ???????????? 4 - ?????????????????? ?????????? ???? ??????????????
        scr4but.bind(on_release=self.tomain)
        scr4lb = Label(
            text="???????? ?????? ???????????????????? ?????????????????? ?????????? \n???? ???????????????????????? ??????????????, ?????????????? ?? ????????????\n?????????? ??????????, ?????????????? ???????? ??????????????????,\n ???? ???????????? ?????????? ??????????????, ???? \n?????????????? ?????????????????????? ?????????? \n?? ?????????????? ???????????? ????????????????????. \n(????????????: ?????????????????? ?????????? 120 ???? 40%)",
            halign='center', size_hint= (1, 1), underline=True)
        self.scr4inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr4inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ?????????????? ???? ?????????????? ??????????????????", input_type="number")
        self.scr4rez = Label(text="??????????????????: ")
        scr4but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr4but1.bind(on_press=self.scr4count)
        blscr4.add_widget(scr4but)
        blscr4.add_widget(scr4lb)
        blscr4.add_widget(self.scr4inp1)
        blscr4.add_widget(self.scr4inp2)
        blscr4.add_widget(self.scr4rez)
        blscr4.add_widget(scr4but1)
        scr4.add_widget(blscr4)


        scr5but = Button(text='?????????????? ?? ????????', size_hint=(1,.2))  # ???????? ???????????? 5 ??? ???????????? 3 ???????????? 5
        scr5but.bind(on_release=self.tomain)
        scr5lb = Label(
            text="?????????? ?? ?????????????????????? ?????????????? ??????????????: \n???????????? ???????????? ???? ????????????????????.... \n?????? ???? ?????? ????????????? ?????? ????????????, ?????? ???? ???????? \n???????????????????? ??????????, ???????? ?????????????? ???? \n?????? ?????????? ????????????. ?????? ?????????????? ?????????????? ?? \n???????????? ?????????? ?????????? (3-???? ?????? 5-????)\n?? ???? ???????????? ??????????, ???? ???????????? ?????? ???????????? ??????????.\n(????????????: ???????????? 5 ???? ???????? 500000 ??????????????)",
            halign='center', size_hint= (1, 1), underline=True)
        self.scr5inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ??????????????)", input_type="number")
        self.scr5inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="???????? ???? ???????????? ??????????", input_type="number")
        self.scr5rez = Label(text="??????????????????: ")
        scr5but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr5but1.bind(on_press=self.scr5count)
        blscr5.add_widget(scr5but)
        blscr5.add_widget(scr5lb)
        blscr5.add_widget(self.scr5inp1)
        blscr5.add_widget(self.scr5inp2)
        blscr5.add_widget(self.scr5rez)
        blscr5.add_widget(scr5but1)
        scr5.add_widget(blscr5)


        scr6but = Button(text='?????????????? ?? ????????', size_hint=(1,.2))  # ???????? ???????????? 6 ??? ?????????? ???? ?????????? (??????????, ??????????, ????????????????)
        scr6but.bind(on_release=self.tomain)
        scr6lb = Label(
            text="???????????? ???????????????? ?????????????? ?????????? \n?????????? ???? ??????????.?? ???????????? ?????????? \n?????????????? ?????????? (3, 4, 5 ?? ??.??.),\n???? ???????????? ?????????? ??????????, ???? ???????????????? ??????????\n(????????????: ??????????(3 ??????????) ???? ?????????? 600",
            halign='center', size_hint= (1, 1), underline=True)
        self.scr6inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr6inp2 = FloatInput(size_hint=(1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr6rez = Label(text="??????????????????: ")
        scr6but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr6but1.bind(on_press=self.scr6count)
        blscr6.add_widget(scr6but)
        blscr6.add_widget(scr6lb)
        blscr6.add_widget(self.scr6inp1)
        blscr6.add_widget(self.scr6inp2)
        blscr6.add_widget(self.scr6rez)
        blscr6.add_widget(scr6but1)
        scr6.add_widget(blscr6)


        scr7but = Button(text='?????????????? ?? ????????', size_hint=(1,.2))  # ???????? ???????????? 7 ??? ?????????? ???? ?????????? (??????????????????)
        scr7but.bind(on_release=self.tomain)
        scr7lb = Label(
            text="???????????? ???????????????? ???????????????? ?????????? ???? ??????????.\n ???? ????????, ???????????????????? ?????????????? ?????????? ???? ??????????\n  ?? ???????????? ?????????? ?????????????? ?????????? ?????????? ???/???.\n ???? ???????????? ?????????? ?????????????? ??????????. \n(????????????: 2/3 ???? ?????????? 600)",
            halign='center', size_hint=(1, 1), underline=True)
        self.scr7inp1 = FloatInput1(size_hint=(1, None), height="30dp", hint_text="???????? ?????????? ?????????? /")
        self.scr7inp2 = FloatInput(size_hint=(1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr7rez = Label(text="??????????????????: ")
        scr7but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr7but1.bind(on_press=self.scr7count)
        blscr7.add_widget(scr7but)
        blscr7.add_widget(scr7lb)
        blscr7.add_widget(self.scr7inp1)
        blscr7.add_widget(self.scr7inp2)
        blscr7.add_widget(self.scr7rez)
        blscr7.add_widget(scr7but1)
        scr7.add_widget(blscr7)


        scr8but = Button(text='?????????????? ?? ????????', size_hint=(1,.2))  # ???????? ???????????? 8 ??? ?????????? ???? ?????????? (??????????????)
        scr8but.bind(on_release=self.tomain)
        scr8lb = Label(
            text="???????????? ???????????????? ?????????? ?????????? ???? ??????????.\n ?? ???????????? ?????????? ?????????????? ??????????.\n ???? ???????????? ?????????? ?????????????? ?????????? ?????????? ???/???. \n(????????????: ?????????? 600 ???????????? ???? 2/3)",
            halign='center', size_hint=(1, 1), underline=True)
        self.scr8inp1 = FloatInput (size_hint=(1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr8inp2 = FloatInput1(size_hint=(1, None), height="30dp", hint_text="???????? ?????????? ?????????? /")
        self.scr8rez = Label(text="??????????????????: ")
        scr8but1 = Button(text='????????????????????', size_hint=(1,.2))
        scr8but1.bind(on_press=self.scr8count)
        blscr8.add_widget(scr8but)
        blscr8.add_widget(scr8lb)
        blscr8.add_widget(self.scr8inp1)
        blscr8.add_widget(self.scr8inp2)
        blscr8.add_widget(self.scr8rez)
        blscr8.add_widget(scr8but1)
        scr8.add_widget(blscr8)


        scr9but = Button(text='?????????????? ?? ????????', size_hint=(1,.2))  # ???????? ???????????? 9 ??? ?????????? ???? ?????????? (??????????????)
        scr9but.bind(on_release=self.tomain)
        scr9lb = Label(
            text="???????????? ???????????????? ?????????????? ?????????? ?????? ??????.\n ???? ????????, ???????? ?????? ????????????????\n ?????????? ?? ??????( ?? ?????? ?????????? ??????)\n ?? ???????????? ?????????? ?????????????? ??????????,\n ???? ???????????? ?????????? ?????????????? ?????????????? ?????? \n(18 ?????? 20 ?????? ????????????). \n(????????????: ?????????? ?? ?????? 1200, ?????? 20%)",
            halign='center', size_hint=(1, 1), underline=True)
        self.scr9inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr9inp2 = FloatInput1(size_hint=(1, None), height="30dp", hint_text="???????? ?????????????? ??????", input_type="number")
        self.scr9rez = Label(text="??????????????????: ")
        scr9but1 = Button(text='????????????????????', size_hint=(1, .2))
        scr9but1.bind(on_press=self.scr9count)
        blscr9.add_widget(scr9but)
        blscr9.add_widget(scr9lb)
        blscr9.add_widget(self.scr9inp1)
        blscr9.add_widget(self.scr9inp2)
        blscr9.add_widget(self.scr9rez)
        blscr9.add_widget(scr9but1)
        scr9.add_widget(blscr9)

        scr10but = Button(text='?????????????? ?? ????????', size_hint=(1, .2))  # ???????? ???????????? 10 ??? ?????????????? ??????????
        scr10but.bind(on_release=self.tomain)
        scr10lb = Label(
            text="???????????? ???????????????? ???????????????? ??????????\n ?? ???????????????? ??????????????\n ???? ???????? ?????????????? ??????????, ?????? ??\n ???????????? ??????????????. \n ?? ???????????? ?????????? ?????????????? ??????????,\n ?????????????? ?????????????????? ?? ??????????????. \n???? ???????????? ?????????? - ?????????????? \n(????????????: ?????????? 11 ?? ?????????????? 5",
            halign='center', size_hint=(1, 1), underline=True)
        self.scr10inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="???????? ??????????", input_type="number")
        self.scr10inp2 = FloatInput1(size_hint=(1, None), height="30dp", hint_text="???????? ??????????????", input_type="number")
        self.scr10rez = Label(text="??????????????????: ")
        scr10but1 = Button(text='????????????????????', size_hint=(1, .2))
        scr10but1.bind(on_press=self.scr10count)
        blscr10.add_widget(scr10but)
        blscr10.add_widget(scr10lb)
        blscr10.add_widget(self.scr10inp1)
        blscr10.add_widget(self.scr10inp2)
        blscr10.add_widget(self.scr10rez)
        blscr10.add_widget(scr10but1)
        scr10.add_widget(blscr10)

        scrStorybut = Button(text='?????????????? ?? ????????', size_hint=(1, 0.05))  # ???????? ???????????? 11 ??? ???????????? ??????????????????????
        scrollStory = ScrollView()
        scrStorybut.bind(on_release=self.tomain)
        scrStorylb = Label(
            text="???????????? ?????????? ?????????????????????? ???????? ????????????????.\n (???????????? 1000 ????????????????).\n???????? ???????????? ???????????????? ??????????????,\n ?????????????? ????????????????.",
            halign='center', size_hint=(1, 0.1), underline=True)
        scrStorybut1 = Button(text='????????????????', size_hint=(1, 0.05))
        scrStorybut1.bind(on_press=self.scrStorycount)
        self.scrStoryrez = Label(text="??????????????:\n", halign='center',valign='top', size_hint=(1, 1))



        blscrStory.add_widget(scrStorybut)
        blscrStory.add_widget(scrStorylb)
        blscrStory.add_widget(scrStorybut1)
        blscrStory.add_widget(self.scrStoryrez)
        scrollStory.add_widget(blscrStory)
        scrStory.add_widget(scrollStory)


        FeedBackScrbut = Button(text='?????????????? ?? ????????', size_hint=(1, .1)) # ?????????? ???????????????? ??????????
        FeedBackScrbut.bind(on_release=self.tomain)
        FeedBackScrlb = Label(
            text="?????? ???????? ?????????????????? ?? ?????????????????? ???? \n?????????????? ???????????????????? ???? ?????????????????????? ??????????:\n Percenthelper@yandex.ru\n ???????? ???????? ?????????????? ???????????????? ???????????? ???????????? ????????????????????:\n ??????????????????????????:\n 0x47a5f8b28e4fd470367c1f8123167fbb6fcdb13d\n ?????????? ??????????: 5536 9137 6801 9172",
            halign='center', size_hint=(1, 1), underline=True)

        blFBS.add_widget(FeedBackScrbut)
        blFBS.add_widget(FeedBackScrlb)
        FeedBackScr.add_widget(blFBS)


        self.sm.add_widget(LogoScr)
        self.sm.add_widget(MainScr)
        self.sm.add_widget(scr1)
        self.sm.add_widget(scr2)
        self.sm.add_widget(scr3)
        self.sm.add_widget(scr4)
        self.sm.add_widget(scr5)
        self.sm.add_widget(scr6)
        self.sm.add_widget(scr7)
        self.sm.add_widget(scr8)
        self.sm.add_widget(scr9)
        self.sm.add_widget(scr10)
        self.sm.add_widget(scrStory)
        self.sm.add_widget(FeedBackScr)
        self.sm.current='Main Screen'
        return self.sm

    def toset1(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='First Screen'
    def toset2(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Second Screen'
    def toset3(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Third Screen'
    def toset4(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Fourth Screen'
    def toset5(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Fifth Screen'
    def toset6(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Sixth Screen'
    def toset7(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Seventh Screen'
    def toset8(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Eighth Screen'
    def toset9(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Ninth Screen'
    def toset10(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Tenth Screen'
    def tosetStory(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Story'
    def tosetFB(self, instance):
        self.sm.transition = SlideTransition(direction='left')
        self.sm.current='Feedback'

    def tomain(self, instance):
        if self.sm.current=='First Screen':
            self.scr1rez.text = str("??????????????????: ")
            self.scr1inp1.text = ''
            self.scr1inp2.text = ''
        elif self.sm.current=='Second Screen':
            self.scr2rez.text = str("??????????????????: ")
            self.scr2inp1.text = ''
            self.scr2inp2.text = ''
        elif self.sm.current=='Third Screen':
            self.scr3rez.text = str("??????????????????: ")
            self.scr3inp1.text = ''
            self.scr3inp2.text = ''
        elif self.sm.current=='Fourth Screen':
            self.scr4rez.text = str("??????????????????: ")
            self.scr4inp1.text = ''
            self.scr4inp2.text = ''
        elif self.sm.current=='Fifth Screen':
            self.scr5rez.text = str("??????????????????: ")
            self.scr5inp1.text = ''
            self.scr5inp2.text = ''
        elif self.sm.current=='Sixth Screen':
            self.scr6rez.text = str("??????????????????: ")
            self.scr6inp1.text = ''
            self.scr6inp2.text = ''
        elif self.sm.current=='Seventh Screen':
            self.scr7rez.text = str("??????????????????: ")
            self.scr7inp1.text = ''
            self.scr7inp2.text = ''
        elif self.sm.current=='Eighth Screen':
            self.scr8rez.text = str("??????????????????: ")
            self.scr8inp1.text = ''
            self.scr8inp2.text = ''
        elif self.sm.current=='Ninth Screen':
            self.scr9rez.text = str("??????????????????: ")
            self.scr9inp1.text = ''
            self.scr9inp2.text = ''
        elif self.sm.current=='Tenth Screen':
            self.scr10rez.text = str("??????????????????: ")
            self.scr10inp1.text = ''
            self.scr10inp2.text = ''
        if len(self.scrStoryrez.text)>1000:
            self.scrStoryrez.text = "??????????????:\n"
        self.sm.transition = SlideTransition(direction='right')
        self.sm.current='Main Screen'
    def scr1count(self, instance):
        try:
            (float(self.scr1inp1.text) * float(self.scr1inp2.text) / 100)
            self.scr1rez.text = f"??????????????????: {self.scr1inp2.text}% \n???? ?????????? {self.scr1inp1.text} \n ???????????????????? {round((float(self.scr1inp1.text)*float(self.scr1inp2.text)/100),5)}\n"
            self.scr1inp1.text=''
            self.scr1inp2.text = ''
            self.scrStoryrez.text+= self.scr1rez.text
        except OverflowError:
            self.scr1rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr1rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")
    def scr2count(self, instance):
        try:
            float(self.scr2inp1.text) / float(self.scr2inp2.text)
            self.scr2rez.text = f"??????????????????: ?????????? {self.scr2inp1.text}\n???????????????????? {round(((float(self.scr2inp1.text))/float(self.scr2inp2.text)*100),5)}% \n???? ?????????? {self.scr2inp2.text}\n"
            self.scr2inp1.text = ''
            self.scr2inp2.text = ''
            self.scrStoryrez.text += self.scr2rez.text
        except OverflowError:
            self.scr2rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr2rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")


    def scr3count(self, instance):
        try:
            (float(self.scr3inp1.text) * (1 + (float(self.scr3inp2.text) / 100)))
            self.scr3rez.text = f"??????????????????: ?????????? {self.scr3inp1.text}\n?????????????????????? ???? {self.scr3inp2.text}% \n ???????????????????? {round((float(self.scr3inp1.text)*(1+(float(self.scr3inp2.text)/100))),5)}\n"
            self.scr3inp1.text = ''
            self.scr3inp2.text = ''
            self.scrStoryrez.text += self.scr3rez.text
        except OverflowError:
            self.scr3rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr3rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")


    def scr4count(self, instance):
        try:
            (float(self.scr4inp1.text) * (1 - (float(self.scr4inp2.text) / 100)))
            self.scr4rez.text =f"??????????????????: ?????????? {self.scr4inp1.text} \n?????????????????????? ???? {self.scr4inp2.text}% \n ???????????????????? {round((float(self.scr4inp1.text)*(1-(float(self.scr4inp2.text)/100))),5)}\n"
            self.scr4inp1.text = ''
            self.scr4inp2.text = ''
            self.scrStoryrez.text += self.scr4rez.text
        except OverflowError:
            self.scr4rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr4rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")


    def scr5count(self, instance):
        try:
            float(self.scr5inp2.text) / float(self.scr5inp1.text)
            self.scr5rez.text = f"??????????????????: ???????????? {self.scr5inp1.text}\n???? ?????????? {self.scr5inp2.text}\n ???????????????????? {round((float(self.scr5inp2.text) / float(self.scr5inp1.text)),5)}\n"
            self.scr5inp1.text = ''
            self.scr5inp2.text = ''
            self.scrStoryrez.text += self.scr5rez.text
        except OverflowError:
            self.scr5rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr5rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")

    def scr6count(self, instance):
        try:
            float(self.scr6inp2.text) / float(self.scr6inp1.text)
            self.scr6rez.text = f"??????????????????: {self.scr6inp1.text} ?????????? \n???? ?????????? {self.scr6inp2.text}\n ???????????????????? {round((float(self.scr6inp2.text) / float(self.scr6inp1.text)),5)}\n"
            self.scr6inp1.text = ''
            self.scr6inp2.text = ''
            self.scrStoryrez.text += self.scr6rez.text
        except OverflowError:
            self.scr6rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr6rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")


    def scr7count(self, instance):
        try:
            (eval(self.scr7inp1.text) * float(self.scr7inp2.text))
            self.scr7rez.text = f"??????????????????: ?????????? {self.scr7inp1.text}\n???? ?????????? {self.scr7inp2.text}\n ???????????????????? {round((eval(self.scr7inp1.text) * float(self.scr7inp2.text)),5)}\n"
            self.scr7inp1.text = ''
            self.scr7inp2.text = ''
            self.scrStoryrez.text += self.scr7rez.text
        except OverflowError:
            self.scr7rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr7rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")


    def scr8count(self, instance):
        try:
            (float(self.scr8inp1.text) / eval(self.scr8inp2.text))
            self.scr8rez.text = f"??????????????????: ?????????? {self.scr8inp1.text} \n ???????????????? ???? ?????????? {self.scr8inp2.text}\n ???????????????????? {round((float(self.scr8inp1.text) / eval(self.scr8inp2.text)),5)}\n"
            self.scr8inp1.text = ''
            self.scr8inp2.text = ''
            self.scrStoryrez.text += self.scr8rez.text
        except OverflowError:
            self.scr8rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr8rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")

    def scr9count(self, instance):
        try:
            (float(self.scr9inp1.text) / float(self.scr9inp2.text))
            self.scr9rez.text = f"??????????????????: ?????????? {self.scr9inp1.text} (?? ??????), ????????????????????: \n?????? ??????: {(float(self.scr9inp1.text) / (100+float(self.scr9inp2.text)))*100}.\n ?????????? ?????? {self.scr9inp2.text}%: {float(self.scr9inp1.text) / (float(100)+float(self.scr9inp2.text))*float(self.scr9inp2.text)}\n"
            self.scr9inp1.text = ''
            self.scr9inp2.text = ''
            self.scrStoryrez.text += self.scr9rez.text
        except OverflowError:
            self.scr9rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr9rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")
    def scr10count(self, instance):
        try:
            (float(self.scr10inp1.text) ** float(self.scr10inp2.text))
            self.scr10rez.text = f"??????????????????: ?????????? {self.scr10inp1.text}\n?? ?????????????? {self.scr10inp2.text}\n????????????????????: {float(self.scr10inp1.text) ** (float(self.scr10inp2.text))}\n"
            self.scr10inp1.text = ''
            self.scr10inp2.text = ''
            self.scrStoryrez.text += self.scr10rez.text
        except OverflowError:
            self.scr10rez.text = str("???? ?????????? ?????????????? ?????????????? ??????????, \n?? ??????????????????, ???? ???????????? ??????????????????(")
        except:
            self.scr10rez.text = str("??????????????????: ???????????? ?????????????? ???????? ?????? ??????????")


    def scrStorycount(self, instance):
            self.scrStoryrez.text = str("??????????????:\n")



    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            if self.sm.current != 'Main Screen':
                self.sm.transition = SlideTransition(direction='right')
                self.sm.current = 'Main Screen'
            else:
                return False
            # do what you want, return True for stopping the propagation
            return True
class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring) #???????????? ???? ?????????? ???? ?????????? (??????????????)
        else:
            s = '.'.join(re.sub(pat, '', s) for s in substring.split('.', 1))



        return super().insert_text(s, from_undo=from_undo)
class FloatInput1(FloatInput):
    pat = re.compile('[^0-9/]')



if __name__ == '__main__':
    MyApp().run()