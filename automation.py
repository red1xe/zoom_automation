import schedule
import time
import webbrowser
import datetime

today = datetime.date.today()
day_of_week = today.strftime("%A")

print("--- Zoom Meeting Automation Script ---")
print("Happy " + day_of_week)
print("Wait until your lecturer starts the zoom session...")

def open_link(link):
    webbrowser.open(link)

def XXX101(): ## Replace XXX101 with your course code and create a function for each course
    print("Opening Zoom Meeting for XXX101") ## Replace XXX101 with your course code
    open_link("{ZOOM LINK YOUR COURSE}") ## Replace {ZOOM LINK YOUR COURSE} with your zoom link


def monday(): ## create a function for each day of the week
    schedule.every().monday.at("{TIME}").do(XXX101) ## Replace {TIME} with your class time in format "HH:MM" if you have more than one class on the same day, create another function for that day and add it to the schedule

def tuesday():
    schedule.every().tuesday.at("{TIME}").do(XXX101) 
    
def wednesday():
    schedule.every().wednesday.at("{TIME}").do(XXX101) 
 
def thursday():
    schedule.every().thursday.at("{TIME}").do(XXX101) 
    
def friday(): 
    schedule.every().friday.at("{TIME}").do(XXX101) 

def saturday():
    print("No class today")

def sunday():
    print("No class today")

days = {
    0: monday,
    1: tuesday,
    2: wednesday,
    3: thursday,
    4: friday,
    5: saturday,
    6: sunday,
}
today = datetime.datetime.today().weekday()
days[today]()

while 1:
    schedule.run_pending()
    time.sleep(1)
