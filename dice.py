from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from random import randint

class LayerRoot(BoxLayout):
    """Main Layout"""
    
    img_src = ObjectProperty()
    img_src2 = ObjectProperty()
    source_file = "dice_images/dice_{}.png"

    def play(self):
    	"""Roll two dices """

    	val1 = Dice(6).roll()
    	val2 = Dice(6).roll()
    	self.img_src.source = self.source_file.format(val1)
    	self.img_src2.source = self.source_file.format(val2)

class Dice():
    """Define a Dice"""

    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        """Generate Random number"""
        return randint(1, self.faces)


class DiceApp(App):
    """Dice App"""

    title = "Dice Roller App"
    def build(self):
        return LayerRoot()

if __name__ == '__main__':
    myApp = DiceApp()
    myApp.run()
