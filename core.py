from pathlib import Path
import json,math
import numpy as np,pandas as pd
ROOT=Path(__file__).parent

def analyze(p):
 country=p.get('country','India');start=int(p.get('start',2000));end=int(p.get('end',2024))
 if not 2000<=start<end<=2024:raise ValueError('Choose 2000 ≤ start < end ≤ 2024')
 df=pd.read_csv(ROOT/'data/energy.csv');countries=sorted(df.country.unique())
 if country not in countries:raise ValueError('Unsupported country')
 if df.duplicated(['country','year']).any():raise ValueError('Duplicate country-year')
 frame=df[(df.country==country)&df.year.between(start,end)].sort_values('year');valid=frame.dropna(subset=['electricity_generation','renewables_share_elec'])
 if len(valid)<2:raise ValueError('Insufficient observations for this period')
 first,last=valid.iloc[0],valid.iloc[-1];years=int(last.year-first.year);growth=((last.electricity_generation/first.electricity_generation)**(1/years)-1) if first.electricity_generation>0 and years>0 else None
 change=float(last.renewables_share_elec-first.renewables_share_elec)
 rows=frame[['year','electricity_generation','renewables_share_elec','fossil_share_elec','nuclear_share_elec']].round(3).replace({np.nan:None}).to_dict('records')
 source=json.loads((ROOT/'data/source.json').read_text())
 answer=f"{country}: renewable electricity share changed by {change:.2f} percentage points between {int(first.year)} and {int(last.year)}. Electricity generation changed from {first.electricity_generation:,.1f} to {last.electricity_generation:,.1f} TWh. This descriptive comparison does not identify policy effects or investment returns."
 return dict(metrics={'Latest generation':f'{last.electricity_generation:,.1f} TWh','Renewables share':f'{last.renewables_share_elec:.1f}%','Share change':f'{change:+.2f} pp','Generation CAGR':f'{growth:.2%}' if growth is not None else 'undefined'},rows=rows,bars=[dict(label=str(int(r.year)),value=float(r.renewables_share_elec)) for r in valid.itertuples()],chart_title='Renewable share of electricity (%)',answer=answer,details={'source':source,'missing_values':{k:int(v) for k,v in frame.isna().sum().items() if v},'requested_years':[start,end],'observed_endpoints':[int(first.year),int(last.year)],'scope':'electricity generation, not total energy consumption','annual_growth_method':'geometric growth across observed endpoints; missing intermediate observations not interpolated'},notice='Research snapshot through 2024, not a live forecast. Compare observed endpoints and inspect missingness before interpreting trends.')
