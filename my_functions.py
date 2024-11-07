def banner():
    """
    This is a docstring, this is what is shown when you use the help function
    """

    print("This is a warning")


def banner_with_return():
    x = "This is a warning"
    return x


def adder(a, b):
    """
    Please provide 2 values to add them
    """
    print(a + b)


def better_adder(*args):  # *accepts multiple args
    total = 0
    for n in args:
        total = total + n
    print(total)


def device_login(username, hostname, platform="cisco"):
    if platform == "cisco":
        print(f"ssh {username}@{hostname}")


def new_device_login(**kwargs):
    for k, v in kwargs.items():
        print(
            f"the keyword argument {k} has been passed to this function with value {v}"
        )


def cool_maths(a, b):  ## function that returns two valus in a tuple
    x = a + b
    y = a * b
    return x, y


if __name__ == "__main__":
    print("hello")
    help(adder)  ## this show the docstring
    print(adder.__doc__)  ## this also prints the docstring

    banner()
    x = banner()
    print(x)  # this return None
    x = banner_with_return()
    print(x)  # this returns z (string)

    adder(5, 9)
    adder("soleman", "zaghlool")
    device_login("szaghlool", "192.168.1.1", "cisco")
    device_login(
        hostname="1.1.1.1", username="szagh"
    )  # default platform value is cisco

    better_adder(10, 20, 30, 40, 50, 60, 70)
    new_device_login(
        user="szagh", passwd=12345, hostname="192.168.1.1", ssh_enabled=True
    )

    x = cool_maths(2, 5)
    print(x)
    a, b = cool_maths(2, 5)
    print(a, b)

    ##using lambda
    adder_with_lambda = lambda x, y=10: x + y  # default value of y=10
    print(adder_with_lambda(2))
    print(adder_with_lambda(2, 20))

    over_under = lambda x: f"{x} is under age 10" if x < 10 else f"{x} is over 10"
    print(over_under(4))
    print(over_under(11))
