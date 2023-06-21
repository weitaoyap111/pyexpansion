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
    {
        "country": "Singapore",
        "ic_word": "S1234567K",
        "test_condition": "Correct Case",
        "special": "",
    },
]

for count, x in enumerate(test_case_material, start=1):
    try:
        del test_case
    except NameError:
        pass
    print("Test Condition: ", x["test_condition"])
    test_case = main.PyIC(x["country"], x["ic_word"])
    print("Case %s (sample: %s): " % (str(count), x["ic_word"]), test_case.get_detail())
    print("Error Check Case %s: " % str(count), test_case.check_error())
    if x.get("special", ""):
        print("This function", x["special"])
    if x["country"] == "Singapore":
        print("Is Valid: ", main.Singapore.PyIC(x["ic_word"]).valid_ic())
    print("\n")
