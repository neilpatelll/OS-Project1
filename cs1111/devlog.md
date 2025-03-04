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