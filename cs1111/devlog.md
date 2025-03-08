# CS4348 Project 1 Development Log
**2025-03-03 11:30pm**

CS4348 Project 1 has been an interesting challenge. Inter-process communication (IPC) is both engaging and frustrating. At this point, I feel like I’ve spent half my time navigating pipes and debugging cryptic process interactions. The project consists of three programs—a logger, an encryption module, and a driver program—all communicating via pipes. When it works, it’s great. When it doesn’t, it’s a mystery waiting to be unraveled.

Initially, I chose Python for implementation since managing subprocesses in C felt unnecessarily complicated. The logger records events, the encryption module applies a Vigenère cipher, and the driver coordinates everything. Conceptually straightforward, but practically messy. Debugging has been a mix of small victories and unexpected setbacks.


## Progress and Challenges:

### Logger:
- Implemented timestamped logging with millisecond precision.
- Handles "QUIT" command cleanly—no rogue processes lurking in the shadows. Though I half expect them to rise from the dead at any moment.
- Improved error logging for better debugging insights.
- Added color-coded log levels to distinguish errors visually.
- Considered adding sarcastic messages for critical errors but opted for professionalism.

### Encryption Program:
- Vigenère cipher implementation is functional and secure.
- Input validation added to handle unexpected inputs.
- Passkeys are not stored in plaintext for security.
- Implemented key rotation for extra security. Not required, but felt smug about it for approximately 3 minutes before it broke everything else.
- Debug mode added to display encryption matrix for troubleshooting.

### Decryption Module:
- Ensured correct decryption without garbled output.
- Fixed a bizarre edge case where decrypting twice would give me hieroglyphics instead of the original text. Turns out I was reading from the wrong pipe end. I spent 4 hours on this. I'm fine.
- Implemented buffer clearing to avoid memory issues.
- Added error handling for incorrect decryption keys.
- Optimized decryption speed slightly, but more improvements are possible.

### Driver Program:
- Command parsing (PASS, ENCRYPT, DECRYPT, QUIT) implemented. Feels nice to type commands and have them not instantly crash everything.- Manages pipes for inter-process communication.
- Implemented proper signal handling to prevent orphaned processes.
- Added timeout detection for unresponsive processes.

## Inter-Process Communication:
- Pipes set up using `pipe()` and `fork()`.
- Implemented newline-delimited message protocol.
- Used `fcntl()` for non-blocking I/O.
- Addressed potential race conditions with synchronization techniques.
- Managed pipe congestion issues with artificial delays and buffering strategies.

## Testing:
- Threw random inputs at it, some expected, some questionable. The questionable ones were very questionable. No regrets.
- Small-scale stress tests ran well, but I need bigger, angrier tests. Going to spam it with commands until something screams.
- Created a test script to stress test encryption with large text blocks.
- Implemented a max-length check to prevent crashes with large inputs.

## Challenges Faced:

### Process Management:
- Subprocess termination required SIGTERM and SIGKILL handling.
- Exceeded OS process limits during testing, leading to unexpected failures.
- Addressed potential memory leaks after prolonged execution.

### Pipes and Buffers:
- Large messages occasionally truncated or lost.
- Debugging revealed unexpected stdout and pipe conflicts.
- Buffer size limitations required adjustments.

### Communication Delays:
- Messages sometimes take their sweet time getting to their destination. I like to imagine they're stopping for coffee breaks.
- Could be pipe buffering, could be my OS mocking me. Probably both. The OS is laughing at me. I can feel it.
- Implemented a timeout-based retry mechanism for stalled messages.
- Added sequence numbers to maintain message order during high-load scenarios.

## Next Steps:
- Conduct larger-scale stress testing.
- Refine synchronization to improve reliability.
- Optimize resource usage and efficiency.
- Enhance error reporting with more meaningful messages.
- Implement a heartbeat mechanism to detect silent process failures.


## Random Experiences from Phase 1:
- Debugging pipes feels like trying to reason with stubborn ghosts.
- Forgetting a single character in a command can break everything.
- My test script now includes encrypting and decrypting song lyrics for fun.
- Watching messages randomly delay is oddly relatable.
- Debugging race conditions at 3 AM is an existential experience.
- The feeling of fixing an obscure bug is great… until the next one appears.

So far man, this project has been an engaging learning experience, but also as expected you know it is filled with both frustrating moments and satisfying breakthroughs. Every time I think I've got it under control, something weird happens. But at the same time, it's kind of satisfying. Still got some work to do but made a lot of progess today. 


**2025-03-06 4:00pm**

**Progress:**
* Solid progress made on encryption module and driver program.
* Implemented proper handling of PASS, ENCRYPT, and DECRYPT commands.
* Improved data flow and command execution.

**Updates:**

