from PyExpansion.just_for_fun.PyDeadFish import main

c = main.DeadFish()
hello_world = "iiisdsiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiooiiiodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoddddddddddddodddddddddddddddddddddsddoddddddddoiiioddddddoddddddddodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo"
print("Decode for %s:" % hello_world)
c.decode(hello_world)
print()
hello_world2 = "Hello, World!"
print("Encode for %s:" % hello_world2)
print(c.encode(hello_world2))
