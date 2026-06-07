from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import student
import os
from train import train
from face_recognition import Face_reconition
from Attendance import Attendance
from student_login import StudentLogin
from facedetect_login import FaceLogin
from Developer import Developer
from help import Help
from time import strftime
from datetime import datetime

# ── Stylish login screen (runs before main window) ────────────────────────────
from login import show_login


class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        # bg image
        img_bg = Image.open(r"college photos\background phot0.jpg")
        img_bg = img_bg.resize((1530, 710), resample=Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        self.bg_img = Label(self.root, image=self.photoimg_bg)
        self.bg_img.place(x=0, y=130, width=1530, height=710)

        # first image
        img = Image.open(r"college photos\67a1040cb519f74d5c6cd7f4_thumbnail.250129.jpg")
        img = img.resize((500, 130), resample=Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"college photos\face-recognition.jpg")
        img1 = img1.resize((500, 130), resample=Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"college photos\facial-recognition-software_52683-104208.avif")
        img2 = img2.resize((500, 130), resample=Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=130)

        title_lbl = Label(self.root,
                          text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        # time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'),
                    background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # student button
        img3 = Image.open(r"college photos\download.jpg")
        img3 = img3.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Button(self.root, image=self.photoimg3, command=self.open_student_login,
               cursor="hand2").place(x=200, y=200, width=220, height=220)
        Button(self.root, text="Student Details", cursor="hand2",
               command=self.open_student_login,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=200, y=420, width=220, height=40)

        # detect face button
        img4 = Image.open(r"college photos\download (1).jpg")
        img4 = img4.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        Button(self.root, image=self.photoimg4, cursor="hand2",
               command=self.open_face_login).place(x=500, y=200, width=220, height=220)
        Button(self.root, text="Face Detector", cursor="hand2",
               command=self.open_face_login,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=500, y=420, width=220, height=40)

        # attendance button
        img5 = Image.open(r"college photos\attendance.png")
        img5 = img5.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        Button(self.root, image=self.photoimg5, cursor="hand2",
               command=self.Attendance_data).place(x=800, y=200, width=220, height=220)
        Button(self.root, text="Attendance", cursor="hand2",
               command=self.Attendance_data,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=800, y=420, width=220, height=40)

        # help desk button
        img6 = Image.open(r"college photos\helpdesk.jpg")
        img6 = img6.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        Button(self.root, image=self.photoimg6, cursor="hand2",
               command=self.help_desk).place(x=1100, y=200, width=220, height=220)
        Button(self.root, text="Help Desk", cursor="hand2", command=self.help_desk,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=1100, y=420, width=220, height=40)

        # train face button
        img7 = Image.open(r"college photos\train face.jpg")
        img7 = img7.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        Button(self.root, image=self.photoimg7, cursor="hand2",
               command=self.train_data).place(x=200, y=500, width=220, height=220)
        Button(self.root, text="Train Face", cursor="hand2", command=self.train_data,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=200, y=720, width=220, height=40)

        # photos button
        img8 = Image.open(r"college photos\photos.jpg")
        img8 = img8.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        Button(self.root, image=self.photoimg8, cursor="hand2",
               command=self.open_img).place(x=500, y=500, width=220, height=220)
        Button(self.root, text="Photos", cursor="hand2", command=self.open_img,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=500, y=720, width=220, height=40)

        # developer button
        img9 = Image.open(r"college photos\developers.jpg")
        img9 = img9.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        Button(self.root, image=self.photoimg9, cursor="hand2",
               command=self.Developer_data).place(x=800, y=500, width=220, height=220)
        Button(self.root, text="Developer", cursor="hand2", command=self.Developer_data,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=800, y=720, width=220, height=40)

        # exit button
        img10 = Image.open(r"college photos\exit.jpg")
        img10 = img10.resize((220, 220), resample=Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        Button(self.root, image=self.photoimg10, cursor="hand2",
               command=self.iExit).place(x=1100, y=500, width=220, height=220)
        Button(self.root, text="Exit", cursor="hand2", command=self.iExit,
               font=("times new roman", 15, "bold"), bg="darkblue",
               fg="white").place(x=1100, y=720, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_reconition(self.new_window)

    def Attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def open_student_login(self):
        self.new_window = Toplevel(self.root)
        StudentLogin(self.new_window, self.student_details)

    def open_face_login(self):
        self.new_window = Toplevel(self.root)
        FaceLogin(self.new_window, self.face_data)

    def Developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Step 1: show login (its own Tk window, fully independent)
    logged_in = show_login()

    # Step 2: only open main app if login succeeded
    if logged_in:
        root = Tk()
        obj = face_recognition_system(root)
        root.mainloop()