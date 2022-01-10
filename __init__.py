from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


class Ledtester(MycroftSkill):
	def __init__(self):
		super().__init__()

	@intent_handler(IntentBuilder('DoorUnlock').require('lock').require('door'))
	def handle_Door_Unlock(self, message):
		if message.data['lock'].upper() == 'UNLOCK':
			GPIO.output(27, GPIO.HIGH)
			self.speak('Door is unlocked')
		elif message.data['lock'].upper() == 'LOCK':
			GPIO.output(27, GPIO.LOW)
			self.speak('Door is locked')

	@intent_handler(IntentBuilder('BlindOpen').require('open').require('blind'))
	def handle_Blind_Open(self, message):
		if message.data['open'].upper() == 'OPEN':
			GPIO.output(22, GPIO.HIGH)
			self.speak('Blind is open')
		elif message.data['open'].upper() == 'CLOSE':
			GPIO.output(22, GPIO.LOW)
			self.speak('Blind is closed')
								  

def create_skill():
	return Ledtester()
