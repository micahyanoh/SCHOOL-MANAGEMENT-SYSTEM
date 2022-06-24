import datetime
import tkinter as tk

import customtkinter

# from  login import App
# new
from login import LogInView

customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"

# initializing application
class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TAMARIND   SCHOOL  MANAGEMENT  SYSTEM")
        self.geometry(f"{1000}x{500}")
        self.wm_attributes('-fullscreen','True')
        #self.eval("tk::PlaceWindow . left")
        self.label_w = 800
        # keyboard shortcuts
        self.bind("<Q>", exit)
        self.bind("<q>", exit)

        # creating frames
        self.frame1 = customtkinter.CTkFrame(master=self, width=200)
        self.frame1.configure(fg_color=("#F4F4FA", "#1E2742"))
        self.frame1.pack(side=customtkinter.LEFT, expand=0, fill=tk.Y)

        self.frame2 = customtkinter.CTkFrame(
            master=self, width=320, height=80, corner_radius=10
        )
        self.frame2.configure(fg_color=("#F4F4FA", "#1E2742"))
        self.frame2.pack(fill=customtkinter.BOTH, pady=20, padx=20)

        self.frame3 = customtkinter.CTkFrame(
            master=self, width=320, height=700, corner_radius=10
        )
        self.frame3.pack(fill=customtkinter.BOTH, padx=20)

        # creating frame one buttons NB:- To the left
        self.acc = customtkinter.CTkLabel(master=self.frame1, text="ACCOUNT-USER")
        self.acc.pack(
            pady=20,
            padx=20,
        )
        self.add = customtkinter.CTkButton(
            master=self.frame1, text="NEW STUDENT", command=self.add_customer
        )
        self.add.pack(pady=20, padx=20)
        self.fee = customtkinter.CTkButton(master=self.frame1, text="FEES")
        self.fee.pack(pady=20, padx=20)
        self.exams = customtkinter.CTkButton(master=self.frame1, text="EXAMINATIONS")
        self.exams.pack(pady=20, padx=20)
        self.lib = customtkinter.CTkButton(master=self.frame1, text="LIBRARY")
        self.lib.pack(pady=20, padx=20)
        self.staff = customtkinter.CTkButton(master=self.frame1, text="TIME-TABLE")
        self.staff.pack(pady=20, padx=20)
        self.mode = customtkinter.CTkSwitch(
            master=self.frame1, command=self.change_mode, text="DARK MODE"
        )
        self.mode.pack(side=tk.BOTTOM, pady=20, padx=20)
        self.sett = customtkinter.CTkButton(master=self.frame1, text="ADMINISTRATOR")
        self.sett.pack(side=tk.BOTTOM, pady=20, padx=20)
        self.sport = customtkinter.CTkButton(master=self.frame1, text="SPORTS")
        self.sport.pack(side=tk.BOTTOM, pady=20, padx=20)
        self.std = customtkinter.CTkButton(master=self.frame1, text="CLASS")
        self.std.pack(side=tk.BOTTOM, pady=20, padx=20)

        # creating frame two buttons
        self.homeb = customtkinter.CTkButton(
            master=self.frame2,
            width=5,
            text="HOME",
            command=self.home,
            corner_radius=20,
        )
        self.homeb.pack(side=tk.LEFT, pady=15, padx=10)
        # search bar
        self.searchb = customtkinter.CTkButton(
            master=self.frame2, width=2, text="SEARCH", corner_radius=20
        )
        self.searchb.pack(side=tk.RIGHT, pady=15, padx=10)
        self.search = customtkinter.CTkEntry(
            master=self.frame2,
            width=200,
            placeholder_text="Stolen_Pen-Labs",
            corner_radius=30,
        )
        self.search.pack(side=tk.RIGHT, pady=15, padx=10)
        self.drp1 = customtkinter.CTkOptionMenu(master=self.frame2, corner_radius=20)
        self.drp1.pack(side=tk.RIGHT, pady=15, padx=20)
        self.drp = customtkinter.CTkOptionMenu(master=self.frame2, corner_radius=20)
        self.drp.pack(side=tk.RIGHT, pady=15, padx=20)

    # creating home widgets on frame3
    def disp(self):
        self.homeb.configure(state=tk.DISABLED)
        self.fh = customtkinter.CTkFrame(master=self.frame3)
        self.fh.pack(fill=tk.BOTH, expand=1, padx=20, pady=10)
        self.welcome = customtkinter.CTkLabel(master=self.fh)
        self.welcome.pack(pady=10)
        self.ddate = customtkinter.CTkLabel(master=self.fh)
        self.ddate.pack(pady=10)
        self.dclock = customtkinter.CTkLabel(master=self.fh)
        self.dclock.pack(pady=10, padx=100)
        self.ulock = customtkinter.CTkButton(master=self.fh, corner_radius=30)
        self.ulock.configure(fg_color=("#F4F4FA", "#1E2742"))
        self.ulock.pack(pady=20, padx=100)

        # creating frame to hold custom buttons
        self.custom = customtkinter.CTkFrame(master=self.fh, corner_radius=30)
        self.custom.pack(pady=30, expand=1)

        self.custom1 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom1.grid(row=0, column=0, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom2 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom2.grid(row=0, column=1, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom3 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom3.grid(row=0, column=2, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom4 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom4.grid(row=1, column=0, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom5 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom5.grid(row=1, column=1, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom6 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom6.grid(row=1, column=2, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom7 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom7.grid(row=2, column=0, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom8 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom8.grid(row=2, column=1, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custom9 = customtkinter.CTkButton(master=self.custom, corner_radius=30)
        self.custom9.grid(row=2, column=2, padx=100, pady=20, sticky=tk.E + tk.W)

        self.custombtns = (
            self.custom1,
            self.custom2,
            self.custom3,
            self.custom4,
            self.custom5,
            self.custom6,
            self.custom7,
            self.custom8,
            self.custom9,
        )

        # calling the clock and date functions
        self.clock_time()
        self.today_date()

    # home screen prompt
    def home(self):
        self.homeb.configure(state=tk.DISABLED)
        self.add.configure(state=tk.NORMAL)
        self.f1.destroy()
        self.disp()
        self.ulock.config(text="LOCK", command=self.lock_buttons)
        self.acc.configure(text="ACTIVE")
        self.welcome.configure(
            text="\n THANK YOU FOR CHOOSING TAMARIND,\nTHIS IS YOUR WORK STATION"
        )

    # dark and light mode configuration
    def change_mode(self):
        if self.mode.get() == 1:
            customtkinter.set_appearance_mode("dark")
            self.ddate.configure(foreground="#3d6466")
            self.welcome.configure(foreground="#3d6466")
            
        else:
            customtkinter.set_appearance_mode("light")
            self.ddate.configure(foreground="#3d6466")
            self.welcome.configure(foreground="#3d6466")

    # student registration window
    def add_customer(self):
        self.homeb.configure(state=tk.NORMAL)
        self.fh.destroy()
        self.radio_var = tk.IntVar(value=0)
        # dissable button on click
        self.add.configure(state=tk.DISABLED)
        # create a frame to hold widgets
        self.f1 = customtkinter.CTkFrame(master=self.frame3)
        self.f1.pack(fill=tk.BOTH, expand=1, padx=20, pady=10)
        # create widgets
        self.f_label = customtkinter.CTkLabel(master=self.f1, text="STUDENT DETAILS")
        self.p_label = customtkinter.CTkLabel(
            master=self.f1, text="PARENT/GUARDIAN DETAILS"
        )
        self.g_label = customtkinter.CTkLabel(
            master=self.f1, text="ALTERNATIVE CONTACT"
        )
        self.f_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="FIRST NAME"
        )
        self.m_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="MIDDLE NAME"
        )
        self.l_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="LAST NAME"
        )
        self.adm_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="ADM NUMBER"
        )
        self.dob_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="D.O.B (DD/MM/YY)"
        )
        # frame to hold radio button
        self.gender = customtkinter.CTkFrame(master=self.f1)
        self.gender.pack(pady=5)
        self.male = customtkinter.CTkRadioButton(
            master=self.gender, text="MALE", variable=self.radio_var, value=0
        )
        self.male.pack(side=tk.LEFT, pady=5, padx=25)
        self.male = customtkinter.CTkRadioButton(
            master=self.gender, text="FEMALE", variable=self.radio_var, value=1
        )
        self.male.pack(side=tk.LEFT, pady=5, padx=25)
        self.guardian = customtkinter.CTkCheckBox(master=self.gender, text="GUARDIAN")
        self.guardian.pack(side=tk.RIGHT, pady=5, padx=25)
        self.parent = customtkinter.CTkCheckBox(master=self.gender, text="PARENT")
        self.parent.pack(side=tk.RIGHT, pady=5, padx=25)
        # self.f_label=customtkinter.CTkLabel(master=self.f1,text='PARENT/GUARDIAN DETAILS'
        self.p_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="PARENT/ GUARDIAN"
        )
        self.pn_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="PHONE NUMBER"
        )
        self.e_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="E-MAIL"
        )
        self.g_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="ALTERNATIVE GUARDIAN"
        )
        self.pg_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="PHONE NUMBER"
        )
        self.area_name = customtkinter.CTkEntry(
            master=self.f1, width=self.label_w, placeholder_text="HOME AREA/LOCATION"
        )

        self.form_entry = (
            self.f_label,
            self.f_name,
            self.l_name,
            self.m_name,
            self.adm_name,
            self.dob_name,
            self.p_label,
            self.p_name,
            self.pg_name,
            self.e_name,
            self.g_label,
            self.g_name,
            self.area_name,
        )

        for i in self.form_entry:
            i.pack(pady=5)
        self.submit = customtkinter.CTkButton(
            master=self.f1, text="SUBMIT", corner_radius=20
        )
        self.submit.pack(side=tk.RIGHT, pady=5, padx=150)
        self.parent.select()

        # getting and displaying the digital clock

    def clock_time(self):
        self.clock = datetime.datetime.now()
        self.clock = self.clock.strftime("%I:%M:%S %p")
        self.dclock.configure(
            text=self.clock, font=("ariel", 50, "bold"), foreground="#3d6466"
        )
        self.welcome.configure(font=("ariel", 20, "bold"), foreground="gray38")
        self.dclock.after(200, self.clock_time)
        # getting and displaying the date

    def today_date(self):
        self.today = datetime.date.today()
        self.today = self.today.strftime("%A %d %B %Y")
        self.ddate.configure(
            text=self.today, font=("ariel", 20, "bold"), foreground="#3d6466"
        )
        self.ddate.after(2000, self.today_date)

    # locking and unlocking the screen
    # frame buttons dissabled on screen lock
    def lock_buttons(self):
        customtkinter.set_default_color_theme("dark-blue")
        self.acc.configure(text="LOCKED")
        # new
        self.ulock.configure(text=" UNLOCK", command=self.login_window)
        self.welcome.configure(text="\n WELCOME TO TAMARIND SCHOOL MANAGEMENT SYSTEM\n")
        self.mode.select()

        self.buttons = (
            self.fee,
            self.add,
            self.exams,
            self.lib,
            self.staff,
            self.sett,
            self.sport,
            self.std,
            self.searchb,
            self.drp,
            self.drp1,
            self.search,
        )

        for self.button in self.buttons:
            self.button.configure(state=tk.DISABLED)
        for self.btn in self.custombtns:
            # self.btn.grid(padx=100,pady=20,sticky=tk.E+tk.W)
            self.btn.configure(fg_color=("#3d6466"))

    # managing lock/unlock button
    def unlock(self):
        for self.button in self.buttons:
            self.button.configure(state=tk.NORMAL)
        self.ulock.config(text="LOCK", command=self.lock_buttons, fg_color=("#3d6466"))
        self.acc.configure(text="ACTIVE")
        self.welcome.configure(
            text="\n THANK YOU FOR CHOOSING TAMARIND,\nTHIS IS YOUR WORK STATION"
        )
        for self.btn in self.custombtns:
            # self.btn.grid(padx=100,pady=20,sticky=tk.E+tk.W)
            self.btn.configure(fg_color=("#F4F4FA", "#1E2742"))

    # default color mode
    def states(self):
        # default state values
        self.mode.select()

    # new
    def login_window(self):
        # signin view
        self.login = LogInView(self)
        self.login.ok.configure(command=self.hh)
    def hh(self):
        self.login.destroy()
        self.unlock()
        #self.login.destroy()
        #self.login.grab_set()


#################################################################

#################################################################
if __name__ == "__main__":
    window = Window()
    window.disp()
    window.lock_buttons()

    window.mainloop()
