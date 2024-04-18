from time import strftime, localtime, sleep
import tkinter as tk
from cla import Clock
import requests

k = tk.Tk()
k.geometry("800x480")
k.title("summa")
d = Clock()
k.config(highlightthickness=0)


c = tk.Canvas(width=800, height=200, bg="black", highlightthickness=0)
c.grid(column=0, row=0)
d.update_clc(a=c)

location = ""
max_temp = ""
min_temp = ""
time_condition = ""
icon = ""
current_temperature_c = ""
wind_speed = ""
humidity_cur = ""
cloud = ""
feels_like_c = ""
chance_rain = ""
uv = ""
x_cor = 480
x_cor2 = 700
font = 'mukta medium'
fill1 = '#E7F6F2'


def time1():
    # Get the current time
    current_time = strftime('%I:%M', localtime())
    pm1 = strftime('%p', localtime())

    # Get the current day and date
    current_day = (strftime('%A')).upper()

    current_date = strftime('%d  %b %Y').upper()

    # Update the Canvas text with the current time
    c.itemconfig(label_time, text=current_time)
    c.itemconfig(label_day, text=current_day)
    c.itemconfig(label_date, text=current_date)
    c.itemconfig(pm, text=pm1)

    # Call the time() function after 1 second
    k.after(1000, time1)


def weather():
    global location, max_temp, min_temp, time_condition, icon, current_temperature_c
    global wind_speed, humidity_cur, cloud, feels_like_c, chance_rain, uv
    response = requests.get(
        url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/chennai/today"
            "?unitGroup=metric&include=current&key=NE93DT4WNFKTVT53ZDSQTZPX9&contentType=json")

    response.raise_for_status()

    data = response.json()
    location = data["address"]
    max_temp = data["days"][0]["tempmax"]
    min_temp = data["days"][0]["tempmin"]
    time_condition = data["currentConditions"]["conditions"]
    icon = data["currentConditions"]["icon"]
    current_temperature_c = data["currentConditions"]["temp"]
    wind_speed = data["currentConditions"]["windspeed"]
    humidity_cur = data["currentConditions"]["humidity"]
    cloud = data["currentConditions"]["cloudcover"]
    feels_like_c = data["currentConditions"]["feelslike"]
    chance_rain = data["currentConditions"]["precipprob"]
    uv = data["currentConditions"]["uvindex"]

    c.itemconfig(text1, text=f"Location : {location}")
    # c.itemconfig(text2, text=f"Max Temperature : {max_temp}°C")
    # c.itemconfig(text3, text=f"Min Temperature : {min_temp}°C")
    c.itemconfig(text4, text=f"Current Temperature : {current_temperature_c}°C")
    c.itemconfig(text5, text=f"Feels Like : {feels_like_c}°C")
    c.itemconfig(text6, text=f"Condition : {time_condition}")
    # c.itemconfig(text7, text=f"Wind Speed : {wind_speed}mph")
    c.itemconfig(text8, text=f"Humidity : {humidity_cur}")
    # c.itemconfig(text9, text=f"Cloud Coverage : {cloud}%")
    c.itemconfig(text10, text=f"Chance of PRP : {chance_rain}%")
    # c.itemconfig(text11, text=f"UV : {uv}")
    k.after(900000, weather)


label_time = c.create_text(120, 90, text="", font=('Anurati', 50, "italic"), fill='#DAF4F5')
label_day = c.create_text(150, 170, text="", font=('Anurati', 25, 'italic'), fill='#DAF4F5')
label_date = c.create_text(135, 25, text="", font=('Anurati', 30, 'italic'), fill='#DAF4F5')
pm = c.create_text(250, 100, text="", font=('Anurati', 18, 'italic'), fill='#DAF4F5')

text1 = c.create_text(580, 30, text="", font=(font, 25, "normal"), fill=fill1)
# text2 = c.create_text(x_cor, 75, text="", font=(font, 14, "normal"), fill=fill1)
# text3 = c.create_text(x_cor, 110, text="", font=(font, 14, "normal"), fill=fill1)
text4 = c.create_text(580, 145, text="", font=(font, 18, "normal"), fill=fill1)
text5 = c.create_text(580, 180, text="", font=(font, 18, "normal"), fill=fill1)
text6 = c.create_text(580, 215, text="", font=(font, 18, "normal"), fill=fill1)
# text7 = c.create_text(x_cor2, 40, text="", font=(font, 14, "normal"), fill=fill1)
text8 = c.create_text(580, 75, text="", font=(font, 18, "normal"), fill=fill1)
# text9 = c.create_text(x_cor2, 110, text="", font=(font, 14, "normal"), fill=fill1)
text10 = c.create_text(580, 110, text="", font=(font, 18, "normal"), fill=fill1)
# text11 = c.create_text(x_cor2, 180, text="", font=(font, 14, "normal"), fill=fill1)
# text12=c.create_text(720,110,text="",font=('freehand written', 12, "normal"), fill='white')

