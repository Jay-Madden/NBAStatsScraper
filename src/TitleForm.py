import npyscreen
import Constants as Constants

class TitleForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.ButtonPress, name='Acknowledge', when_pressed_function= self.onAcknowledgePressed)

        self.title = self.add(npyscreen.TitleFixedText, name= 'Welcome to NBA Stats Scraper')
        self.title.value = 'Created by Jay Cox'
        
        self.github = self.add(npyscreen.TitleFixedText, name= 'Github:' , )
        self.github.value = 'https://github.com/Jay-Madden/NBAStatsScraper'

        self.add(npyscreen.TitleFixedText, name= 'License:' , )
        self.license = self.add(npyscreen.MultiLineEdit, name="License:", editable=False)
        self.license.value = Constants.Constants.LICENSE

    def onAcknowledgePressed(self):
        self.parentApp.switchForm('MainForm')
