from tkinter import *


class Converter:

    def __init__(self):
        # common format for all buttons (Arial size 14, bold, white text)
        button_font = ("Arial", "14", "bold")
        button_fg = "#000000"
        # background button colours doesn't work on Mac, see this link:
        # https://stackoverflow.com/questions/72056706/tkinter-button-background-color-is-not-working-in-mac-os
        button_bg_metre = "#990099"
        button_bg_feet = "#009900"
        button_bg_help = "#CC6600"
        button_bg_history = "#004C99"

        # set up GUI frame
        self.altitude_frame = Frame(padx=10, pady=10)
        self.altitude_frame.grid()

        # conversion, help and history/export buttons
        self.button_frame = Frame(self.altitude_frame)
        self.button_frame.grid(row=4)

        self.help_button = Button(self.button_frame,
                                  text="Help/Info",
                                  bg=button_bg_help,
                                  fg=button_fg,
                                  font=button_font, width=12,
                                  command=self.to_help)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

    @staticmethod
    def to_help():
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        background = "#ffe6cc"

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Altitude Converter")
    Converter()
    root.mainloop()
