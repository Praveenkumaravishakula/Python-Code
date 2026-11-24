"""Convert text emoticons in a message to emojis."""


def convert_emojis(message):
    """Replace :) and :( in the message with emojis."""
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
result = convert_emojis(message)
print(result)
