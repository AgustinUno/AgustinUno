# tools

Two generators, one source of truth each. Both are deterministic: run them and the
committed artefacts in `assets/` and `resume/` are rebuilt byte-for-byte.

## `banner_gen.mjs`

Builds `assets/header-banner.svg` — the 1200 × 400 profile banner.

```bash
node tools/banner_gen.mjs assets/header-banner.svg
```

No dependencies. The seeded PRNG means the skyline is identical on every run; change
`seed` for a different city, change the palette constants at the top for a different
identity.

## `build_resume.py`

Builds `resume/Justine-Lloyd-Bautista-Resume.docx` and `.pdf` from one content model,
so the two files cannot drift apart.

```bash
pip install python-docx reportlab
python tools/build_resume.py
```

The PDF registers Segoe UI from `C:/Windows/Fonts`; on another platform those
`registerFont` calls fail and reportlab falls back to Helvetica.
