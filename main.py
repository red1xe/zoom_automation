import schedule
import time
import webbrowser

print("---AGU Zoom Meeting Automation Script---")
print("Wait until your lecturer starts the zoom session...")


def open_link(link):
    webbrowser.open(link)


def phys():
    print("Joining PHYS102.02")
    open_link('https://zoom.us/j/94085075189?pwd=NFdEUDlvRHpxRDJtaGxONnpCZDV2dz09')


def math():
    print("Joining MATH152.01")
    open_link('https://zoom.us/j/9542546083?pwd=TytSQ2xQZ2tTTzlwaXM0Z2pKZXdFQT09')


def comp104():
    print("Joining COMP104.01")
    open_link('https://zoom.us/j/92436093775?pwd=dlMvR29VVGpINmwvUy9PaFhvdTBzQT09')


def comp112():
    print("Joining COMP112.02")
    open_link('https://zoom.us/j/5077391879')


def glb():
    print("Joining GLB104.16")
    open_link('https://zoom.us/j/93654566759?pwd=WENDL25TMlBqZTh4QVprdkNVQUJyZz09')


def cp():
    print("Joining CP100.01")
    open_link('https://zoom.us/j/91632102893')


schedule.every().monday.at("09:20").do(phys)
schedule.every().monday.at("11:20").do(math)
schedule.every().monday.at("12:10").do(comp104)

schedule.every().tuesday.at("09:20").do(glb)
schedule.every().tuesday.at("13:20").do(math)

schedule.every().wednesday.at("12:20").do(math)
schedule.every().wednesday.at("20:00").do(comp112)

schedule.every().thursday.at("14:20").do(phys)

schedule.every().friday.at("09:20").do(comp104)
schedule.every().friday.at("11:20").do(cp)
schedule.every().friday.at("16:20").do(comp112)

while 1:
    schedule.run_pending()
    time.sleep(1)
