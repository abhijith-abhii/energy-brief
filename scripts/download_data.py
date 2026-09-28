"""Reproduce the committed subset from the pinned OWID revision (network required)."""
from pathlib import Path
import csv,hashlib,io,json,urllib.request
ROOT=Path(__file__).resolve().parents[1]
meta=json.loads((ROOT/'data/source.json').read_text())
raw=urllib.request.urlopen(meta['source_url'],timeout=120).read()
if hashlib.sha256(raw).hexdigest()!=meta['source_sha256']:raise SystemExit('Source checksum mismatch; existing data unchanged')
columns=next(csv.reader((ROOT/'data/energy.csv').open()))
rows=[{k:r[k] for k in columns} for r in csv.DictReader(io.StringIO(raw.decode())) if r['country'] in ['United States','India','China','Germany','United Kingdom','Brazil'] and 2000<=int(r['year'])<=2024]
buffer=io.StringIO(newline='');writer=csv.DictWriter(buffer,fieldnames=columns);writer.writeheader();writer.writerows(rows)
data=buffer.getvalue().encode()
if hashlib.sha256(data).hexdigest()!=meta['subset_sha256']:raise SystemExit('Subset checksum mismatch; existing data unchanged')
(ROOT/'data/energy.csv').write_bytes(data)
print(f'Reproduced {len(rows)} rows; source and subset checksums match')
