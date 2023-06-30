Hi, I am PyDeadFish

A library to convert Dead Fish code to word or vice versa.

Let me teach you how to use me.
```
from PyExpansion.just_for_fun.PyDeadFish import main
```
This line is to use me (call library)

So, next step is:
```
c = main.DeadFish()
```

From here, I have two main function. <br>

- encode
- decode

### encode
Convert human-readable word to dead fish code

### decode
Convert dead fish to human-readable word

So, nex step is:

```
word = "Hello, world!"
print(c.encode(word))
```

Output will be:
```
iisiiiisiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiooiiiodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiioiiioddddddoddddddddodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo
```

Another one is decode:

```
dead_fish = "iiisdsiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiooiiiodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoddddddddddddodddddddddddddddddddddsddoddddddddoiiioddddddoddddddddodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo"
print(c.decode(word))
```

Output will be:
```
Hello, world!
```

That is all about me(Dead Fish). Hope you enjoy.<br>
Say ya.
