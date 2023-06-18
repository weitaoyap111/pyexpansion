from PyExpansion.common.data_type.lists import main

test_case_material = [
    {
        "list1": [1, 2, 3],
        "list2": [2, 2, 3],
    },
    {
        "list1": [1, 2, 3],
        "list2": [2, 2, 3, 5],
    },
]

for count, x in enumerate(test_case_material, start=1):
    print("Case %s: " % str(count), main.ListExpansion.compare_two_list_length(x["list1"], x["list2"]))
