import winsound
from tkinter import *
import datetime
import time
import playsound
from threading import *

root = Tk()
root.geometry('400x400')
root.title("Alarm Clock App")
root.resizable(0, 0)


def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def clock():
    curr_time = datetime.datetime.now().strftime('%H:%M:%S')
    cur_time.config(text=curr_time)
    cur_time.after(1000, clock)


def alarm():
    while True:
        set_alarm_time = f'{ahour.get()}:{aminute.get()}:{asecond.get()}'
        time.sleep(1)
        curr_time = datetime.datetime.now().strftime('%H:%M:%S')
        if curr_time == set_alarm_time:
            winsound.PlaySound('Ring03.wav', winsound.SND_ASYNC)
            break
            t1.stop()


Label(root, text='Alarm Clock', font='Helvetica 20 bold ', fg='red').pack(pady=10)
Label(root, text='Current Time is:', font='arial 12 bold ', fg='red').pack(pady=2)
cur_time = Label(root, text="00:00:00", font='arial 12 bold')
cur_time.place(x=163, y=100)
clock()
frame = Frame(root)
frame.pack(pady=40)
ahour = StringVar()
ahours = (
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
    '19',
    '20', '21', '22', '23', '24')
ahour.set(ahours[0])
hour = OptionMenu(frame, ahour, *ahours)
hour.pack(side=LEFT)
aminute = StringVar()
aminutes = (
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
    '18', '19',
    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
    '38', '39', '40',
    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58',
    '59', '60')
aminute.set(aminutes[0])
minute = OptionMenu(frame, aminute, *aminutes)
minute.pack(side=LEFT)
asecond = StringVar()
aseconds = (
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
    '18', '19',
    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
    '38', '39', '40',
    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58',
    '59', '60')
asecond.set(aseconds[0])
second = OptionMenu(frame, asecond, *aseconds)
second.pack(side=LEFT)

Button(root, text='Set Alarm', font='Helvetica 15', command=Threading).pack(pady=20)

root.mainloop()

if __name__ == '__main__':
    pass