# p=tk.Canvas(width=100,height=100,background="white")
# p.grid(column=0,row=0)
time1()
weather()

from tkinter import *
from time import sleep
from random import randint

w = 800
h = 280
x1 = (w // 2)
y1 = (h // 2)
my_canvas = Canvas(width=w, height=h, bg="black",highlightthickness=0)
my_canvas.grid(column=0, row=1)
pix_colour_1 = "#faf9f6"


def x(x1, y1, f=20):
    global x2, y2, pix
    pix = f
    x2 = x1 + (f * 7)
    y2 = y1 + (f * 7)

    line = my_canvas.create_rectangle(x1, y1, x1 + (f * 1), y1 + (f * 1), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 1), x1 + (f * 2), y1 + (f * 2), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 2), x1 + (f * 3), y1 + (f * 3), fill=pix_colour_1)
    center = my_canvas.create_rectangle(x1 + (f * 3), y1 + (f * 3), x1 + (f * 4), y1 + (f * 4), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 4), y1 + (f * 4), x1 + (f * 5), y1 + (f * 5), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 5), y1 + (f * 5), x1 + (f * 6), y1 + (f * 6), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 6), y1 + (f * 6), x1 + (f * 7), y1 + (f * 7), fill=pix_colour_1)
    # inverse line
    line = my_canvas.create_rectangle(x2 - (f * 1), y2 - (f * 7), x2, y2 - (f * 6), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x2 - (f * 2), y2 - (f * 6), x2 - (f * 1), y2 - (f * 5), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x2 - (f * 3), y2 - (f * 5), x2 - (f * 2), y2 - (f * 4), fill=pix_colour_1)
    center = my_canvas.create_rectangle(x2 - (f * 4), y2 - (f * 4), x2 - (f * 3), y2 - (f * 3), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x2 - (f * 5), y2 - (f * 3), x2 - (f * 4), y2 - (f * 2), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x2 - (f * 6), y2 - (f * 2), x2 - (f * 5), y2 - (f * 1), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x2 - (f * 7), y2 - (f * 1), x2 - (f * 6), y2, fill=pix_colour_1)


def x_x(ux, uy):
    x(ux, uy)
    x(ux + (pix * 10), uy)


def choice(i):
    s = randint(0, i)
    return s


def closed(x1, y1, f=20):
    global x2, y2
    x2 = x1 + (f * 7)
    y2 = y1 + (f * 7)

    # >
    line = my_canvas.create_rectangle(x1, y1, x1 + (f * 1), y1 + (f * 1), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 1), x1 + (f * 2), y1 + (f * 2), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 2), x1 + (f * 3), y1 + (f * 3), fill=pix_colour_1)
    center = my_canvas.create_rectangle(x1 + (f * 3), y1 + (f * 3), x1 + (f * 4), y1 + (f * 4), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x2 - (f * 5), y2 - (f * 3), x2 - (f * 4), y2 - (f * 2), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x2 - (f * 6), y2 - (f * 2), x2 - (f * 5), y2 - (f * 1), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x2 - (f * 7), y2 - (f * 1), x2 - (f * 6), y2, fill=pix_colour_1)
    # <
    line = my_canvas.create_rectangle(x2 - (f * -4), y2 - (f * 7), x2 - (f * -3), y2 - (f * 6), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x2 - (f * -3), y2 - (f * 6), x2 - (f * -2), y2 - (f * 5), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x2 - (f * -2), y2 - (f * 5), x2 - (f * -1), y2 - (f * 4), fill=pix_colour_1)
    center = my_canvas.create_rectangle(x2 - (f * -1), y2 - (f * 4), x2, y2 - (f * 3), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 8), y1 + (f * 4), x1 + (f * 9), y1 + (f * 5), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 9), y1 + (f * 5), x1 + (f * 10), y1 + (f * 6), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 10), y1 + (f * 6), x1 + (f * 11), y1 + (f * 7), fill=pix_colour_1)


def equalto(x1, y1, f=20):
    x2 = x1 + (f * 9)

    # first =
    line = my_canvas.create_rectangle(x1, y1, x1 + (f * 5), y1 + f, fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1, y1 + (f * 3), x1 + (f * 5), y1 + (f * 4), fill=pix_colour_1)
    # second =
    line = my_canvas.create_rectangle(x2, y1, x2 + (f * 5), y1 + f, fill=pix_colour_1)
    line = my_canvas.create_rectangle(x2, y1 + (f * 3), x2 + (f * 5), y1 + (f * 4), fill=pix_colour_1)


