import json

def load_data(filename):
       with open(filename,"r") as f:
              data=json.load(f)
       return data
data=load_data("data.json")
def display_users(data):
    print("Users and Their Connections:\n")
    for user in data["users"]:
        print(f"{user['name']} (ID: {user['id']}) - Friends: {user['friends']} - Liked Pages: {user['liked_pages']}")
    print("\nPages:\n")
    for page in data["pages"]:
        print(f"{page['id']}: {page['name']}")
 
# Load and display the data
data = load_data("data.json")
display_users(data)