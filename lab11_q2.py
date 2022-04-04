class clockTime:
    def __init__(self):
        self.hours = 0;
        self.minutes = 0;
        self.seconds = 0;

    def setHours(self,hours): # set the hours
        self.hours = hours;

    def setMinutes(self,minutes): # set the minutes
        self.minutes = minutes;

    def setSeconds(self,seconds): # set the seconds
        self.seconds = seconds;

    def setTime(self,hours,minutes,seconds): # set hours minutes and seconds
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)
        #self.hours = hours;
        #self.minutes = minutes;
        #self.seconds = seconds;

    def showTime(self): # print time in the format
        print(self.hours,":",self.minutes,":",self.seconds);

def main():
    hours = int(input("Enter hours: ")) # get user input for hours
    while(hours<0 or hours>23): # check if input is negative or above 23
        print("ERROR! Hours must be a positive number less than 24")
        hours = int(input("Enter hours: "))
    
    minutes = int(input("Enter minutes: ")) # get user input for minutes
    while(minutes<0 or minutes>59): #check if input is negaticve or above 59
        print("ERROR! Minutes must be a positive number less than 60")
        minutes = int(input("Enter minutes: "))
    
    seconds = int(input("Enter seconds: ")) # get user input for seconds
    while(seconds<0 or seconds>59):#check if input is negaticve or above 59
        print("ERROR! Seconds must be a positive number less than 60")
        seconds = int(input("Enter seconds: "))
    
    clock = clockTime() # create new object clock
    clock.setTime(hours,minutes,seconds)
    clock.showTime()



if __name__ == "__main__":
    main()