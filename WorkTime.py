import Timer

class WorkTime(Timer.Timer):
    """
    WorkTime inherits from Timer, it is more specific into calculation working Time

    needs module:
    -   Timer
    """

    __targetTime_sec = 28800

    def __init__ (self):
        """
        initialize
        """
        Timer.Timer.__init__(self)

    def start (self):
        """
        populates an variable with the current datetime.
        Used to start a workprocess
        """
        self.__startTime = self.setTime()

    def end (self):
        """
        populates an variable with the current datetime.
        Used to end a workprocess
        """
        self.__endTime = self.setTime()

    def calcDeviation (self,workTime_sec):
        """
        calculates the deviation between target worktime and actual worktime

        returns string

        param:
        -   workTime_sec        -> int
        -   __targetTime_sec    -> int
        """
        if workTime_sec > self.__targetTime_sec:
            return ("+ {}".format(self.getTimeDiffString(workTime_sec - self.__targetTime_sec)))
        else:
            return ("- {}".format(self.getTimeDiffString(self.__targetTime_sec - workTime_sec)))

    def calcWorkday (self):
        """
        calculates difference between startTime and endTime

        populates:  -   __workTime_sec      ->  int
                    -   __timeDiff_String   ->  string
        """
        self.__workTime_sec = self.calcTimeDiff(self.__startTime,self.__endTime)
        self.__timeDiff_String = self.getTimeDiffString(self.__workTime_sec.seconds)

    def getWorkTime_sec (self):
        """
        returns __workTime_sec  ->  int
        """
        return self.__workTime_sec

    def getStartTime (self):
        """
        returns __startTime     ->  datetime
        """
        return self.__startTime
    
    def setStartTime (self,time):
        """

        """
        self.__startTime = time

    def getEndTime (self):
        """
        returns __endTime       -> datetime
        """
        return self.__endTime
    
    def getWorkTime_String (self):
        """
        returns __timeDiff_String   -> String
        """
        return self.__timeDiff_String

    def striptime (self,string,form = "%d.%m.%Y %H:%M:%S"):
        return self._striptime(string, form)
    

if __name__ == "__main__":
    
    wt = WorkTime()

    #wt.start()
    print(wt.getstrfTime(wt.getStartTime()))

    from time import sleep

    sleep(15)

    wt.end()
    wt.calcWorkday()
    print(wt.calcDeviation(wt.getWorkTime_sec().seconds))
