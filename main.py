import sys
import unicodedata
import csv


def txt_red(text):
    print(f'\033[91m{text}\033[0m')


def clean_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.category(c).startswith('C') and c != '\u200e'
    ).strip().lower()


person1 = input("Enter the name of the first person (Exactly as it appears on their WhatsApp profile): ")
person2 = input("Enter the name of the second person (Exactly as it appears on their WhatsApp profile): ")

code_person1 = clean_text(person1 + ":")
code_person2 = clean_text(person2 + ":")

banned_words = [code_person1, code_person2, "omitted", "audio", "sticker", "image", "a.m.]", "p.m.]"]
banned_words += clean_text(person1).split() + clean_text(person2).split() + clean_text(code_person1).split() + clean_text(code_person2).split()

with open('ban.csv', mode='r', newline='', encoding='utf-8') as ban_archive:
    reader = csv.reader(ban_archive)

    for fila in reader:
        banned_words += [palabra.strip().strip('"') for palabra in fila]

print()
print("Do you want to omit a word?")
print("Add all the words you want to omit (one per line), and when you don’t want to add more words, just type 0")
while True:
    word_to_omit = input("Word to omit: ")
    if word_to_omit != "0":
        banned_words.append(word_to_omit)
    else:
        break


try:
    with open("chat.txt", "r", encoding="utf-8") as archive:
        archive_lines = archive.readlines()
except FileNotFoundError:
    txt_red("The file 'chat.txt' was not found. Please make sure it exists in the same directory.")
    sys.exit()


person1_count = 0
person2_count = 0
message_am = 0
message_pm = 0
message_sticker = 0
message_audio = 0
message_image = 0
word_counts = {}

for line in archive_lines:
    clean_line = clean_text(line)

    if code_person1 in clean_line:
        person1_count += 1
    elif code_person2 in clean_line:
        person2_count += 1

    if "a.m.]" in line:
        message_am += 1
    elif "p.m.]" in line:
        message_pm += 1
    if "sticker omitted" in line:
        message_sticker += 1
    if "audio omitted" in line:
        message_audio += 1
    if "image omitted" in line:
        message_image += 1

    for word in clean_line.split():
        if word not in banned_words:
            word_counts[word] = word_counts.get(word, 0) + 1

most_used_word = max(word_counts, key=word_counts.get, default="null")
most_used_word_count = word_counts.get(most_used_word, 0)

if message_am > message_pm:
    messages_time = message_am
    messages_print = f"You text more in the morning with {messages_time} messages."
else:
    messages_time = message_pm
    messages_print = f"You text more in the afternoon with {messages_time} messages."

print()
print("- - -")
print(
    f"The most messages sender was {person1 if person1_count > person2_count else person2} with {max(person1_count, person2_count)} messages in total.")
print(f"The most used word in the chat was '{most_used_word}' with {most_used_word_count} uses.")
print(f"There are {message_sticker} stickers, {message_audio} audios, and {message_image} images.")
print(messages_print)
print("- - -")