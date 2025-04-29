from random import *

occupation = [
    "Frontend dasturchi",
    "Backend dasturchi",
    "Freelancer",
    "Mobil dasturchi",
    "Dizayner"
]
people = [
    "Sulaymon",
    "Jasurbek",
    "Qadamboy",
    "Javohir",
    "Gulnoza"
]


for i in people:
    random1 = choice(people)
    random2 = choice(occupation)
    print(f"{random1}ning kasbi {random2}")
    continue