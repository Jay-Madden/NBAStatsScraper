import npyscreen
import inspect
from enum import Enum

class Output(Enum):
    json = 1
    csv = 2

    @staticmethod
    def GetEnumAsList():
        return [e.name for e in Output]

class MainForm(npyscreen.FormBaseNew):

    def create(self):
        self.player = self.add(npyscreen.TitleText, name= 'Enter a Player:')
        self.myDepartment = self.add(npyscreen.TitleSelectOne, 
            scroll_exit=True, 
            max_height = len(Output.GetEnumAsList())+1,
            name='Select File Output', 
            values = Output.GetEnumAsList())
        self.add(npyscreen.ButtonPress, name='Submit', when_pressed_function= self.onSubmit)
    
    def onSubmit(self):
        a = 3

    def afterEditing(self):
        self.parentApp.setNextForm(None)