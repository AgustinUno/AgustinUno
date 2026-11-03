# Case study — the Claims XML Engine

> **Status: draft for author review.** This file sits in a public repository. The technical claims below are drawn from the master resume; everything else is reasoning from those facts. Read [NDA boundary](#nda-boundary) and [Before publishing](#before-publishing) before this ships.

**One line:** a browser-native tool that extracts, validates, and cleans 50,000+ PhilHealth claim rows per run — without the tab dying.

---

## 1 · The problem

PhilHealth claims arrive as XML. Before a batch leaves a provider, every row has to be extracted, checked against a rule set, and cleaned: required fields, code validity, cross-field consistency, totals that reconcile. A run is not a handful of records — it is tens of thousands of rows from 2,000+ healthcare units, and the output determines hospital reimbursement.

The work is iterative by nature. A batch gets loaded, problems surface, rows get corrected, the batch is checked again. That loop is why the tool is web-native rather than a submit-and-wait job on a server: the person cleaning the data has to stay in the same surface as the data.

Which means the browser has to hold all of it. That is where it broke.

## 2 · Why it broke

The first version worked, then locked the tab. The causes are not exotic:

- **JavaScript strings are UTF-16.** A large XML document arriving as a string is already twice its on-disk size before a parser touches it.
- **Parsing produces objects, not data.** A DOM build makes every element an object with a prototype, attributes, and child references. For a flat table of 50,000 rows that is millions of nodes, each costing far more than the bytes it represents.
- **Nothing gets collected.** Rows are retained for error reporting, the view retains rows for rendering, and the parsed tree is reachable from both. Peak memory becomes the sum of every copy, not the largest one.
- **Chromium has a per-renderer ceiling.** Cross it and the renderer is killed — not slowed, killed. There is no graceful degradation to fall back on.

The naive pipeline — read → parse → map → render — keeps four representations of one dataset alive at once, each larger than the last.

## 3 · The approach

Two mechanisms did the work, in the words the master resume already uses: **binary-level optimisation** and **browser thread management**.

**Binary-level optimisation.** Stop treating a row as an object graph and start treating it as a fixed-width record. Counts, flags, and indexes live in typed arrays; text lives once in a backed buffer with offsets into it. A row then costs a predictable number of bytes instead of an unpredictable number of objects plus their hidden-class overhead. The same data that previously existed as XML string, DOM tree, DTO, and view model collapses into one compact structure.

**Browser thread management.** Parsing and validating 50,000+ rows on the main thread blocks paint and grows the renderer's heap in one contiguous burst. Moving that work to a worker keeps the main thread free, bounds where the allocations happen, and lets the UI report progress instead of freezing. The worker sends back compact results, not a second copy of the dataset.

The two are complementary: threads solve the freeze, compact representations solve the ceiling. Either alone only moves the failure.

## 4 · What changed

| | Before | After |
| :--- | :--- | :--- |
| Peak memory at 50,000+ rows | Renderer killed | Stable across a full run |
| Main thread | Blocked during parse and validation | Responsive, with progress |
| Row representation | Object per row | Fixed-width binary records |
| Financial accuracy | Correct, but only at small scale | Correct at full scale |

The number that matters is not the peak — it is that the peak stopped scaling with batch size.

## 5 · What I would carry forward

1. **Pick the representation before the framework.** The framework was never the problem; an object-per-row model under a 50,000-row dataset was. Changing the model changed the app.
2. **A renderer kill is a data-modelling bug.** Treat an OOM as evidence that the same data exists in too many forms — not as a reason to add a spinner and hope.
3. **Freeze and memory are different bugs.** Thread offloading fixes the freeze; it does nothing for the ceiling, and can even raise it by duplicating data across threads. Fix both, cheaply.
4. **Measure the ceiling early.** Knowing the actual row count at which the renderer dies turns "it's laggy" into a budget you can defend in review.

## 6 · NDA boundary

Deliberately excluded from this write-up, and from anything derived from it:

- The validation rule set: which fields are required, which codes are valid, how cross-field checks are expressed.
- Client, payer, and provider identifiers; any real claim data or schema fragments.
- Internal system names beyond what the resume already states, module boundaries, database schema, deployment topology.
- Specific memory figures, timings, and batch sizes beyond the public "50,000+ rows per run".

The employer relationship and the shape of the work are already public on the resume. Everything above that line stays out.

## 7 · Before publishing

Confirm each of these, and delete the ones you do not want to defend:

- [ ] "Binary-level optimisation" really means typed arrays / backed buffers, not just a leaner DTO.
- [ ] Validation actually runs in a worker, not merely in an async loop.
- [ ] The "renderer killed" framing describes what happened, not a dramatisation of "it got slow".
- [ ] No client name, payer, schema fragment, or rule example has slipped into sections 1–5.
- [ ] The employer is comfortable with the architecture description, not just the job title.
- [ ] The profile README links here only if this file is published.

---

*Related: [profile integration notes](profile-options.md) · [README](../README.md)*
