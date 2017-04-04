def negate(num):
    return -num
def large_num(num):
    res = (num>10000)
    return res
b=3
print 'b:', b, 'neg_b:', negate(b)
print 'b is big:',large_num(b)

class Adress:
    def __init__(self, number, street_name):
        self.number= number
        self.street_name= street_name
Soon= Adress(4,'Calixto')

class Clock:
    def __init__(self,time):
        self.time= time
    def print_time(self):
        time='6:30'
        print self.time
clock=Clock('5:30')
print clock.print_time()
#'5:30'

class Clock:
    def __init__(self,time):
        self.time= time
    def print_time(self,time):
        print time

clock=Clock('5:30')
clock.print_time('10:30')
#10:30

class Clock:
    def __init__(self,time):
        self.time= time
    def print_time(self):
        print self.time
boston_clock= Clock('5:30')
paris_clock=boston_clock
paris_clock.time='10:30'
boston_clock.print_time()
#'10:30'
print paris_clock
print boston_clock
