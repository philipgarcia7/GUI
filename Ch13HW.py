from multiprocessing.sharedctypes import Value
import tkinter
import tkinter.messagebox


class pizzatime:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("600x300")
        self.main_window.configure(bg="sky blue")

        self.top_frame = tkinter.Frame(self.main_window)
        self.two_frame = tkinter.Frame(self.main_window)
        self.tm_frame = tkinter.Frame(self.main_window)
        self.three_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(10)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)

        self.top_frame.pack(side="top")
        self.two_frame.pack(side="top")
        self.tm_frame.pack(side="top")
        self.three_frame.pack(side="top")
        self.mid_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.t1_label = tkinter.Label(self.top_frame, text="Enter Customer's Name:")

        self.t1_label.pack(side="top")

        self.t1_entry = tkinter.Entry(self.top_frame, width=10)

        self.t1_label.pack(side="left")
        self.t1_entry.pack(side="left")
        self.t1_label.configure(bg="sky blue")

        self.t2_label = tkinter.Label(self.two_frame)
        self.t2_label.pack(side="bottom")

        self.t2_label.configure(bg="sky blue")

        self.t3_label = tkinter.Label(self.three_frame)
        self.t3_label.pack(side="bottom")

        self.t3_label.configure(bg="sky blue")

        self.rb1 = tkinter.Radiobutton(
            self.tm_frame,
            text="Original Crust: $10.00",
            variable=self.radio_var,
            value=10,
        )

        self.rb1.pack(side="left")
        self.rb1.configure(bg="sky blue")

        self.rb2 = tkinter.Radiobutton(
            self.tm_frame, text="Thin Crust: $8.00", variable=self.radio_var, value=8
        )

        self.rb2.pack(side="left")
        self.rb2.configure(bg="sky blue")

        self.rb3 = tkinter.Radiobutton(
            self.tm_frame,
            text="Stuffed Crust: $12.00",
            variable=self.radio_var,
            value=12,
        )

        self.rb3.pack(side="left")
        self.rb3.configure(bg="sky blue")

        self.cb1 = tkinter.Checkbutton(
            self.mid_frame, text="Pepperoni: $1.50", variable=self.cb_var1
        )
        self.cb2 = tkinter.Checkbutton(
            self.mid_frame, text="Sausage: $1.75", variable=self.cb_var2
        )
        self.cb3 = tkinter.Checkbutton(
            self.mid_frame, text="Bell Peppers: $2.00", variable=self.cb_var3
        )

        self.cb4 = tkinter.Checkbutton(
            self.mid_frame, text="Pineapple: $5.00", variable=self.cb_var4
        )

        self.cb1.pack(side="left")
        self.cb2.pack(side="left")
        self.cb3.pack(side="left")
        self.cb4.pack(side="left")
        self.cb1.configure(bg="sky blue")
        self.cb2.configure(bg="sky blue")
        self.cb3.configure(bg="sky blue")
        self.cb4.configure(bg="sky blue")

        self.totbutton = tkinter.Button(
            self.main_window, text="Calculate Total", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.totbutton.pack(side="left")

        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def convert(self):

        total = float(self.radio_var.get())

        if self.cb_var1.get() == 1:
            total += 1.50
        if self.cb_var2.get() == 1:
            total += 1.75
        if self.cb_var3.get() == 1:
            total += 2.00
        if self.cb_var4.get() == 1:
            total += 5.00

        tkinter.messagebox.showinfo(
            "The total cost of ", self.t1_entry.get() + "'s pizza is: $" + str(total)
        )


pizza = pizzatime()
