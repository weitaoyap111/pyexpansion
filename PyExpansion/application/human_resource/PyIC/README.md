Hi, I am PyIC

A library to extract to information from IC
Currently I only support on two country, Malaysia and Singapore

Let me teach you how to use me.
```
from PyExpansion.application.human_resource.PyIC import main
```
This line is to use me (call library)

So, next step is:
```
country = "Malaysia"
ic_word = "001112108790"
c = main.PyIC(country, ic_word)
```

From here, I have two main function. <br>

- get_detail
- check_error

### get_detail
Is to get the information from ic word

### check_error
Is to check the error if get_detail have error

So, nex step is:

```
print(c.get_detail())
```

Output will be:
```
{'birthday': datetime.date(2000, 11, 12), 'states': 'Selangor', 'gender': 'Female', 'error': False}
```

Another one is check_error:

```
print(c.check_error())
```

Output will be:
```
{'Correct Code': 'A_PYIC_200'}
```

That is all about me(PyIC). Hope you enjoy.<br>
Say ya.
