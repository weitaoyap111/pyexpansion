front_pattern = "A_PYIC_"

# common
correct_code = front_pattern + "200"
error_code_1 = front_pattern + "500_1"
error_code_2 = front_pattern + "500_2"
error_code_3 = front_pattern + "500_2"

# country
# Malaysia
error_code_M_1 = front_pattern + "500_M_1"

code_list = {
    correct_code: "Correct IC Format",
    error_code_1: "Country name is not found in the list",
    error_code_2: "Invalid IC Format",
    error_code_3: "IC length is not same as IC length of the country",

    error_code_M_1: "Invalid Date Format",
}
