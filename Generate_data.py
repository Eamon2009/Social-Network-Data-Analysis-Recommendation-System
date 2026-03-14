import json
import random

NUM_USERS = 500
NUM_PAGES = 150

names = [
"Amit","Priya","Rahul","Sara","Neha","Vikram","Kunal","Anjali","Ravi","Sneha",
"Arjun","Meera","Kabir","Tanya","Varun","Rhea","Ishan","Simran","Pooja","Yash",
"Ananya","Dev","Aditi","Rohan","Nisha","Gautam","Kriti","Harsh","Naveen","Ishita"
]

page_topics = [
"Python Developers","Data Science Enthusiasts","AI & ML Community","Web Dev Hub",
"Blockchain Innovators","Cybersecurity Experts","Cloud Computing Pros",
"Competitive Programmers","Startup Founders","UI/UX Designers",
"Full-Stack Developers","Tech Entrepreneurs","IoT Enthusiasts","Game Developers",
"Big Data Analysts","DevOps Engineers","Cloud AI Researchers",
"5G & Edge Computing","AR/VR Creators","Freelance Coders",
"Open Source Contributors","Algorithmic Traders","Low-Code Developers",
"Cyber Ethics Forum","AI Ethics & Policy","Digital Nomads","Women in Tech"
]

# generate pages
pages = []
for i in range(1, NUM_PAGES + 1):
    pages.append({
        "id": 100 + i,
        "name": random.choice(page_topics) + f" {i}"
    })

# generate users
users = []

for i in range(1, NUM_USERS + 1):

    friend_count = random.randint(4, 8)
    friends = random.sample(range(1, NUM_USERS + 1), friend_count)

    if i in friends:
        friends.remove(i)

    liked_pages = random.sample(
        [page["id"] for page in pages],
        random.randint(1, 4)
    )

    users.append({
        "id": i,
        "name": random.choice(names) + f"_{i}",
        "friends": friends,
        "liked_pages": liked_pages
    })

data = {
    "users": users,
    "pages": pages
}

with open("social_network_large.json", "w") as f:
    json.dump(data, f, indent=4)

print("Dataset generated successfully.")
