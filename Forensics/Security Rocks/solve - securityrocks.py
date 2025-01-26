import hashlib

def find_collision(target_hash_prefix):
    with open("rockyou.txt", "r", errors="ignore") as file:
        for word in file:
            word = word.strip()
            if hashlib.md5(word.encode()).hexdigest().startswith(target_hash_prefix):
                print(f"Found collision: {word}")
                return word
    return None

target_hash_prefix = "c58360"
collision = find_collision(target_hash_prefix)
if collision:
    print(f"Collision: {collision}")
else:
    print("No collision found")
