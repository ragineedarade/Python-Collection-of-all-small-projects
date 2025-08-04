from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Make sure you have installed the library:
# pip install googletrans==4.0.0-rc1


def change(text="type", src="en", dest="hi"):
    """Translates the text and returns the translated text."""
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text  # Access the .text attribute for the translated string


def data():
    """Gets text and languages from widgets, translates, and displays."""
    try:
        # Get language names from the combo boxes
        src_lang_name = comb_sor.get()
        dest_lang_name = comb_dest.get()

        # Find the language codes from the reversed dictionary
        src_lang_code = lang_name_to_code.get(
            src_lang_name, 'en')  # Default to English if not found
        dest_lang_code = lang_name_to_code.get(
            dest_lang_name, 'hi')  # Default to Hindi if not found

        # Get the text from the source Text widget
        # .strip() removes leading/trailing whitespace
        masg = sor_txt.get(1.0, END).strip()

        if masg:
            # Call the translation function with language codes
            textget = change(text=masg, src=src_lang_code, dest=dest_lang_code)

            # Clear the destination Text widget and insert the new text
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, textget)

    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, f"Error: {e}")
        print(f"An error occurred: {e}")

# --- Tkinter Setup ---


root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='purple')

# Create a reversed dictionary for easy lookup (language name -> code)
lang_name_to_code = {name: code for code, name in LANGUAGES.items()}
list_text = sorted(list(LANGUAGES.values()))  # Sort the list of language names

# Title Label
title_label = Label(root, text="Translator", font=(
    "time new roman", 20, "bold"), bg="pink")
title_label.place(x=100, y=20, height=50, width=250)

# Main Frame
main_frame = Frame(root, bg='purple')
main_frame.pack(side=BOTTOM, fill=BOTH, expand=True, pady=10)

# Source Text Label
source_txt_label = Label(main_frame, text="Source Text", font=(
    "time new roman", 15, "bold"), fg="black", bg="purple")
source_txt_label.pack(pady=(0, 5))

# Source Text Widget
sor_txt = Text(main_frame, font=("time new roman", 12, "bold"),
               wrap=WORD, height=8, width=40)
sor_txt.pack(padx=10, pady=(0, 10))

# Language Selection Frame
lang_select_frame = Frame(main_frame, bg='purple')
lang_select_frame.pack(pady=5)

# Source Language Combobox
comb_sor = ttk.Combobox(lang_select_frame, value=list_text,
                        font=("time new roman", 10))
comb_sor.pack(side=LEFT, padx=5)
comb_sor.set("english")

# Translate Button
button_change = Button(lang_select_frame, text="Translate",
                       relief=RAISED, command=data, font=("time new roman", 10, "bold"))
button_change.pack(side=LEFT, padx=5)

# Destination Language Combobox
comb_dest = ttk.Combobox(
    lang_select_frame, value=list_text, font=("time new roman", 10))
comb_dest.pack(side=LEFT, padx=5)
comb_dest.set("hindi")

# Destination Text Label
dest_txt_label = Label(main_frame, text="Destination Text", font=(
    "time new roman", 15, "bold"), fg="black", bg="purple")
dest_txt_label.pack(pady=(10, 5))

# Destination Text Widget
dest_txt = Text(main_frame, font=("time new roman", 12,
                "bold"), wrap=WORD, height=8, width=40)
dest_txt.pack(padx=10, pady=(0, 10))

root.mainloop()
