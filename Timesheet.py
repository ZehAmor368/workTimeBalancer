from YamlHandler import YamlHandler
from WorkTime import WorkTime
from Timer import Timer


class Timesheet(YamlHandler):
    """
    handles interaction between time calculation and filesystem

    inherits from YamlHandler
    """

    def __init__ (self, filename):
        YamlHandler.__init__(self,filename)
        self.__timer = WorkTime()
        self._readYml()

    def getTimesheet (self):
        return self._getYmlContent()
        
    def newEntry (self):
        return {
            'Datum': self.__timer.getstrfDate(self.__timer.setTime()),
            'Wochentag': self.__timer.getWeekday(self.__timer.setTime()),
            'Beginn': '',
            'Ende': '',
            'Arbeitszeit': '',
            'Abweichung': '',
        }
 

    def checkEintragKeys (self):
        if self.__timer.setTime().year in self.__eintrag.keys():
            if self.__timer.setTime().month in self.__eintrag[self.__timer.setTime().year].keys():
                if self.__timer.setTime().day in self.__eintrag[self.__timer.setTime().year][self.__timer.setTime().month].keys():
                    return True
                else:
                    self.__eintrag[self.__timer.setTime().year][self.__timer.setTime().month][self.__timer.setTime().day] = self.newEntry()
            else:
                self.__eintrag[self.__timer.setTime().year][self.__timer.setTime().month] = {self.__timer.setTime().day: self.newEntry()}
        else:
            self.__eintrag[self.__timer.setTime().year] = {self.__timer.setTime().month:{self.__timer.setTime().day:self.newEntry()}}

    def checkTimesheet (self):
        if self.getTimesheet() == None:
            self.__eintrag = {self.__timer.setTime().year:{self.__timer.setTime().month:{self.__timer.setTime().day:self.newEntry()}}}
        else:
            self.__eintrag = self.getTimesheet()

        return self.__eintrag

    def setData(self, key, value):
        self.__eintrag[self.__timer.setTime().year][self.__timer.setTime().month][self.__timer.setTime().day][key] = value

    def getEintrag(self):
        return self.__eintrag
    
    def writeTimesheet(self):
        self.setYmlContent(self.__eintrag)
        self._writeYml(append=False)

    def startWork(self):
        self.__timer.start()
        self.checkTimesheet()
        self.checkEintragKeys()
        self.setData('Beginn',self.__timer.getstrfTime(self.__timer.getStartTime()))
        self.writeTimesheet()
    
    def endWork(self):
        self.__timer.end()
        self.checkTimesheet()
        self.__startTime_timestamp = "{} {}".format(self.__eintrag[self.__timer.setTime().year][self.__timer.setTime().month][self.__timer.setTime().day]['Datum'],self.__eintrag[self.__timer.setTime().year][self.__timer.setTime().month][self.__timer.setTime().day]['Beginn'])
        self.__timer.setStartTime(self.__timer.striptime(self.__startTime_timestamp))
        self.__timer.calcWorkday()
        self.setData('Ende',self.__timer.getstrfTime(self.__timer.getEndTime()))
        self.setData('Arbeitszeit',self.__timer.getWorkTime_String())
        self.setData('Abweichung',self.__timer.calcDeviation(self.__timer.getWorkTime_sec().seconds))
        self.writeTimesheet()



if __name__ == "__main__":
    ts = Timesheet('Timesheet.yml')
    ts.checkTimesheet()
    #ts.setData('Beginn','now, but later')
    #ts.startWork()
    #ts.endWork()

    print(ts.checkEintragKeys())
    print(ts.getEintrag())

    #print(ts)