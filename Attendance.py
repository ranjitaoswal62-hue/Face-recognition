from tkinter import *
from tkinter import ttk
from tkinter import font     
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata=[]
class Attendance :
     def __init__(self, root):
                self.root = root
                self.root.title("Face Recognition System")
                self.root.geometry("1530x790+0+0")

                #============variables==============
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_time=StringVar()
                


                 #first image
                img=Image.open(r"college photos\Smart-Attendance-System.jpg")
                img=img.resize((800,200), resample=Image.Resampling.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root, image=self.photoimg)
                f_lbl.place(x=0, y=0, width=800, height=200)

                #second image


                img1=Image.open(r"college photos\college face attendance.jpg")
                img1=img1.resize((800,200), resample=Image.Resampling.LANCZOS)              
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root, image=self.photoimg1)
                f_lbl.place(x=800, y=0, width=800, height=200)

                #bg image 
                img_bg=Image.open(r"C:\Users\asus\OneDrive\Desktop\faec recognition system\college photos\background phot0.jpg")
                img_bg=img_bg.resize((1530,710), resample=Image.Resampling.LANCZOS)
                self.photoimg_bg=ImageTk.PhotoImage(img_bg)

                self.bg_img=Label(self.root, image=self.photoimg_bg)
                self.bg_img.place(x=0, y=200, width=1530, height=710)

                title_lbl=Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
                title_lbl.place(x=0, y=200, width=1530, height=45)

                main_frame=Frame(self.bg_img,bd=2)
                main_frame.place(x=20,y=50,width=1490,height=600)

                #left Label Frame
                left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Attendance Details",font=("times new roman",12,"bold"))
                left_frame.place(x=10,y=10,width=760,height=580)

                img_left=Image.open(r"college photos\student details.jpg")
                img_left=img_left.resize((750,130), resample=Image.Resampling.LANCZOS)              
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                
                f_lbl=Label(left_frame, image=self.photoimg_left)
                f_lbl.place(x=5, y=0, width=750, height=130)

                left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
                left_inside_frame.place(x=0,y=135,width=740,height=370)

                #label and entry
                #Attendance id
                AttendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
                AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

                AttendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
                AttendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

                #Name
                rolllabel=Label(left_inside_frame,text="Roll:",font=("comicsansns",11,"bold"))
                rolllabel.grid(row=0,column=2,padx=4,pady=8,)

                atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("omicsansns",11,"bold"))
                atten_roll.grid(row=0,column=3,pady=8,)

                #date
                namelabel=Label(left_inside_frame,text="Name:",bg="white",font=("comicsansns",11,"bold"))
                namelabel.grid(row=1,column=0)

                atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("omicsansns",11,"bold"))
                atten_name.grid(row=1,column=1,pady=8,)

                #Department
                deplabel=Label(left_inside_frame,text="Department:",bg="white",font=("comicsansns",11,"bold"))
                deplabel.grid(row=1,column=2)

                atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font=("omicsansns",11,"bold"))
                atten_dep.grid(row=1,column=3,pady=8,)

                #time
                timelabel=Label(left_inside_frame,text="Time:",bg="white",font=("comicsansns",11,"bold"))
                timelabel.grid(row=2,column=0)

                atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("omicsansns",11,"bold"))
                atten_time.grid(row=2,column=1,pady=8,)

                #date
                datelabel=Label(left_inside_frame,text="Date:",bg="white",font=("comicsansns",11,"bold"))
                datelabel.grid(row=2,column=2)

                atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("omicsansns",11,"bold"))
                atten_date.grid(row=2,column=3,pady=8,)

                #Attendance 
                attendancelabel=Label(left_inside_frame,text="Attendance Status:",bg="white",font=("comicsansns",11,"bold"))
                attendancelabel.grid(row=3,column=0,)

                self.atten_status=ttk.Combobox(left_inside_frame,font=("comicsansns",11,"bold"),width=20,state="readonly")
                self.atten_status["values"]=("PRESENT")
                self.atten_status.current(0)
                self.atten_status.grid(row=3,column=1,pady=8)

                #buttons Frame
                btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=300,width=725,height=70)

                save_btn=Button(btn_frame,text="Import csv",width=17,command=self.importCsv,font=("times new roman",13,"bold"),bg="blue",fg="white")
                save_btn.grid(row=0,column=0)

                update_btn=Button(btn_frame,text="Export csv",width=17,command=self.exportCsv,font=("times new roman",13,"bold"),bg="blue",fg="white")
                update_btn.grid(row=0,column=1)

                delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
                delete_btn.grid(row=0,column=2)

                reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
                reset_btn.grid(row=0,column=3)
                    
                #Right label Frame
                Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
                Right_frame.place(x=750,y=10,width=720,height=580)

                table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
                table_frame.place(x=5,y=5,width=700,height=455)

                #========scroll bar table==========
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.attendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","date","time",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.attendanceReportTable.xview)
                scroll_y.config(command=self.attendanceReportTable.yview)

                self.attendanceReportTable.heading("id",text="student Id")
                self.attendanceReportTable.heading("roll",text="Roll")
                self.attendanceReportTable.heading("name",text="Name")
                self.attendanceReportTable.heading("department",text="Department")
                self.attendanceReportTable.heading("date",text="Date")
                self.attendanceReportTable.heading("time",text="Time")
                

                self.attendanceReportTable["show"]="headings"
                self.attendanceReportTable.column("id",width=100)
                self.attendanceReportTable.column("roll",width=100)
                self.attendanceReportTable.column("name",width=100)
                self.attendanceReportTable.column("department",width=100)
                self.attendanceReportTable.column("date",width=100)
                self.attendanceReportTable.column("time",width=100)
                
                



                self.attendanceReportTable.pack(fill=BOTH,expand=1)

                self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

     #==========fetch data=============

     def fetchdata(self,rows):
         self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
         for i in rows:
              self.attendanceReportTable.insert("",END,values=i)

    #import csv
                                        
     def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                  csvread=csv.reader(myfile,delimiter=",")
                  for i in csvread:
                        mydata.append(i)
                  self.fetchdata(mydata)

       #export csv

     def exportCsv(self):
            try:
                 if len(mydata)<1:
                     messagebox.showerror("No Data", "No Data found to export",parent=self.root)
                     return False
                 fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                 with open(fln,mode="w",newline="") as myfile:
                  exp_write=csv.writer(myfile,delimiter=",")
                  for i in mydata:
                    exp_write.writerow(i)
                  messagebox.showinfo("Data export","your data exported to"+os.path.basename(fln)+"successfully")
            except Exception as es:
                   messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

     def get_cursor(self,event=""):
                 cursor_row=self.attendanceReportTable.focus()
                 content=self.attendanceReportTable.item(cursor_row)
                 rows=content['values']
                 self.var_atten_id.set(rows[0])
                 self.var_atten_roll.set(rows[1])
                 self.var_atten_name.set(rows[2])
                 self.var_atten_dep.set(rows[3])
                 self.var_atten_date.set(rows[4])
                 self.var_atten_time.set(rows[5])
                 

     def reset_data(self):
           self.var_atten_id.set("")
           self.var_atten_roll.set("")
           self.var_atten_name.set("")
           self.var_atten_dep.set("")
           self.var_atten_date.set("")
           self.var_atten_time.set("")
          

           




       
       



if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()