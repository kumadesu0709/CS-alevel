def hashtag_generator(string):
    string = "#" + string.title()
    string.replace(" ", "")
    if len(string) > 140:
        return False
    else:
        return string



