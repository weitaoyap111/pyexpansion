from PyExpansion.application.PyIC import main

test_case_material = [
    {
       "country": "M",
       "ic_word": "123456478",
       "test_condition": "Invalid Country",
       "special": "",
    },
    {
       "country": "Malaysia",
       "ic_word": "001112108790",
       "test_condition": "Correct Case",
       "special": "",
    },
    {
       "country": "Malaysia",
       "ic_word": "00111108790",
       "test_condition": "IC length is not correct",
       "special": "only apply to the country that have ic length validation",
    },
    {
       "country": "Malaysia",
       "ic_word": "001112-108790",
       "test_condition": "Format IC Invalid",
       "special": "only apply to the country that have ic pattern validation",
    },
    {
        "country": "Malaysia",
        "ic_word": "001512108790",
        "test_condition": "Format Date Invalid",
        "special": "only apply to the country that have date validation",
    },
]

for count, x in enumerate(test_case_material, start=1):
    try:
        del test_case
    except NameError:
        pass
    test_case = main.PyIC(x["country"], x["ic_word"])
    print("Case %s: " % str(count), test_case.get_detail())
    print("Error Check Case %s: " % str(count), test_case.check_error())
    if x["special"]:
        print("This function ", x["special"])
