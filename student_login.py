from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


class StudentLogin:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success   # function to call after successful login

        self.root.title("Student Login")
        self.root.geometry("500x400+500+200")
        self.root.resizable(False, False)
        self.root.config(bg="#1a1a2e")

        # ── Title ────────────────────────────────────────────────────────
        Label(self.root, text="STUDENT LOGIN",
              font=("times new roman", 22, "bold"),
              bg="#1a1a2e", fg="white").pack(pady=(30, 5))

        Label(self.root, text="Enter your credentials to continue",
              font=("times new roman", 11),
              bg="#1a1a2e", fg="#aaaaaa").pack(pady=(0, 20))

        # ── Form frame ───────────────────────────────────────────────────
        form = Frame(self.root, bg="#16213e", bd=0)
        form.pack(padx=40, pady=10, fill=BOTH)

        # Username
        Label(form, text="Username", font=("times new roman", 12, "bold"),
              bg="#16213e", fg="white").grid(row=0, column=0, sticky=W, padx=20, pady=(20, 5))

        self.var_user = StringVar()
        user_entry = Entry(form, textvariable=self.var_user,
                           font=("times new roman", 13), width=25,
                           bd=0, bg="#0f3460", fg="white",
                           insertbackground="white")
        user_entry.grid(row=1, column=0, padx=20, pady=(0, 15), ipady=6)
        user_entry.focus()

        # Password
        Label(form, text="Password", font=("times new roman", 12, "bold"),
              bg="#16213e", fg="white").grid(row=2, column=0, sticky=W, padx=20, pady=(5, 5))

        self.var_pass = StringVar()
        pass_entry = Entry(form, textvariable=self.var_pass,
                           font=("times new roman", 13), width=25,
                           show="*", bd=0, bg="#0f3460", fg="white",
                           insertbackground="white")
        pass_entry.grid(row=3, column=0, padx=20, pady=(0, 20), ipady=6)

        # Bind Enter key
        self.root.bind("<Return>", lambda e: self.login())

        # ── Login button ─────────────────────────────────────────────────
        Button(self.root, text="LOGIN", command=self.login,
               font=("times new roman", 13, "bold"),
               bg="#e94560", fg="white", cursor="hand2",
               activebackground="#c73652", bd=0,
               width=20, height=2).pack(pady=10)

        # ── Cancel ───────────────────────────────────────────────────────
        Button(self.root, text="Cancel", command=self.root.destroy,
               font=("times new roman", 11),
               bg="#1a1a2e", fg="#aaaaaa", cursor="hand2",
               bd=0, activebackground="#1a1a2e").pack()

    # ─────────────────────────────────────────────
    def login(self):
        username = self.var_user.get().strip()
        password = self.var_pass.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "Username and Password are required!", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="12345", database="face_recognition"
            )
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                (username, password)
            )
            row = cursor.fetchone()
            conn.close()

            if row:
                messagebox.showinfo("Success", f"Welcome, {username}!", parent=self.root)
                self.root.destroy()
                self.on_success()   # open student details window
            else:
                messagebox.showerror("Login Failed", "Invalid username or password!", parent=self.root)

        except Exception as e:
            # If no users table exists, fall back to hardcoded admin credentials
            if username == "admin" and password == "admin123":
                messagebox.showinfo("Success", f"Welcome, {username}!", parent=self.root)
                self.root.destroy()
                self.on_success()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    StudentLogin(root, lambda: print("Login success"))
    root.mainloop()