def upturned(x1, y1, f=20):
    global upix

    upix = f
    # backdrop = my_canvas.create_rectangle(x1,y1,x1+(f*5),y1+(f*6),fill="grey")
    # upward line
    line = my_canvas.create_rectangle(x1, y1 + (f * 4), x1 + (f * 1), y1 + (f * 6), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 2), x1 + (f * 2), y1 + (f * 4), fill=pix_colour_1)
    # center line
    line = my_canvas.create_rectangle(x1 + (f * 2), y1, x1 + (f * 3), y1 + (f * 2), fill=pix_colour_1)
    # downward line
    line = my_canvas.create_rectangle(x1 + (f * 3), y1 + (f * 2), x1 + (f * 4), y1 + (f * 4), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 4), y1 + (f * 4), x1 + (f * 5), y1 + (f * 6), fill=pix_colour_1)


def two_upturned(ux, uy):
    upturned(ux, uy)
    upturned(ux + (upix * 8), uy)


def backwardslash(x1, y1, f=20):
    # test = my_canvas.create_rectangle(x1,y1,x1+(f*5),y1+(f*5),fill = "grey")
    line = my_canvas.create_rectangle(x1, y1, x1 + (f * 1), y1 + (f * 1), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 1), x1 + (f * 2), y1 + (f * 2), fill=pix_colour_1)
    center = my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 2), x1 + (f * 3), y1 + (f * 3), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 3), y1 + (f * 3), x1 + (f * 4), y1 + (f * 4), fill=pix_colour_1)
    l2 = my_canvas.create_rectangle(x1 + (f * 4), y1 + (f * 4), x1 + (f * 5), y1 + (f * 5), fill=pix_colour_1)


def fowardslash(x1, y1, f=20):
    # test = my_canvas.create_rectangle(x1,y1,x1+(f*5),y1+(f*5),fill = "grey")
    line = my_canvas.create_rectangle(x1 + (f * 4), y1, x1 + (f * 5), y1 + (f * 1), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 3), y1 + (f * 1), x1 + (f * 4), y1 + (f * 2), fill=pix_colour_1)
    center = my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 2), x1 + (f * 3), y1 + (f * 3), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 3), x1 + (f * 2), y1 + (f * 4), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1, y1 + (f * 4), x1 + (f * 1), y1 + (f * 5), fill=pix_colour_1)


# ----------------------------------------------------------------------------------------------------------------------------------------------
# / \
def dontknowwhatthisis(ux, uy):
    fowardslash(ux, uy)
    backwardslash(ux + (30 * 9), uy)


# \ /
def angry(ux, uy):
    backwardslash(ux, uy)
    fowardslash(ux + (30 * 9), uy)


# --------------------------------------------------------------------------------------------------------------------------------------------
# sleep ZZ
def z(x1, y1, f=18):
    global apix
    apix = f
    c2 = "#b5b5b5"
    # test = my_canvas.create_rectangle(x1,y1,x1+(f*6),y1+(f*7),fill="pink")
    line = my_canvas.create_rectangle(x1, y1, x1 + (f * 6), y1 + (f * 1), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 5), y1 + (f * 1), x1 + (f * 6), y1 + (f * 2), fill=pix_colour_1, )
    line = my_canvas.create_rectangle(x1 + (f * 4), y1 + (f * 1), x1 + (f * 5), y1 + (f * 2), fill=c2)
    line = my_canvas.create_rectangle(x1 + (f * 4), y1 + (f * 2), x1 + (f * 5), y1 + (f * 3), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 3), y1 + (f * 2), x1 + (f * 4), y1 + (f * 3), fill=c2)
    line = my_canvas.create_rectangle(x1 + (f * 3), y1 + (f * 3), x1 + (f * 4), y1 + (f * 4), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 3), x1 + (f * 3), y1 + (f * 4), fill=c2)
    line = my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 4), x1 + (f * 3), y1 + (f * 5), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 4), x1 + (f * 2), y1 + (f * 5), fill=c2)
    line = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 5), x1 + (f * 2), y1 + (f * 6), fill=pix_colour_1)
    line = my_canvas.create_rectangle(x1, y1 + (f * 5), x1 + (f * 1), y1 + (f * 6), fill=c2)
    line = my_canvas.create_rectangle(x1, y1 + (f * 6), x1 + (f * 6), y1 + (f * 7), fill=pix_colour_1)


# sleping ZZ
def z_z(ux, uy):
    z(ux, uy)
    z(ux + (apix * 12), uy)


# ---------------------------------------------------------------------------------------------------------------------------------------------
# ! mark
def excl(x1, y1, f=20):
    global bpix
    bpix = f
    c2 = "#b5b5b5"
    # test = my_canvas.create_rectangle(x1,y1,x1+(f*3),y1+(f*7),fill = "pink")
    linel = my_canvas.create_rectangle(x1, y1 + (f * 1), x1 + (f * 1), y1 + (f * 4), fill=c2)
    line = my_canvas.create_rectangle(x1 + (f * 1), y1, x1 + (f * 2), y1 + (f * 5), fill=pix_colour_1)
    spot = my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 6), x1 + (f * 2), y1 + (f * 7), fill=pix_colour_1)
    liner = my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 1), x1 + (f * 3), y1 + (f * 4), fill=c2)


