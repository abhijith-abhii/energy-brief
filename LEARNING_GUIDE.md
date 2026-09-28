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

1. **What problem does this project solve, and what is its unit of work?** Explain research electricity generation trends reproducibly, identify industry researchers as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Pin the public dataset commit and hash both source and extracted subset. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Retain missing observations and report the actual endpoints used instead of interpolating silently. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Keep electricity-generation units and renewable-share changes distinct from total energy or causal policy effects. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** Six selected countries and years 2000–2024. Source revisions, missingness and country coverage affect comparisons. Descriptive research, not an investment forecast or causal estimate. Upstream data attribution and terms remain applicable. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add a seventh country through the pinned acquisition script and document selection bias.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated research electricity generation trends reproducibly using Python · pandas · Flask, with pinned public data and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
