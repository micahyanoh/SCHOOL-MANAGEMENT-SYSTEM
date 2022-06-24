import tkinter as tk
import customtkinter


# new
class LogInView(tk.Toplevel):
    """creates a login top window"""

    customtkinter.set_appearance_mode("dark")
    APP_NAME = "TAMARIND LOGIN"
    WIDTH = 300
    HEIGHT = 400

    def __init__(self, *args, **kwargs):
        """initialize super class and attributes"""
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", "true")
        self.title(LogInView.APP_NAME)
        self.resizable(0, 0)
        self.geometry("350x450")
        self.overrideredirect(True)
        self.configure(bg="#3d6466")
       
        #new
        self.account_text=tk.StringVar()
        self.passw_text=tk.StringVar()
        #self.gp=self.account_text.get()
        
        self.frame0 = customtkinter.CTkFrame(
            master=self, width=250,fg_color="#3d6466"
        )
        self.frame0.pack(fill=tk.BOTH, expand=1)

        self.frame = customtkinter.CTkFrame(
            master=self.frame0, width=250, height=350, corner_radius=30, fg_color=("#3d6466")
        )
        self.frame.pack(pady=20, padx=10, fill=tk.BOTH, expand=1)
        self.label_frame = customtkinter.CTkFrame(
            master=self.frame, height=30, corner_radius=30
        )
        self.label_frame.pack(pady=50, expand=0)
        self.label = customtkinter.CTkLabel(master=self.label_frame, text="TAMARIND")
        self.label.pack()

        self.account = customtkinter.CTkEntry(
            master=self.frame,
            placeholder_text="\n    ACCOUNT NAME",
            width=200,
            height=40,
            corner_radius=30,
        )
        self.account.pack(pady=20)
        self.passw = customtkinter.CTkEntry(
            master=self.frame,
            placeholder_text="\n      PASSWORD",
            width=200,
            height=40,
            show='*',
            corner_radius=30,
            textvar=self.account_text,
        )
        self.passw.pack(pady=20)
        self.ok = customtkinter.CTkButton(
            master=self.frame,
            text="OK",
            width=200,
            corner_radius=30,
            fg_color=("#F4F4FA", "#1E2742"),
            
        )
        self.ok.pack(pady=20)
        self.account_text=self.account.get()
        self.passw_text=self.passw.get()
        self.after(20_000,self.destroy)

    
        
