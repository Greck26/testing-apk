#!/usr/bin/kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class TestApp(App):

   Window.size = (320, 240)
   title = 'Testing App'

   def build(self):
       return Button(text='Hello World')

TestApp().run()
