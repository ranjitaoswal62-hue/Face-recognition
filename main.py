from tkinter import *
from tkinter import ttk     
from PIL import Image,ImageTk
from student import student
import os
from train import train
from face_recognition import Face_reconition


class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

       #bg image 
        img_bg=Image.open(r"college photos\background phot0.jpg")
        img_bg=img_bg.resize((1530,710), resample=Image.Resampling.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)

        self.bg_img=Label(self.root, image=self.photoimg_bg)
        self.bg_img.place(x=0, y=130, width=1530, height=710)




        #first image

        img=Image.open(r"college photos\67a1040cb519f74d5c6cd7f4_thumbnail.250129.jpg")
        img=img.resize((500,130), resample=Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        #second image


        img1=Image.open(r"college photos\face-recognition.jpg")
        img1=img1.resize((500,130), resample=Image.Resampling.LANCZOS)              
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        #third image


        img2=Image.open(r"college photos\facial-recognition-software_52683-104208.avif")
        img2=img2.resize((500,130), resample=Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)
        
        title_lbl=Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        #student button
        img3=Image.open(r"college photos\download.jpg")
        img3=img3.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(self.root, image=self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=200, width=220, height=220)

        b1_1=Button(self.root, text="Student Details", cursor="hand2",command=self.student_details, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=420, width=220, height=40)


        #detect face button
        img4=Image.open(r"college photos\download (1).jpg")
        img4=img4.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b2=Button(self.root, image=self.photoimg4,cursor="hand2",command=self.face_data)
        b2.place(x=500, y=200, width=220, height=220)

        b2_1=Button(self.root, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=420, width=220, height=40)

            #attendance face button
        img5=Image.open(r"college photos\attendance.png")
        img5=img5.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b3=Button(self.root, image=self.photoimg5,cursor="hand2")
        b3.place(x=800, y=200, width=220, height=220)   

        b3_1=Button(self.root, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=420, width=220, height=40)

            #help desk button
        img6=Image.open(r"college photos\helpdesk.jpg")
        img6=img6.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b4=Button(self.root, image=self.photoimg6,cursor="hand2")
        b4.place(x=1100, y=200, width=220, height=220)
        
        b4_1=Button(self.root, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=420, width=220, height=40) 

        #train face button
        img7=Image.open(r"college photos\train face.jpg")
        img7=img7.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7) 

        b5=Button(self.root, image=self.photoimg7,cursor="hand2",command=self.train_data)
        b5.place(x=200, y=500, width=220, height=220)
        b5_1=Button(self.root, text="Train Face", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=720, width=220, height=40)

        #photos face button
        img8=Image.open(r"college photos\photos.jpg")
        img8=img8.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b6=Button(self.root, image=self.photoimg8,cursor="hand2",command=self.open_img)
        b6.place(x=500, y=500, width=220, height=220)   

        b6_1=Button(self.root, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=720, width=220, height=40)

        #developer button
        img9=Image.open(r"college photos\developers.jpg")
        img9=img9.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)    

        b7=Button(self.root, image=self.photoimg9,cursor="hand2")
        b7.place(x=800, y=500, width=220, height=220)  

        b7_1=Button(self.root, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=720, width=220, height=40)

            #exit button 
        img10=Image.open(r"college photos\exit.jpg")
        img10=img10.resize((220,220), resample=Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)      

        b8=Button(self.root, image=self.photoimg10,cursor="hand2")  
        b8.place(x=1100, y=500, width=220, height=220)

        b8_1=Button(self.root, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=720, width=220, height=40) 

    def open_img(self):
        os.startfile("data")

    #=======================function buttons =============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)   


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_reconition(self.new_window)




            
if __name__ =="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
    
