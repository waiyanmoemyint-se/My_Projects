#My Loggin Form

from tkinter import*
def Myloggin_From():
    window = Tk()
    window.title("Login System")
    lbl    = Label(window,text = "Login",width=15,height="2",font=("unicode",15),fg ="black",bg="white")
    lbl.pack()
    lbl    = Label(window,text= "E-Mail Address")
    lbl.pack()
    Ent    = Entry(window,width = 20)
    Ent.pack() 
    lbl    = Label(window,text = "Password", width = 10)
    lbl.pack()
    Ent    = Entry(window,width = 20)
    Ent.pack()
    Bnt    = Button(text = "Login",bg ="white",fg = "blue",height='2')
    Bnt.pack()
    window.mainloop()
Myloggin_From()
 
