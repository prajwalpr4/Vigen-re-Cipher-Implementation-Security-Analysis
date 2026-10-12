"""
====================================================================
 PROJECT      : Vigenère Cipher Implementation with Security Analysis
 SUBJECT      : Cryptography & Network Security (CNS) 
 FILE NAME    : vigenere_project.py
 DESCRIPTION  : Complete implementation of Vigenère cipher with
                encryption, decryption, Caesar cipher comparison,
                and frequency analysis demonstration.
====================================================================
"""

# ------------------------------------------------------------------
# 1. VIGENÈRE CIPHER - CORE FUNCTIONS
# ------------------------------------------------------------------

def vigenere_encrypt(plaintext, key):
    """Encrypts plaintext using the Vigenère cipher.
       Formula: C = (P + K) mod 26"""
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')                      # letter -> 0-25
            k = ord(key[key_index % len(key)]) - ord('A') # key letter -> 0-25
            c = (p + k) % 26                              # Vigenère formula
            ciphertext.append(chr(c + ord('A')))          # 0-25 -> letter
            key_index += 1
        else:
            ciphertext.append(char)   # spaces/digits pass through unchanged

    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext, key):
    """Decrypts ciphertext using the Vigenère cipher.
       Formula: P = (C - K) mod 26"""
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            p = (c - k) % 26                              # decryption formula
            plaintext.append(chr(p + ord('A')))
            key_index += 1
        else:
            plaintext.append(char)

    return ''.join(plaintext)


# ------------------------------------------------------------------
# 2. CAESAR CIPHER - FOR COMPARISON (Shows why Vigenère is better)
# ------------------------------------------------------------------

