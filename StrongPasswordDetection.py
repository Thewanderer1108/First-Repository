import re


def get_password(p_regex):
    while True:
        p_strength = input("Please enter your password: ")
        trial = p_regex.search(p_strength)
        if len(p_strength) >= 8:
            if trial:
                print('Your password "{}" is strong'.format(p_strength))
                break
            else:
                print("Weak password, please try again.\nPassword should have 2 Upper Case letters,")
                print("3 Lower case letters and at least 1 special\ncharacter and at least 1 number")
        else:
            print("Your password should have at least 8 characters.\nPlease try again.")


def check_password_strength():
    """
        1.(?=.*[A-Z]{2}) -> indicates that the password string should contain at least 2 Uppercase letters.
        2.(?=.*[a-z]{3}) -> indicates that the password string should contain at least 3 Lowercase letters.
        3.(?=.*[/!@#$%^&_*+'\"-?.:;<>,]) -> indicates that the password string should contain at least 1 special
        character
        4.(?=.*[0-9]) -> indicates that the password string should contain at least 1 number.
        5. .{8,} -> indicates that the password length should be at least 8 characters.

        Note: ^, $ and .{8,} is not compulsory as long as we used the VERBOSE method of Regex
        which in turn rids us of using the ^ -> that indicates the start of the line and $ -> that indicates
        the end of the line. Lastly, the .{8,} is not that important as long as we are putting in an if statement
        that checks the length of the password string entered by the user. Implemented in the get_password() fn.
    """

    password_regex = re.compile(r'''(
        (?=.*[A-Z]{2})
        (?=.*[a-z]{3})
        (?=.*[/!@#$%^&_*+'\"-?.:;<>,])
        (?=.*[0-9])
        .{8,}
        )''', re.VERBOSE)

    get_password(password_regex)


if __name__ == "__main__":
    check_password_strength()
