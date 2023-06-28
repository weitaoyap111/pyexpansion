from PyExpansion.just_for_fun.PyMorseCode import main

c = main.MorseCode()
word = "Hello World"
print(c.encode(word))
morse_code = ".... . ._.. ._.. ___ .__ ___ ._. ._.. _.."
print(c.decode(morse_code))
