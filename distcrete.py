# The most popular mathematician in the world is throwing a party for all of his friends. As a way to kick things off, 
#they decide that everyone should shake hands. Assuming all 10 people at the party each shake hands with every other person (but not themselves, 
#obviously) exactly once, how many handshakes take place?


def calculate_handshakes(n):
    total_handshakes = 0

    # Loop through each person
    for i in range(n):
        # Each person shakes hands with every person after them
        for j in range(i + 1, n):
            total_handshakes += 1

    return total_handshakes


# Number of people at the party
num_people = 10


def calculate_handshakes(n):
    # Calculate the number of unique handshakes using the combination formula C(n, 2)
    handshakes = n * (n - 1) // 2
    return handshakes


# Number of people at the party
num_people = 10

# Calculate the total number of handshakes
total_handshakes = calculate_handshakes(num_people)
print(f"Total number of handshakes: {total_handshakes}")

# Calculate the total number of handshakes
total_handshakes = calculate_handshakes(num_people)
print(f"Total number of handshakes: {total_handshakes}")


# At the warm-up event for Oscar's All Star Hot Dog Eating Contest, Al ate one hot dog. Bob then showed him up by eating three hot dogs.
# Not to be outdone, Carl ate five. This continued with each contestant eating two more hot dogs than the previous contestant. 
# How many hot dogs did Zeno (the 26th and final contestant) eat? How many hot dogs were eaten all together?


def hot_dog_eating_contest(num_contestants):
    # Calculate the number of hot dogs Zeno ate
    zeno_hot_dogs = 2 * num_contestants - 1

    # Calculate the total number of hot dogs eaten by all contestants
    total_hot_dogs = num_contestants * (2 * 1 + (num_contestants - 1) * 2) // 2

    return zeno_hot_dogs, total_hot_dogs


# Number of contestants (26 in this case)
num_contestants = 26

# Calculate results
zeno_hot_dogs, total_hot_dogs = hot_dog_eating_contest(num_contestants)

# Print results
print(f"Hot dogs eaten by Zeno: {zeno_hot_dogs}")
print(f"Total hot dogs eaten by all contestants: {total_hot_dogs}")


def hotDog(eaters):
    # Initialize the first contestant's hot dog count
    first_hot_dogs = 1

    # Initialize the total count of hot dogs
    total_hot_dogs = 0

    # Loop through each contestant
    for i in range(eaters):
        # Calculate the number of hot dogs for the current contestant
        hot_dogs = first_hot_dogs + 2 * i

        # Add the current contestant's hot dogs to the total count
        total_hot_dogs += hot_dogs

        # If this is the last contestant, print the number of hot dogs they ate
        if i == eaters - 1:
            print(
                f"Number of hot dogs eaten by the {i + 1}th contestant (Zeno): {hot_dogs}")

    # Return the total number of hot dogs eaten by all contestants
    return total_hot_dogs


# Number of contestants
num_contestants = 26

# Calculate the total number of hot dogs eaten
total_hot_dogs = hotDog(num_contestants)
print(f"Total number of hot dogs eaten by all contestants: {total_hot_dogs}")
