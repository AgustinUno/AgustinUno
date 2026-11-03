# Case study — the Claims XML Engine

> **Status: draft for author review.** This file sits in a public repository. Everything below is either already public in the profile README or generic engineering reasoning. Read [NDA boundary](#nda-boundary) and [Before publishing](#before-publishing) before this ships.

**One line:** a browser-native validator that checks 50,000+ PhilHealth claim rows per run without the tab falling over.

---

## 1 · The problem

PhilHealth claims are submitted as XML. Before a claim batch leaves a provider, every row has to be checked against a rule set — required fields, code validity, cross-field consistency, totals that must reconcile. A single run is not a handful of records; it is tens of thousands of rows produced by 2,000+ healthcare units.

The obvious architecture is a server job: upload, queue, validate, download a report. That was rejected for the reason most of these systems get rejected — the people doing the work need to see *which* row failed *while* they are fixing it, not after a round trip. The validator had to live in the browser, next to the table the user was editing.

That constraint is what made the project interesting. Browsers are excellent at rendering and terrible at holding large structured data in memory.

## 2 · Why it broke

The first working version validated correctly and then locked the tab. The cause is not exotic:

- **JavaScript strings are UTF-16.** A 40 MB XML document arriving as a string is already ~80 MB before it is parsed.
- **Parsing produces objects, not data.** `DOMParser` builds a full node tree: every element is an object with a prototype, attributes, and child references. For a flat table of 50,000 rows that is millions of nodes, and each one costs far more than the bytes it represents.
- **Nothing gets collected.** Validation retains rows for error reporting, the table retains rows for rendering, and the parsed tree is reachable from both. Peak memory is the sum, not the maximum.
- **Chromium has a per-renderer ceiling.** Once the tab crosses it, the renderer is killed — not slowed, killed. There is no graceful degradation to fall back on.

So the naive pipeline — read → parse → map → render — has four copies of the same dataset alive at once, each one larger than the last.

## 3 · The approach

The mechanisms below are what the implementation settled on — confirm the level of detail you are comfortable publishing before this goes live.

The fix was to stop treating the document as a document and start treating it as a fixed record layout.

**Validate the stream, not the tree.** The XML is consumed as a sequence of records. Each record is validated and reduced to a compact result tuple — row index, rule id, severity — and then discarded. The node tree never exists as a whole.

**Use binary-level representations for the row data.** Instead of an array of objects, columns are stored in typed arrays (integers for counts and flags, offsets into one shared character buffer for strings). A row costs a predictable number of bytes instead of an unpredictable number of objects. "Binary-level" here means exactly that: the working set is bytes, not object graphs.

**Render a window, not a table.** The visible viewport is a small slice of the row set. Only that slice is materialized as DOM; scrolling swaps the slice. The DOM never grows past a few hundred rows regardless of batch size.

**Keep the report, drop the evidence.** Errors are kept as indexes into the compact store. The original XML is re-read only if the user asks to see the offending fragment — the common path holds no source text at all.

## 4 · What changed

| | Before | After |
| :--- | :--- | :--- |
| Peak memory at 50k rows | Renderer killed | Stable through repeated runs |
| DOM rows | Every row | Visible window only |
| Row representation | Object per row | Columnar typed arrays |
| Failure mode | Tab crash | Per-row error report |

The number that matters is not the peak — it is that the peak stopped scaling with batch size.

## 5 · What I would carry forward

1. **Pick the representation before the framework.** React was never the problem; an object-per-row data model under a virtualized table was. Fixing the model fixed the app.
2. **A renderer crash is a data-model bug.** Treat an OOM as a signal that the same data exists in too many forms, not as a reason to add a worker thread and hope.
3. **Validate incrementally.** Whole-batch validation is easier to write and worse to use. Per-record validation gives you progress, cancellation, and a natural place to bound memory.
4. **Measure the ceiling early.** Knowing the actual limit — and the row count at which you hit it — turns a vague "it's slow" into a budget.

## 6 · NDA boundary

Deliberately excluded from this write-up, and from anything derived from it:

- The rule set itself: which fields are required, which codes are valid, how cross-field checks are expressed.
- Client, payer, and provider identifiers; any real claim data or schema fragments.
- Internal system names, module boundaries, database schema, deployment topology.
- Specific memory figures, timing benchmarks, and batch sizes beyond the public "50,000+ rows per run".

The employer relationship and the general shape of the work are already public in the profile README. Everything above that line stays out.

## 7 · Before publishing

Confirm each of these, and delete the ones you do not want to defend:

- [ ] The row count and the "renderer was killed" framing match what actually happened.
- [ ] The implementation really did move to columnar typed arrays, not only to virtualized rendering.
- [ ] No client name, file format detail, or rule example has slipped into sections 1–5.
- [ ] The employer is comfortable with the architecture description, not just the job title.
- [ ] The profile README links here only if this file is published.

---

*Related: [profile integration notes](profile-options.md) · [README](../README.md)*
