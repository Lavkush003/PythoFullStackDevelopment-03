

def rem(text):
    val = ["<", ">", "/"]
    for char in val:
        text = text.replace(char, "")
    return text
def remo(text,Val ):
    return text.replace(Val, "")
def doc_help():
    """
    This provides help.
    """
    print(__doc__)





