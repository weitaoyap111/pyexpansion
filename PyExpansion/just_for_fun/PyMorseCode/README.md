Hi, I am PyMorseCode

A library to convert Morse Code to word or vice versa.

Let me teach you how to use me.
```
from PyExpansion.just_for_fun.PyMorseCode import main
```
This line is to use me (call library)

So, next step is:
```
c = main.MorseCode()
```

From here, I have two main function. <br>

- encode
- decode

### encode
Convert human-readable word to morse code

### decode
Convert morse code to human-readable word

So, nex step is:

```
word = "Hello World"
print(c.encode(word))
```

Output will be:
```
.... . ._.. ._.. ___ | .__ ___ ._. _..
```

Another one is decode:

```
morse_code = ".... . ._.. ._.. ___ .__ ___ ._. ._.. _.."
print(c.decode(word))
```

Output will be:
```
HELLOWORLD
```

That is all about me(Morse Code). Hope you enjoy.<br>
Say ya.
