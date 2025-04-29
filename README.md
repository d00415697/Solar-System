# Solar-System# 🌌 Knowing Your Solar System 🪐

**Knowing Your Solar System** is a fun and educational mini game designed to test your knowledge of the planets in our solar system. The player is given mysterious descriptions of planets and must guess which planet is being described — all within a strict 10-second window! With every correct or incorrect answer, the game builds a secret encrypted message you’ll need to decipher by the end — if you survive long enough!

---

## 🎯 Objective

Correctly identify all 8 planets of the solar system based on short descriptive clues. Each correct guess earns you a hidden "code word" — encrypted using Caesar Cipher. Fail three times, and the game ends with your encrypted message revealed but not solved.

If you guess all planets right, you must try to **decrypt the final message** to win the game!

---

## 🕹️ How to Play

1. **Start the Game**:
   - Run the script:  
     ```bash
     python Solar_System.py
     ```

2. **Game Flow**:
   - You'll be shown a random description of a planet.
   - You have **10 seconds** to input your guess.
   - If you're **correct**, a secret encrypted word is added to the final message.
   - If you're **incorrect**, a different encrypted word is still added, and you lose one life.
   - You get up to **3 incorrect guesses**. After that, the game ends.

3. **Winning**:
   - Guess **all 8 planets correctly** before making 3 mistakes.
   - Then, you'll be shown the full encrypted message.
   - You'll be asked to **decrypt** it manually.

4. **Losing**:
   - If you make **3 incorrect guesses**, the game ends.
   - You'll still see the decrypted message, but you won’t get a chance to solve it.

---

## 🔐 Encryption Mechanism

This game uses a **Caesar Cipher (Shift +3)** for encrypting words.

- Example:
  - Plain text: `orbit`
  - Encrypted: `ruelw`

When decrypting, the game shifts characters **backward by 3**.

---

## 📂 Project Structure

```plaintext
.
├── Solar_System.py   # Main game file
└── README.md         # Game instructions and documentation
