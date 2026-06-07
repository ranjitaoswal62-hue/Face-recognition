import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import font     
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top=Image.open(r"C:\Users\asus\OneDrive\Desktop\faec recognition system\college photos\college photos\istockphoto-2208404589-612x612.jpg")
        img_top=img_top.resize((1530,720), resample=Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=720)

        # EMAIL
        email_lbl = Label(f_lbl, text="📧 Email: Rohitoswal338@gmail.com",
                          font=("times new roman",20,"bold"),
                          bg="black", fg="cyan", cursor="hand2")
        email_lbl.place(x=500, y=200)
        email_lbl.bind("<Button-1>", lambda e: self.open_email())

        # WHATSAPP
        whatsapp_lbl = Label(f_lbl, text="💬 WhatsApp: +91 7898615450",
                             font=("times new roman",20,"bold"),
                             bg="black", fg="green", cursor="hand2")
        whatsapp_lbl.place(x=500, y=260)
        whatsapp_lbl.bind("<Button-1>", lambda e: self.open_whatsapp())

        # PHONE
        phone_lbl = Label(f_lbl, text="📞 Call: +91 7898615450",
                          font=("times new roman",20,"bold"),
                          bg="black", fg="yellow", cursor="hand2")
        phone_lbl.place(x=500, y=320)
        phone_lbl.bind("<Button-1>", lambda e: self.open_phone())

    # FUNCTIONS
    def open_email(self):
        webbrowser.open("mailto:Rohitoswal338@gmail.com?subject=Help&body=I need support")

    def open_whatsapp(self):
        webbrowser.open("https://wa.me/7898615450")  # no + sign

    def open_phone(self):
        webbrowser.open("tel:+91 7898615450")