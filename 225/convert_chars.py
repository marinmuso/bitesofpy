PYBITES = "pybites"


def convert_pybites_chars(text):
   swapped = [letter.swapcase() 
              if letter.lower() in PYBITES
              else letter
              for letter in text]
   return "".join(swapped) 