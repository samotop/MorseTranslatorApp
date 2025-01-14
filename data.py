text_to_morse_json_data = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-",
  " ": "       "
}

morse_to_text_json_data = {
  '-----': '0',
  '.----': '1',
  '..---': '2',
  '...--': '3',
  '....-': '4',
  '.....': '5',
  '-....': '6',
  '--...': '7',
  '---..': '8',
  '----.': '9',
  '.-': 'a',
  '-...': 'b',
  '-.-.': 'c',
  '-..': 'd',
  '.': 'e',
  '..-.': 'f',
  '--.': 'g',
  '....': 'h',
  '..': 'i',
  '.---': 'j',
  '-.-': 'k',
  '.-..': 'l',
  '--': 'm',
  '-.': 'n',
  '---': 'o',
  '.--.': 'p',
  '--.-': 'q',
  '.-.': 'r',
  '...': 's',
  '-': 't',
  '..-': 'u',
  '...-': 'v',
  '.--': 'w',
  '-..-': 'x',
  '-.--': 'y',
  '--..': 'z',
  '.-.-.-': '.',
  '--..--': ',',
  '..--..': '?',
  '-.-.--': '!',
  '-....-': '-',
  '-..-.': '/',
  '.--.-.': '@',
  '-.--.': '(',
  '-.--.-': ')',
}

rules_text = """
Rules of Use for Text-to-Morse and Morse-to-Text Translation Tool

1. Purpose of the Tool
   This tool is designed for converting standard text to Morse code and translating Morse code back into text. It is 
   intended for educational, personal, and non-commercial use only.

2. Input Guidelines
   - When entering text, use only valid characters (letters, numbers, and basic punctuation).
   - When entering Morse code:
     - Separate individual letters with three spaces.
     - Separate words with seven spaces.
   - Incorrect spacing or invalid characters may result in translation errors.

3. Accuracy of Translation
   While the tool aims to provide accurate translations, variations in input formatting may affect the output. Users are
    encouraged to double-check the results for accuracy.

4. Limitations
   - The tool does not support non-standard Morse code variations or complex symbols.
   - Extremely long inputs may cause slower processing.

By clicking "Agree," you confirm that you understand and accept these rules of use.
"""

type_error_text = "Invalid input detected. Please ensure your message contains only valid characters and uses correct" \
                  " spacing. Try again!"

no_image_error_text = "Failed to load image. Please ensure 'morse_code_logo.png' is in the correct directory."