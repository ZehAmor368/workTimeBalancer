import datetime

class Timer:
    """handles time specific calculations

needs module:
-   datetime
"""
    __weekday = {
        0: "Montag",
        1: "Dienstag",
        2: "Mittwoch",
        3: "Donnerstag",
        4: "Freitag",
        5: "Samstag",
        6: "Sonntag"
    }

    def setTime (self):
        return datetime.datetime.now()

    def calcTimeDiff (self,time0,time1):
        """
        returns difference between time0 and time1 in datetime.timedelta(seconds,microseconds)

        both time parameter are instance of type datetime
        """
        return (time1 - time0)

    def getstrfTime (self,time,form = "%H:%M:%S"):
        """
        returns timestring formatted using form

        param:
        time - datetime
        form - string
        """
        return time.strftime(form)
    
    def getstrfDate (self, time, form = "%d.%m.%Y"):
        """
        returns datestring formatted using form

        param:
        time - datetime
        form - string
        """
        return time.strftime(form)

    def getWeekday (self, time):
        """
        returns string like 'Montag' using datetime.weekday() function

        param:
        time - datetime
        """
        return self.__weekday[time.weekday()]

    def _striptime (self,string,form = "%d.%m.%Y %H:M:S"):
        """
        converts string to datetime object
        """
        return datetime.datetime.strptime(string,form)

    def getTimeDiffString (self, seconds): 
        """
        converts timedelta.seconds into a HH:MM:SS string

        param:
        seconds - tin
        """
        self.__hour = seconds // 3600
        self.__r = seconds % 3600
        self.__minute = self.__r // 60
        self.__r = self.__r % 60
        self.__seconds = self.__r
        return ("{0:02}:{1:02}:{2:02}".format(self.__hour,self.__minute, self.__seconds))


    



if __name__ == "__main__":
    import datetime

    t = Timer()
    print(t.getstrfDate(t.setTime()))
    print(t.getTimeDiffString(20800))