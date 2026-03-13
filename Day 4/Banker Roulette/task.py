import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
random_friend = random.choice(friends)
print(random_friend)

# option 2
random_friend = random.randint(0, len(friends) - 1  )
print(friends[random_friend])

