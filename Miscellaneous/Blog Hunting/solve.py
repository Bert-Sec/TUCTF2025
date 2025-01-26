from itertools import permutations, combinations

books = [
    "RappacinnisDaughter",
    "TheSphinx",
    "Sphinx",
    "Expanse",
    "TheExpanse",
    "Stormlight",
    "Archive",
    "StormlightArchive",
    "TheStormlightArchive",
    "1984",
    "American",
    "Prometheus",
    "AmericanPrometheus"
]

years = {"2019", "2024"}
dog = "Hash"

passwords = open('passwords.txt', 'w')

with open("passwords.txt", "w") as passwords:
    for book in books:
        for year in years:
            items = [book, dog, year]
            for perm in list(permutations(items)):
                password = ''.join(perm)
                passwords.write(password + '\n')
                passwords.write(password.upper() + '\n')
                passwords.write(password.lower() + '\n')
