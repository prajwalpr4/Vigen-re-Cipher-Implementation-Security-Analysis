# Vigenere Cipher - Implementation & Security Analysis

This project is a pure-Python implementation of the Vigenere cipher with a small command-line interface, Caesar cipher comparison, letter frequency analysis, file encryption, and self-tests.

## Overview

The Vigenere cipher is a classical polyalphabetic substitution cipher. Unlike a Caesar cipher, it uses a repeating keyword so the same plaintext letter can encrypt to different ciphertext letters depending on position.

This repository is intended for educational and analytical use. It demonstrates both how the cipher works and why it is not secure by modern standards.

## Features

- Vigenere encryption and decryption
- Caesar cipher comparison
- Letter frequency analysis
- File encryption and decryption
- Built-in self-tests
- Interactive menu-driven CLI

## Project Structure

- vigenere_project.py: main implementation and CLI
- README.md: project documentation

## Requirements

- Python 3.6 or later

No third-party packages are required.

## Installation

```bash
git clone https://github.com/prajwalpr4/Vigen-re-Cipher-Implementation-Security-Analysis.git
cd Vigen-re-Cipher-Implementation-Security-Analysis
python vigenere_project.py
```

## Usage

Run the script and choose an option from the menu:

```text
1. Encrypt a message (Vigenere)
2. Decrypt a message (Vigenere)
3. Encrypt with Caesar cipher (comparison)
4. Run full demonstration + frequency analysis
5. Encrypt a text file
6. Decrypt a text file
7. Run self-tests (verify correctness)
8. Exit
```

### Example

```text
Plaintext : ATTACKATDAWN
Key       : LEMON
Ciphertext: LXFOPVEFRNHR
```

## How It Works

For each alphabetic character, the script converts letters to values in the range 0-25 and applies the Vigenere formula:

```text
Encryption: C = (P + K) mod 26
Decryption: P = (C - K) mod 26
```

Spaces, punctuation, and digits are preserved unchanged. The key advances only when an alphabetic character is processed.

## Security Analysis

### Strengths

- More resistant to simple frequency analysis than a Caesar cipher
- Uses a repeating keyword, which creates multiple substitution patterns
- Demonstrates the historical advantage of polyalphabetic ciphers over monoalphabetic ones

### Weaknesses

- Vulnerable to Kasiski examination and key-length discovery
- Once the key length is known, it reduces to several Caesar ciphers
- Provides confidentiality only, not integrity or authentication
- Not suitable for real-world security

## Verification

The script includes self-tests for standard cases such as:

- ATTACKATDAWN with key LEMON -> LXFOPVEFRNHR
- HELLO with key KEY -> RIJVS

Run option 7 in the menu to verify the implementation.

## License

No license file is included by default. Add one if you want to distribute or reuse the project under specific terms.