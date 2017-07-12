from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('shivani', 'Miss.', 18, 4.7)

friend_one = Spy('sabha', 'Ms.', 19, 4.9)
friend_two = Spy('shabnam', 'Ms.', 21, 4.39)
friend_three = Spy('Mohit', 'Mr.', 19, 4.95)


friends = [friend_one, friend_two, friend_three]
messages = ["save me","help me","SOS","help"]