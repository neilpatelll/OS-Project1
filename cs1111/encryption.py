#!/usr/bin/env python3
import sys

def vigenere_cipher(text, key, mode="ENCRYPT"):
    result = []
    key_length = len(key)
    if key_length == 0:
        return None
    text_nums = [ord(ch) - ord('A') for ch in text]
    key_nums = [ord(ch) - ord('A') for ch in key]
    for i, val in enumerate(text_nums):
        shift = key_nums[i % key_length]
        if mode == "ENCRYPT":
            new_val = (val + shift) % 26
        else:
            new_val = (val - shift) % 26
        result.append(chr(new_val + ord('A')))
    return "".join(result)

def main():
    passkey = ""
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        command = parts[0].upper()
        if command == "QUIT":
            break
        argument = ""
        if len(parts) > 1:
            argument = parts[1].upper()
        if command == "PASS":
            passkey = argument
            print("RESULT")
            sys.stdout.flush()
        elif command == "ENCRYPT":
            if not passkey:
                print("ERROR Password not set")
            else:
                ciphertext = vigenere_cipher(argument, passkey, mode="ENCRYPT")
                if ciphertext is None:
                    print("ERROR Invalid passkey")
                else:
                    print(f"RESULT {ciphertext}")
            sys.stdout.flush()
        elif command == "DECRYPT":
            if not passkey:
                print("ERROR Password not set")
            else:
                plaintext = vigenere_cipher(argument, passkey, mode="DECRYPT")
                if plaintext is None:
                    print("ERROR Invalid passkey")
                else:
                    print(f"RESULT {plaintext}")
            sys.stdout.flush()
        else:
            print("ERROR Unknown command")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
