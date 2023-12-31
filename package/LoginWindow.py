import customtkinter as ctk


class LoginWindow(ctk.CTk):

    def __init__(self, master, other_window, mainImage, crud, **kwargs):
        super().__init__(**kwargs)
        self.master = master

        self.imageLabel = ctk.CTkLabel(self.master, image=mainImage, text="", bg_color="white")
        self.imageLabel.place(x=280, y=35)

        self.mainLabel = ctk.CTkLabel(self.master, text="MileageMate", text_color="#555555",
                                      font=("Trebuchet", 28, "bold"),
                                      bg_color="white")
        self.mainLabel.place(x=90, y=40)

        self.logIntoLabel = ctk.CTkLabel(self.master, text="Login into your account", text_color="#12833b",
                                         font=("Trebuchet", 12, "bold"),
                                         bg_color="white")
        self.logIntoLabel.pack(pady=75)

        self.emailLabel = ctk.CTkLabel(self.master, text="Email:", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                       bg_color="white")
        self.emailLabel.place(x=50, y=145)

        self.emailTextBox = ctk.CTkTextbox(self.master, width=310, height=30, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                           border_spacing=0)
        self.emailTextBox.pack(pady=0)

        self.passwordLabel = ctk.CTkLabel(self.master, text="Password:", text_color="#555555",
                                          font=("Trebuchet", 12, "bold"),
                                          bg_color="white")
        self.passwordLabel.place(x=50, y=235)

        self.passwordTextBox = ctk.CTkTextbox(self.master, width=310, height=30, corner_radius=5, fg_color="#dbfde7",
                                              bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                              border_spacing=0)
        self.passwordTextBox.pack(pady=60)

        self.loginButton = ctk.CTkButton(self.master, text="Login", fg_color="#146734", font=("Trebuchet", 14, "bold"),
                                         width=310, height=40, corner_radius=5, hover_color="#12552d", bg_color="white",
                                         command=lambda: self.login_callback())
        self.loginButton.pack()

        self.registerButton = ctk.CTkButton(self.master, text="Register now", fg_color="white",
                                            font=("Trebuchet", 14, "bold"),
                                            width=310, height=35, corner_radius=5, hover_color="#dbdbd9",
                                            bg_color="white", border_width=1, text_color="#555555",
                                            command=lambda: self.register_callback(other_window))
        self.registerButton.pack(pady=50)

        self.notRegisteredLabel = ctk.CTkLabel(self.master, text="Not registered?", text_color="#555555",
                                               font=("Trebuchet", 12, "bold"),
                                               bg_color="white")
        self.notRegisteredLabel.place(x=50, y=420)

    def register_callback(self, other_window):
        self.master.withdraw()
        other_window.deiconify()

    def login_callback(self):
        self.master.after(1, self.resizeWindow(0))

    def resizeWindow(self, score):
        score += 1
        if score < 30:
            width = int(self.master.winfo_width() + 10)
            self.master.geometry(str(width) + "x540")
            self.master.update()
            self.master.after(1, self.resizeWindow(score))
