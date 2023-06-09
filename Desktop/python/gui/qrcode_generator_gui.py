from cgitb import text
from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Genertor:
    def __init__(self,root):#default construcor
       self.root=root#to cll the self again
       self.root.geometry("900x500+200+40")#geometry 900 iswidth  500 is height and x and y axis
       self.root.title("Qr generator| Developed by Rajath")
       self.root.resizable(False,False)#to hide the resizable option
       
       
       titile=Label(self.root,text="  QR code generator",font=("times new roman",40),bg='black',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
       #employe details window=================
       #==========varialble==========
       self.var_emp_id=StringVar()
       self.var_emp_name=StringVar()
       self.var_emp_department=StringVar()
       self.var_emp_designation=StringVar()


       emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
       emp_Frame.place(x=50,y=100,width=500,height=380)
       emp_titile=Label(emp_Frame,text="  Employe details",font=("goudy old styles",20),bg='black',fg='white').place(x=0,y=0,relwidth=1)
       emp_id=Label(emp_Frame,text="Employe ID",font=("goudy old styles",15,'bold'),bg='white').place(x=20,y=60)
       emp_name=Label(emp_Frame,text="Employe name",font=("goudy old styles",15,'bold'),bg='white').place(x=20,y=100)
       emp_department=Label(emp_Frame,text="Department",font=("goudy old styles",15,'bold'),bg='white').place(x=20,y=140)
       emp_designation=Label(emp_Frame,text="Designation",font=("goudy old styles",15,'bold'),bg='white').place(x=20,y=180)
       
       #textfield==============================================================
       txt_id=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_id,bg='white').place(x=200,y=60)
       txt_name=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_name,bg='white').place(x=200,y=100)
       txt_department=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_department,bg='white').place(x=200,y=140)
       txt_designation=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_designation,bg='white').place(x=200,y=180)
       
       btn=Button(emp_Frame,text="QR Generate",command=self.generate,font=("times new roman",18,'bold'),bg='light green',fg='white').place(x=90,y=250,width=180,height=30)
       btn_clr=Button(emp_Frame,text="clear",command=self.clear,font=("times new roman",18,'bold'),bg='grey',fg='white').place(x=280,y=250,width=120,height=30)
       
       self.msg=""
       self.label_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
       self.label_msg.place(x=0,y=310,relwidth=1)
       
       #this for the qr frame===========================================================================================
       qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
       qr_Frame.place(x=600,y=100,width=250,height=380) 
       qr_titile=Label(qr_Frame,text="  QR Code",font=("goudy old styles",20),bg='black',fg='white').place(x=0,y=0,relwidth=1)
       self.qr_code=Label(qr_Frame,text="no Qr \nAvalible",font=("times new roman",15),bg='dark blue',fg='white')
       self.qr_code.place(x=35,y=100,width=180,height=180)

       #====================================================================================
    def clear(self):
        self.var_emp_id.set('')
        self.var_emp_name.set('')
        self.var_emp_department.set('')
        self.var_emp_designation.set('')
        self.msg=""
        self.label_msg.config(text=self.msg)
        self.qr_code.config(image='')
    
    def generate(self):
        if self.var_emp_designation.get()=="" or self.var_emp_id.get()=='' or self.var_emp_department.get()==''or self.var_emp_name.get()=='':
            self.msg="All fields are required!!!!!"
            self.label_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Emoloyee ID : {self.var_emp_id.get()}\nEmployee Name : {self.var_emp_name.get()}\nDepartment : {self.var_emp_department.get()}\n Designation :{self.var_emp_designation.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            #qrcode image update
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            #updating notification====================================================
            self.msg="QR Generated Sucessfully"
            self.label_msg.config(text=self.msg,fg='green')
            
           
root=Tk()
raj=Qr_Genertor(root)#object for class
root.mainloop()#to not to close the window 