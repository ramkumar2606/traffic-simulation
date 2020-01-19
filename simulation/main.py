import sys

def interact_with_user(prompt):
    """
    This function is to interact with the user
    :return:
    """
    user_input = input(prompt)
    while True:
        if user_input == 'exit':
            print("Exiting Traffic Light Simulator. Goodbye!")
            sys.exit(0)
        elif outputtype == 'int' and user_input == 'forever':
            return 'forever'
        try:
            output = float(user_input)
            if output > 0:
                return output
            else:
                raise ValueError('Negative numbers are not allowed')
        except ValueError:
            print
            "Whoops! That's not right! Please try again."
            user_input = raw_input(prompt)


def main():
    print("################")
    print("Welcome to the Traffic Light Simulator!")
    print("If at any time you'd like to exit just type 'exit'")
    print("################")
    interact_with_user()

if __name__ == "__main__":
    main()