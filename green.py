#!/usr/bin/python3


import sys
import argparse
import configparser
import smtplib
from datetime import datetime
import os

from light import L
from temp import T
from moisture import M



def main():
    parser = argparse.ArgumentParser(description="Argument parsing")
    parser.add_argument("-a", "--all", action='store_true',  help="This will return all sensor information")
    parser.add_argument("-l", "--light", action='store_true',  help="This will check the light sensors only, and give current external light levles")
    parser.add_argument("-t", "--temp", action='store_true', help="This will check the temperature sensors only, and give current internal temperature levels")
    parser.add_argument("-m", "--moisture", action='store_true', help="This will check the mositure sensors only, and provide current moisture levels")
    parser.add_argument("-e", "--email", help="Sends report to an email address. EMAIL file containing email configuration options")
    args = parser.parse_args()
    if  args.all:
        a = args.all
        print("All sensor information requested at ", y)
        light()
        temp()
        moist()
    if args.light:
        l = args.light
        print("Light sensor information requested at ", y)
        light()
    if args.temp:
        t = args.temp
        print("Temperature sensor information requested at ", y)
        temp()
    if args.moisture:
        m = args.moisture
        print("Moisture sensor information requested at ", y)
        moist()
    if args.email:
        global x
        x = args.email
        check()


#   Light
def light():
    current = datetime.now()
    hour = int(current.strftime('%H'))
    if hour < 9 and hour > 17:
        if L < 450000:
            print("Current light level outside is {0} lux. Internal grow lights are \"ON\" to meet opitional growing condition.".format(L))
        else:
            print("Current light level outside is {0} lux. Internal grow lights are \"OFF\" since this meets the opitional ranger for growing.")
    else:
        print("Current time is {0}, for best growing conditions light is only required between the hours of 09:00 and 17:00. Internal grow lights are off.".format(y))

#   Tempreture
def temp():
    if T > 82:
        print("Current temperature is {0} degrees. The AC unit is currently running to bring the temperture down to opitional growing conditions.".format(T))
    elif T < 75:
        print("Current temperature is {0} degrees. The heater is currently running to bring the temperature up to opitional growing conditions.".format(T))
    else:
        print("Current temperature is {0} degrees. This is within the range of opitional growing conditions.".format(T))


#   Moisture
def moist():
    if M > .5:
        print("Currnet moisture level of {0} is above recomended levels. Watering is suspended until levels come down.".format(M))
    elif M < .4:
        print("Current moisture level of {0} is below recomended levels. Sprinkler systems are currently running.".format(M))
    else:
        print("Current moisture level of {0} is opitional for growing.".format(M))


#   Time
def TIME():
    current = datetime.now()
    time = current.strftime('%H:%M:%S')
    global y
    y = time


#   Check all for email
def check():
    current = datetime.now()
    hour = int(current.strftime('%H'))
    if hour < 9 and hour > 17:
        if L < 450000:
            lights = "ON"
            l = L
        else:
            lights = "OFF"
            l = L
    else:
        l = "0"
        lights = "OFF"
    if T > 82:
        AC = "ON"
        heater = "OFF"
    elif T < 75:
        AC ="OFF"
        heater = "ON"
    else:
        AC = "OFF"
        heater = "OFF"
    if M > .5:
        sprinklers = "OFF"
    elif M < .4:
        sprinklers = "ON"
    else:
        sprinklers = "OFF"
    email(lights, AC, heater, sprinklers, l)


#  Email
def email(lights, AC, heater, sprinklers, l): 
    now = datetime.now()
    time = now.strftime('%m-%d-%Y')
    message = "Sensor Reading at {0}\nLight: {1} Lux\nTemptreture: {2} degrees\nMoisture: {3} percent\n\nOperational Status\nInternal Lights: {4}\nAir Conditioner: {5}\nHeater: {6}\nSprinklers: {7}\n".format(y, l, T, M, lights, AC, heater, sprinklers)
    config = configparser.ConfigParser()
    config.read(x)
    smtp = smtplib.SMTP(config['mail']['SMTP'], config['mail']['PORT'])
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config['mail']['USERNAME'], config['mail']['PASSWORD'])
    msg = "From: {0}\nTo: {1}\nSubject: {2} Greenhouse report\n\n{3}".format(config['mail']['FROM_EMAIL'], config['mail']['TO_EMAIL'], time, message)
    smtp.sendmail(config['mail']['FROM_EMAIL'], config['mail']['TO_EMAIL'], msg)
    smtp.close()


if __name__ == "__main__":
    TIME()
    main()
