from tkinter import *


class Converter:

    def __init__(self):

        # set up GUI frame
        self.altitude_frame = Frame(padx=10, pady=10)
        self.altitude_frame.grid()

        self.altitude_heading = Label(self.altitude_frame, text="Altitude Convertor", font=("Arial", "16", "bold"))

        self.altitude_heading.grid(row=0)

        instructions = "Please enter an altitude below and press one of the buttons to convert it from metres to feet."
        self.altitude_instructions = Label(self.altitude_frame, text=instructions, wrap=300, width=50, justify="left")

        self.altitude_instructions.grid(row=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Altitude Converter")
    Converter()
    root.mainloop()
