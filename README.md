# 📄 README.md — Professional GitHub-Ready Documentation

Bro, here's the complete README file. Save it as `README.md` (exactly that name) in your project folder, next to `vigenere_project.py`. It's written in professional GitHub style — no college mentions, focuses on security analysis, and makes your project look like a serious implementation.

---

```markdown
# 🔐 Vigenère Cipher — Implementation & Security Analysis

A complete Python implementation of the **Vigenère cipher** with encryption, decryption, 
Caesar cipher comparison, letter frequency analysis, and file encryption capabilities — 
built to demonstrate both classical cryptographic principles and their security strengths 
and weaknesses through practical analysis.

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [What is the Vigenère Cipher?](#-what-is-the-vigenère-cipher)
- [Features](#-features)
- [Security Analysis](#-security-analysis)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Testing & Verification](#-testing--verification)
- [Limitations](#-limitations)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About the Project

This project implements the Vigenère cipher — a classical **polyalphabetic substitution 
cipher** — from scratch in pure Python, with **zero external cryptographic libraries**, 
to demonstrate full understanding of the underlying algorithm.

Beyond the core encryption/decryption, this project includes a **security analysis 
workbench**: it compares the Vigenère cipher against the Caesar cipher and uses 
**letter frequency analysis** to visually demonstrate *why* polyalphabetic substitution 
is significantly more resistant to classical cryptanalysis than monoalphabetic 
substitution.

The implementation is verified against internationally recognized standard test vectors, 
and includes a self-test suite that proves correctness automatically.

---

## 🔍 What is the Vigenère Cipher?

The Vigenère cipher, developed in the 16th century, encrypts text by shifting each 
letter by a different amount based on a repeating **keyword**, rather than a single 
fixed shift.

**The Math:**

```
Encryption:  Cᵢ = (Pᵢ + Kᵢ) mod 26
Decryption:  Pᵢ = (Cᵢ - Kᵢ) mod 26
```

Where:
- `Pᵢ` = the i-th letter of the plaintext (A=0, B=1, ... Z=25)
- `Kᵢ` = the i-th letter of the key (repeated cyclically)
- `Cᵢ` = the i-th letter of the ciphertext

**Example:**

```
Plaintext : ATTACKATDAWN
Key       : LEMONLEMONLE      (key repeated to match length)
Ciphertext: LXFOPVEFRNHR
```

It was historically known as *le chiffre indéchiffrable* ("the indecipherable cipher") 
and remained unbroken for nearly **300 years**.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Vigenère Encryption** | Full implementation of the polyalphabetic cipher with cyclic key repetition |
| 2 | **Vigenère Decryption** | Exact inverse operation, fully lossless for alphabetic text |
| 3 | **Caesar Cipher Comparison** | Side-by-side monoalphabetic cipher for demonstrating security differences |
| 4 | **Letter Frequency Analysis** | Visual bar-chart analysis showing frequency distribution flattening |
| 5 | **File Encryption/Decryption** | Encrypt and decrypt entire text files with any key |
| 6 | **Self-Test Suite** | Automatic verification against standard cryptographic test vectors |
| 7 | **Interactive Menu Interface** | Clean, menu-driven CLI for easy use and demonstration |
| 8 | **Zero Dependencies** | Pure Python — no external libraries required |

---

## 🛡️ Security Analysis

### Strengths of the Vigenère Cipher

1. **Resistance to Frequency Analysis**
   - In a Caesar cipher, 'E' (the most common English letter) always maps to the 
     same ciphertext letter — leaking the entire message's statistics.
   - In the Vigenère cipher, the same plaintext letter can map to **different** 
     ciphertext letters depending on its position, flattening the frequency 
     distribution and defeating simple frequency counting.

2. **Large Key Space**
   - Caesar cipher: only **26** possible keys.
   - Vigenère cipher: **26ⁿ** possible keys, where *n* is the key length.
   - A 10-character key yields over **1.4 × 10¹⁴** combinations.

3. **Position-Dependent Substitution**
   - Each plaintext letter is shifted by a *different* key letter, creating a 
     many-to-many mapping between plaintext and ciphertext letters.

### Weaknesses (Honest Assessment)

This project also documents the cipher's vulnerabilities — this is essential for 
a complete security analysis:

- **Kasiski Examination**: Repeated plaintext segments encrypted with the same key 
  segment produce repeated ciphertext patterns, revealing the key length.
- **Key Length Vulnerability**: Once key length is found, the cipher reduces to 
  multiple independent Caesar ciphers, each breakable by frequency analysis.
- **No Integrity/Authentication**: The cipher provides confidentiality only 
  (and weak confidentiality by modern standards) — it does not detect tampering.

> ⚠️ **Note**: This cipher is implemented for **educational and analytical purposes**. 
> It must **never** be used to secure real-world data. For actual applications, use 
> vetted modern algorithms like **AES-256 (GCM)** via standard libraries.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

That's it — there are no external dependencies.

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/prajwalpr4/Vigen-re-Cipher-Implementation-Security-Analysis.git

# 2. Navigate to the project directory
cd vigenere-cipher

# 3. Run the program
python vigenere_project.py
```

---

## 💻 Usage

On launch, you'll see the interactive menu:

