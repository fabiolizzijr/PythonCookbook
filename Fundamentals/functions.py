def greet_user():
    """ () -> print()

    Print Hello\nWelcome in the terminal

    >>> greet_user()
    Hello
    Welcome
    """
    print("Hello")
    print("Welcome")

def greet_user_by_name(name="user", greeting="Welcome"):
    """ (str,str) -> print(str, str)
    Print greeting message with the parameters given

    >>> greet_user_by_name()
    Welcome user
    >>> greet_user_by_name("Fabio")
    Welcome Fabio
    >>> greet_user_by_name("Mario P B", "Seja bem vindo!")
    Seja bem vindo! Mario P B

    """
    print(f"{greeting} {name}")

greet_user()

greet_user_by_name()
greet_user_by_name("Fabio")
greet_user_by_name("Mario P B", "Seja bem vindo!")
greet_user_by_name(input("Whats your name? "))

