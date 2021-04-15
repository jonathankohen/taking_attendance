from functions import cleanUp, spaces_bt_caps, startup, to_website
from example_data import students
import pprint
import pytesseract as p

try:
    from PIL import Image
except ImportError:
    import Image


pp = pprint.PrettyPrinter(indent=4).pprint


img = Image.open("./example_data/images/example.png")
new_size = tuple(2 * x for x in img.size)
img = img.resize(new_size, Image.ANTIALIAS)
print("    ")
print("-------- STRINGS FROM TEXT")
print("    ")
pp(p.image_to_string(img))

names = p.image_to_string(img).split()
print("    ")
print("-------- STRINGS TO LIST")
print("    ")
pp(names)

filtered = filter(cleanUp, names)
filtered = list(filtered)
print("    ")
print("-------- FILTERED LIST")
print("    ")
pp(list(filtered))

capitalized = [word.capitalize() for word in filtered]
print("    ")
print("-------- CAPITALIZED")
print("    ")
pp(capitalized)

namesCombined = [i + j for i, j in zip(capitalized[::2], capitalized[1::2])]
print("    ")
print("-------- FIRST AND LAST NAMES COMBINED")
print("    ")
pp(namesCombined)

newList = [spaces_bt_caps(i) for i in namesCombined]
print("    ")
print("-------- ADDED SPACES FIRST AND LAST")
print("    ")
pp(newList)

present_emails = []

for name in newList:
    for student in students:
        if name == student["name"]:
            present_emails.append(student["email"])

startup()

absent_emails = []

for student in students:
    if student["email"] not in present_emails:
        absent_emails.append(student["email"])


pp("    ")
pp("-------- PRESENT EMAILS")
pp("    ")
pp(present_emails)
pp("    ")
pp("-------- ABSENT EMAILS")
pp("    ")
pp(absent_emails)
pp("    ")
pp("-------- END")
pp("    ")

to_website(present_emails, absent_emails)
