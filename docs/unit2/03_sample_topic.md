# Topic 03: Synchronization & IPC

**Source**: Lecture 2.1–2.4 (Unit 2) + Textbook Ch. 5–7 ({TEXTBOOKS})

---

## 03.1 Race Conditions & The Critical Section Problem

A **race condition** occurs when multiple concurrent processes or threads access and manipulate shared data, and the final outcome depends on the non-deterministic order of instruction execution.

### The Three Critical Section Requirements

1. **Mutual Exclusion**: If process $P_i$ is executing in its critical section, no other processes can be executing in their critical sections.
2. **Progress**: If no process is executing in its critical section and some processes wish to enter, only those processes not executing in their remainder sections can participate in deciding who enters next.
3. **Bounded Waiting**: There exists a bound on the number of times that other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted.

---

## 03.2 Semaphores vs. Mutexes

| Feature | Mutex | Counting Semaphore |
|---------|-------|--------------------|
| **Ownership** | Locked by and unlocked exclusively by the owning thread | No ownership; any thread can signal/post |
| **Value Range** | Binary (`0` or `1`) | Non-negative integer (`0` to $N$) |
| **Typical Use** | Strict mutual exclusion for a single critical section | Resource pooling & cross-thread signaling |

---

## 03.3 POSIX Synchronization Primitives in C

```c
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
sem_t sem_items;

void *worker(void *arg) {
    pthread_mutex_lock(&lock);
    // Protected Critical Section
    pthread_mutex_unlock(&lock);
    return NULL;
}
```

---

## 03.4 Key Takeaways

1. **Mutual Exclusion**: Non-negotiable requirement to eliminate race conditions on shared memory.
2. **Deadlock Danger**: Careless lock acquisition ordering produces cyclic wait deadlocks.
3. **Hardware Support**: Atomic instructions (`test_and_set`, `compare_and_swap`) form the bedrock of user-level locking primitives.
