import time
import random
import threading

# Planet data: description and name
PLANETS = {
    "Mercury": "The smallest and closest planet to the Sun. It has a rocky surface and no atmosphere.",
    "Venus": "Often called Earth's twin. It has a thick atmosphere of CO2 and sulfuric acid clouds.",
    "Earth": "The only planet known to support life. It has oceans, air, and a protective magnetic field.",
    "Mars": "Known as the Red Planet, it has the tallest volcano and signs of ancient water.",
    "Jupiter": "The largest planet with a giant red storm and dozens of moons.",
    "Saturn": "Famous for its stunning ring system and many moons.",
    "Uranus": "A gas giant that spins on its side. It has a bluish tint due to methane.",
    "Neptune": "The farthest known planet, dark and cold with strong winds and a deep blue color.",
}

# Encrypted word list
ENCRYPT_WORDS = ["orbit", "galaxy", "sunshine", "gravity", "comet", "asteroid", "nova", "eclipse"]

# Caesar Cipher encryption
def caesar_cipher(word, shift=3):
    encrypted = ''
    for char in word:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# Input with timeout
def timed_input(prompt, timeout=20):
    print(prompt, end=': ', flush=True)
    answer = [None]

    def get_input():
        answer[0] = input()

    t = threading.Thread(target=get_input)
    t.daemon = True
    t.start()
    t.join(timeout)
    if t.is_alive():
        print("\n⏰ Time's up!")
    return answer[0]

def main():
    guessed_planets = set()
    incorrect_guesses = 0
    encrypted_message = []

    print("🚀 Welcome to 'Knowing your Solar System'!\n")
    print("Guess the planet from the clue. You have 10 seconds to answer each!\n")

    all_planets = list(PLANETS.keys())
    random.shuffle(all_planets)

    for planet in all_planets:
        if incorrect_guesses >= 3:
            print("\n❌ You’ve made 3 incorrect guesses. Game over!")
            print("🔐 The encrypted message was:", ''.join(encrypted_message))
            decrypted = ''.join(caesar_cipher(word, -3) for word in encrypted_message)
            print("🔓 Decrypted message:", decrypted)
            return

        desc = PLANETS[planet]
        print("🌍 Description:", desc)
        guess = timed_input("👉 Your guess", 10)
        
        if guess is None:
            print("❌ No answer provided!")
            incorrect_guesses += 1
            encrypted_message.append(caesar_cipher(random.choice(ENCRYPT_WORDS)))
        elif guess.strip().lower() == planet.lower():
            print("✅ Correct!")
            guessed_planets.add(planet)
            encrypted_message.append(caesar_cipher(random.choice(ENCRYPT_WORDS)))
        else:
            print(f"❌ Wrong! The correct answer was {planet}")
            incorrect_guesses += 1
            encrypted_message.append(caesar_cipher(random.choice(ENCRYPT_WORDS)))

        print(f"Progress: {len(guessed_planets)}/8 planets guessed correctly.\n")

    # All planets guessed
    print("🎉 You've guessed all planets!")
    encrypted = ''.join(encrypted_message)
    print("🔐 Your encrypted message is:", encrypted)
    decrypted_guess = input("🧠 What do you think the decrypted message is? ").strip()
    actual_decryption = ''.join(caesar_cipher(word, -3) for word in encrypted_message)
    if decrypted_guess.lower() == actual_decryption.lower():
        print("🎊 Correct! You're a true space genius!")
    else:
        print("🤖 Not quite! The actual decrypted message was:", actual_decryption)

if __name__ == "__main__":
    main()
