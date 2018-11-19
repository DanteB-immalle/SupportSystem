import random
class Responder:

    def __init__(self):
        
        self.responses = []
        self.fillResponses()

    def generateResponse(self):
        index = random.randint(0, len(self.responses) -1)
        return self.responses[index]
    def fillResponses(self):
        self.responses.append("That sounds odd. Could you describe this in more detail?")
        self.responses.append("No other customer has ever complained about this \n" + "before. What is your system configuration?")
        self.responses.append("I need a bit more information on that.")
        self.responses.append("Have you checked that you do not have a dll conflict?")
        self.responses.append("That is covered in the manual. Have you read the manual?")
        self.responses.append("Your description is a bit wishy-washy. Have you got \n" + "an expert there with you who could describe this better?")
        self.responses.append("That's not a bug, it's a feature!")
        self.responses.append("Could you elaborate on that?")
        self.responses.append("Have you tried running the app on your phone?")
        self.responses.append("I just checked StackOverflow - they don't know either.")


        