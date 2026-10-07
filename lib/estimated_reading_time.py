def estimate(text):
    if text == "":
        raise Exception ("Can't estimate time for empty text")
    words = len(text.split(" "))
    time = words/200
    return f"{time} minutes"