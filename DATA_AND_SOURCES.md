# Data, code and model sources

The topic comes from the source mapping in the portfolio index. Original authored synthetic fixtures and procedural images are distributed under the repository MIT license. Synthetic records do not describe actual customers, employees, players or transactions.

Implementation references:
- Flask: https://flask.palletsprojects.com/en/stable/ — request handling and security considerations.
- Python SQLite: https://docs.python.org/3/library/sqlite3.html — transactions, parameter binding and authorizers.
- scikit-learn: https://scikit-learn.org/stable/common_pitfalls.html — leakage prevention and fitted preprocessing.

Only applicable libraries are used; their upstream licenses remain in installed distributions. Project code does not claim authorship of dependencies.

Public source: [Our World in Data energy dataset](https://github.com/owid/energy-data), exact commit and hashes in `data/source.json`. OWID-produced content is CC BY; original provider terms remain applicable. [OWID Energy](https://ourworldindata.org/energy) credits Hannah Ritchie, Pablo Rosado and Max Roser. Electricity series in the bundled codebook cite Ember and Energy Institute; consult `data/source-codebook.csv`. Subsetting and calculations were performed here; missing values remain missing.

Reproduce the exact committed subset with `python scripts/download_data.py`. It fetches the pinned revision, verifies both source and subset SHA-256, and preserves the existing file on any mismatch.
