def inverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def check_length(text):
    return len(text)

def delete_spaces(text):
    return text.replace(" ", "")