# supprised
def suprised(ux, uy):
    excl(ux, uy)
    excl(ux + (bpix * 5), uy)


def bigcircle(x1, y1, f=20):
    my_canvas.create_rectangle(x1 + (f * 2), y1, x1 + (f * 5), y1 + (f * 1), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 1), x1 + (f * 2), y1 + (f * 2), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 5), y1 + (f * 1), x1 + (f * 6), y1 + (f * 2), fill=pix_colour_1)
    my_canvas.create_rectangle(x1, y1 + (f * 2), x1 + (f * 1), y1 + (f * 5), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 6), y1 + (f * 2), x1 + (f * 7), y1 + (f * 5), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 5), x1 + (f * 2), y1 + (f * 6), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 5), y1 + (f * 5), x1 + (f * 6), y1 + (f * 6), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 2), y1 + (f * 6), x1 + (f * 5), y1 + (f * 7), fill=pix_colour_1)


def smallcircle(x1, y1, f=20):
    my_canvas.create_rectangle(x1 + (f * 1), y1, x1 + (f * 4), y1 + (f * 1), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 1), y1 + (f * 4), x1 + (f * 4), y1 + (f * 5), fill=pix_colour_1)
    my_canvas.create_rectangle(x1, y1 + (f * 1), x1 + (f * 1), y1 + (f * 4), fill=pix_colour_1)
    my_canvas.create_rectangle(x1 + (f * 4), y1 + (f * 1), x1 + (f * 5), y1 + (f * 4), fill=pix_colour_1)


def goofy(ux, uy):
    bigcircle(ux, uy)
    smallcircle(ux + (20 * 11), uy + (20 * 3))


def goofy2(ux, uy):
    bigcircle(ux, uy)
    smallcircle(ux + (20 * 11), uy + (20 * 2))


def normalsmall(ux, uy):
    smallcircle(ux, uy)
    smallcircle(ux + (20 * 8), uy)


def normalbig(ux, uy):
    bigcircle(ux, uy)
    bigcircle(ux + (20 * 11), uy)


# ---------------------------------------------------TRANSINSHIN OR THINKING-------------------------------------------------------------------
def thinking():
    s = 1
    clear()
    Thight = (h // 2) - 25
    com = 40  # distance betewee per itration
    for j in range(s):
        for i in range(-3, 11):  # changing distance
            b1 = my_canvas.create_rectangle((w // 2) + (-125 + com * i), Thight, (w // 2) + (-100 + com * i),
                                            Thight + 25, fill=pix_colour_1)
            sleep(0.1)
            k.update()
        clear()


# --------------------------------------------------------------------------------------------------------------------------------------------

def clear():  # function that clears the canvas
    my_canvas.delete("all")


# --------------------------------------------------CALLING THE FUNCTIONS--------------------------------------------------------------------
def start():
    s = choice(11)
    thinking()
    clear()
    if s == 1:
        clear()
        x_x(x1 - (20 * 8.5), y1 - (20 * 3.5))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()
        clear()
    elif s == 2:
        clear()
        closed(x1 - (20 * 5.5), y1 - (20 * 3.5), 20)

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()
        clear()
    elif s == 3:
        clear()
        equalto(x1 - (20 * 7), y1 - (20 * 2))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()

        clear()
    elif s == 4:
        clear()
        two_upturned(x1 - (30 * 5), y1 - (30 * 3))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()

        clear()
    elif s == 5:
        clear()
        dontknowwhatthisis(x1 - (30 * 6.5), y1 - (30 * 2.5))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()

        clear()
    elif s == 6:
        clear()
        angry(x1 - (30 * 6), y1 - (30 * 2.5))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()

        clear()
    elif s == 7:
        clear()
        z_z(x1 - (30 * 6), y1 - (30 * 3))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()

        clear()
    elif s == 8:
        clear()
        suprised(x1 - (20 * 4), y1 - (20 * 4))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()
        clear()
    elif s == 9:
        clear()
        goofy(x1 - (30 * 6), y1 - (30 * 3))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()
        clear()
    elif s == 10:
        clear()
        normalsmall(x1 - (20 * 6.5), y1 - (20 * 2.5))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()
        clear()
    elif s == 11:
        clear()
        normalsmall(x1 - (20 * 6.5), y1 - (20 * 2.5))

        k.update()
        # k.after(1000)
        sleep(5)
        thinking()
        clear()


i = 0
while i < 1:
    start()

k.mainloop()
