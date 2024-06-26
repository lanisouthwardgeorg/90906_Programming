from tkinter import *


class Converter:

    def __init__(self):

        # common format for all buttons (Arial size 14, bold, white text)
        button_font = ("Arial", "14", "bold")
        button_fg = "#000000"
        # background button colours doesn't work on mac, see this link:
        # https://stackoverflow.com/questions/72056706/tkinter-button-background-color-is-not-working-in-mac-os
        button_bg_metre = "#990099"
        button_bg_feet = "#009900"
        button_bg_help = "#CC6600"
        button_bg_history = "#004C99"

        # set up GUI frame
        self.altitude_frame = Frame(padx=10, pady=10)
        self.altitude_frame.grid()

        self.altitude_heading = Label(self.altitude_frame,
                                      text="Altitude Convertor",
                                      font=("Arial", "16", "bold"))

        self.altitude_heading.grid(row=0)

        instructions = "Please enter an altitude below and press one of the buttons to convert it from metres to feet."
        self.altitude_instructions = Label(self.altitude_frame,
                                           text=instructions,
                                           wrap=300, width=50,
                                           justify="left")

        self.altitude_instructions.grid(row=1)

        self.altitude_entry = Entry(self.altitude_frame,
                                    font=("Arial", "14"))
        self.altitude_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.altitude_error = Label(self.altitude_frame,
                                    text="",
                                    fg="#9A1B00")
        self.altitude_error.grid(row=3)

        # conversion, help and history/export buttons
        self.button_frame = Frame(self.altitude_frame)
        self.button_frame.grid(row=4)

        self.to_metres_button = Button(self.button_frame,
                                       text="To metres",
                                       bg=button_bg_metre,
                                       fg=button_fg,
                                       font=button_font,
                                       width=12,
                                       command=self.to_metres
                                       )
        self.to_metres_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_feet_button = Button(self.button_frame,
                                     text="To feet",
                                     bg=button_bg_feet,
                                     fg=button_fg,
                                     font=button_font,
                                     width=12
                                     )
        self.to_feet_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = Button(self.button_frame,
                                  text="Help/Info",
                                  bg=button_bg_help,
                                  fg=button_fg,
                                  font=button_font,
                                  width=12
                                  )
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_button = Button(self.button_frame,
                                     text="History/Export",
                                     bg=button_bg_history,
                                     fg=button_fg,
                                     font=button_font,
                                     width=12,
                                     state=DISABLED
                                     )
        self.history_button.grid(row=1, column=1, padx=5, pady=5)

    # checks for valid input, converts altitude
    def check_altitude(self, min_value):

        has_error = "no"
        error = "Please enter a number that is more than {}".format(min_value)

        # check that user has entered a valid number
        try:
            response = self.altitude_entry.get()
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # if the number is invalid, display error message
        if has_error == "yes":
            self.altitude_error.config(text=error, fg="#9C0000")
        else:
            self.altitude_error.config(text="Success", fg="blue")

            # if we have at least one valid calculation, enable history/export button
            self.history_button.config(state=NORMAL)

    def to_metres(self):

        self.check_altitude(0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Altitude Converter")
    Converter()
    root.mainloop()
