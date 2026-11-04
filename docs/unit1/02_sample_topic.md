# Topic 02: Process Concepts & Lifecycle

**Source**: Lecture 1.4–1.6 (Unit 1) + Textbook Ch. 3 ({TEXTBOOKS})

---

## 02.1 Process State Model

A process transitions through discrete execution states managed by the OS scheduler:

```text
[ New ] ──Admit──► [ Ready ] ◄──Interrupt── [ Running ] ──Exit──► [ Terminated ]
                       ▲                         │
                       │                         ▼
                       └─── I/O Event Done ─── [ Waiting / Blocked ]
```

### Process Control Block (PCB) Contents
- **Process ID (PID)**: Unique integer identifier.
- **Process State**: Running, Ready, Waiting, etc.
- **Program Counter (PC)**: Memory address of next instruction.
- **CPU Registers**: General-purpose registers, stack pointer, flags.
- **Memory Management Info**: Base/limit registers, page table pointers.
- **Accounting & Scheduling**: Priority, CPU execution time limits.
- **I/O Status**: Open file descriptors, allocated devices.

---

## 02.2 Process Creation & Destruction in Unix

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void) {
    pid_t pid = fork();

    if (pid < 0) {
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        // Child Process
        printf("Child process running with PID: %d\n", getpid());
        _exit(0);
    } else {
        // Parent Process
        wait(NULL); // Reap child to avoid zombie state
        printf("Parent reaped child.\n");
    }
    return 0;
}
```

---

## 02.3 Zombie vs. Orphan Processes

| Type | Condition | Resolution |
|------|-----------|------------|
| **Zombie Process** | Child has terminated, but parent has not called `wait()` | Parent calls `wait()`, or if parent dies, `init`/`systemd` reaps it. |
| **Orphan Process** | Parent terminated while child continues running | Re-parented to `init` (PID 1) / `systemd`, which periodically calls `wait()`. |

---

## 02.4 Key Takeaways

1. **PCB as Identity**: The PCB is the single source of truth for process tracking in kernel memory.
2. **Context Switching Cost**: Involves saving register states, flushing pipeline caches, and loading memory tables.
3. **Reaping Requirement**: Every terminated child process must be collected by its parent to release its PCB slot.
