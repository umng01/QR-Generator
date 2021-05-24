from tkinter import*
import qrcode
from resizeimage import resizeimage
from PIL import ImageTk,Image


class Qr_Generator:
    qr = qrcode.QRCode(
        version = 1,
        box_size = 5,
        border = 5
    )
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False,False)

        title = Label(self.root,text = "             QR CODE GENERATOR",font = ("times new roman",40),bg = "blue",fg = "white",anchor ="w").place(x=0,y=0,relwidth=1)

        # employee detail window
        #variables
        
        self.v1=StringVar()
        self.v2=StringVar()
        self.v3=StringVar()
        self.v4=StringVar()
        
    
        emp_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title = Label(emp_Frame,text = "Employee Details",font = ("goudy old style",30),bg = "#043256",fg = "white")
        emp_title.place(x=0,y=0,relwidth=1)

        l1 = Label(emp_Frame,text = "Employee ID",font = ("times new roman",15,'bold'),bg = "white").place(x=20,y=60)
        l2=  Label(emp_Frame,text = "Name",font = ("times new roman",15,'bold'),bg = "white").place(x=20,y=100)
        l3 = Label(emp_Frame,text = "Department",font = ("times new roman",15,'bold'),bg = "white").place(x=20,y=140)
        l4 = Label(emp_Frame,text = "Designation",font = ("times new roman",15,'bold'),bg = "white").place(x=20,y=180)

        e1 = Entry(emp_Frame,font = ("times new roman",15,),textvariable=self.v1,bg = "light yellow").place(x=200,y=60)
        e2 = Entry(emp_Frame,font = ("times new roman",15,),textvariable=self.v2,bg = "light yellow").place(x=200,y=100)
        e3 = Entry(emp_Frame,font = ("times new roman",15,),textvariable=self.v3,bg = "light yellow").place(x=200,y=140)
        e4 = Entry(emp_Frame,font = ("times new roman",15,),textvariable=self.v4,bg = "light yellow").place(x=200,y=180)

        b1 = Button(emp_Frame,text='QR Generate',command = self.generate,font =('times new roman',18,'bold'),bg='#2196f3',fg='white')
        b1.place(x=90,y=250,width=180,height=30)
        clear = Button(emp_Frame,text='Clear',font =('times new roman',18,'bold'),command = self.clear,bg='#607d8b',fg='white').place(x=280,y=250,width=120,height=30)

        self.msg=''
        self.l=Label(emp_Frame,text =self.msg,font = ("times new roman",20),bg = "white",fg = "green")
        self.l.place(x=0,y=320,relwidth=1)
# new frame 

        qr_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=600,y=100,width=250,height=380)
        qr_title = Label(qr_Frame,text = "Employee QR Code",font = ("goudy old style",20),bg = "#043256",fg = "white").place(x=0,y=0,relwidth=1)

        self.qr_code = Label(qr_Frame,text='No QR\n Available',font=('times new roman',15),bg="#3f51b5",fg = "white",bd=1,relief = RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.v1.set('')
        self.v2.set('')
        self.v3.set('')
        self.v4.set('')

        self.msg=''
        self.l.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.v1.get()=='' or self.v2.get()=='' or self.v3.get()=='' or self.v4.get()=='':
            self.msg='All fields required !!'
            self.l.config(text=self.msg,fg='red')
        else:
            qr_data =(f"Employee ID :\n\n{self.v1.get()}Employee Name :\n\n{self.v2.get()}Department :\n\n{self.v3.get()}Designation :{self.v4.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_QR/Emp_"+str(self.v1.get())+'.png')

            self.im = ImageTk.PhotoImage(file="Employee_QR/Emp_"+str(self.v1.get())+'.png')
            self.qr_code.config(image=self.im)

            self.msg = "Qr Generated Successfully!"
            self.l.config(text=self.msg,fg='green')

root = Tk()
obj = Qr_Generator(root)
root.mainloop()
