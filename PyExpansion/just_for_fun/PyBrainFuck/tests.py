from PyExpansion.just_for_fun.PyBrainFuck import main

c = main.BrainFuck()
test_bf = ">++++++++[-<+++++++++>]<.>>+>-[+]++>++>+++[>[->+++<<+++>]<<]>-----.>->+++..+++.>-.<<+[>[+>+]>>]<--------------.>>.+++.------.--------.>+."
c.bf_to_word(test_bf, False)
word_bf = "".join(x for x in c.word_to_bf("I Love Brain Fuck", True))
print(word_bf)
