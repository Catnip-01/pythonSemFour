class TimeClass:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def displayTime(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")
        
    def addTime(self, t1, t2):
        self.hours = t1.hours + t2.hours
        self.minutes = t1.minutes + t2.minutes
        self.seconds = t1.seconds + t2.seconds
        print(f"added time is : {self.hours}:{self.minutes}:{self.seconds}")
        
    
    
    def subtractTime(self, t1, t2):
        self.hours = t1.hours - t2.hours
        self.minutes = t1.minutes - t2.minutes
        self.seconds = t1.seconds - t2.seconds
        print(f"subtracted time is : {self.hours}:{self.minutes}:{self.seconds}")
        
    def countSeconds(self):
        print(self.hours * 3600 + self.minutes * 60 + self.seconds, "seconds.")
        
Shobhit = TimeClass(12, 15, 30)
time2 = TimeClass(0, 30, 10)
time3 = TimeClass(4, 50, 50)

Shobhit.displayTime()

Shobhit.addTime(time2, time3)
Shobhit.subtractTime(time3, time2)
Shobhit.countSeconds()

