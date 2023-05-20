from requests_toolbelt.sessions import BaseUrlSession
from bs4 import BeautifulSoup as Soup
import pandas as pd


s = BaseUrlSession('https://raex-rr.com')
response = s.get('ESG/ESG_companies/ESG_rating_companies/2023.5')

soup = Soup(response.content, 'html.parser')
df, = pd.read_html(str(soup.select_one('#rrp_table_wrapper')))
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth',None)
# print(df)