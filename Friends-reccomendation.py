import json
def read_file(filename):
       with open(filename,"r") as file:
              return json.load(file)
data=read_file("network.json")

def friend_recommendation(user_id, data):
    user_friends = {}

    # Build dictionary of users and their friends
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])

    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    suggestions = {}

    # Find mutual friends
    for friend in direct_friends:
        for mutual in user_friends.get(friend, []):
            if mutual != user_id and mutual not in direct_friends:
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    # Sort by number of mutual friends
    sorted_suggestions = sorted(
        suggestions.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [uid for uid, _ in sorted_suggestions]
# Load data
data = read_file("network.json")
user_id = 50
recommendations = friend_recommendation(user_id, data)

print(f"People You May Know for User {user_id}: {recommendations}")