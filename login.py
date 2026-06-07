import tkinter as tk

# ── Change these credentials as needed ────────────────────────────────────────
USERNAME = "rohit"
PASSWORD = "rohit123"


def show_login():
    """
    Shows a stylish dark login window.
    Returns True if login succeeded, False if user closed the window.
    Call this BEFORE creating your main Tk() window.
    """
    result = {"success": False}

    win = tk.Tk()
    win.title("Login — Face Recognition System")
    win.geometry("460x530+530+160")
    win.resizable(False, False)
    win.configure(bg="#0d0d1f")

    # ── Top accent bar ────────────────────────────────────────────────────────
    tk.Frame(win, bg="#1a1aff", height=5).pack(fill="x")

    # ── Logo (Canvas-drawn face icon) ─────────────────────────────────────────
    c = tk.Canvas(win, width=88, height=88, bg="#0d0d1f", highlightthickness=0)
    c.pack(pady=(28, 0))
    c.create_oval(4, 4, 84, 84, outline="#2233ff", width=3)
    c.create_oval(16, 16, 72, 72, fill="#111133", outline="#1122cc", width=2)
    c.create_oval(27, 29, 37, 39, fill="white", outline="")   # left eye
    c.create_oval(51, 29, 61, 39, fill="white", outline="")   # right eye
    c.create_arc(27, 44, 61, 66, start=200, extent=140, outline="white",
                 width=2, style="arc")                         # smile
    c.create_line(4, 44, 84, 44, fill="#2233ff", dash=(4, 3)) # scan line

    # ── Title text ────────────────────────────────────────────────────────────
    tk.Label(win, text="FACE RECOGNITION SYSTEM",
             font=("Courier", 13, "bold"), fg="#3355ff",
             bg="#0d0d1f").pack(pady=(12, 2))
    tk.Label(win, text="Administrator Login",
             font=("Courier", 10), fg="#3a4466",
             bg="#0d0d1f").pack()

    # ── Thin divider ─────────────────────────────────────────────────────────
    tk.Frame(win, bg="#18205a", height=1).pack(fill="x", padx=48, pady=16)

    # ── Form fields ──────────────────────────────────────────────────────────
    form = tk.Frame(win, bg="#0d0d1f")
    form.pack(padx=48, fill="x")

    def labeled_entry(parent, label, show=""):
        tk.Label(parent, text=label, font=("Courier", 9, "bold"),
                 fg="#2d3d77", bg="#0d0d1f", anchor="w").pack(fill="x",
                                                               pady=(10, 3))
        var = tk.StringVar()
        e = tk.Entry(parent, textvariable=var, show=show,
                     font=("Courier", 12), fg="#99aaee", bg="#09091c",
                     insertbackground="#3355ff",
                     relief="flat", bd=0,
                     highlightthickness=1,
                     highlightbackground="#1b2460",
                     highlightcolor="#3355ff")
        e.pack(fill="x", ipady=9)
        return var, e

    user_var, user_entry = labeled_entry(form, "USERNAME")
    pass_var, pass_entry = labeled_entry(form, "PASSWORD", show="●")

    # Show / hide password checkbox
    show_var = tk.BooleanVar(value=False)
    tk.Checkbutton(form, text=" Show password",
                   variable=show_var,
                   command=lambda: pass_entry.config(
                       show="" if show_var.get() else "●"),
                   bg="#0d0d1f", fg="#3a4466",
                   activebackground="#0d0d1f", activeforeground="#5566aa",
                   selectcolor="#0d0d1f",
                   font=("Courier", 9), cursor="hand2").pack(anchor="w",
                                                              pady=(6, 0))

    # ── Status label ─────────────────────────────────────────────────────────
    status_var = tk.StringVar()
    tk.Label(win, textvariable=status_var, font=("Courier", 9),
             fg="#ff3344", bg="#0d0d1f").pack(pady=(10, 2))

    # ── Login button ─────────────────────────────────────────────────────────
    def attempt(event=None):
        if (user_var.get().strip() == USERNAME and
                pass_var.get().strip() == PASSWORD):
            result["success"] = True
            win.destroy()
        else:
            status_var.set("✘  Incorrect username or password.")
            pass_entry.delete(0, "end")
            pass_entry.focus_set()

    btn = tk.Button(win, text="LOGIN", font=("Courier", 12, "bold"),
                    fg="white", bg="#1a1aff",
                    activebackground="#2a2aff", activeforeground="white",
                    relief="flat", bd=0, cursor="hand2", command=attempt)
    btn.pack(fill="x", padx=48, ipady=11)
    btn.bind("<Enter>", lambda e: btn.config(bg="#2a2aff"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#1a1aff"))

    win.bind("<Return>", attempt)
    user_entry.focus_set()

    # ── Footer ────────────────────────────────────────────────────────────────
    tk.Label(win, text="© Face Recognition Attendance System",
             font=("Courier", 8), fg="#191f42",
             bg="#0d0d1f").pack(side="bottom", pady=10)

    win.mainloop()
    return result["success"]