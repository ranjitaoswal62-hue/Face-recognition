from tkinter import *
from tkinter import ttk
from tkinter import font     
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top=Image.open(r"college photos\software-developer-coding-laptop.jpg")
        img_top=img_top.resize((1530,720), resample=Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=720)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

      

        #developer info

        dev_label=Label(main_frame,text="Hello my name is Rohit",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am a student of MCU,Bhopal",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img_top2=Image.open(r"college photos\developers.jpg")
        img_top2=img_top2.resize((500,390), resample=Image.Resampling.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame, image=self.photoimg_top2)
        f_lbl.place(x=0, y=210 ,width=500, height=390)









if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()


    