from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
from rasa_core.channels.channel import UserMessage, OutputChannel

nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp...', #app verification token
							'xoxb...', # bot verification token
							'...', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))