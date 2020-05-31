from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
#from PIL import Image
import pymysql as my

window=Tk()

window.configure(background="lightgreen")

window.title("Welcome to DL license Application")
window.geometry("400x350")
a=IntVar()
c1=Checkbutton(window,text="Are you Indian",variable=a)
c1.grid(column=1,row=1)
lbl=Label(window,text="Please enter your age:",font=("Arial Bold",20))
lbl.grid(column=0,row=0)
text=Entry(window,width=13)
text.grid(column=1,row=0)

def click2():
    window2=Tk()
    window2.geometry("400x380")
    window2.configure(background="lightblue")

    lb1=Label(window2,text="Welcome to DL registration Page")

    l1 = Label(window2, text="First Name:")
    l1.grid(column=0, row=0)
    txt1 = Entry(window2, width=25)
    txt1.grid(column=1, row=0)
    firstname=str(txt1.get())
    print(firstname)
    l2 = Label(window2, text="Last Name :")
    l2.grid(column=0, row=1)
    txt2 = Entry(window2, width=25)
    txt2.grid(column=1, row=1)
    lastname=str(txt2.get())

    l3 = Label(window2, text="Gender :")
    l3.grid(column=0, row=2)
    combo = Combobox(window2)
    combo['values'] = ['MALE', 'FEMALE', 'OTHERS']
    gender = combo.get()
    txt3 = Entry(window2, width=25)
    combo.grid(column=1, row=2)


    l4 = Label(window2, text="Address:")
    l4.grid(column=0, row=3)
    txt4 = Entry(window2, width=25)
    txt4.grid(column=1, row=3)
    address=str(txt4.get())

    l5 = Label(window2, text="License Type:")
    l5.grid(column=0, row=4)

    combo = Combobox(window2)
    combo['values'] = ['LMV', 'HMV','Both']
    licensetype=combo.get()
    combo.grid(column=1, row=4)


    def browse():
        filename=filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("jpeg",".jpg"),("all files",".*")))
        print(filename)
        f = open(filename,'rb')
        f1 = open('img.jpg', 'wb')
        for i in f:
            f1.write(i)
        f.close()
        f1.close()
    def button():
        button = Button(window2, text = "Browse",command=browse)
        button.grid(column=1, row=6)


    l6 = Label(window2,text="Birth Certificate : ")
    l6.grid(column=0,row=6)
    button()







    def save():
        print("inside save")
        firstname = str(txt1.get())
        lastname=str(txt2.get())
        gender=combo.get();
        address=str(txt4.get())

        licensetype=combo.get();
        q1="""insert into userinfo(first_name,last_name,gender,address,license_type)values('"+firstname+"','"+lastname+"','"+gender+"','"+address+"','"+licensetype+"');"""
        conn=my.connect(host="127.0.0.1",user="your_user_name_sql",
                             password="your_password_for _Database",
                             db="driving_license")
        #print("conn created")
        cur=conn.cursor()
        print(conn)
        cur.execute("insert into driving_license.userinfo(first_name,last_name,gender,address,license_type)values('"+firstname+"','"+lastname+"','"+gender+"','"+address+"','"+licensetype+"');")
        conn.commit()
        messagebox.showinfo(window2,"Registration completed")
        conn.close()
    def exit():
        import sys
        sys.exit()

    bt1 = Button(window2, text="Save",command=save)
    bt1.grid(column=1, row=9)
    bt2 = Button(window2, text="Close",command=exit)
    bt2.grid(column=3, row=9)

    window2.geometry("400x300")
    window2.mainloop()

btn2=Button(window,text="Next",command=click2)
btn2.grid(column=1,row=7)
def click():
    if a.get()==0:
        #text.configure(state="disabled")
        messagebox.showinfo(window,"Non Indian can not file for Driving License")
    else:
        age=int(text.get())
        if age>=18:
            messagebox.showinfo(window,"You can apply")
            lb2 = Label(window, text="You can apply click next button to fill the form")
            lb2.grid(column=0, row=6)
        else:
            messagebox.showinfo(window,"Request Denied")

btn=Button(window,text="Submit",command=click)
btn.grid(column=0,row=7)
window.mainloop()
