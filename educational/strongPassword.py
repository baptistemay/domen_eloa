
import re

#pattern
check_chr_length = re.compile(r'''(
.{8} #At least 8 characters
)''',re.VERBOSE | re.IGNORECASE)
check_cap = re.compile(r'''(
[A-Z]{1} #At least one cap
)''',re.VERBOSE)
check_min = re.compile(r'''(
[a-z]{1} #At least one min
)''',re.VERBOSE)
check_digit = re.compile(r'''(
\d{1} #At least one digit
)''',re.VERBOSE)

#input
your_password = ""
def _create_password():
    global your_password
    your_password = input("""
Set your password here
(It must contains at least :
- 8 characters.
- Both cases.
- One digit.) 
: """)
    checking_lenght = check_chr_length.search(your_password)
    checking_cap =check_cap.search(your_password)
    checking_digit = check_digit.search(your_password)
    checking_min = check_min.search(your_password)
    if checking_lenght == None:
        print("You password must be set with at least 8 characters.")
        _create_password()
        return True
    if checking_cap == None:
        print("Your password must be set with at least one cap.")
        _create_password()
        return True
    if checking_digit == None:
        print("Your password must be set with at least one digit.")
        _create_password()
        return True
    if checking_min == None:
        print("Your passwowrd must be set with at least one min character.")
        _create_password()
        return True


_create_password()
print("password registered")
masked_password = re.compile(r"(..)(.*)")
print(f"Your password is {masked_password.sub(r"\1***...", your_password)}")