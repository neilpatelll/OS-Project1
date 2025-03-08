# Encryption and Logging System

## Overview
This project contains three programs:
1. **logger.py** – Logs messages to a specified log file.
2. **encryption.py** – Performs Vigenère cipher encryption and decryption.
3. **driver.py** – The main driver that launches both `logger.py` and `encryption.py`, provides a menu, and coordinates all input/output.

## Files and Their Roles

### 1. logger.py
* Takes a single command-line argument (the log file name).
* Reads lines from `stdin`.
* For each line, it splits out the "action" (first token) and the "message" (remainder).
* Logs them to the specified file with a timestamp.
* Stops when it reads `"QUIT"`.

### 2. encryption.py
* A simple command-based encryption program using the Vigenère cipher.
* Accepts commands via `stdin`:
  * `PASS <key>` sets the internal passkey.
  * `ENCRYPT <text>` encrypts the text using the current passkey (if any).
  * `DECRYPT <text>` decrypts the text using the current passkey (if any).
  * `QUIT` causes the program to exit.
* Prints results or errors to `stdout`.

### 3. driver.py
* The main program to run.
* Takes one command-line argument: the log file name.
* Spawns `logger.py` and `encryption.py`, sets up pipes, and communicates with both.
* Presents an interactive menu for the user:
  1. **password** – set a new passkey (by user input or from history).
  2. **encrypt** – encrypt a new string (by user input or from history).
  3. **decrypt** – decrypt a new string (by user input or from history).
  4. **history** – view all past strings (from this run).
  5. **quit** – terminate the program.
* Maintains a history of user-entered (or resulting) strings for convenience.
* Logs relevant actions and results to the logger.

## How to Run

### Prerequisites
* Python 3
* (Optional) Make all Python scripts executable on Linux:

```bash
chmod +x logger.py encryption.py driver.py
```

### Step-by-Step Execution

#### 1. Running `logger.py`
No direct standalone usage is strictly required, but for reference:

```bash
python3 logger.py <logfilename>
```
This will run the logger on `<logfilename>`. It will exit if it receives `"QUIT"` via standard input.

#### 2. Running `encryption.py`
No direct standalone usage is needed for normal operation, but for testing:

```bash
python3 encryption.py
```
Type commands (`PASS`, `ENCRYPT`, `DECRYPT`, `QUIT`) interactively.

#### 3. Running `driver.py` (Main Entry Point)

```bash
python3 driver.py mylog.txt
```
* `mylog.txt` is the name of the log file that `logger.py` will write to.
* The driver will start up and present a menu of options.
* Use the menu to set passwords, encrypt/decrypt text, view history, or quit.

# Run the driver with a desired log file name
./driver.py mylog.txt


## Notes
* The project is structured to meet the requirement of using multiple processes:
  * `driver.py` creates two child processes for logging and encryption.
  * Communication is done via pipes (subprocess pipes in Python).
* Only **letters A-Z** are valid for passkeys and text to be encrypted/decrypted.
* Passwords (passkeys) are **not** logged in plaintext to avoid security issues.
* The history is kept **only in memory** and is not saved to disk. It is cleared when `driver.py` exits.
* The log file (`mylog.txt` in the example) will show each command, the timestamps, and any relevant error messages or results.
