import tkinter
import tkinter.messagebox

from click import secho


class averagemaker:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("600x300")
        # self.main_window.colormapwindows("Green")

        self.top_frame = tkinter.Frame(self.main_window)
        self.tm_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bavg_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.t1_label = tkinter.Label(self.top_frame, text="Enter a score for test 1:")

        self.t1_label.pack(side="top")

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.t1_entry = tkinter.Entry(self.top_frame, width=10)

        self.t1_label.pack(side="left")
        self.t1_entry.pack(side="left")

        self.t2_label = tkinter.Label(self.tm_frame, text="Enter a score for test 2:")

        self.t2_label.pack(side="top")

        self.tm_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.t2_entry = tkinter.Entry(self.tm_frame, width=10)

        self.t2_label.pack(side="left")
        self.t2_entry.pack(side="left")

        self.t3_label = tkinter.Label(self.mid_frame, text="Enter a score for test 3:")

        self.t3_label.pack(side="top")

        self.mid_frame.pack(side="top")
        self.bavg_frame.pack(side="top")

        self.bottom_frame.pack(side="top")

        self.t3_entry = tkinter.Entry(self.mid_frame, width=10)

        self.t3_label.pack(side="left")
        self.t3_entry.pack(side="left")

        self.descr_label = tkinter.Label(self.bavg_frame, text="Average: ")
        self.avg_var = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.bavg_frame, textvariable=self.avg_var)

        self.descr_label.pack(side="left")
        self.avg_label.pack(side="left")

        self.avgbutton = tkinter.Button(
            self.main_window, text="Average", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.avgbutton.pack(side="left")

        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def convert(self):
        total = (
            float(self.t1_entry.get())
            + float(self.t2_entry.get())
            + float(self.t3_entry.get())
        )

        avg = round(total / 3, 2)

        self.avg_var.set(avg)


avg_conv = averagemaker()

print("moving on.....")
