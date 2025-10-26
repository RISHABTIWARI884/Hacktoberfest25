import random

nouns = ["wind", "moon", "mountain", "river", "flower", "snow"]
verbs = ["whispers", "flows", "shines", "falls", "dances"]
adjectives = ["silent", "bright", "gentle", "cold", "soft"]

def generate_haiku():
    line1 = f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}"
    line2 = f"{random.choice(nouns)} {random.choice(verbs)} {random.choice(adjectives)}"
    line3 = f"{random.choice(verbs)} {random.choice(nouns)} {random.choice(adjectives)}"
    return f"{line1}\n{line2}\n{line3}"

if __name__ == "__main__":
    print(generate_haiku())
