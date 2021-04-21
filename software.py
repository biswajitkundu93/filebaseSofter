from tkinter import *
from tkinter import ttk,messagebox
import time
import os

class Login:
    def __init__(self,root):
        #creating windonw
        self.root = root
        self.root.title("File base recored system")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg='skyblue')

        #all veriable
        self.sid = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.contact = StringVar()
        self.date = StringVar()
        self.degree = StringVar()
        self.proof = StringVar()
        self.payment = StringVar()

        title = Label(self.root, text="File Base Record System ",bg="yellow", bd=10,padx=5,pady=10,relief=GROOVE,font=("times new roman", 30,"bold")).pack(fill=X)
        
        Student_frame = Frame(self.root, bd=10, relief=GROOVE, bg='RoyalBlue4')
        Student_frame.place(x=20,y=100, height=520)
        stitle = Label(Student_frame,text="Student Deteails",bg='RoyalBlue4',fg="white", font=("times new roman", 30,"bold")).grid(row=0,columnspan=4,pady=20)

        lblsid = Label(Student_frame,text="Student ID",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=1,column=0,pady=10,padx=20,sticky="w")
        textid = Entry(Student_frame,bd=7, relief=GROOVE,textvariable=self.sid, width=20, font="arial 15 bold").grid(row=1,column=1,padx=10,pady=20)

        lblname = Label(Student_frame,text="Name",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=2,column=0,pady=10,padx=20,sticky="w")
        textname = Entry(Student_frame,bd=7, relief=GROOVE, width=20,textvariable=self.name, font="arial 15 bold").grid(row=2,column=1,padx=10,pady=20)

        lblcontact = Label(Student_frame,text="Contact No",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=1,column=2,pady=10,padx=20,sticky="w")
        textcontact = Entry(Student_frame,bd=7, relief=GROOVE, width=20,textvariable=self.contact, font="arial 15 bold").grid(row=1,column=3,padx=10,pady=20)
        
        lbldate = Label(Student_frame,text="Date(dd/mm/yyyy)",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=2,column=2,pady=10,padx=20,sticky="w")
        textdate = Entry(Student_frame,bd=7, relief=GROOVE, width=20,textvariable=self.date, font="arial 15 bold").grid(row=2,column=3,padx=10,pady=20)
        
        lblcourse = Label(Student_frame,text="Course",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=3,column=0,pady=10,padx=20,sticky="w")
        textcourse = Entry(Student_frame,bd=7, relief=GROOVE, width=20,textvariable=self.course, font="arial 15 bold").grid(row=3,column=1,padx=10,pady=20)
        
        lbladdress = Label(Student_frame,text="Address",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=4,column=0,pady=10,padx=20,sticky="w")
        textaddress = Entry(Student_frame,bd=7, relief=GROOVE, width=20,textvariable=self.address, font="arial 15 bold").grid(row=4,column=1,padx=10,pady=20)
        
        lblcity = Label(Student_frame,text="City",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=5,column=0,pady=10,padx=20,sticky="w")
        textcity = Entry(Student_frame,bd=7, relief=GROOVE, width=20,textvariable=self.city, font="arial 15 bold").grid(row=5,column=1,padx=10,pady=20)

        lblselect = Label(Student_frame,text="Select Degree",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=3,column=2,pady=10,padx=20,sticky="w")
        degreecombo = ttk.Combobox(Student_frame,width=20,state="readonly",textvariable=self.degree, font="arial 15 bold")
        degreecombo['values'] = ("BCA",'MCA',"MBA","B.Tech","M.Tech")
        degreecombo.grid(row=3,column=3,pady=10,padx=20)

        lblid = Label(Student_frame,text="Id Proof",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=4,column=2,pady=10,padx=20,sticky="w")
        idcombo = ttk.Combobox(Student_frame,width=20,state="readonly",textvariable=self.proof, font="arial 15 bold")
        idcombo['values'] = ("Pan Card","Driving Lincense", "Student Id card","Voter Card")
        idcombo.grid(row=4,column=3,pady=10,padx=20)

        lblpayment = Label(Student_frame,text="Payment Mode",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold")).grid(row=5,column=2,pady=10,padx=20,sticky="w")
        paymentcombo = ttk.Combobox(Student_frame,width=20,state="readonly",textvariable=self.payment, font="arial 15 bold")
        paymentcombo['values'] = ("Cash","UPI","Card")
        paymentcombo.grid(row=5,column=3,pady=10,padx=20)

        btnFrame = Frame(self.root, bd=10, relief=GROOVE,bg='RoyalBlue4')
        btnFrame.place(x=10,y=630)
        btnsave = Button(btnFrame,text="save", bd=7,bg="yellow2",fg="black", width=18,font="arial 15 bold",command=self.save_data).grid(row=0,column=0,padx=12,pady=10)
        btndelete = Button(btnFrame,text="Delete", bd=7,bg="yellow2",fg="black", width=18,font="arial 15 bold",command=self.delete_file).grid(row=0,column=1,padx=12,pady=10)
        btnclear = Button(btnFrame,text="Clear", bd=7,bg="yellow2",fg="black", width=18,font="arial 15 bold",command=self.clear_value).grid(row=0,column=2,padx=12,pady=10)
        btnlog = Button(btnFrame,text="Logout", bd=7,bg="yellow2",fg="black", width=19,font="arial 15 bold",command=self.logout_fun).grid(row=0,column=3,padx=12,pady=10)
        btnexit = Button(btnFrame,text="Exit", bd=7,bg="yellow2",fg="black", width=19,font="arial 15 bold",command=self.exit_fun).grid(row=0,column=4,padx=12,pady=10)

        fileFrame = Frame(self.root, bd=10, relief=GROOVE,bg='RoyalBlue4')
        fileFrame.place(x=1010,y=100,height=520,width=350)

        ftitle = Label(fileFrame,text="All Files",bg='RoyalBlue4',fg="white", font=("times new roman", 20,"bold"),bd=5,relief=GROOVE).pack(side=TOP,fill=X)
        scroll_y = Scrollbar(fileFrame,orient=VERTICAL)
        self.file_list = Listbox(fileFrame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()

    def save_data(self):
        present = "no"
        if self.sid.get()=="":
            messagebox.showerror("Error","Student must be required!!!")
        else:
            f = os.listdir('file/')
            if len(f) > 0 :
                for i in f:
                    if i.split('.')[0] == self.sid.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Update", "file already present \nDo you really want to update?")
                    if ask > 0:
                        self.save_files()
                        messagebox.showinfo("Update", "Record has updated successfully")
                        self.show_files()
                else:
                    self.save_files()
                    messagebox.showinfo("Saved", "Record has saved successfully")
                    self.show_files()
            else:
                self.save_files()
                messagebox.showinfo("Saved", "Record has saved successfully")
                self.show_files()

    def save_files(self):
        f=open('file/'+str(self.sid.get())+".txt",'w')
        f.write(
            str(self.sid.get())+","+
            str(self.name.get())+","+
            str(self.course.get())+","+
            str(self.address.get())+","+
            str(self.city.get())+","+
            str(self.contact.get())+","+
            str(self.date.get())+","+
            str(self.degree.get())+","+
            str(self.proof.get())+","+
            str(self.payment.get())
        )
        f.close()  
    
    def show_files(self):
        files=os.listdir("file/")
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)

    def get_data(self,ev):
        get_cursor = self.file_list.curselection()
        f1 = open('file/'+self.file_list.get(get_cursor),'r')
        value = []
        value.extend(f1.read().split(','))

        self.sid.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])

    def clear_value(self):
        self.sid.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")
    
    def delete_file(self):
        present = "no"
        if self.sid.get()=="":
            messagebox.showerror("Error","Student must be required!!!")
        else:
            f = os.listdir('file/')
            if len(f) > 0 :
                for i in f:
                    if i.split('.')[0] == self.sid.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Delete", "Do you really want to Delete?")
                    if ask > 0:
                        os.remove("file/"+self.sid.get()+".txt")
                        messagebox.showinfo("Success", "Deleted successfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error","File not found")
    
    
    def exit_fun(self):
        option = messagebox.askyesno("Exit", "Do you really want to exit...!!! ")
        if option > 0:
            self.root.destroy()
        else:
            return
    
    def logout_fun(self):
        self.root.destroy()
        import login


root = Tk()
ob = Login(root)
root.mainloop()
