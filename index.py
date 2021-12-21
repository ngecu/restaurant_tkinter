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

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
       return ''.join(random.choice(chars) for _ in range(size))

var = StringVar()
label = Label( window, textvariable=var, relief=FLAT,fg="#ce281c",bg="white",font = ('courier', 30, 'bold') )
var.set(id_generator())
label.place(relx=.45,rely=.25,relwidth=.2,relheight=.055)

#LIVE TIME
# -------------------------------------------------------------------------------------------------------------
def my_time():
    time_string = strftime('%H:%M:%S %p %d %B %Y') # time format 
    l1.config(text=("Time is {}".format(time_string)))
    l1.after(1000,my_time) # time delay of 1000 milliseconds 






def show_food():
    food_frame.place(relx=0)
    drink_frame.place_forget()
    welcome_frame.place_forget()
    food_btn.config(background="#ffcc4d")
    drink_btn.config(background="#ce281c")
    


def reset():
    welcome_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    drink_frame.place_forget()
    food_frame.place_forget()
    var.set(id_generator())
    food_btn.config(background="#ce281c")
    drink_btn.config(background="#ce281c")

def show_drink():
    drink_frame.place(relx=0)
    food_frame.place_forget()
    welcome_frame.place_forget()
    food_btn.config(background="#ce281c")
    drink_btn.config(background="#ffcc4d")





#REF NO
# --------------------------------------------------------------------------------------------------------------------




l1=Label(window,font=('times',20,'bold'),bg='white')
l1.place(relx=.30,rely=.10,relwidth=.5,relheight=.055)

#NAVIGATION BUTTONS
# --------------------------------------------------------------------------------------------------------
food_btn = Button(window,text="FOOD",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold'),command= lambda : show_food() )
food_btn.place(relx=.08,rely=.45,relwidth=.1,relheight=.055)


drink_btn = Button(window,text="DRINK",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold'),command= lambda : show_drink() )
drink_btn.place(relx=.08,rely=.584,relwidth=.1,relheight=.055)

logout_btn = Button(window,text="LOGOUT",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold'))
logout_btn.place(relx=.08,rely=.715,relwidth=.1,relheight=.055)


about_btn = Button(window,text="ABOUT",relief=FLAT,bg="#ce281c",fg="white",font = ('courier', 20, 'bold') )
about_btn.place(relx=.08,rely=.845,relwidth=.1,relheight=.055)
# -------------------------------------------------------------------------------------------------------------


#COMPUTATION BUTTONSS
# ---------------------------------------------------------------------------------------------------------------
compute_btn = Button(window,text="COMPUTE",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold') )
compute_btn.place(relx=.23,rely=.90,relwidth=.21,relheight=.055)


reset_btn = Button(window,text="RESET",relief=FLAT,bg="#1d73be",fg="white",font = ('courier', 20, 'bold'),command=lambda : reset() )
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

food_label = Label(food_frame,text="food Menu")
food_frame.grid(row=3,column=1,ipadx=20, ipady=10,padx=10,pady=10 )


foods = [
    {
        "name":"Biryani",
        "price":"1.2 USD",
        "image":"images/biryani.png"
    },
   {
        "name":"Burger",
        "price":"3.2 USD",
        "image":"images/burger.png"
    },
   {
        "name":"Chicken",
        "price":"2.0 USD",
        "image":"images/chicken.png"
    },

       {
        "name":"Fries",
        "price":"1.5 USD",
        "image":"images/fries.png"
    },
       {
        "name":"Pizza",
        "price":"10 USD",
        "image":"images/pizza.png"
    },
       {
        "name":"Samosa",
        "price":"0.5 USD",
        "image":"images/samosa.png"
    },
]




    # Button(food_frame
    # ,image=ImageTk.PhotoImage(Image.open(food.get("image")).resize((100, 100), Image.ANTIALIAS))).grid(row=1,column=idx,ipadx=20, ipady=10,padx=10,pady=10 )

# food_text = Label(food_frame,text="food")
# food_text.pack()



drink_frame = Frame(selection_frame)
drink_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

chimagex = Image.open('images/cocktail.png')
chimagex = chimagex.resize((100, 100), Image.ANTIALIAS)
chiphoto_imagex = ImageTk.PhotoImage(chimagex)
chilabel = Button(drink_frame, image = chiphoto_imagex,text="Ngecu")
chilabel.grid(row=1,column=1,ipadx=20, ipady=10,padx=10,pady=10 )

lk = Label(drink_frame,text="Cocktail @ 10")
lk.grid(row=2,column=1)

# chilabel2 = Button(drink_frame, image = chiphoto_imagex)
# chilabel2.grid(row=1,column=2,ipadx=20, ipady=10,padx=10,pady=10)

# lk2 = Label(drink_frame,text="Choma @ 10")
# lk2.grid(row=2,column=2)

# chilabel3 = Button(drink_frame, image = chiphoto_imagex)
# chilabel3.grid(row=1,column=3,ipadx=20, ipady=10)

# lk3 = Label(drink_frame,text="Choma @ 10")
# lk3.grid(row=2,column=3)

# chilabel4 = Button(drink_frame, image = chiphoto_imagex,text="Ngecu")
# chilabel4.grid(row=3,column=1,ipadx=20, ipady=20 )

# lk4 = Label(drink_frame,text="Choma @ 10")
# lk4.grid(row=3,column=1)

# chilabel5 = Button(drink_frame, image = chiphoto_imagex)
# chilabel5.grid(row=3,column=2,ipadx=20, ipady=20)

# lk5 = Label(drink_frame,text="Choma @ 10")
# lk5.grid(row=3,column=2)

# chilabel6 = Button(drink_frame, image = chiphoto_imagex)
# chilabel6.grid(row=3,column=3,ipadx=20, ipady=20)

# lk6 = Label(drink_frame,text="Choma @ 10")
# lk6.grid(row=3,column=3)

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