* **Encryption Program:**
    * Added `main()` function for stdin command handling.
    * Passkey storage in memory, encryption/decryption enabled only when set.
    * RESULT response for successful PASS command.
    * Error handling for ENCRYPT without passkey.
    * Calls `vigenere_cipher()` for encryption/decryption.
    * Handles unknown commands gracefully.
    * Implemented error handling for edge cases (empty inputs, malformed commands).
    * Input validation for data integrity.
    * Refactored code for readability and maintainability.
    * Optimized memory usage for large text blocks.
    * Detailed comments added for Vigenere cipher implementation.
    * Created simple test cases for functionality verification.

**Next Steps:**

* Add unit tests for each command type.
* Implement key rotation for enhanced security.
* Investigate potential buffer overflow vulnerabilities.
* Consider adding command history feature for debugging.
* Conduct stress tests with large text inputs to assess performance.
* Optimize pipe communication for better efficiency under heavy loads.
* Review logging mechanisms to ensure all crucial events are captured.
* Integrate with the driver program and test end-to-end functionality.

Main this is to work on the driver program, I have for the most part set up everything that needs to be set up. So driver is last thing that is left to do. 


# 2025-03-7 10:00am

## Thoughts Since Last Session

Looking back at my entry from March 6th, I'm still a bit surprised at how smoothly the implementation of the encryption program went. In my experience, when things go "too well," it usually means I've overlooked something crucial. Since that session, I've been mentally reviewing the architecture and potential weak points in the system. Right after putting it into git I also started looking at the driver and started planning what I needed and also wanted to do. And I think I have a plan on how I want to do it. It will be different from how the project guidelines says it should be, but I think this is a WAY better verison of how it should have went. 

## Plan for This Session

Today, I plan to focus on hardening the implementation through more rigorous testing and some targeted improvements:

1. **I want to list it out:**
    print("\nAvailable commands:")
    print("  1) password  - Set/change the encryption passkey")
    print("  2) encrypt   - Encrypt a new string or one from history")
    print("  3) decrypt   - Decrypt a new string or one from history")
    print("  4) history   - Display the history of strings")
    print("  5) quit      - Quit the program")

I basically want the user to select it then it will go through. 

I like how the user first has to chose then the word will come through then I can process. In the actual project, all it is is that you enter the command of what you want to do and also the word with it. I think this way it is easier. 

Some additional thoughts that have occurred to me:
- The pipe communication system could potentially face deadlocks in certain edge cases
- We might need better handling for very large files during encryption/decryption
- There's a possibility of resource leaks if the program terminates unexpectedly during an operation
- I haven't thoroughly tested against malformed inputs that might circumvent our error handling

These concerns weren't apparent during initial testing because our test cases, while comprehensive, might still be following expected patterns too closely.

2. **Enhanced Error Handling**
    - Double-check every command input so nothing weird slips through.
    - Add a timeout so pipes don’t freeze indefinitely (because that’s been a fun issue).
    - Make error messages actually useful instead of just yelling “Error” at me."

3. **Resource Management Review**
   - Audit all file and memory operations to ensure proper cleanup
   - Implement signal handlers to catch unexpected terminations
   - Add resource usage logging to track potential memory leaks

4. **Documentation Updates**
   - Add detailed comments for complex sections of code
   - Update the README with installation and usage instructions
   - Document all error codes and their meanings
   - Create example usage scenarios

I just need to wrap up the error handling and get the driver program fully functional. If I have time, I'll throw in some extra edge case tests, but that depends on how many unexpected bugs decide to show up.

I expect this hardening phase to reveal at least a few issues that will need addressing before final submission. Finding these now will save considerable trouble later.


**2025-03-08 2:00pm**

**Progress:**

* Driver program command handling finalized.
* Comprehensive testing and validation completed.
* Encryption and logger modules performed flawlessly.

Ran a full round of tests encryption and logger modules worked without a hitch. Almost suspiciously smooth, but I'll take the win

**Updates:**

* **Driver Program:**
    * Implemented and tested PASS, ENCRYPT, DECRYPT, and QUIT commands.
    * Verified correct data transmission through pipes.
    * Ensured proper error handling for incorrect or missing inputs.
* **Testing and Validation:**
    * Full test suite executed, including edge cases and stress tests.
    * Confirmed consistent encryption/decryption results.
    * Logger verified to record all actions with accurate timestamps.
* **Encryption & Logger:**
    * No modifications required after testing.

**Next Steps:**

* Revisit all components for final checks later in the week.
* Conduct additional stress testing for 100% certainty.
* Double check for any unnoticed edge cases.
* Final documentation and cleanup before submission.

**Before Submission Checklist:**
    * Run all test cases one final time
    * Ensure documentation is complete
