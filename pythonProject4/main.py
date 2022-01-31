import tkinter
import tkinter.messagebox
import customtkinter
import sys

# Set dark appearance mode:
customtkinter.set_appearance_mode("Dark")  # Other: "Light", "System"


class App(tkinter.Tk):

    APP_NAME = "Alisveris Listesi"
    WIDTH = 700
    HEIGHT = 500
    MAIN_COLOR = "#5EA880"
    MAIN_COLOR_DARK = "#2D5862"
    MAIN_HOVER = "#458577"


    def __init__(self, *args, **kwargs):


        tkinter.Tk.__init__(self, *args, **kwargs)

        if "win" in sys.platform:
            if customtkinter.get_appearance_mode() == "Dark":
                self.configure(bg="gray20")  # set window background to dark color

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)


        self.createcommand('tk::mac::Quit', self.on_closing)

        # ============ create two CTkFrames ============

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=200,
                                                 height=App.HEIGHT-40,
                                                 corner_radius=5)
        self.frame_left.place(relx=0.32, rely=0.5, anchor=tkinter.E)

        self.frame_right = customtkinter.CTkFrame(master=self,
                                                  width=420,
                                                  height=App.HEIGHT-40,
                                                  corner_radius=5)
        self.frame_right.place(relx=0.365, rely=0.5, anchor=tkinter.W)

        # ============ frame_left ============

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                border_color=App.MAIN_COLOR,
                                                fg_color=None,
                                                hover_color=App.MAIN_HOVER,
                                                text="Sil",
                                                command=self.delete,
                                                border_width=3,
                                                corner_radius=5)
        self.button_1.place(relx=0.5, y=50, anchor=tkinter.CENTER)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                border_color=App.MAIN_COLOR,
                                                fg_color=None,
                                                hover_color=App.MAIN_HOVER,
                                                text="Kaydet",
                                                command=self.save,
                                                border_width=3,
                                                corner_radius=5)
        self.button_2.place(relx=0.5, y=100, anchor=tkinter.CENTER)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                border_color=App.MAIN_COLOR,
                                                fg_color=None,
                                                hover_color=App.MAIN_HOVER,
                                                text="Yükle",
                                                command=self.load,
                                                border_width=3,
                                                corner_radius=5)
        self.button_3.place(relx=0.5, y=150, anchor=tkinter.CENTER)


        # ============ frame_right ============

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right,
                                                 width=380,
                                                 height=200,
                                                 corner_radius=5)
        self.frame_info.place(relx=0.5, y=20, anchor=tkinter.N)

        # ============ frame_right -> frame_info ============


        self.box = tkinter.Listbox(master=self.frame_info, bg="gray20", height=12,width=60,fg="white")
        self.box.place(relx=0.5, y=100, anchor=tkinter.CENTER)
        self.label_info_2 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Urun adı giriniz     " ,
                                                   width=180,
                                                   height=28,
                                                   corner_radius=5,

                                                   text_color=App.MAIN_COLOR,
                                                   justify=tkinter.LEFT)
        self.label_info_2.place(relx=0.28, rely=0.60, anchor=tkinter.CENTER)
        self.label_info_3 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Urun adeti giriniz  ",
                                                   width=180,
                                                   height=28,
                                                   corner_radius=5,

                                                   text_color=App.MAIN_COLOR,
                                                   justify=tkinter.LEFT)
        self.label_info_3.place(relx=0.28, rely=0.70, anchor=tkinter.CENTER)
        self.label_info_2 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Urun fiyatini giriniz ",
                                                   width=180,
                                                   height=28,
                                                   corner_radius=5,

                                                   text_color=App.MAIN_COLOR,
                                                   justify=tkinter.LEFT)
        self.label_info_2.place(relx=0.28, rely=0.80, anchor=tkinter.CENTER)




        # ============ frame_right <- ============

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=28,
                                            corner_radius=5)
        self.entry.place(relx=0.66, rely=0.60, anchor=tkinter.CENTER)
        self.entry.insert(0, "")
        self.entry2 = customtkinter.CTkEntry(master=self.frame_right,
                                             width=120,
                                             height=28,
                                             corner_radius=5)
        self.entry2.place(relx=0.66, rely=0.70, anchor=tkinter.CENTER)
        self.entry2.insert(0, "")
        self.entry3 = customtkinter.CTkEntry(master=self.frame_right,
                                             width=120,
                                             height=28,
                                             corner_radius=5)
        self.entry3.place(relx=0.66, rely=0.80, anchor=tkinter.CENTER)
        self.entry3.insert(0, "")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                border_color=App.MAIN_COLOR,
                                                fg_color=None,
                                                hover_color=App.MAIN_HOVER,
                                                height=28,
                                                text="Listeye Ekle",
                                                command=self.add,
                                                border_width=3,
                                                corner_radius=5)
        self.button_5.place(relx=0.66, rely=0.92, anchor=tkinter.CENTER)

    def add(self):
        self.box.insert(tkinter.END,
        self.entry.get() + "                      " + self.entry2.get() + "                      " + self.entry3.get())
        self.entry.delete(0, tkinter.END)
        self.entry2.delete(0, tkinter.END)
        self.entry3.delete(0, tkinter.END)

    def delete(self):
        if len(self.box.curselection()) > 0:
            index = self.box.curselection()[0]
            self.box.delete(index)

    def save(self):
        f = open('yap.txt', 'w', encoding='utf-8')
        gorevler = self.box.get(0, tkinter.END)
        f.writelines('\n'.join(gorevler))
        f.close()

    def load(self):
        f = open('yap.txt', 'r', encoding='utf-8')
        gorevler = f.readlines()
        self.box.delete(0, tkinter.END)
        for gorev in gorevler:
            if '\n' in gorev:
                gorev = gorev.replace('\n', '')
            self.box.insert(tkinter.END, gorev)



    def on_closing(self, event=0):
        customtkinter.disable_macos_darkmode()
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()