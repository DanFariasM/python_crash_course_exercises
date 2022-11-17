def make_shirt(size="large", text="I Love Python"):
    """Gets the size of the shirt and the printed message on it"""
    print(f'You are making a {size} shirt displaying "{text}".')

make_shirt()
make_shirt(size="medium")
make_shirt(text="Python is the best", size="small")