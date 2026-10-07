def is_Initial_letter_capital(text):
    if text.strip()[0] == text.strip()[0].upper():
        return True
    else:
        return False

def is_end_punctuation_mark_present(text):
    if text.strip()[-1] == "." or text.strip()[-1] == "!" or text.strip()[-1] == "?":
        return True
    else:
        return False


def verify_grammar(text):
    if text == "" or text.isspace():
        raise Exception("Grammar can't be verified with an empty string")
    elif is_Initial_letter_capital(text) and is_end_punctuation_mark_present(text):
        return True 
    else:
        return False

