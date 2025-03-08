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

def main():
    if len(sys.argv) < 2:
        print("Usage: driver.py <logfilename>")
        sys.exit(1)

    log_filename = sys.argv[1]

    logger_proc = subprocess.Popen(
        ["python3", "logger.py", log_filename],
        stdin=subprocess.PIPE,
        text=True
    )

    encrypt_proc = subprocess.Popen(
        ["python3", "encryption.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    log_message(logger_proc.stdin, "START", "Driver program started.")
    history = []

    while True:
        print_menu()
        cmd = input("Enter a command: ").strip().lower()

        if cmd == "quit" or cmd == "5":
            log_message(logger_proc.stdin, "CMD", "quit")
            encrypt_proc.stdin.write("QUIT\n")
            encrypt_proc.stdin.flush()
            log_message(logger_proc.stdin, "QUIT", "")
            encrypt_proc.wait()
            logger_proc.wait()
            print("Exiting driver.")
            break

        elif cmd in ["password", "1"]:
            log_message(logger_proc.stdin, "CMD", "password")
            passkey = input("Enter new passkey (letters only): ").strip().upper()

            if not passkey.isalpha():
                print("Error: passkey must contain only letters A-Z.")
                log_message(logger_proc.stdin, "ERROR", "Passkey invalid input")
                continue

            encrypt_proc.stdin.write(f"PASS {passkey}\n")
            encrypt_proc.stdin.flush()
            resp = encrypt_proc.stdout.readline().strip()
            if resp.startswith("RESULT"):
                print("Password set successfully.")
                log_message(logger_proc.stdin, "PASS", "Password set successfully")
            else:
                print("Error setting password.")
                log_message(logger_proc.stdin, "ERROR", resp)

        elif cmd in ["encrypt", "2"]:
            log_message(logger_proc.stdin, "CMD", "encrypt")
            use_history = input("Use a string from history? (y/n): ").strip().lower()
            if use_history.startswith('y') and len(history) > 0:
                chosen = choose_from_history(history)
                plaintext = chosen.upper() if chosen else input("Enter string to encrypt (letters only): ").strip().upper()
            else:
                plaintext = input("Enter string to encrypt (letters only): ").strip().upper()

            if not plaintext.isalpha():
                print("Error: plaintext must contain only letters A-Z.")
                log_message(logger_proc.stdin, "ERROR", "Invalid plaintext input")
                continue

            encrypt_proc.stdin.write(f"ENCRYPT {plaintext}\n")
            encrypt_proc.stdin.flush()
            resp = encrypt_proc.stdout.readline().strip()
            if resp.startswith("RESULT"):
                parts = resp.split(maxsplit=1)
                if len(parts) == 2:
                    _, ciphertext = parts
                    print(f"Encrypted string: {ciphertext}")
                    history.append(plaintext)
                    history.append(ciphertext)
                    log_message(logger_proc.stdin, "ENCRYPT", f"{plaintext} => {ciphertext}")
                else:
                    print("Unexpected result format.")
            else:
                print(resp)
                log_message(logger_proc.stdin, "ERROR", resp)

        elif cmd in ["decrypt", "3"]:
            log_message(logger_proc.stdin, "CMD", "decrypt")
            use_history = input("Use a string from history? (y/n): ").strip().lower()
            if use_history.startswith('y') and len(history) > 0:
                chosen = choose_from_history(history)
                ciphertext = chosen.upper() if chosen else input("Enter string to decrypt (letters only): ").strip().upper()
            else:
                ciphertext = input("Enter string to decrypt (letters only): ").strip().upper()

            if not ciphertext.isalpha():
                print("Error: ciphertext must contain only letters A-Z.")
                log_message(logger_proc.stdin, "ERROR", "Invalid ciphertext input")
                continue

            encrypt_proc.stdin.write(f"DECRYPT {ciphertext}\n")
            encrypt_proc.stdin.flush()
            resp = encrypt_proc.stdout.readline().strip()
            if resp.startswith("RESULT"):
                parts = resp.split(maxsplit=1)
                if len(parts) == 2:
                    _, plaintext = parts
                    print(f"Decrypted string: {plaintext}")
                    history.append(ciphertext)
                    history.append(plaintext)
                    log_message(logger_proc.stdin, "DECRYPT", f"{ciphertext} => {plaintext}")
                else:
                    print("Unexpected result format.")
            else:
                print(resp)
                log_message(logger_proc.stdin, "ERROR", resp)

        elif cmd in ["history", "4"]:
            log_message(logger_proc.stdin, "CMD", "history")
            print("\nHistory:")
            for idx, item in enumerate(history):
                print(f"{idx+1}) {item}")
        else:
            print("Invalid command.")
            log_message(logger_proc.stdin, "ERROR", "Unknown command entered by user")

if __name__ == "__main__":
    main()