def caesar_encrypt(plaintext, shift):
    """Encrypts plaintext using simple Caesar cipher (fixed shift)."""
    result = []
    for char in plaintext.upper():
        if char.isalpha():
            c = (ord(char) - ord('A') + shift) % 26
            result.append(chr(c + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


def caesar_decrypt(ciphertext, shift):
    """Decrypts Caesar cipher."""
    result = []
    for char in ciphertext.upper():
        if char.isalpha():
            p = (ord(char) - ord('A') - shift) % 26
            result.append(chr(p + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


# ------------------------------------------------------------------
# 3. SECURITY ANALYSIS - FREQUENCY COUNT (The "Wow" Factor)
# ------------------------------------------------------------------

def letter_frequency(text):
    """Counts frequency of each letter (A-Z) in the text.
       Demonstrates that Caesar cipher preserves frequency patterns
       while Vigenère flattens them out."""
    text = text.upper()
    freq = {chr(i + ord('A')): 0 for i in range(26)}
    for char in text:
        if char.isalpha():
            freq[char] += 1
    return freq


def display_frequency(text, title):
    """Displays letter frequency as a simple text bar chart."""
    freq = letter_frequency(text)
    print(f"\n--- Letter Frequency of {title} ---")
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        count = freq[letter]
        bar = '#' * count
        if count > 0:
            print(f"  {letter}: {count:3d} {bar}")
    print()


# ------------------------------------------------------------------
# 4. DEMONSTRATION FUNCTION (For report screenshots / viva demo)
# ------------------------------------------------------------------

def run_demo():
    """Runs the standard textbook example + frequency comparison."""
    print("\n" + "=" * 60)
    print("        VIGENÈRE CIPHER DEMONSTRATION")
    print("=" * 60)

    plaintext = "ATTACKATDAWN"
    key = "LEMON"

    print(f"\nPlaintext  : {plaintext}")
    print(f"Key        : {key}")

    # Vigenère encryption
    encrypted = vigenere_encrypt(plaintext, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"\n[Vigenère]")
    print(f"  Encrypted: {encrypted}")     # Expected: LXFOPVEFRNHR
    print(f"  Decrypted: {decrypted}")     # Expected: ATTACKATDAWN

    # Caesar encryption (same plaintext, shift = 3)
    caesar_enc = caesar_encrypt(plaintext, 3)
    caesar_dec = caesar_decrypt(caesar_enc, 3)
    print(f"\n[Caesar - shift 3]")
    print(f"  Encrypted: {caesar_enc}")
    print(f"  Decrypted: {caesar_dec}")

    # Frequency analysis comparison on a longer text
    print("\n" + "-" * 60)
    print("FREQUENCY ANALYSIS COMPARISON")
    print("(Shows why Vigenère resists frequency analysis)")
    print("-" * 60)

    long_text = ("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG "
                 "AND RUNS ACROSS THE FIELD TO CATCH ANOTHER FOX "
                 "BECAUSE THE FIRST FOX WAS TOO SLOW FOR THE DOG")

    print(f"\nOriginal text : {long_text[:50]}...")

    caesar_text = caesar_encrypt(long_text, 5)
    vigenere_text = vigenere_encrypt(long_text, "SECRET")

    display_frequency(long_text,      "PLAINTEXT (English has clear patterns)")
    display_frequency(caesar_text,    "CAESAR CIPHER (patterns still visible!)")
    display_frequency(vigenere_text,  "VIGENÈRE CIPHER (patterns flattened!)")

    print("CONCLUSION: Caesar cipher keeps letter frequency patterns,")
    print("making it easy to break. Vigenère flattens the frequencies,")
    print("resisting simple frequency analysis.")


# ------------------------------------------------------------------
# 5. FILE ENCRYPTION / DECRYPTION (Bonus Feature)
# ------------------------------------------------------------------

def encrypt_file(input_file, output_file, key):
    """Reads a text file, encrypts it, writes result to output file."""
    try:
        with open(input_file, 'r') as f:
            content = f.read()
        encrypted = vigenere_encrypt(content, key)
        with open(output_file, 'w') as f:
            f.write(encrypted)
        print(f"\n[SUCCESS] Encrypted '{input_file}' -> '{output_file}'")
    except FileNotFoundError:
        print(f"\n[ERROR] File '{input_file}' not found.")


def decrypt_file(input_file, output_file, key):
    """Reads an encrypted file, decrypts it, writes result to output file."""
    try:
        with open(input_file, 'r') as f:
            content = f.read()
        decrypted = vigenere_decrypt(content, key)
        with open(output_file, 'w') as f:
            f.write(decrypted)
        print(f"\n[SUCCESS] Decrypted '{input_file}' -> '{output_file}'")
    except FileNotFoundError:
        print(f"\n[ERROR] File '{input_file}' not found.")


# ------------------------------------------------------------------
# 6. SELF-TEST (Proves correctness automatically)
# ------------------------------------------------------------------

def run_tests():
    """Runs standard test vectors to verify the implementation is correct."""
    print("\n" + "=" * 60)
    print("        RUNNING SELF-TESTS")
    print("=" * 60)

    tests = [
        ("ATTACKATDAWN", "LEMON", "LXFOPVEFRNHR"),  # Textbook standard
        ("HELLO",        "KEY",   "RIJVS"),
        ("CRYPTOGRAPHY", "SECRET", "UVAGXHYVCGLR"), # Corrected vector
    ]

    all_passed = True
    for plaintext, key, expected in tests:
        encrypted = vigenere_encrypt(plaintext, key)
        decrypted = vigenere_decrypt(encrypted, key)

        status_enc = "PASS" if encrypted == expected else "FAIL"
        status_dec = "PASS" if decrypted == plaintext else "FAIL"

        if "FAIL" in (status_enc, status_dec):
            all_passed = False

        print(f"\nPlaintext : {plaintext}")
        print(f"Key       : {key}")
        print(f"Encrypted : {encrypted}  (expected {expected})  [{status_enc}]")
        print(f"Decrypted : {decrypted}  [{status_dec}]")

    print("\n" + "=" * 60)
    if all_passed:
        print("ALL TESTS PASSED - IMPLEMENTATION IS CORRECT ✓")
    else:
        print("SOME TESTS FAILED - CHECK CODE ✗")
    print("=" * 60)


# ------------------------------------------------------------------
# 7. MAIN MENU (Interactive Interface)
# ------------------------------------------------------------------

def main():
    while True:
        print("\n" + "=" * 60)
        print("     VIGENÈRE CIPHER - CRYPTOGRAPHY PROJECT")
        print("            CNS - 7th Semester VTU")
        print("=" * 60)
        print(" 1. Encrypt a message (Vigenère)")
        print(" 2. Decrypt a message (Vigenère)")
        print(" 3. Encrypt with Caesar cipher (comparison)")
        print(" 4. Run full demonstration + frequency analysis")
        print(" 5. Encrypt a text file")
        print(" 6. Decrypt a text file")
        print(" 7. Run self-tests (verify correctness)")
        print(" 8. Exit")
        print("=" * 60)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            text = input("Enter plaintext: ")
            key = input("Enter key (letters only): ")
            if not key.isalpha():
                print("[ERROR] Key must contain only letters.")
                continue
            print(f"\nEncrypted: {vigenere_encrypt(text, key)}")

        elif choice == '2':
            text = input("Enter ciphertext: ")
            key = input("Enter key (letters only): ")
            if not key.isalpha():
                print("[ERROR] Key must contain only letters.")
                continue
            print(f"\nDecrypted: {vigenere_decrypt(text, key)}")

        elif choice == '3':
            text = input("Enter plaintext: ")
            try:
                shift = int(input("Enter shift value (e.g., 3): "))
            except ValueError:
                print("[ERROR] Shift must be a number.")
                continue
            enc = caesar_encrypt(text, shift)
            print(f"\nEncrypted (Caesar): {enc}")
            print(f"Decrypted back  : {caesar_decrypt(enc, shift)}")

        elif choice == '4':
            run_demo()

        elif choice == '5':
            infile = input("Enter input file name: ")
            outfile = input("Enter output file name: ")
            key = input("Enter key: ")
            encrypt_file(infile, outfile, key)

        elif choice == '6':
            infile = input("Enter encrypted file name: ")
            outfile = input("Enter output file name: ")
            key = input("Enter key: ")
            decrypt_file(infile, outfile, key)

        elif choice == '7':
            run_tests()

        elif choice == '8':
            print("\nThank you! Project by [YOUR NAME], [USN]")
            print("Exiting...")
            break

        else:
            print("\n[ERROR] Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()