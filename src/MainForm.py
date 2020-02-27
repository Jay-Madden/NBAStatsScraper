import npyscreen
import inspect
from Enums import Output
from NBAData import NBAData
class MainForm(npyscreen.FormBaseNew):

    def create(self):
        self.api = NBAData()

        self.player = self.add(npyscreen.TitleText, name= 'Enter a Player:')
        self.fileTypePicker = self.add(npyscreen.TitleSelectOne, 
            scroll_exit=True, 
            max_height = len(Output.GetEnumAsList())+1,
            name='Select File Output Type', 
            values = Output.GetEnumAsList())

        self.fileName = self.add(npyscreen.TitleText, name= 'Enter a File Name')

        self.add(npyscreen.ButtonPress, name='Submit', when_pressed_function= self.onSubmitPressed)
        self.add(npyscreen.ButtonPress, name='Exit', when_pressed_function= self.onExitPressed)
    
    def onSubmitPressed(self):

        if not self.__validateFields():
            self.__displayError('One or more Input Fields missing')
            return

        npyscreen.notify('Loading Data, Please Wait', title='In Progress')
        shotcharts = self.api.getData(self.player.value, Output(self.fileTypePicker.value[0]))
        self.writeData(shotcharts)
        self.display()

    def onExitPressed(self):
        exit(0)
    
    def __validateFields(self) -> bool:
        if len(self.fileTypePicker.get_selected_objects()) < 1:
            return False
        if self.player.value == '':
            return False
        if self.fileName.value == '':
            return False
        return True
    
    def writeData(self, shotCharts):
        for key, value in shotCharts.items():
            with open(f'{self.fileName.value}-{key}.{self.fileTypePicker.get_selected_objects()[0]}', 'w') as f:
                f.write(value)

    def __displayError(self, error):
        npyscreen.notify_confirm(error, title='VALIDATION ERROR')
        self.display()

    def afterEditing(self):
        self.parentApp.setNextForm(None)
