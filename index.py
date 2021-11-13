from tkinter import *
from PIL import Image, ImageTk
import string
import random
from time import strftime

#WINDOW
# -------------------------------------------------------------------------------------------------------------
window = Tk()
window.title ("MUT Restaurant")
window.resizable(0,0)

#BACKGROUND IMAGE
# ------------------------------------------------------------------------------------------------------------
image = Image.open('bg.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(window, image = photo_image)
label.pack()


#LIVE TIME
# -------------------------------------------------------------------------------------------------------------
def my_time():
    time_string = strftime('%H:%M:%S %p %d %B %Y') # time format 
    l1.config(text=("Time is {}".format(time_string)))
    l1.after(1000,my_time) # time delay of 1000 milliseconds 

var = StringVar()
label = Label( window, textvariable=var, relief=FLAT,fg="#ce281c",bg="white",font = ('courier', 30, 'bold') )



#REF NO
# --------------------------------------------------------------------------------------------------------------------
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
       return ''.join(random.choice(chars) for _ in range(size))

var.set(id_generator())
label.place(relx=.45,rely=.25,relwidth=.2,relheight=.055)

l1=Label(window,font=('times',20,'bold'),bg='white')
l1.place(relx=.30,rely=.10,relwidth=.5,relheight=.055)

#NAVIGATION BUTTONS
# --------------------------------------------------------------------------------------------------------
food_btn = Button(window,text="FOOD",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold') )
food_btn.place(relx=.08,rely=.45,relwidth=.1,relheight=.055)


drink_btn = Button(window,text="DRINK",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold') )
drink_btn.place(relx=.08,rely=.584,relwidth=.1,relheight=.055)

logout_btn = Button(window,text="LOGOUT",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold') )
logout_btn.place(relx=.08,rely=.715,relwidth=.1,relheight=.055)


about_btn = Button(window,text="ABOUT",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold') )
about_btn.place(relx=.08,rely=.845,relwidth=.1,relheight=.055)
# -------------------------------------------------------------------------------------------------------------


#COMPUTATION BUTTONS
# ---------------------------------------------------------------------------------------------------------------
compute_btn = Button(window,text="COMPUTE",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold') )
compute_btn.place(relx=.23,rely=.90,relwidth=.21,relheight=.055)


reset_btn = Button(window,text="RESET",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold') )
reset_btn.place(relx=.50,rely=.90,relwidth=.21,relheight=.055)

process_btn = Button(window,text="PROCESS",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold') )
process_btn.place(relx=.75,rely=.90,relwidth=.21,relheight=.055)
# ----------------------------------------------------------------------------------------------------------------

my_time()
window.mainloop()