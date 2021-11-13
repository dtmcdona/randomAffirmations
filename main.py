import random
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_affirmation(self):
        affirmations = ["I am the architect of my life; \nI build its foundation and choose its contents.",
                        "I am brimming with energy and \noverflowing with joy.",
                        "My body is healthy; my mind is brilliant; \nmy soul is tranquil.",
                        "I forgive those who have harmed me in my past and \npeacefully detach from them.",
                        "A river of compassion washes away my anger \nand replaces it with love.",
                        "Creative energy surges through me and leads \nme to new and brilliant ideas.",
                        "The only thing to fear is fear itself.",
                        "My ability to exceed my goals is limitless; \nmy potential to succeed is infinite.",
                        "I acknowledge my own self-worth; \nmy confidence is soaring.",
                        "Everything that is happening now is \nhappening for my ultimate good.",
                        "I woke up today with strength in my \nheart and clarity in my mind."]
        rand_num = random.randint(0, len(affirmations)-1)
        self.rand_aff.text = affirmations[rand_num]

class RandAffirmations(App):

    def build(self):
        return MyRoot()

randAffirmations = RandAffirmations()
randAffirmations.run()