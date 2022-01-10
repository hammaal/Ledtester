from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUTPUT)


class Ledtester(MycroftSkill):
	def __init__(self):
		super().__init__()

	@intent_handler(IntentBuilder('DoorUnlock').require('lock').require('door'))
	def handle_Door_Unlock(self, message):
		if message.data['lock'].upper() == "UNLOCK":
			GPIO.output(27, GPIO.HIGH)
			self.speak('Door is unlocked')
								  

def create_skill():
	return Ledtester()