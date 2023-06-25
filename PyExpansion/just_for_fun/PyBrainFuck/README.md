Hi, I am PyBrainFuck

A library to convert brainfuck to word or vice versa.

Let me teach you how to use me.
```
from PyExpansion.just_for_fun.PyBrainFuck import main
```
This line is to use me (call library)

So, next step is:
```
c = main.BrainFuck()
```

From here, I have two main function. <br>

- bf_to_word
- word_to_bf

<strike>bf in here not mean boyfriend</strike>

### bf_to_word
Convert brainfuck word to human-readable word

### word_to_bf
Convert human-readable word to brainfuck word

So, nex step is:

```
bf_word = ">++++++++[-<+++++++++>]<.>>+>-[+]++>++>+++[>[->+++<<+++>]<<]>-----.>->+++..+++.>-.<<+[>[+>+]>>]<--------------.>>.+++.------.--------.>+."
c.bf_to_word(bf_word)
```

Output will be:
```
Hello World!
```

Another one is word_to_bf:

```
word_bf = "".join(x for x in c.word_to_bf("I Love Brain Fuck", True))
print(word_bf)
```

Output will be:
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.-----------------------------------------.++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++.+++++++.-----------------.---------------------------------------------------------------------.++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++.-----------------.++++++++.+++++.------------------------------------------------------------------------------.++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++.------------------.++++++++.
```

That is all about me(BrainFuck). Hope you enjoy.<br>
Say ya.
