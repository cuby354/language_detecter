import tkinter as tk
from tkinter import messagebox
from langdetect import detect
from langdetect import lang_detect_exception

# Mapping of language codes to their full names
LANGUAGE_NAMES = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'bg': 'Bulgarian',
    'bn': 'Bengali',
    'ca': 'Catalan',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'et': 'Estonian',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'gu': 'Gujarati',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'kn': 'Kannada',
    'ko': 'Korean',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepali',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pa': 'Punjabi',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'sq': 'Albanian',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tl': 'Tagalog',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)'
}

def detect_language(text):
    try:
        language_code = detect(text)
        language_name = LANGUAGE_NAMES.get(language_code, 'Unknown')
    except lang_detect_exception.LangDetectException as e:
        # Handle exceptions, such as when the input is too short
        print("Error during language detection:", e)
        return None
    return language_name

def detect_and_show_language():
    text = entry.get()
    language = detect_language(text)
    if language:
        messagebox.showinfo("Language Detection", f"The detected language is: {language}")
    else:
        messagebox.showerror("Error", "Unable to detect language.")

# Create the main window
root = tk.Tk()
root.title("Language Detection")

# Create a label and an entry for user input
label = tk.Label(root, text="Enter text:")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button to trigger language detection
button = tk.Button(root, text="Detect Language", command=detect_and_show_language)
button.pack()

# Run the main event loop
root.mainloop()
