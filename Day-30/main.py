# FilesNotFound
# with open("a_file.txt") as file:
#       file.read()

# KeyError
# a dictionary = {"key" : "value" }
# value = a_dictionary["non_existent_key]

# Index error
# fruit_list = ["apple", "banana", "Pear"]
# fruit = fruit[3]

# TypeError
# Text = "abc"
# print(text + 5)
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["Pradeep"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Pradeep")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")
#
# height = folat(input("Enter Height : "))
# weight = int(input("Enter Weight : "))
#
# bmi = weight / (height ** 2)
# print(bmi)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    try:
        total_likes = 0
        for post in posts:
            total_likes = total_likes + post['Likes']

        return total_likes
    except KeyError:
        print("No posts found")


count_likes(facebook_posts)


