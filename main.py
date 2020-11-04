from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

from time import strftime

LabelBase.register(name = 'Roboto', fn_regular = 'regular.ttf',fn_bold = 'bold.ttf')

class clockApp(App):
	st_sec = 0
	st_min = 0
	started = False

	def build(self):
		self.icon ='icon.png'
	def on_start(self):
		Clock.schedule_interval(self.update,0)

	def update(self,nap):
		self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

		if(self.started):
			self.st_sec += nap
			if(self.st_sec/60 >= 1):		
				self.st_min += 1 
			self.st_sec = self.st_sec%60
		
		self.root.ids.stopwatch.text = ('%02d:%02d.[size=30]%02d[/size]'%(int(self.st_min),int(self.st_sec),int(self.st_sec*100%100)))
	
	def start_st(self):
		self.started = True
	def pause_st(self):
		self.started = False
	def reset_st(self):
		self.started = False
		self.st_sec = 0
		self.st_min = 0
		
		
if __name__=='__main__':
	clockApp().run()	
