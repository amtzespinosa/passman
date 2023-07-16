import tkinter as tk
import customtkinter, random, pyperclip, sqlite3, hashlib
from cryptography.fernet import Fernet

class PassMan(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("PassMan")
        self.iconphoto(True, tk.PhotoImage(file="/usr/lib/passman/icon.png"))
        self.geometry("600x370")

        # set styling
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, 
                                                             text="#passman ", 
                                                             compound="left", 
                                                             font=customtkinter.CTkFont(size=30, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.generate_button = customtkinter.CTkButton(self.navigation_frame, 
                                                       corner_radius=0, 
                                                       height=40, 
                                                       border_spacing=10, 
                                                       text="PassGen", 
                                                       fg_color="transparent", 
                                                       text_color=("gray10", "gray90"), 
                                                       hover_color=("gray70", "gray30"), 
                                                       anchor="w", 
                                                       command=self.generate_button_event, 
                                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        self.generate_button.grid(row=1, column=0, sticky="ew")

        self.add_button = customtkinter.CTkButton(self.navigation_frame, 
                                                  corner_radius=0, 
                                                  height=40, 
                                                  border_spacing=10, 
                                                  text="Add New", 
                                                  fg_color="transparent", 
                                                  text_color=("gray10", "gray90"), 
                                                  hover_color=("gray70", "gray30"), 
                                                  anchor="w", 
                                                  command=self.add_button_event, 
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
        self.add_button.grid(row=2, column=0, sticky="ew")

        self.saved_button = customtkinter.CTkButton(self.navigation_frame, 
                                                    corner_radius=0, 
                                                    height=40, 
                                                    border_spacing=10, 
                                                    text="List", 
                                                    fg_color="transparent", 
                                                    text_color=("gray10", "gray90"), 
                                                    hover_color=("gray70", "gray30"), 
                                                    anchor="w", 
                                                    command=self.saved_button_event, 
                                                    font=customtkinter.CTkFont(size=15, weight="bold"))
        self.saved_button.grid(row=3, column=0, sticky="ew")

        self.delete_button = customtkinter.CTkButton(self.navigation_frame, 
                                                    corner_radius=0, 
                                                    height=40, 
                                                    border_spacing=10, 
                                                    text="Delete", 
                                                    fg_color="transparent", 
                                                    text_color=("gray10", "gray90"), 
                                                    hover_color="#901212", 
                                                    anchor="w", 
                                                    command=self.delete_button_event, 
                                                    font=customtkinter.CTkFont(size=15, weight="bold"))
        self.delete_button.grid(row=4, column=0, sticky="ew")

        # create password generator frame
        self.generate_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.generate_frame.grid_columnconfigure((0, 1), weight=1)
        self.generate_frame.grid_rowconfigure(0, weight=1)

        # passgen label
        self.passgen_frame_label = customtkinter.CTkLabel(self.generate_frame, 
                                                             text="#passgen ", 
                                                             font=customtkinter.CTkFont(size=40, weight="bold"))
        self.passgen_frame_label.grid(row=0, column=0, columnspan=2)

        # password generator
        self.pass_box = customtkinter.CTkTextbox(self.generate_frame, width=400, height=30, corner_radius=10, font=customtkinter.CTkFont(size=15))
        self.pass_box.configure(state="disabled")
        self.pass_box.grid(row=1, column=0, columnspan=2, padx=(50, 50), sticky="ew")
        self.generate_button = customtkinter.CTkButton(self.generate_frame, 
                                                       width=150, 
                                                       height=40, 
                                                       corner_radius=10, 
                                                       text="Generate", 
                                                       command=self.generate_pass, 
                                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        self.generate_button.grid(row=2, column=0, padx=(50, 5), pady=(10, 50), sticky="ew")
        self.copy_button = customtkinter.CTkButton(self.generate_frame, 
                                                   width=150, 
                                                   height=40, 
                                                   corner_radius=10, 
                                                   text="Copy", 
                                                   command=self.copy_pass, 
                                                   font=customtkinter.CTkFont(size=15, weight="bold"))
        self.copy_button.grid(row=2, column=1, padx=(5, 50), pady=(10, 50), sticky="ew")

        # advanced options
        self.advanced_options_label = customtkinter.CTkLabel(self.generate_frame, text="Advanced options:", font=customtkinter.CTkFont(size=15))
        self.advanced_options_label.grid(row=3, column=0)
        self.generate_options_frame = customtkinter.CTkFrame(self.generate_frame, corner_radius=10, fg_color="gray10")
        self.generate_options_frame.grid(row=4, column=0, columnspan=2, padx=50, pady=(5, 50), sticky="nsew")

        # slider option
        self.pass_length_label = customtkinter.CTkLabel(self.generate_options_frame, text="Password length:", padx=30)
        self.pass_length_label.grid(row=1, column=0)
        self.pass_length_slider = customtkinter.CTkSlider(self.generate_options_frame, 
                                                          from_=5, 
                                                          to=50, 
                                                          number_of_steps=45, 
                                                          width=320, 
                                                          command=self.print_slider_value)
        self.pass_length_slider.grid(row=2, column=0, columnspan=3, padx=(10, 5), pady=0)
        self.pass_length_slider.set(20)
        self.pass_length_box = customtkinter.CTkTextbox(self.generate_options_frame, 
                                                        width=40, 
                                                        height=15, 
                                                        corner_radius=10, 
                                                        activate_scrollbars=False)
        self.pass_length_box.grid(row=1, column=2, pady=(20, 10), padx=(0, 0))
        self.pass_length_box.insert("0.0", "20")

        # checkbox options
        self.chars_upper_checkbox = customtkinter.CTkCheckBox(self.generate_options_frame, text="Uppercase")
        self.chars_upper_checkbox.grid(row=3, column=0, padx=(10, 5), pady=20)
        self.chars_upper_checkbox.select()
        self.chars_lower_checkbox = customtkinter.CTkCheckBox(self.generate_options_frame, text="Lowercase")
        self.chars_lower_checkbox.grid(row=3, column=1, padx=5, pady=20)
        self.chars_lower_checkbox.select()
        self.chars_nums_checkbox = customtkinter.CTkCheckBox(self.generate_options_frame, text="Numbers")
        self.chars_nums_checkbox.grid(row=3, column=2, padx=5, pady=20)
        self.chars_nums_checkbox.select()
        self.chars_syms_checkbox = customtkinter.CTkCheckBox(self.generate_options_frame, text="Symbols")
        self.chars_syms_checkbox.grid(row=3, column=3, padx=5, pady=20)
        self.chars_syms_checkbox.select()

        # create add new password frame
        self.add_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.add_frame.grid_columnconfigure((0, 1), weight=1)
        self.add_frame.grid_rowconfigure(0, weight=1)

        # add new label
        self.add_frame_label = customtkinter.CTkLabel(self.add_frame, 
                                                             text="#add new ", 
                                                             font=customtkinter.CTkFont(size=40, weight="bold"))
        self.add_frame_label.grid(row=0, column=0, columnspan=2)

        # service entry
        self.service_entry = customtkinter.CTkEntry(self.add_frame, 
                                                    placeholder_text="Service",
                                                    fg_color="gray25",
                                                    border_width=0,
                                                    width=400, height=42, corner_radius=10,
                                                    font=customtkinter.CTkFont(size=15))
        self.service_entry.grid(row=1, column=0, columnspan=2, padx=(100, 100), pady=(10, 5), sticky="ew")

        # user or mail entry
        self.user_mail_entry = customtkinter.CTkEntry(self.add_frame, 
                                                    placeholder_text="Username or email",
                                                    fg_color="gray25",
                                                    border_width=0,
                                                    width=400, height=42, corner_radius=10,
                                                    font=customtkinter.CTkFont(size=15))
        self.user_mail_entry.grid(row=2, column=0, columnspan=2, padx=(100, 100), pady=(5, 5), sticky="ew")

        # password entry
        self.password_entry = customtkinter.CTkEntry(self.add_frame, 
                                                    placeholder_text="Password",
                                                    fg_color="gray25",
                                                    show="*",
                                                    border_width=0,
                                                    width=400, height=42, corner_radius=10,
                                                    font=customtkinter.CTkFont(size=15))
        self.password_entry.grid(row=3, column=0, columnspan=2, padx=(100, 100), pady=(5, 5), sticky="ew")

        # show pass checkbox
        self.show_pass_check = customtkinter.CTkCheckBox(self.add_frame,
                                                   text="Show password",
                                                   command=self.show_hide_add_pass)
        self.show_pass_check.grid(row=4, column=0, padx=(100, 5), pady=(10, 165), sticky="ew")

        # add button
        self.add_service_button = customtkinter.CTkButton(self.add_frame, 
                                                       height=40, 
                                                       corner_radius=10, 
                                                       text="Add", 
                                                       command=self.add_password, 
                                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        self.add_service_button.grid(row=4, column=1, padx=(5, 100), pady=(10, 165), sticky="ew")

        # create list frame
        self.saved_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent")
        self.saved_frame.grid_columnconfigure((0, 1), weight=1)
        self.saved_frame.grid_rowconfigure(0, weight=1)

        # refresh button
        self.refresh_list_button = customtkinter.CTkButton(self.saved_frame, 
                                                       height=40, 
                                                       corner_radius=10, 
                                                       text="Refresh", 
                                                       command=self.print_frames, 
                                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        self.refresh_list_button.grid(row=0, column=1, padx=20, pady=(50, 0), sticky="e")

        # saved label
        self.passgen_frame_label = customtkinter.CTkLabel(self.saved_frame, 
                                                             text="#saved passwords ", 
                                                             font=customtkinter.CTkFont(size=40, weight="bold"))
        self.passgen_frame_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(50, 0), sticky="w")

        # create delete frame
        self.delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.delete_frame.grid_columnconfigure((0, 1), weight=1)
        self.delete_frame.grid_rowconfigure((0, 3), weight=1)

        # delete label
        self.passgen_frame_label = customtkinter.CTkLabel(self.delete_frame, 
                                                             text="#delete ", 
                                                             font=customtkinter.CTkFont(size=40, weight="bold"))
        self.passgen_frame_label.grid(row=0, column=0, columnspan=2)

        self.delete_service_button = customtkinter.CTkButton(self.delete_frame,
                                                             width=150, 
                                                            height=40,
                                                            corner_radius=10,
                                                            text="Delete",
                                                            fg_color="#901212",
                                                            hover_color="#801212",
                                                            command=self.delete_service,
                                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.delete_service_button.grid(row=2, column=1, padx=(5, 50), pady=(10, 50), sticky="e")

        # select default frame
        self.select_frame_by_name("generate")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.generate_button.configure(fg_color=("gray75", "gray25") if name == "generate" else "transparent")
        self.add_button.configure(fg_color=("gray75", "gray25") if name == "add" else "transparent")
        self.saved_button.configure(fg_color=("gray75", "gray25") if name == "saved" else "transparent")
        self.delete_button.configure(fg_color="#901212" if name == "delete" else "transparent")

        # show selected frame
        if name == "generate":
            self.generate_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.generate_frame.grid_forget()
        if name == "add":
            self.add_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.add_frame.grid_forget()
        if name == "saved":
            self.saved_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.saved_frame.grid_forget()
        if name == "delete":
            self.delete_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.delete_frame.grid_forget()    

    def generate_button_event(self):
        self.select_frame_by_name("generate")

    def add_button_event(self):
        self.select_frame_by_name("add")

    def saved_button_event(self):
        self.select_frame_by_name("saved")
    
    def delete_button_event(self):
        self.select_frame_by_name("delete")

    # password generator functions
    def generate_pass(self):

        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase_letters = uppercase_letters.lower()
        numbers = "1234567890"
        symbols = "()[]{}.:,;-_/\\?+*#"

        upper = self.chars_upper_checkbox.get()
        lower = self.chars_lower_checkbox.get()
        nums = self.chars_nums_checkbox.get()
        syms = self.chars_syms_checkbox.get()
        length = int(self.pass_length_slider.get())

        chars = ""

        if upper == 1:
            chars += uppercase_letters*3
        if lower == 1:
            chars += lowercase_letters*3
        if nums == 1:
            chars += numbers*5
        if syms == 1:
            chars += symbols*3

        if chars == "":
            password = "C'm0n-U-z1nk-Ur-Funny:$?"
        else:
            password = "".join(random.sample(chars, length))

        self.pass_box.configure(state="normal")

        self.pass_box.delete("1.0", tk.END)
        self.pass_box.insert(tk.END, password)

        self.pass_box.configure(state="disabled")

        self.password = password

    def copy_pass(self):

        if hasattr(self, "password"):
            pyperclip.copy(self.password)
            self.pass_box.configure(state="normal")
            self.pass_box.delete("0.0", "end")
            self.pass_box.configure(state="disabled")

    def print_slider_value(self, value):

        self.pass_length_box.delete("1.0", tk.END)
        self.pass_length_box.insert(tk.END, int(value))

    # add password functions
    def show_hide_add_pass(self):

        checkbox_value = self.show_pass_check.get()

        if checkbox_value == 1:
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def generate_keys(self):

        key = Fernet.generate_key().decode()

        sql_connection = sqlite3.connect("/usr/lib/passman/passman.db")
        cursor = sql_connection.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='key'")

        if cursor.fetchone()[0] == 1:

            cursor.execute("SELECT * FROM key")
            sql_connection.commit()

        else:

            cursor.execute("CREATE TABLE key (key TEXT)")
            cursor.execute(f"INSERT INTO key (key) VALUES('{key}')")
            sql_connection.commit()
    
    def add_password(self):

        sql_connection = sqlite3.connect("/usr/lib/passman/passman.db")
        cursor = sql_connection.cursor()
        cursor.execute("SELECT * FROM key")
        key = cursor.fetchone()[0]
        key = key.encode()
        
        service = self.service_entry.get()
        user_mail = self.user_mail_entry.get()
        saved_password = self.password_entry.get().encode()

        f_key = Fernet(key)

        saved_password = f_key.encrypt(saved_password).decode()

        enc_credentials = [(service, user_mail, saved_password)]
        cursor.executemany("INSERT INTO services VALUES (?,?,?)", enc_credentials)
        cursor.execute("SELECT * FROM services")

        sql_connection.commit()
        sql_connection.close()

        service = self.service_entry.delete(0, "end")
        user_mail = self.user_mail_entry.delete(0, "end")
        saved_password = self.password_entry.delete(0, "end")

        self.print_frames()
        self.set_delete_options()

    def print_frames(self):

        global data_rows

        sql_connection = sqlite3.connect("/usr/lib/passman/passman.db")
        cursor = sql_connection.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='services'")

        if cursor.fetchone()[0] == 1:

            cursor.execute("SELECT * FROM services")
            data_rows = len(cursor.fetchall())
            sql_connection.commit()

        else:

            cursor.execute("CREATE TABLE services (service TEXT, user_mail TEXT, password TEXT)")
            data_rows = 0
            sql_connection.commit()

        # saved passwords frames
        #_________________________________________________________________________  

        global stored_credentials
        stored_credentials = []
        row = 1
        selected_row = 0

        cursor.execute("SELECT * FROM key")
        key = cursor.fetchone()[0]
        key = key.encode()

        f_key = Fernet(key)

        for i in range(0,data_rows):

            cursor.execute("SELECT service FROM services")
            service = cursor.fetchall()[selected_row][0]

            cursor.execute("SELECT user_mail FROM services")
            user_mail = cursor.fetchall()[selected_row][0]

            cursor.execute("SELECT password FROM services")
            saved_password = cursor.fetchall()[selected_row][0]
            saved_password = saved_password.encode()
            saved_password = f_key.decrypt(saved_password)
            saved_password = saved_password.decode()

            sql_connection.commit()

            # saved pass frame
            self.saved_pass_frame = customtkinter.CTkFrame(self.saved_frame, corner_radius=10, height=100, fg_color="gray10")
            self.saved_pass_frame.grid(row=row, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="ew")
        
            # service label
            self.saved_service_label = customtkinter.CTkLabel(self.saved_pass_frame,
                                                        text="#"+service, 
                                                        font=customtkinter.CTkFont(size=20, weight="bold"))
            self.saved_service_label.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 5), sticky="w")

            # user label
            self.saved_user_label = customtkinter.CTkLabel(self.saved_pass_frame,
                                                        text="User/email:")
            self.saved_user_label.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(0, 10), sticky="nse")

            # saved user
            self.saved_user_box = customtkinter.CTkTextbox(self.saved_pass_frame, 
                                                    width=350, 
                                                    height=30, 
                                                    corner_radius=10,
                                                    state="disabled",
                                                    font=customtkinter.CTkFont(size=15))
            self.saved_user_box.grid(row=1, column=2, columnspan=2, padx=(5, 0), pady=(0, 10), sticky="nse")

            # pass label
            self.saved_pass_label = customtkinter.CTkLabel(self.saved_pass_frame,
                                                        text="Password:")
            self.saved_pass_label.grid(row=2, column=0, columnspan=2, padx=(20, 20), pady=(0, 10), sticky="nse")

            # saved pass
            self.saved_pass_box = customtkinter.CTkTextbox(self.saved_pass_frame, 
                                                    width=350, 
                                                    height=30, 
                                                    corner_radius=10,
                                                    state="disabled",
                                                    font=customtkinter.CTkFont(size=15))
            self.saved_pass_box.grid(row=2, column=2, columnspan=2, padx=(5, 0), pady=(0, 20), sticky="nse")

            self.saved_user_box.configure(state="normal")
            self.saved_pass_box.configure(state="normal")

            self.saved_user_box.delete("1.0", tk.END)
            self.saved_user_box.insert(tk.END, user_mail)
            self.saved_pass_box.delete("1.0", tk.END)
            self.saved_pass_box.insert(tk.END, saved_password)

            self.saved_user_box.configure(state="disabled")
            self.saved_pass_box.configure(state="disabled")

            row += 1
            selected_row += 1
            stored_credentials.append((service, user_mail))
        
        sql_connection.commit()
        sql_connection.close()

    def set_delete_options(self):

        delete_options_array = []
        total_services = len(stored_credentials)

        for creds in range(0,total_services):
            service = stored_credentials[creds][0]
            user_mail = stored_credentials[creds][1]

            delete_options_array.append(f"{service} for {user_mail}")
        service = ""

        self.delete_options = customtkinter.CTkOptionMenu(self.delete_frame,
                                                            values=delete_options_array,
                                                            placeholder_text="No saved passwords yet...",
                                                            width=400,
                                                            height=40,
                                                            corner_radius=10,
                                                            fg_color="gray25",
                                                            button_color="gray30",
                                                            button_hover_color="gray20",
                                                            dropdown_hover_color="#901212",
                                                            font=customtkinter.CTkFont(size=15),
                                                            dropdown_font=customtkinter.CTkFont(size=15))
        self.delete_options.grid(row=1, column=0, columnspan=2, padx=(50, 50), sticky="ew")
            

        #_________________________________________________________________________   
    
    def delete_service(self):
        
        service = self.delete_options.get().split()[0]
        user_mail = self.delete_options.get().split()[2]

        sql_connection = sqlite3.connect("/usr/lib/passman/passman.db")
        cursor = sql_connection.cursor()

        cursor.execute(f"DELETE FROM services WHERE service='{service}' AND user_mail='{user_mail}'")
        sql_connection.commit()
        sql_connection.close()

        self.print_frames()
        self.set_delete_options()

    def register_page(self):

        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # login label
        self.login_frame_label = customtkinter.CTkLabel(self.login_frame, 
                                                                text="#register ", 
                                                                font=customtkinter.CTkFont(size=40, weight="bold"))
        self.login_frame_label.grid(row=0, column=0, columnspan=2, pady=(50, 25))

        # user or mail entry
        self.login_user_entry = customtkinter.CTkEntry(self.login_frame, 
                                                    placeholder_text="User",
                                                    fg_color="gray25",
                                                    border_width=0,
                                                    width=400, height=42, corner_radius=10,
                                                    font=customtkinter.CTkFont(size=15))
        self.login_user_entry.grid(row=1, column=0, columnspan=2, padx=(100, 100), pady=(5, 5), sticky="ew")

        # password entry
        self.login_password_entry = customtkinter.CTkEntry(self.login_frame, 
                                                    placeholder_text="Password",
                                                    fg_color="gray25",
                                                    show="*",
                                                    border_width=0,
                                                    width=400, height=42, corner_radius=10,
                                                    font=customtkinter.CTkFont(size=15))
        self.login_password_entry.grid(row=2, column=0, columnspan=2, padx=(100, 100), pady=(5, 5), sticky="ew")

        # login button
        self.login_button = customtkinter.CTkButton(self.login_frame, 
                                                       height=40, 
                                                       corner_radius=10, 
                                                       text="Register",
                                                       command=self.create_login_credentials,
                                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        self.login_button.grid(row=3, column=1, padx=(100, 100), pady=(5, 5), sticky="e") 

        # show pass checkbox
        self.show_login_pass_check = customtkinter.CTkCheckBox(self.login_frame,
                                                   text="Show password",
                                                   command=self.show_hide_login_pass)
        self.show_login_pass_check.grid(row=3, column=0, padx=(100, 5), pady=(5, 5), sticky="ew")

        # wrong pass label
        self.wrong_pass_label = customtkinter.CTkLabel(self.login_frame, 
                                                                text="", 
                                                                font=customtkinter.CTkFont(size=15))
        self.wrong_pass_label.grid(row=4, column=0, columnspan=2, padx=(100, 100), pady=(5, 25))

    def login_page(self):

        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # login label
        self.login_frame_label = customtkinter.CTkLabel(self.login_frame, 
                                                                text="#login ", 
                                                                font=customtkinter.CTkFont(size=40, weight="bold"))
        self.login_frame_label.grid(row=0, column=0, columnspan=2, pady=(50, 25))

        # user or mail entry
        self.login_user_entry = customtkinter.CTkEntry(self.login_frame, 
                                                    placeholder_text="User",
                                                    fg_color="gray25",
                                                    border_width=0,
                                                    width=400, height=42, corner_radius=10,
                                                    font=customtkinter.CTkFont(size=15))
        self.login_user_entry.grid(row=1, column=0, columnspan=2, padx=(100, 100), pady=(5, 5), sticky="ew")

        # password entry
        self.login_password_entry = customtkinter.CTkEntry(self.login_frame, 
                                                    placeholder_text="Password",
                                                    fg_color="gray25",
                                                    show="*",
                                                    border_width=0,
                                                    width=400, height=42, corner_radius=10,
                                                    font=customtkinter.CTkFont(size=15))
        self.login_password_entry.grid(row=2, column=0, columnspan=2, padx=(100, 100), pady=(5, 5), sticky="ew")

        # login button
        self.login_button = customtkinter.CTkButton(self.login_frame, 
                                                       height=40, 
                                                       corner_radius=10, 
                                                       text="Login",
                                                       command=self.check_credentials,
                                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        self.login_button.grid(row=3, column=1, padx=(100, 100), pady=(5, 5), sticky="e") 

        # show pass checkbox
        self.show_login_pass_check = customtkinter.CTkCheckBox(self.login_frame,
                                                   text="Show password",
                                                   command=self.show_hide_login_pass)
        self.show_login_pass_check.grid(row=3, column=0, padx=(100, 5), pady=(5, 5), sticky="ew")

        # wrong pass label
        self.wrong_pass_label = customtkinter.CTkLabel(self.login_frame, 
                                                                text="", 
                                                                font=customtkinter.CTkFont(size=15))
        self.wrong_pass_label.grid(row=4, column=0, columnspan=2, padx=(100, 100), pady=(5, 25))

    def create_login_credentials(self):

        input_user = self.login_user_entry.get()
        hashed_user = hashlib.sha256(input_user.encode("utf-8")).hexdigest()
        input_passwd = self.login_password_entry.get()
        hashed_passwd = hashlib.sha256(input_passwd.encode("utf-8")).hexdigest()
        login_creds = [hashed_user, hashed_passwd]

        sql_connection = sqlite3.connect("/usr/lib/passman/passman.db")
        cursor = sql_connection.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='master'")

        if cursor.fetchone()[0] == 1:
            self.check_credentials()

        else:
            cursor.execute("CREATE TABLE master (user TEXT, passwd TEXT)")          
            cursor.executemany("INSERT INTO master (user,passwd) VALUES (?,?)", [login_creds])
            sql_connection.commit() 
            self.check_credentials()

    def check_credentials(self):

        input_user = self.login_user_entry.get()
        hashed_user = hashlib.sha256(input_user.encode("utf-8")).hexdigest()
        input_passwd = self.login_password_entry.get()
        hashed_passwd = hashlib.sha256(input_passwd.encode("utf-8")).hexdigest()

        if input_user and input_passwd:

                sql_connection = sqlite3.connect("/usr/lib/passman/passman.db")
                cursor = sql_connection.cursor()

                cursor.execute("SELECT user FROM master")
                login_user = cursor.fetchall()[0][0]
                cursor.execute("SELECT passwd FROM master")
                login_passwd = cursor.fetchall()[0][0]

                sql_connection.commit()

                if hashed_user == login_user and hashed_passwd == login_passwd:
                    self.login_frame.destroy()
                    self.geometry("800x600")
                    
                else: 
                    self.wrong_pass_label.configure(text="Wrong password or username")
        else:
            self.wrong_pass_label.configure(text="Invalid password or username")

    def show_hide_login_pass(self):

        checkbox_value = self.show_login_pass_check.get()

        if checkbox_value == 1:
            self.login_password_entry.configure(show="")
        else:
            self.login_password_entry.configure(show="*")
    

if __name__ == "__main__":

    passman = PassMan()

    sql_connection = sqlite3.connect("/usr/lib/passman/passman.db")
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='master'")

    if cursor.fetchone()[0] == 1:
        passman.login_page()
    else:
        passman.register_page()

    passman.generate_keys()
    passman.print_frames()
    passman.set_delete_options()

    passman.mainloop()
