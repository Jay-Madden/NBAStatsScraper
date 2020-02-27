import npyscreen
import MainForm
import TitleForm
# This application class serves as a wrapper for the initialization of curses
# and also manages the actual forms of the application
class NBAStatsScraper(npyscreen.NPSAppManaged):
    STARTING_FORM = 'TitleForm'
    title = 'NBA Stats Scraper'
    def onStart(self):
        self.addForm("TitleForm", TitleForm.TitleForm, name= NBAStatsScraper.title) 
        self.addForm("MainForm", MainForm.MainForm, name= NBAStatsScraper.title) 

