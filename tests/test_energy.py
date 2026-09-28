import hashlib,json,pandas as pd,pytest
from core import ROOT,analyze

def test_source_checksum():
 m=json.loads((ROOT/'data/source.json').read_text());assert hashlib.sha256((ROOT/'data/energy.csv').read_bytes()).hexdigest()==m['subset_sha256']
def test_keys_and_units():
 df=pd.read_csv(ROOT/'data/energy.csv');assert not df.duplicated(['country','year']).any();assert (df.electricity_generation.dropna()>=0).all()
 for col in ['renewables_share_elec','fossil_share_elec','nuclear_share_elec']:assert df[col].dropna().between(0,100).all()
def test_actual_report():assert analyze({})['rows']
@pytest.mark.parametrize('p',[{'start':2024,'end':2000},{'country':'Atlantis'},{'end':2030}])
def test_invalid(p):
 with pytest.raises(ValueError):analyze(p)
