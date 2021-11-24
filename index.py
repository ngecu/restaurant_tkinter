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


def show_food():
    time_string = strftime('%H:%M:%S %p %d %B %Y') # time format 
    l1.config(text=("Time is {}".format(time_string)))
    l1.after(1000,my_time) # time delay of 1000 milliseconds 


def show_drink():
    time_string = strftime('%H:%M:%S %p %d %B %Y') # time format 
    l1.config(text=("Time is {}".format(time_string)))
    l1.after(1000,my_time) # time delay of 1000 milliseconds 

def logout():
    time_string = strftime('%H:%M:%S %p %d %B %Y') # time format 
    l1.config(text=("Time is {}".format(time_string)))
    l1.after(1000,my_time) # time delay of 1000 milliseconds 

def about():
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
food_btn = Button(window,text="FOOD",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold'),command= lambda : show_food() )
food_btn.place(relx=.08,rely=.45,relwidth=.1,relheight=.055)


drink_btn = Button(window,text="DRINK",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold'),command= lambda : show_drink() )
drink_btn.place(relx=.08,rely=.584,relwidth=.1,relheight=.055)

logout_btn = Button(window,text="LOGOUT",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold'),command= lambda : logout() )
logout_btn.place(relx=.08,rely=.715,relwidth=.1,relheight=.055)


about_btn = Button(window,text="ABOUT",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold'),command= lambda : about() )
about_btn.place(relx=.08,rely=.845,relwidth=.1,relheight=.055)
# -------------------------------------------------------------------------------------------------------------


#COMPUTATION BUTTONSS
# ---------------------------------------------------------------------------------------------------------------
compute_btn = Button(window,text="COMPUTE",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold') )
compute_btn.place(relx=.23,rely=.90,relwidth=.21,relheight=.055)


reset_btn = Button(window,text="RESET",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold') )
reset_btn.place(relx=.50,rely=.90,relwidth=.21,relheight=.055)

process_btn = Button(window,text="PROCESS",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold') )
process_btn.place(relx=.75,rely=.90,relwidth=.21,relheight=.055)
# ----------------------------------------------------------------------------------------------------------------



#SELECTION FRAME
# -------------------------------------------------------------------------------------------------------------------
selection_frame = Frame(window,bg="#bec8bb",borderwidth=10,relief=RAISED)
selection_frame.place(relx=.20,rely=.4,relwidth=.40,relheight=.48)






food_frame = Frame(selection_frame)
food_frame.place(relx=0,rely=0,relwidth=1,relheight=1)


food_text = Label(food_frame,text="food")
food_text.pack()



drink_frame = Frame(selection_frame)
drink_frame.place(relx=0,rely=0,relwidth=1,relheight=1)


drink_text = Label(drink_frame,text="drink")
drink_text.pack()


welcome_frame = Frame(selection_frame)
welcome_frame.place(relx=0,rely=0,relwidth=1,relheight=1)


chimage = Image.open('chicken.png')
chimage = chimage.resize((450, 350), Image.ANTIALIAS)
chiphoto_image = ImageTk.PhotoImage(chimage)
chilabel = Label(welcome_frame, image = chiphoto_image)
chilabel.pack()



#RECIPT FRAME
# ---------------------------------------------------------------------------------------------------------------------
receipt_frame = Frame(window,bg="white",relief=SUNKEN)
receipt_frame.place(relx=.60,rely=.4,relwidth=.375,relheight=.48)


b_frame = Label(receipt_frame,text="Bill Area")
b_frame.pack()



labelframe_widget = LabelFrame(receipt_frame,
                                   text="Bill Receipt")
label_widget=Label(labelframe_widget,bg="white",font = ('courier', 15, 'bold'),
       text="    ============= MUT MESS ACCOUNTS ============= \n                  ORDER TIME :                   \n                   SERVED BY :                   \n  ===================================================== \n Product      QTY   Price      Total    \n  =====================================================")

labelframe_widget.place(relx=0,rely=0,relwidth=1,relheight=.45)
label_widget.place(relx=0,rely=0,relwidth=1,relheight=1)


Lb1 = Listbox(receipt_frame,bg="white")
Lb1.place(relx=0,rely=0.45,relwidth=1,relheight=.65)



my_time()
window.mainloop()