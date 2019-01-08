#%%
import pandas

#%%
data = pandas.read_csv('https://raw.githubusercontent.com/Zadigo/open-data-party/master/wta/genie_bouchard.csv', parse_dates=['date'])

#%%
df = pandas.DataFrame(data=data)

#%%
def fix_event(previous_event_name, new_event_name):
    def _iterator(x):
        if x == previous_event_name:
            return new_event_name
        else:
            return x
    df['tour'] = df['tour'].apply(_iterator)

fix_event('Washington dc', 'Washington DC')
fix_event('Acapulco - acapulco', 'Acapulco')
fix_event('Washington dc - washington dc', 'Washington DC')
fix_event('Burnie - burnie', 'Burnie')
fix_event('Hong kong - hong kong', 'Hong Kong')
fix_event('Mallorca - mallorca', 'Mallorca')
fix_event('Birmingham - birmingham', 'Birmingham')
fix_event('Cincinnati - cincinnati', 'Cincinnati')
fix_event('French open', 'Roland garros')
fix_event('Wuhan - wuhan', 'Wuhan')
fix_event('Beijing - beijing', 'Beijing')
fix_event('N�rnberg - n�rnberg', 'Nurnberg')
fix_event('Us open', 'US open')
fix_event('Kuala lumpur - kuala lumpur', 'Kuala lumpur')
fix_event('Oeiras (estoril)', 'Oeiras')
fix_event('Monterrey - monterrey', 'Monterrey')
fix_event('Istanbul - istanbul', 'Istanbul')
fix_event('Madrid - madird', 'Madrid')
fix_event('Madrid - madrid', 'Madrid')
fix_event('Antwerp - antwerp', 'Antwerp')
fix_event('Hobart - hobart', 'Hobart')
fix_event('Doha - doha', 'Doha')
fix_event('Mallorca  - mallorca', 'Mallorca')
fix_event('Wta finals', 'WTA finals')
fix_event('Dallas - dallas', 'Dallas')
fix_event('Cali - cali', 'Cali')
fix_event('Auckland - auckland', 'Auckland')
fix_event('Tokyo - tokyo', 'Tokyo')
fix_event('Shenzhen - shenzhen', 'Shenzhen')
fix_event('\'s-hertogenbosch', 'S-hertogenbosch')

#%%
def fix_usa(x):
    if x == 'Usa':
        return x.upper()
    else:
        return x
df['tour_country'] = df['tour_country'].apply(fix_usa)

def fix_shertoge(x):
    if x == "'S-":
        return 'SHE'
    else:
        return x
df['tour_country'] = df['tour_country'].apply(fix_shertoge)

#%%
def fix_tour_type(x):
    if x == 'Itf':
        return x.upper()
    if x == 'Tier i':
        return 'Premier 5'
    if x == 'R1' or x == 'R2':
        return 'Fed cup'
    if x == '':
        return 'Olympics'
    return x
df['tour_type'] = df['tour_type'].apply(fix_tour_type)

#%%
def fix_tour_code(x):
    if x == 'US':
        return 'USO'
    return x
df['tour_type'] = df['tour_type'].apply(fix_tour_type)

#%%
unique_tours = df['tour'].drop_duplicates()
unique_tours.to_csv('D:\\Programs\\Repositories\\Others')

#%%
wta_tour = df[df['tour_type']!='ITF']
wta_tour.groupby(by='match_result')['match_result'].count()
wta_tour.groupby(by='tour_type')['match_result'].count()
# wta_tour['tour'].count()

#%%
df.groupby(by='tour_surface')['year'].count()
df.groupby(by='match_result')['match_result'].count()

#%%
two_sets = df[df['num_sets']=='Two']


#%%
three_sets = df[df['num_sets']=='Three']

#%%
# df.to_csv('D:\\Programs\\Repositories\\Others')