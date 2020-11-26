#Phillips Hue Home automation project
#Allows control of Phillips Hue Bulbs
(r'^phue', 'phue'),
def myAPI(request):
    run();

from tkinter import *
from tkinter import ttk
import time
import urllib.request
import phue
from phue import Bridge

def run():
    b = Bridge('192.168.1.151') #Replace with your Phllips Hue Hub Address

    try:
        b.connect()
        bridgeState = b.get_api()
        
    except:
        print("Failed to connect to bridge")

    lights = b.lights

    for lightBulb in lights:
        print(lightBulb.name)

    root = Tk()
    root.style = ttk.Style() 
    root.style.theme_use('clam')
    #root.configure(background='black')

    frame = Frame(root)
    frame.grid(row=0)

    def turn_on():
        check = b.get_light(1, 'on')
        print (check)
        if (check == False):
            b.set_light(1, 'on', True)
            print("Light turned on")
        else:
            print("Light is already on")

    def turn_off():
        check = b.get_light(1, 'on')
        print (check)
        if (check == True):
            b.set_light(1, 'on', False)
            print("Light turned off")
        else:
            print("Light is already off")

    def quit():
        root.destroy()

    """ def quit_popUp():

        def quit2():
            popup.destroy
            popup.destroy()
    
        popup = Tk()
        popup.wm_title("!")
        popup.title("Quit")
        msg = Message(popup, text= "Are you sure you want to quit?").grid(row=0)
        button_yes = ttk.Button(popup, text = "Yes",width = 10, command = quit).grid(row=1)
        button_no = ttk.Button(popup, text = "No",width = 10, command = quit2).grid(row=2)
        popup.mainloop() """

    """ img = PhotoImage(file ="/home/pi/Desktop/Python Images/OnButton.png")
    img2 = PhotoImage(file ="/home/pi/Desktop/Python Images/OffButton.png")
    img3 = PhotoImage(file ="/home/pi/Desktop/Python Images/QuitButton.png") """

    lights = b.get_light_objects('id')

    rowNum = 0
    for light_id in lights:

        scale_command = lambda x, light_id=light_id: b.set_light(light_id,{'bri': int(x), 'transitiontime': 1})
        scale = Scale(frame, from_ = 254, to = 0,activebackground='gray',fg= 'white',highlightbackground='gray', command = scale_command, length = 200,borderwidth=.001, showvalue=0,troughcolor = 'lightgray', orient = 'horizontal', bg = 'gray', label= "Brightness")
        scale.set(b.get_light(light_id,'bri'))
        scale.grid(row = rowNum, column = 2)

        button_var = BooleanVar()
        button_var.set(b.get_light(light_id, 'on'))
        button_command = lambda button_var=button_var, light_id=light_id: b.set_light(light_id, 'on', button_var.get())


        button = Checkbutton(frame, variable = button_var, command = button_command)
        button.grid(row= rowNum, column = 0)

        label = Label(frame)
        label.config(text = b.get_light(light_id,'name'))
        label.grid(row = rowNum, column = 1)
        rowNum = rowNum + 1


    root.mainloop()
