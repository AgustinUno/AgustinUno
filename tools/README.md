# tools

One generator. Deterministic: run it and the committed artefact in `assets/` is rebuilt
with no diff.

## `banner_gen.mjs`

Builds `assets/header-banner.svg` — the 1200 × 400 profile banner.

```bash
node tools/banner_gen.mjs assets/header-banner.svg
```

No dependencies. The seeded PRNG means the skyline is identical on every run; change
`seed` for a different city, change the palette constants at the top for a different
identity.

The resume is not generated here — see `resume/Bautista_Master_Resume.pdf` and the
[resume notes](../docs/profile-options.md#resume).
