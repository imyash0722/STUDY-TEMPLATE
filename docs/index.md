# {SUBJECT} Exam Prep — {COURSE_CODE} ({UNITS})

Complete study guide and exam preparation resource for **{SUBJECT} ({COURSE_CODE})** covering **{UNITS}**.

---

## Course Information

| Detail | Value |
|--------|-------|
| **Course** | {SUBJECT} ({COURSE_CODE}) |
| **Exam Date** | {EXAM_DATE} |
| **Coverage** | {UNITS} |
| **Question Pattern** | {EXAM_PATTERN} (e.g., 100 MCQs / Theory + Numerical + Code) |
| **Primary Focus** | Lab Programs, System APIs, Algorithm Tracing, Calculations & Conceptual Rigor |

---

## Prescribed Textbooks & References

- **{AUTHOR_1}** — *{TEXTBOOK_1_TITLE}*, {EDITION_1}, {PUBLISHER_1} ({YEAR_1})
- **{AUTHOR_2}** — *{TEXTBOOK_2_TITLE}*, {EDITION_2}, {PUBLISHER_2} ({YEAR_2})
- **{AUTHOR_3}** — *{TEXTBOOK_3_TITLE}*, {EDITION_3}, {PUBLISHER_3} ({YEAR_3})

---

## Quick Navigation

### Unit 1: {UNIT_1_TITLE}
- [Topic 01: Introduction & Architecture](unit1/01_sample_topic.md) — Foundations, system boundary, and hardware interfaces
- [Topic 02: Process Concepts & Lifecycle](unit1/02_sample_topic.md) — State models, PCB, scheduling queues, context switches

### Unit 2: {UNIT_2_TITLE}
- [Topic 03: Synchronization & IPC](unit2/03_sample_topic.md) — Race conditions, semaphores, mutexes, shared memory

### Unit 3: {UNIT_3_TITLE}
- [Topic 15: Main Memory Management](unit3/15_sample_memory_management.md) — Hardware translation, base/limit registers, allocation policies, `mmap`

---

## Exam Preparation Checklist

### High-Yield Algorithms & Numerical Traces (Trace by Hand)
- [ ] Algorithm 1: State transitions, scheduling Gantt charts, and turnaround/wait times
- [ ] Algorithm 2: Deadlock safety algorithms and allocation vector updates
- [ ] Algorithm 3: Producer-consumer and synchronization invariants with semaphores
- [ ] Algorithm 4: Page replacement traces (FIFO, LRU, Optimal, Clock algorithm)
- [ ] Numerical 1: Effective Memory Access Time (EAT) calculation with TLB hit ratios

### Core Conceptual Checkpoints
- [ ] User mode vs. Kernel mode execution boundaries and hardware trap mechanisms
- [ ] Process Control Block (PCB) vs. Thread Control Block (TCB) memory overhead
- [ ] Concurrency pitfalls: Race conditions, critical sections, 3 criteria for mutual exclusion
- [ ] Memory allocation strategies: First Fit vs. Best Fit vs. Worst Fit fragmentation trade-offs
- [ ] Virtual memory: Demand paging, page fault handling overhead, copy-on-write semantics

### Code-Level & Lab Competencies
- [ ] System call flow: `fork()`, `exec()`, `wait()`, and exit status codes
- [ ] Thread management APIs: `pthread_create()`, `pthread_join()`, mutex locking
- [ ] POSIX semaphores: `sem_init()`, `sem_wait()`, `sem_post()`
- [ ] Memory mapping: `mmap()`, `munmap()`, `MAP_SHARED` vs. `MAP_PRIVATE` flags
- [ ] Signal handling: `sigaction()` registration and async-signal safety

---

## Recommended Study Strategy

1. **Follow the Topic Order**: Topics are arranged progressively; subsequent concepts build on earlier foundations.
2. **Hand-Trace Every Example**: Don't just read tables and Gantt charts—draw them out on scratch paper.
3. **Verify with Code**: Run the small lab code snippets provided in each topic to inspect actual OS behavior.
4. **Drill the MCQ Patterns**: Review the "Exam-Relevant MCQ Patterns" section in each topic to avoid tricky traps.
5. **Simulate Timed Practice**: Complete the end-of-topic practice problems before checking the collapsed answers.

---

*Site built with [Zensical](https://github.com/zensical/zensical) &middot; Deployed to [GitHub Pages](https://pages.github.com/)*
