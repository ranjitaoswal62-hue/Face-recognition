from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
import numpy as np


class Face_reconition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First image
        try:
            img_top = Image.open(r"college photos\face recognition 1.jpg")
            img_top = img_top.resize((650, 700), resample=Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            f_lbl = Label(self.root, image=self.photoimg_top)
        except Exception:
            f_lbl = Label(self.root, bg="gray")
        f_lbl.place(x=0, y=45, width=650, height=700)

        # Second image
        try:
            img_bottom = Image.open(r"college photos\face recognition3.webp")
            img_bottom = img_bottom.resize((950, 700), resample=Image.Resampling.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        except Exception:
            f_lbl2 = Label(self.root, bg="darkgray")
        f_lbl2.place(x=650, y=45, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl2, text="FACE RECOGNITION", cursor="hand2",
                      command=self.face_recog,
                      font=("times new roman", 14, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)

    # ─────────────────────────────────────────────
    #  Save attendance to CSV file (no database)
    # ─────────────────────────────────────────────
    def mark_attendance(self, student_id, roll, name, dep):
        """
        Saves attendance to a CSV file: attendance/attendance_YYYY-MM-DD.csv
        Returns True if saved, False if already marked today.
        """
        try:
            # Create attendance folder if it doesn't exist
            folder = "attendance"
            if not os.path.exists(folder):
                os.makedirs(folder)

            today    = datetime.now().strftime("%Y-%m-%d")
            now      = datetime.now().strftime("%H:%M:%S")
            csv_file = os.path.join(folder, f"attendance_{today}.csv")

            # Check if this student is already marked today
            if os.path.exists(csv_file):
                with open(csv_file, "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        # row[0] = Student_id
                        if len(row) > 0 and str(row[0]) == str(student_id):
                            return False   # Already marked today

            # Write header if file is new
            file_exists = os.path.exists(csv_file)
            with open(csv_file, "a", newline="") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Student_id", "Roll", "Name", "Department", "Date", "Time" "attendance"])
                writer.writerow([student_id, roll, name, dep, today, now,self.mark_attendance ])

            print(f"[INFO] Attendance saved to {csv_file}")
            return True

        except Exception as e:
            print(f"[Error] {e}")
            messagebox.showerror("Error",
                                 f"Could not save attendance:\n\n{str(e)}",
                                 parent=self.root)
            return False

    # ─────────────────────────────────────────────
    #  Fetch student info from database
    # ─────────────────────────────────────────────
    def get_student_info(self, student_id):
        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="12345", database="face_recognition"
            )
            cursor = conn.cursor()
            cursor.execute(
                "SELECT Name, Roll, Dep FROM student WHERE Student_id=%s",
                (student_id,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return row[0], row[1], row[2]
        except Exception as e:
            print(f"[DB Error] {e}")
        return "Unknown", "Unknown", "Unknown"

    # ─────────────────────────────────────────────
    #  Draw bounding box + labels on each frame
    # ─────────────────────────────────────────────
    def draw_boundary(self, img, classifier, scalefactor, minNeighbors, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features   = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)

        stop = False

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

            student_id, confidence = clf.predict(gray_image[y:y + h, x:x + w])
            confidence_pct = int(100 * (1 - confidence / 300))

            if confidence_pct > 75:
                name, roll, dep = self.get_student_info(student_id)

                cv2.putText(img, f"Roll: {roll}",       (x, max(y - 65, 15)),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                cv2.putText(img, f"Name: {name}",       (x, max(y - 40, 30)),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                cv2.putText(img, f"Dept: {dep}",        (x, max(y - 15, 45)),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                cv2.putText(img, f"Conf: {confidence_pct}%", (x, y + h + 25),
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

                self._pending_mark = (str(student_id), roll, name, dep)
                stop = True

            else:
                cv2.putText(img, "Unknown Face", (x, max(y - 10, 15)),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

        return stop

    # ─────────────────────────────────────────────
    #  Main face-recognition loop
    # ─────────────────────────────────────────────
    def face_recog(self):
        cascade_path = "haarcascade_frontalface_default.xml"
        if not os.path.exists(cascade_path):
            messagebox.showerror("Error", f"Cascade file not found:\n{cascade_path}", parent=self.root)
            return
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "classifier.xml not found.\nTrain the model first.", parent=self.root)
            return

        faceCascade = cv2.CascadeClassifier(cascade_path)
        clf         = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Camera Error",
                                 "Cannot open camera.\n"
                                 "• Make sure no other app is using it.\n"
                                 "• Try changing index: cv2.VideoCapture(1)",
                                 parent=self.root)
            return

        self._pending_mark = None

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("[Warning] Failed to grab frame.")
                break

            stop = self.draw_boundary(img, faceCascade, 1.1, 10, clf)
            cv2.imshow("Face Recognition  —  Press ESC to quit", img)

            if stop:
                cv2.waitKey(800)
                break

            if cv2.waitKey(1) == 27:
                break

        video_cap.release()
        cv2.destroyAllWindows()

        # Show popup AFTER camera is fully closed
        if self._pending_mark:
            sid, roll, name, dep = self._pending_mark
            marked = self.mark_attendance(sid, roll, name, dep)
            today_str = datetime.now().strftime("%Y-%m-%d")
            time_str  = datetime.now().strftime("%H:%M:%S")
            if marked:
                messagebox.showinfo("Success",
                                    f"Attendance Marked Successfully!\n\n"
                                    f"Name : {name}\nRoll : {roll}\n"
                                    f"Date : {today_str}\nTime : {time_str}\n\n"
                                    f"Saved to: attendance/attendance_{today_str}.csv",
                                    parent=self.root)
            else:
                messagebox.showwarning("Already Marked",
                                       f"Attendance already recorded for:\n\n"
                                       f"Name : {name}\nRoll : {roll}\nDate : {today_str}",
                                       parent=self.root)


# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = Tk()
    obj  = Face_reconition(root)
    root.mainloop()