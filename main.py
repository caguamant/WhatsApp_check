# fix the two names issue

import sys

def txt_red(text):
    print(f'\033[91m{text}\033[0m')

person1 = input("Enter the name of the first person (Exactly as it appears on their WhatsApp profile: ")
person2 = input("Enter the name of the second person (Exactly as it appears on their WhatsApp profile: ")

code_person1 = person1 + ":"
code_person2 = person2 + ":"



with open("chat.txt", "r", encoding="utf-8") as archive:
    archive_content = archive.read()

archive_words = archive_content.split()

# check if person1 and person2 are in the chat
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