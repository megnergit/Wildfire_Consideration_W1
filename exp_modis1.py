import pdb
import requests
import io
from pathlib import Path
import sys
import os

def set_cwd(CWD):
    if Path('.').cwd != CWD:
        os.chdir(CWD)

def get_modis(USERNAME, PASSWORD):

    URL = 'https://e4ftl01.cr.usgs.gov/MOLT/MOD11A1.061/2021.10.26/'
    FILENAME = 'MOD11A1.A2021299.h00v08.061.2021301153445.hdf'

    OUT_DIR = Path('./data3')
    HDF_FILE = Path('dataset.hdf')

    if (OUT_DIR/HDF_FILE).exists():
        (OUT_DIR/HDF_FILE).unlink(missing_ok=True)

    with requests.Session() as session:
        r1 = session.request('get', URL+FILENAME)
        r = session.get(r1.url, auth=(USERNAME, PASSWORD), timeout=120)

        with open(OUT_DIR/HDF_FILE, 'wb') as hd5:
            for chunk in r.iter_content(chunk_size=io.DEFAULT_BUFFER_SIZE):
                hd5.write(chunk)

    return r


# r = get_modis(USERNAME, PASSWORD)
# print(r.text)

if __name__ == '__main__':
    args = sys.argv

    if len(args) == 3:
        USERNAME = args[1]
        PASSWORD = args[2]

    CWD = '/Users/meg/git8/scr/'
    set_cwd(CWD)
    r = get_modis(USERNAME, PASSWORD)
    print(r.reason)

#
#
#  =========================================================
