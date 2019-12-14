#code
test_cases = int(input())
while test_cases:
    temporary_no = 0
    palindromic_number = int(input())
    validate_palindromic_number = palindromic_number
    while validate_palindromic_number:
        rem = validate_palindromic_number % 10
        temporary_no = temporary_no * 10 + rem
        validate_palindromic_number = int(validate_palindromic_number / 10)
    if temporary_no == palindromic_number:
        print("Yes")
    else:
        print("No")
    test_cases -= 1