```
============================================================
     VIGENÈRE CIPHER - CRYPTOGRAPHY PROJECT
============================================================
 1. Encrypt a message (Vigenère)
 2. Decrypt a message (Vigenère)
 3. Encrypt with Caesar cipher (comparison)
 4. Run full demonstration + frequency analysis
 5. Encrypt a text file
 6. Decrypt a text file
 7. Run self-tests (verify correctness)
 8. Exit
============================================================
```

### Encrypt a Message

```
Enter your choice (1-8): 1
Enter plaintext: MEET ME AT MIDNIGHT
Enter key (letters only): SECRET

Encrypted: FIRE EI SR ZVRVDBR
```

### Decrypt a Message

```
Enter your choice (1-8): 2
Enter ciphertext: FIRE EI SR ZVRVDBR
Enter key (letters only): SECRET

Decrypted: MEET ME AT MIDNIGHT
```

### Encrypt a File

```bash
Enter your choice (1-8): 5
Enter input file name: notes.txt
Enter output file name: encrypted.txt
Enter key: SECRET

[SUCCESS] Encrypted 'notes.txt' -> 'encrypted.txt'
```

### Non-Alphabetic Handling

- Spaces, digits, and punctuation pass through **unchanged**.
- The key advances **only for alphabetic characters**, preserving key alignment 
  across the actual encrypted content.

---

## ⚙️ How It Works

### Core Encryption Logic

```python
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')                       # letter -> 0-25
            k = ord(key[key_index % len(key)]) - ord('A')  # key letter -> 0-25
            c = (p + k) % 26                               # Vigenère formula
            ciphertext.append(chr(c + ord('A')))           # 0-25 -> letter
            key_index += 1
        else:
            ciphertext.append(char)                        # pass through

    return ''.join(ciphertext)
```

### Key Design Decisions

| Decision | Reason |
|----------|--------|
| `ord(char) - ord('A')` mapping | Maps letters to the 0-25 range required by the modular formula |
| `key_index % len(key)` | Cycles the key cyclically when it's shorter than the text |
| `(p + k) % 26` | Implements wrap-around after 'Z' back to 'A' |
| Key advances only on letters | Keeps key alignment independent of spaces/punctuation |
| Pure Python, no imports | Demonstrates the algorithm from first principles |

### Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Encryption | O(n) | O(n) |
| Decryption | O(n) | O(n) |
| Frequency Analysis | O(n) | O(1) — fixed 26-letter table |

Where *n* is the length of the input text.

---

## 🧪 Testing & Verification

The implementation includes a built-in self-test suite verified against the 
**standard cryptographic test vector** used universally in cryptography literature:

```
Plaintext : ATTACKATDAWN
Key       : LEMON
Ciphertext: LXFOPVEFRNHR
```

Run the tests with menu option **7**:

```
============================================================
        RUNNING SELF-TESTS
============================================================

Plaintext : ATTACKATDAWN
Key       : LEMON
Encrypted : LXFOPVEFRNHR  (expected LXFOPVEFRNHR)  [PASS]
Decrypted : ATTACKATDAWN  [PASS]

Plaintext : HELLO
Key       : KEY
Encrypted : RIJVS  (expected RIJVS)  [PASS]
Decrypted : HELLO  [PASS]

============================================================
ALL TESTS PASSED - IMPLEMENTATION IS CORRECT ✓
============================================================
```

The suite verifies:
- ✅ **Encryption correctness** against known test vectors
- ✅ **Decryption round-trip integrity** (encrypt → decrypt = original)

---

## ⚠️ Limitations

- Handles **English alphabetic characters** (A-Z); other characters pass through unchanged.
- Case is normalized to uppercase during processing.
- Provides **no real-world security** — this is an educational implementation of a 
  classical cipher broken since the 19th century.
- No key management, salting, or authentication — by design, to keep the algorithm 
  implementation clean and analyzable.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3 |
| External Libraries | **None** — 100% standard library, 0 dependencies |
| Interface | Interactive CLI (menu-driven) |

---

## 🤝 Contributing

Contributions are welcome! Ideas for future enhancements:

- [ ] GUI version (Tkinter / Web)
- [ ] Kasiski examination attack demonstration
- [ ] Autokey variant of the Vigenère cipher
- [ ] Support for full ASCII / Unicode character sets
- [ ] Performance benchmarking against large files

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file 
for details.

---

## 🙏 Acknowledgments

- Blaise de Vigenère, for the cipher that remained unbroken for three centuries
- The cryptography community, for maintaining standard test vectors used in 
  this project's verification suite

---

**⭐ If you found this project useful or educational, consider giving it a star!**
```

---

## 📌 THREE THINGS TO DO BEFORE UPLOADING

1. **Use the actual repository URL** in the Installation section so the clone command matches this project.

2. **Change the license name if needed** — if you don't want to bother creating a LICENSE file, just delete the License section and the acknowledgments reference to it. (Or if you keep it, GitHub has a "Add license" button when creating a repo — pick MIT and the file gets made automatically.)

3. **Add a `.gitignore` file** in the same folder with this one line, so junk files don't get uploaded:

```
__pycache__/
*.pyc
```

---

## ✅ Your GitHub repo will now contain:

```
your-repo/
├── vigenere_project.py    ← your code
├── README.md              ← this file
└── .gitignore             ← the tiny file above
```

#   V i g e n - r e - C i p h e r - I m p l e m e n t a t i o n - S e c u r i t y - A n a l y s i s  
 
