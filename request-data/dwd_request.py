import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from zipfile import ZipFile
import io

#Link with open data
dwd_url0005 = r'https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D0005.csv.zip'

response = requests.get(dwd_url0005, stream=True, verify=True)
with ZipFile(io.BytesIO(response.content)) as myzip:
    with myzip.open(myzip.namelist()[0]) as myfile:
        df0005 = pd.read_csv(myfile, sep = ';')

        