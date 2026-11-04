# Topic 01: Introduction & Architecture

**Source**: Lecture 1.1–1.3 (Unit 1) + Textbook Ch. 1–2 ({TEXTBOOKS})

---

## 01.1 System Architecture & Privilege Rings

### Hardware Privilege Modes

Modern processors implement hardware-enforced protection boundaries (rings) to isolate user applications from privileged kernel instructions.

```text
[ User Applications (Ring 3: Unprivileged) ]
                  │
          System Call Trap
                  ▼
[ Kernel Subsystems (Ring 0: Privileged / Supervisor) ]
                  │
                  ▼
[ Physical CPU, Registers, Memory & I/O Controllers ]
```

### Core Architecture Concepts

- **Dual-Mode Operation**:
  - **User Mode (Ring 3)**: Execution restricted; privileged CPU instructions forbidden.
  - **Kernel / Supervisor Mode (Ring 0)**: Full hardware access; memory management and device control enabled.
  - **Mode Bit**: Hardware register bit indicating current execution level (e.g., `0` for kernel, `1` for user).

- **Mode Transition Triggers**:
  1. **Software Interrupt / System Call (`syscall`, `sysenter`, `int 0x80`)**: User process requests an OS service.
  2. **Hardware Interrupt**: External peripheral device signals an event (keyboard press, timer tick, network packet).
  3. **Hardware Trap / Fault**: CPU-detected synchronous exception (division by zero, page fault).

---

## 01.2 System Calls vs. Library Calls

| Property | Standard Library Call (e.g., `printf`) | System Call (e.g., `write`) |
|----------|---------------------------------------|-----------------------------|
| **Execution Ring** | User space (Ring 3) | Kernel space (Ring 0) |
| **Context Switch** | No privilege change | Enforces mode switch via interrupt/trap |
| **Buffering** | User-space stream buffer (`FILE *`) | Kernel page cache & device buffers |
| **Performance Cost** | Low overhead function call | High overhead (saves registers, switches stack) |

---

## 01.3 Standard Lab Implementation Example

```c
#include <unistd.h>
#include <string.h>

int main(void) {
    const char *msg = "Executing direct write() syscall\n";
    // Directly invokes Ring 0 write syscall without userland buffering
    write(STDOUT_FILENO, msg, strlen(msg));
    return 0;
}
```

---

## 01.4 Key Takeaways

1. **Privilege Separation**: Dual-mode hardware is essential for protecting the OS from errant or malicious user code.
2. **Transition Path**: All transitions from User Mode to Kernel Mode occur strictly via traps, syscalls, or hardware interrupts.
3. **Overhead Consideration**: System calls require state preservation and context switching, making batching and buffering crucial for performance.

---

## 01.5 Exam-Relevant MCQ Patterns

??? question "MCQ Pattern: Mode Bit Transitions"
    When an external timer interrupt occurs during the execution of a user-level process:
    
    - [ ] A) The mode bit stays set to user mode until the scheduler runs.
    - [x] B) The hardware switches the mode bit to kernel mode before invoking the interrupt handler.
    - [ ] C) The user process terminates immediately.
    - [ ] D) The interrupt handler executes in user mode with elevated priority.

    ??? success "Explanation"
        Hardware interrupts force the processor into kernel mode (Ring 0) automatically so that the kernel's Interrupt Service Routine (ISR) can run safely.
