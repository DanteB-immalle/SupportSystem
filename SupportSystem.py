from InputReader import InputReader
from Responder import Responder

class SupportSystem:
    def __init__(self):
        self.reader = InputReader()
        self.responder = Responder()
    
    def start(self):
        finished = False
        self.printWelkom()

        while not finished:
            user_input = self.reader.getInput().lower()

            if user_input.startswith('bye'):
                finished = True
            else:
                response = self.responder.generateResponse()
                print(response)
            
        self.printGoodbye()

    def printWelkom(self):
        print ("Welkom bij het immalle helpsysteem")
        print()
        print("Vertel ons uw probleem...")
        print("Typer 'bye' om te stoppen")

    def printGoodbye(self):
        print("Goodbye!")