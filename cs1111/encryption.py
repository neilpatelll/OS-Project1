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

if __name__ == "__main__":
    main()
