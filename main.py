import sys
import unicodedata

def txt_red(text):
    print(f'\033[91m{text}\033[0m')

def clean_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.category(c).startswith('C')
    ).strip().lower()

person1 = input("Enter the name of the first person (Exactly as it appears on their WhatsApp profile): ")
person2 = input("Enter the name of the second person (Exactly as it appears on their WhatsApp profile): ")

code_person1 = clean_text(person1 + ":")
code_person2 = clean_text(person2 + ":")


try:
    with open("chat.txt", "r", encoding="utf-8") as archive:
        archive_content = archive.read()
except FileNotFoundError:
    txt_red("The file 'chat.txt' was not found. Please make sure it exists in the same directory.")
    sys.exit()

archive_words = [clean_text(word) for word in archive_content.split()]


person1_inChat = archive_words.count(code_person1)
person2_inChat = archive_words.count(code_person2)

if person1_inChat > 1:
    pass
else:
    txt_red(f"{person1} is not in the chat")
    sys.exit()

if person2_inChat > 1:
    pass
else:
    txt_red(f"{person2} is not in the chat")
    sys.exit()

if person1_inChat > person2_inChat:
    mostMessageBy = person1
    mostMessageBy_count = person1_inChat
else:
    mostMessageBy = person2
    mostMessageBy_count = person2_inChat

# most used word
muw_a = "null"
muw_b = 0

print()
print("If the user has another name, add them here")
print("For example, if the user is called Sergio Perez, and you already wrote 'Perez', you should write 'Sergio' now.")
print("To stop adding names, just write 0.")
print("")

banned_words = [code_person1, code_person2, "omitted", "audio", "sticker"]

banned_words = [clean_text(word) for word in banned_words]

while True:
    banned_wordsAdd = input("Write a name: ")
    if banned_wordsAdd != "0":
        banned_words.append(clean_text(banned_wordsAdd))
    else:
        print("Wait until the program reads all messages...")
        break

message_am = 0
message_pm = 0
# tambien checar cuantos stickers y audios se mandaron
for each_word in archive_words:
    if each_word in banned_words:
        pass
    elif each_word == "a.m.]":
        message_am += 1
    elif each_word == "p.m.]":
        message_pm += 1
    else:
        muw_c = archive_words.count(each_word)
        if muw_c > muw_b:
            muw_a = each_word
            muw_b = muw_c

# check what time are most likely to get a message
if message_am > message_pm:
    messages_time = message_am
    messages_print = f"You text more in the morning with {messages_time} messages"
else:
    messages_time = message_pm
    messages_print = f"You text more in the afternoon with {messages_time} messages"

print()
print("- - -")
print(f"The most messages sender was {mostMessageBy} with {mostMessageBy_count} messages in total.")
print(f"The most used word in the chat was '{muw_a}' with {muw_b} uses.")
print(messages_print)
print("- - -")