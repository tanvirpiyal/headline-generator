import random

# Subjects
subjects = [
    "DJ Alok", "Chrono", "Kelly", "Hayato", "Moco",
    "Wukong", "Dimitri", "Skyler", "K", "Tatsuya"
]

# Actions with style tags
actions = [
    ("throws a healing party while enemies panic", "funny"),
    ("declares war on campers inside his shield", "angry"),
    ("outruns danger like it’s a race final", "serious"),
    ("unleashes revenge after losing HP", "angry"),
    ("hacks enemies and exposes their secrets", "serious"),
    ("trolls enemies by turning into a bush", "funny"),
    ("orders a comeback concert in the battlefield", "funny"),
    ("blasts gloo walls like a rockstar attack", "angry"),
    ("teaches survival lessons under pressure", "serious"),
    ("dashes into chaos without fear", "serious")
]

# Places
places_or_things = [
    "at Red Fort", "in Mumbai local train", "a plate of samosa", "inside parliament",
    "on top of skyscraper in Free Fire", "under the Gloo Wall", "inside a loot crate",
    "at Dhaka Metro bus", "on a rickshaw in Narail", "next to a coconut vendor",
    "at KFC counter waiting for burger", "on the roof of a burning building",
    "inside an abandoned warehouse", "on a floating boat in Buriganga",
    "at the playground near school", "inside a Free Fire bunker",
    "at Cox's Bazar beach with loot", "holding a plate of pitha",
    "behind the enemy sniper", "at a crowded Eid market"
]

# Emoji mapping
emoji_map = {
    "funny": "😄",
    "angry": "😤",
    "serious": "🧐"
}

# Ask user how many headlines
num_headlines = int(input("How many headlines do you want to generate? "))

for i in range(num_headlines):
    user_input = input("\nDo you want a headline? (yes/no) ").lower()

    if user_input == "yes":
        subject_choice = random.choice(subjects)
        action_choice, style = random.choice(actions)
        place_choice = random.choice(places_or_things)
        emoji = emoji_map.get(style, "")
        
        headline = f"HEADLINE:- {subject_choice} {action_choice} {place_choice} {emoji}"
        print("\n", headline)

    elif user_input == "no":
        print("Thank you for using me!")
        break

    else:
        print("Invalid input! Please type 'yes' or 'no'.")
