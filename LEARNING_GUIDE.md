# Energy Brief — learning guide

## What it does

Research electricity generation trends reproducibly. The intended user is industry researchers. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Compare a country's electricity generation and renewable share over time, change the period, and inspect observed endpoints plus missingness. Regenerate the report and verify the source checksum.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Pin the public dataset commit and hash both source and extracted subset.
2. Retain missing observations and report the actual endpoints used instead of interpolating silently.
3. Keep electricity-generation units and renewable-share changes distinct from total energy or causal policy effects.

## Five interview questions

1. **Where did the data come from?** A pinned Our World in Data energy-data commit, with original provider attribution preserved in the codebook. The project selects six countries from 2000 through 2024.

2. **How do you reproduce the exact subset?** The acquisition script downloads the pinned CSV and checks both the full-source and selected-subset SHA-256 values. A mismatch stops the process before overwriting the existing data.

3. **Why preserve missing observations?** Replacing missing energy values with zero would turn lack of evidence into a physical claim. Summaries therefore use actual observed endpoints and retain missing values.

4. **How are shares and generation compared?** Generation is measured in TWh. Changes in electricity shares are percentage-point differences, while compound annual growth uses observed positive endpoints and elapsed years.

5. **Does a trend identify its cause?** No. This is a descriptive comparison of selected countries and years. Policy, prices, weather and measurement revisions are possible influences that the dataset alone cannot isolate.

## Independent exercise

Add a seventh country through the pinned acquisition script and document selection bias.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Published a reproducible electricity-generation report across six countries using a pinned 150-row OWID subset, verified checksums and explicit missing-data and unit handling.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
