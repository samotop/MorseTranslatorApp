import tkinter as tk
from tkinter import ttk
import data
import pyperclip

COLOR_BG = "#A6CDC6"
COLOR_BT1 = "#FBF5DD"
COLOR_BT2 = "#16404D"
COLOR_BT3 = "#DDA853"
COLOR_WHITE = "#FFFFFF"
COLOR_ACTIVE_BG = "#edb458"


class MorseTranslatorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Morse Translator")
        self.window.geometry("943x580")
        self.window["bg"] = COLOR_BG

        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        #Morse Data
        self.text_to_morse_characters_json = data.text_to_morse_json_data
        self.morse_to_text_characters_json = data.morse_to_text_json_data

        #Start Frame
        self.start_frame = ttk.Frame(window)
        self.start_frame.grid()
        try:
            self.image = tk.PhotoImage(file="morse_code_logo (1).png")
        except tk.TclError:
            self.show_error(data.no_image_error_text)

        self.start_frame_background = None
        self.start_button = None

        self.start_frame_setup()

        #Custom Style Setup
        self.style = None
        self.style_setup()

        #Second Frame
        self.second_frame = ttk.Frame(window)
        self.second_frame.grid()

        #User Interaction Frame in Second Frame
        self.user_interaction_frame = ttk.Frame(self.second_frame, style="Custom.TFrame")
        self.user_interaction_frame.grid(sticky="nsew")

        self.user_interaction_frame.grid_rowconfigure(0, weight=0)
        self.user_interaction_frame.grid_rowconfigure(1, weight=1)
        self.user_interaction_frame.grid_columnconfigure(0, weight=1)
        self.user_interaction_frame.grid_columnconfigure(1, weight=0)
        self.user_interaction_frame.grid_columnconfigure(2, weight=0)
        self.user_interaction_frame.grid_columnconfigure(3, weight=0)

        # Initialize the variable for letter count
        self.variable = tk.StringVar()

        #Initialize the Selected for radio buttons
        self.selected = tk.StringVar()

        self.max_characters = None

        #Initialization of Widgets
        self.rules = None
        self.main_title = None
        self.message_box = None
        self.translate_button = None
        self.letter_counter = None
        self.translated_text = None
        self.new_translate_button = None
        self.copy_button = None
        self.letter_count = None
        self.r1 = None
        self.r2 = None

    def start_frame_setup(self):
        """Sets up the starting frame of the application, including the background image and the 'START' button.
        The button is configured to initiate the main program when clicked and has visual effects when hovered over."""

        self.start_frame_background = ttk.Label(self.start_frame, image=self.image)
        self.start_frame_background.grid(row=0, column=0)

        self.start_button = tk.Button(self.start_frame, text="START", command=self.start_program, width=10,
                                      background=COLOR_BT3,
                                      font=("Helvetica", 10, "bold"))
        self.start_button.grid(row=1, column=0, pady=10)
        self.start_button.bind("<Enter>", self.on_enter)
        self.start_button.bind("<Leave>", self.on_leave)

    def style_setup(self):
        """Configures the custom style for various widgets in the application, including frames, labels, buttons,
        and radio buttons. The style settings adjust the background, foreground colors, and other visual elements
        to align with the app's design theme."""

        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background=COLOR_BG)
        self.style.configure("Custom.TLabel", background=COLOR_BG, foreground=COLOR_BT2)
        self.style.configure("Custom.TButton", background=COLOR_BT2, highlightthickness=2)
        self.style.configure("Custom.TRadiobutton", background=COLOR_BG)

    def second_frame_setup(self):
        """Sets up the second frame of the application by configuring the widgets and layout for user interaction.
        This includes buttons, labels, input fields, and event bindings for actions such as translating messages,
        copying answers, and showing app rules. It also sets up the necessary callbacks and visual components like
        the letter counter and radio buttons for translation mode selection."""

        #App Rules
        self.rules = tk.Button(self.window, text="RULES", command=self.show_rules, width=10,
                               background=COLOR_BT3,
                               font=("Helvetica", 10, "normal"))
        self.rules.place(x=0, y=0)
        self.rules.bind("<Enter>", self.on_enter)
        self.rules.bind("<Leave>", self.on_leave)

        #Main Title Widget
        self.main_title = ttk.Label(self.user_interaction_frame, text="TYPE YOUR MESSAGE BELLOW", font=("Arial", 25),
                                    style="Custom.TLabel")
        self.main_title.grid(row=0, column=0, columnspan=4, pady=20)

        #User Entry Widget
        self.message_box = ttk.Entry(self.user_interaction_frame, width=60, textvariable=self.variable)
        self.message_box.grid(row=1, column=1)

        #Translate Button Widget
        self.translate_button = tk.Button(self.user_interaction_frame, text="TRANSLATE",
                                          command=self.check_translate_mode, width=24,
                                          background=COLOR_BT3,
                                          font=("Helvetica", 10, "normal"))
        self.translate_button.grid(row=1, column=2)
        self.translate_button.bind("<Enter>", self.on_enter)
        self.translate_button.bind("<Leave>", self.on_leave)

        #Letter Counter
        self.letter_counter = ttk.Label(self.user_interaction_frame, text=f"0/150", font=("Arial", 15),
                                        style="Custom.TLabel")
        self.letter_counter.grid(row=1, column=0, padx=10)

        #Translated Text
        self.translated_text = ttk.Label(self.second_frame, font=("Arial", 25), wraplength=850, style="Custom.TLabel")

        #New Translate Button
        self.new_translate_button = tk.Button(self.user_interaction_frame, text="TRANSLATE NEW MESSAGE",
                                              command=self.translate_new_message,
                                              background=COLOR_BT3,
                                              font=("Helvetica", 10, "normal")
                                              )
        self.new_translate_button.bind("<Enter>", self.on_enter)
        self.new_translate_button.bind("<Leave>", self.on_leave)

        #Copy Button
        self.copy_button = tk.Button(self.user_interaction_frame, text="COPY ANSWER", command=self.copy,
                                     background=COLOR_BT3,
                                     font=("Helvetica", 10, "normal")
                                     )
        self.copy_button.bind("<Enter>", self.on_enter)
        self.copy_button.bind("<Leave>", self.on_leave)

        #Setup user entry for tracking
        self.variable.trace_add(mode="write", callback=self.write_callback)

        #Radio Buttons
        self.r1 = ttk.Radiobutton(self.user_interaction_frame, text='Text To Morse', value='Text To Morse',
                                  variable=self.selected, command=self.update_letter_count, style="Custom.TRadiobutton")
        self.r1.grid(row=2, column=0, columnspan=2)

        self.r2 = ttk.Radiobutton(self.user_interaction_frame, text='Morse To Text', value='Morse To Text',
                                  variable=self.selected, command=self.update_letter_count, style="Custom.TRadiobutton")
        self.r2.grid(row=2, column=1, columnspan=2)

    def start_program(self):
        """Starts the main program by hiding the initial start frame and displaying the second frame with the user
        interface. It also sets the default translation mode to 'Text to Morse'."""

        self.start_frame.grid_forget()
        self.second_frame_setup()
        self.second_frame.grid()
        self.selected.set("Text To Morse")

    def translate_to_morse(self):
        """Translates the text input from the user into Morse code. Each character in the input text is converted
        to its corresponding Morse code using a predefined mapping. If an error occurs during translation, a type
        error message is displayed. After translation, the Morse code is displayed, and the interface is updated
        to reflect the translation."""

        text_input = self.message_box.get().lower()
        list_of_input_characters = list(text_input)

        list_of_translated_characters = []
        for character in list_of_input_characters:
            try:
                translated_character = self.text_to_morse_characters_json.get(character)
                list_of_translated_characters.append(translated_character)
                translated_text = "   ".join(list_of_translated_characters)
                self.translated_text.configure(text=translated_text)
            except TypeError:
                self.show_error(data.type_error_text)

        self.setup_after_translate()

    def translate_to_text(self):
        """Translates Morse code input from the user into text. The input Morse code is split into words and characters,
        which are then translated using the predefined Morse-to-text mapping. If an error occurs during translation,
        a type error message is displayed. After translation, the translated text is displayed
        and the interface is updated."""

        translated_message = []
        morse_code = self.message_box.get()

        try:
            morse_code_input_words = morse_code.split("       ")

            words = []

            for word in morse_code_input_words:
                ready_for_translate_word = word.split("   ")
                words.append(ready_for_translate_word)

            for word in words:
                translated_word = []
                for character in word:
                    if character == "":
                        pass
                    else:
                        translated_character = self.morse_to_text_characters_json.get(character)
                        translated_word.append(translated_character)
                translated_message.append("".join(translated_word))

            self.translated_text.configure(text=" ".join(translated_message))
        except TypeError:
            self.show_error(data.type_error_text)

        self.setup_after_translate()

    def copy(self):
        """Copies the translated text to the clipboard and updates the 'Copy' button to show a confirmation message.
        The button is then disabled to prevent further copying until the next translation."""
        pyperclip.copy(self.translated_text.cget("text"))
        self.copy_button.configure(text="COPIED ✔", state="disabled")

    def translate_new_message(self):
        """Resets the interface for translating a new message. It hides the 'New Translate' and 'Copy' buttons,
        restores the 'Translate' button, clears the message input field and translated text, and re-enables the
        'Copy' button for the next translation."""

        self.new_translate_button.grid_forget()
        self.copy_button.grid_forget()
        self.translate_button.grid(column=2, row=1)
        self.message_box.configure(state="normal")
        self.message_box.delete(0, tk.END)
        self.translated_text.configure(text="")
        self.copy_button.configure(state="normal", text="COPY ANSWER")

    def write_callback(self, var, index, mode):
        """Callback function that tracks changes in the input field. It updates the letter count, adjusts the
        maximum character limit based on the selected translation mode, and disables/enables the translate button
        depending on whether the character count exceeds the limit."""

        current_text = self.variable.get()
        self.letter_count = len(current_text)
        if self.selected.get() == "Text To Morse":
            self.max_characters = 150
        else:
            self.max_characters = 2000
        self.letter_counter.configure(text=f"{self.letter_count}/{self.max_characters}")

        if int(self.letter_count) > self.max_characters:
            self.translate_button.configure(state="disabled")
            self.letter_counter.configure(foreground="red")
        else:
            self.translate_button.configure(state="normal")
            self.letter_counter.configure(foreground="black")

    def check_translate_mode(self):
        """Checks the selected translation mode (Text to Morse or Morse to Text)
        and calls the appropriate translation function based on the user's choice."""

        if self.selected.get() == "Text To Morse":
            self.translate_to_morse()
        else:
            self.translate_to_text()

    def setup_after_translate(self):
        """Configures the layout and behavior of the widgets after a translation is completed.
        It displays the translated text, disables the message input field, hides the translate button,
        and shows the option to translate a new message or copy the translation."""

        if self.window.winfo_exists():
            self.translated_text.grid(column=0, row=3, sticky="nsew")
            self.message_box.configure(state="disabled")
            self.translate_button.grid_forget()
            self.new_translate_button.grid(column=2, row=1)
            self.copy_button.grid(column=3, row=1)

    def update_letter_count(self):
        """Updates the letter count display based on the selected translation mode.
        It shows the current number of characters typed and updates the maximum allowed count
        depending on whether 'Text To Morse' or 'Morse To Text' mode is selected."""

        if self.selected.get() == "Text To Morse":
            self.letter_counter.configure(text=f"{self.letter_count}/150")
        else:
            self.letter_counter.configure(text=f"{self.letter_count}/2000")

    def show_rules(self):
        """Displays a popup window with the application's rules.
        The window contains the rules text and an 'Agree' button that closes the window when clicked."""

        popup_window = tk.Tk()
        popup_window.eval('tk::PlaceWindow . center')
        popup_window.title("App Rules")
        label = ttk.Label(popup_window, text=data.rules_text)
        label.pack(side="top", fill="x", pady=10)
        agree_button = ttk.Button(popup_window, text="Agree", command=popup_window.destroy)
        agree_button.pack()
        popup_window.mainloop()

    def show_error(self, error_text):
        """Displays an error window when the user enters invalid characters or spaces. The window shows an error
        message and a button to acknowledge the error and close the window."""

        error_window = tk.Tk()
        error_window.eval('tk::PlaceWindow . center')
        error_window.title("Oops..")
        label = ttk.Label(error_window, text=error_text)
        label.pack(side="top", fill="x", pady=10)
        agree_button = ttk.Button(error_window, text="Agree", command=error_window.destroy)
        agree_button.pack()
        error_window.mainloop()

    def on_enter(self, event):
        """Changing the background on mouse hover"""
        event.widget.config(background=COLOR_ACTIVE_BG)

    def on_leave(self, event):
        """Restoring the original background after the mouse leaves"""
        event.widget.config(background=COLOR_BT3)


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseTranslatorApp(root)
    root.mainloop()
