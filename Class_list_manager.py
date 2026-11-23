# Class List Manager - Group 11
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Alhaton  (task 3)
def sort_names(names):
    return sorted(names)


# Written by: Alhaton  (task 6)
def to_upper(names):
    return [name.upper() for name in names]


# Written by: Farah (task 2)
def search_name(names, name):
    for n in names:
        if n == name:
            return True
    return False 


# Written by: Farah (task 5)
def names_starting_with(names, letter):
    result = []
    for name in names:
        if name.startswith(letter):
            result.append(name)
    return result


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))
    print("Upper names:", to_upper(names))
    print("Is Reem in the list?", search_name(names, "Reem"))
    print("Names starting with L:", names_starting_with(names, "L"))


main()


# Written by: Leen (Task 1)
def count_names(names):
    return len(names)

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))

main()



# Written by: Leen (Task 7)
def count_vowels(name):
    count = 0
    for letter in name.lower():
        if letter in "aeiou":
            count += 1
    return count

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of vowels:", count_vowels(names[0]))

main()

