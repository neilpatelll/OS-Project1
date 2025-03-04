#!/usr/bin/env python3

import sys
import subprocess

def print_menu():
    print("\nAvailable commands:")
    print("  1) password  - Set/change the encryption passkey")
    print("  2) encrypt   - Encrypt a new string or one from history")
    print("  3) decrypt   - Decrypt a new string or one from history")
    print("  4) history   - Display the history of strings")
    print("  5) quit      - Quit the program")

def log_message(logger_stdin, action, message):
    logger_stdin.write(f"{action} {message}\n")
    logger_stdin.flush()

def choose_from_history(history):
    while True:
        print("\nHistory strings:")
        for i, item in enumerate(history):
            print(f"{i+1}) {item}")
        print(f"{len(history)+1}) Enter a new string instead")

        choice_str = input("Select an option: ")
        if not choice_str.isdigit():
            print("Invalid selection. Try again.")
            continue

        choice = int(choice_str)
        if 1 <= choice <= len(history):
            return history[choice - 1]
        elif choice == len(history) + 1:
            return None
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()
