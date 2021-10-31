password : ryqqir-pybxy7-vIghaf id: megner

EarthData Login
https://urs.earthdata.nasa.gov/users/new

[Summary]

the purpose of the text is to think through what kind of data
engineering is necessary to build a early alarm-system of wildfire in
germany. The system uses satellite imagery. 


## 1. Overview

Here we present some research of the landscape of wildife alaming system. My expectations were that such systems are already
made available, probably at multiple institues in all industrialized
coutries.  Landsat, for instance, has been taking satellite pictures
for 50 years, and the wildfire is of the immeidate interest not only
of the public but also of the business. After accute and repeating
threts in California, in Greece, in Australia, you would not have any
trouble to find a sponsor to finance a wildfire detection project.

However, it actually took me hours to reach such public alarming
systems on the web.

Many of the projects that are related to the forest/wildfire are not
fot the detection, but either

1. __Forecast__ : evaluate the threats, from the amount of vegetations
   that are prone to catch fire. The merit of such projects are to
   advise the forest authorities where to invest the money and man
   power.
   
2. __Evaluation__ : of the aftermath of the fires. This is critically
   important for the insurance payment not only individuals, but to
   agricultural industry.

At first, I was puzzled. The fast alarm would be the question that one
can monetize most easily. Why this topic looks almost circumvented? 

My speculation is that it is __technically hard__ or nearly
impossible, although everyone indeed would like to tackle. The
following is the line of thought.


1. __Wavelength__. The tempearture of the flames of the fire on wood
is 600-1500K.  The temperature range, if they are blackbody,
corresponds to the the emitting power peaking at the wavelengths of
2--5 um.  This is __near to thermal infrated__. The satelite imaging
has been performed in the visible walength (lambda < 1um), in
particular for teh millitary/intelligence purpose. There are plethora
of satellites on the sky, but only the minor part of them are
sensitive to the near-infrared, with even smaller part to the thermal
infrared.  Infrared equippements/cameras/spectrometers calls for much
harder challenges in terms of the cryogenics than visible instruments.

2. __Spatial Resolution__. In order to use satellite imagery
effectively for the fast alarm, i.e., the satellite imagery can report
a fire faster than the people on the ground who noticed it -- the
spatial resolution is critical. In order to get a fire detected, the
size of the fire must be as large as the spatial/(angular) resolution
of the camera. I assume that the fire must fill, or nearly fill the
whole one pixel of the detector to get caught. Currently only a few
newest satellited can have the spatial resolution of ~10 m sclae, with
majority of them, 300m-1km. If a wildfire is 300m wide, I suspect a
ground-based technique would be faster to catch it.

3. __Temporal Resolution__. I suspect this is the most critical factor
that so far makes the fast alarm of the wildfire nearly
impossible. Very minor part of the satellites on the sky are in the
synchronous orbits. It usually takes at least a day, if not a week,
that a satellite comes back to one location and notices the difference
(=fire). This is in a sence inevitable, as a satelite project would be
funded by a county (US) or a group of countries (EU). Such satellites
have to cover wide areas, and if we would like to keep the spatial
resolution high (see q2. above), the satellite has to move around to
cover the entire scope.

There is indeed a gap to close to enable __regioal__ fast wildfire
alarm in terms of hardward (satellite) and software (data pipeline,
deployment). The service has to have approximately in the following
shape.

1. High cadenz in monitoring (longest one hour). The satellites must
be watching same area continuously (will be expensive as an
operation. must be a micro satellite).

2. Thermal wavelength (> 3 um). Longer the wavelenth, one can catch
the low-temperature fire, that probably makes the time required to
notice shorter. One can also live 2.2 um, which is enough to catch the
fire of 1500K.

3. Spatial resolution should not be significantly worse than 10 m.
This will be the compromise among

- the height of satellite orbit.
- size of the detector
- area to cover.

Just a quick calculation. In order to cover Attica (a region in Greece
where Athen is located. about 84 km wide) with 10m pixel scale, the
detecto4 must be 8400px x 8400px big. If we aim for using ultra
resolution technique (using half-pixel shift to have higher
resolution), still need 4k x 4k infrared detector. It costs minimum
200k Euro, and more if we include readout electronics, drivers,
cyogenics (heatsink) and so on.

1) __Geostaionary orbit__\
The geostaionary orbit is 36000 km above the ground.
The angular resolution needed to resolve 10 m on the ground is,
10m/36000 km / (1/3600*3.14/180) = 0.05 arcsec = 50 mas.

To achieve this angular resolution at 2.2 um, the satellite has to
have a telescope with a diameter 8-m. That is impossible. 

2) __20-cm telescope__\
We will set the size of the telescope 20-cm.
The diffraction limited angular resolution is 2 arcsec.

The maximum height of the orbit of this satellite to resolve 10m
on the groun is,

10 / (1/3600*3.14/180) = 2.1 x 10^6 m = 2100 km.
This is a medium earth orbit, and the orbital period is about 130 min.

3) __Low Earth Orbit__ The satellite can be on the low earth orbit.
If it is 350 km above the ground like LANDSAT and ISS, the orbital
period is 91 min.  If a certain place on the Earth has to be covered
every 15 min, at least 6-satellites neccesary in the constellation.


#--------------------------------------------------------------

## 2. Existing Similar Services in Public

The following two would be the similar public service to report
wildfires as fast as opssible. 

(GWID) (Global Wildfire Information System (GWIS) )
https://gwis.jrc.ec.europa.eu/apps/gwis_current_situation/index.html

(EFFIS) (The European Forest Fire Information System (EFFIS))
https://effis.jrc.ec.europa.eu
(Current Situation Viewer)

#--------------------------------------------------------------

## 3. Satellites

What kind satellites are available? It is by no means to get an
overview as there are long linearge of satellites. The neat table we
needed is

- name 
- start of opertion
- end of operation
- if it is in operation
- available bands
- is near-infrared covered? (2.2 um)
- is thermal infrad covered? (>3 um)
- spatial resolution
- temporal resolution
- is europe covered?
- is data publicly available?
- is calibrated data publicly available?
- is data available in (near) real time? 

The following are the rellevant satellites, that are currently in
opertation, infrared, and data is publicly available.

### [US] 
(MODIS) MODerate resolution Imaging Spectroradiometer
https://nifc.maps.arcgis.com/home/item.html?id=b8f4033069f141729ffb298b7418b653
- part of __EOS__ (Earth-Observing System))
- consists of two satellites
  + Terra (looking at lands, EOS-AM) shortname of data MOD*
  + Aqua (looking at oceans, EOS-PM) shortname of data MYD* 

- 500m to 1 km resoulution
- global coverate every 1 to 2 days
- product 6 days cycle?

(VIIRS) Visible Infrared Imaging Radiometer Suite
https://nifc.maps.arcgis.com/home/item.html?id=dece90af1a0242dcbf0ca36d30276aa3
- mid-infrared available (<12 um)
- 375-750 m 
- can catch thermal hotspots


### [EU] Sentinel project (formally known as 'Copernicus')

(Sentinel 2) 
- up to 2.3 um

(Sentinel 3)
- include 3 um (SLSTR)
- 500 m resolution 
- (visible OLCI)
- in 'sentinel-3 Synergy'  OLCI and SLSTR are registered

Other sentinels are either not on the sky yet, or do not have infrared
sensitivity. Most hopeful future addition is __Setinnel 8__, which has
high spatial resolution and infrared sensitvity, but the launch is not
expected before 2029.

__Conclusions:--\
As a proof of concept, we will see if we can retrive MODIS data from its data
server by a Python script (as opposed to web-based GUI download).


#--------------------------------------------------------------
## 4. Data Access

### Complaint.

First, complaints. The data access in the earth observation industy is
a mess. In particular in US. The reason is

1. Too much money to fund new projects.
2. Two many govermental agentcies in play
   (ocean, land, geo, space, civil, agri, security...)
3. Old projects are not deprecated. 

The result is too many redandant systems where it is not even clear
which one is the latest. I do understand researchers resist to close
working systems at their local institutes. However, offering (and
keeping maintenance) perl/shell-script system to the public, just
spreads sparse man power even sparser. One can see numerous
non-working solutions that are maintained half-mindedly.

### Data Servers

There are somehow lots of outlets for same data.  The followings are
only the small fraction of them, as I found on the way.

[US]
- (EARTHDATA) (USGS)
  https://lpdaac.usgs.gov/products/mod11a1v006/
  + MOD11A1 (need to know which MODIS data you woudl like to see)

- (MODIS Data Products)
  https://modis.gsfc.nasa.gov/data/dataprod/

- (LANCE) Land, Atmosphere Near-real-time Capability for EOS (NASA)
   https://lance4.modaps.eosdis.nasa.gov/modis/
   + MODIS-NRT1 (Terra) [MODIS-NRT2 is Aqua]
   + NRT (near real time. 3-5 hours)
   https://nrt4.modaps.eosdis.nasa.gov/archive/allData/61/MOD11_L2/Recent   

- (MODAPS Services)
   https://modaps.modaps.eosdis.nasa.gov/services/about/nomenclature.html
   + just too many of them.
   + documentation is good. 

[EU]
- (Sentinel Data Access)
   https://sentinel.esa.int/web/sentinel/sentinel-data-access

- (Copernicus Open Access Hub)
   https://scihub.copernicus.eu

- (GWIS) Global Wildfire Information System (GEO + Copernicus)
   https://gwis.jrc.ec.europa.eu/applications/data-and-services
   + data already reduced to text tables. 
   + No raw images. 

- Harmonized Landsat and Sentinel-2 (HLS) 
   + munich bounding box 47.64202,9.07351 49.92768,12.13283

__Conclusions:__

1. We will concentrate on MODIS data, and its data products
   - calibrated and reduced, instead of raw images
   - images, instead of tabulated data.

2. Download it from the internet from python script. 
   (not with GUI)

#--------------------------------------------------------------
## 5. Identify files to download

### Goal of Data Engineering.

Originaly, I wanted finish until 5. in the To-Do list below, but it
took too long to do the research. Here I will concentrate on up to
downloading files. FIrst, we have to identify which files to download.


###  What datasets are avilable, and which one we need.

MODIS data consists of lots of[ productlines](https://modis.gsfc.nasa.gov/data/dataprod/). Just pick up a few that are related to the wildfire
and the surface temperature of the land,

(MOD11) MODIS Land Surface Temperature and Emissivity (LST&E)
  + bands 31 and 32.
  - MOD11A1 LST&E daily level3 Global 1 km 
  - MOD11A2 LST&E 8-day level 3 Global 1 km
  - MOD11_L2 Daily 5-min level 2 swath 1 km
  
  => We will take MOD11A1.

  - Access Data : https://lpdaac.usgs.gov/products/mod11a1v061/ => to 
  - User Guid : https://icess.eri.ucsb.edu/modis/LstUsrGuide/usrguide_1dtil.html

(MOD21) MODIS Land Surface Temperature and Emissivity (MOD21) (LST&E)
  What is different from MOD11?
   - bands 29, 31, 32
   - 3-5K bias in MOD11 is corercted
   - full radiation transfer (borrowd from ASTER project)

   - MOD21A1D LST&E daily level-3 Global 1 km Day
   - MOD21A1N LST&E daily level-3 Global 1 km Night
   - MOD21A2 LST&E 8-day level 3 Global 1 km
   - MOD21_L2 Daily 5-min level 2 swath 1 km

   => Looks better than MOD11.

=> conclusion: MOD21A1D 

(MOD14) MODIS Thermal Anomalies - Active Fire
    - 4 and 11 um radiance. Just 2 bands

    - MOD14A1 : daily level 3 global 1 km 
    - MOD14A2 : 8-day level 3 global 1 km
    - MOD14   : 5-min level 2 swqth 1 km

    => MOD14A1
    This is kind of `testset`. We will start with MOD21A1D
    and compre our conclusion (fire detection) wiht MOD14A1. 


### File types

   Which file type we should retriece? 
   
   - `NetCDF` (Network Common Data Form)
     + standard for earth obseving community
   - `NcML` represents metadata part of `NetCDF` in `xml`
   - `HDF4` and `HDF5` (Hieralchical Data Format)
     + I do not undrstand what differes from NetCDF
     + it also has `xml` representatin. 
   
__Conclusion:__ \
   1. I guess we will get either NetCDF or HDF4.

#--------------------------------------------------------------
## 6. Data Access points.

There are at least 5 differnet ways to download MODIS
MOD21A1. 

1. Data Pool => LP DAAC (LP: Land Process)
2. NASA Earthdata Search : GUI base => drop

3. Daac2Disk : a small program available on here
   https://lpdaac.usgs.gov/tools/daac2diskscripts/

   (Manual)
   https://lpdaac.usgs.gov/documents/202/DAAC2DiskUserGuide_QSeQHbQ.pdf
   + You need to give exceptions in 'System Preference'
     on MacOSX for 'Security & Privacy'
   + to download the script
   + to run the script
   + make executable `chmod +x Daac2Dick_mac'

   Need 'shortname' to search. Could not find
   the definition/list of names. 
   

4. LDOPE : Land Data Operational Products Evaluation
   https://lpdaac.usgs.gov/tools/ldope/

   + You need to give exceptions in 'System Preference'
     on MacOSX for 'Security & Privacy' to run the app.

   + Installer for mac does not run. => drop

5. OPenDAP   : GUI base => drop
   https://lpdaac.usgs.gov/tools/opendap/
   https://earthdata.nasa.gov/collaborate/open-data-services-and-software/api/opendap/opendap-user-guide
   - directory structure with no explanation
   - web service => drop

6. Pydap 
   https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+PyDAP
    - documentation too old
    + a few python packages used there do not exist any more.
    - could open session

7. Python/requests : cannot open session
   https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+Python
    - can work around.


--Conclusion:__ \
1. Get to MODIS Data products https://modis.gsfc.nasa.gov/data/dataprod/
2. Clickk on MOD21.
3. Select MOD21A1D
4. 'ACCESS DATA' at a menu-bar under the banner.
5. Data Pool (just to get a directory and the file name)
6. Launch Data Pool (in the banner)
7. Choose the directory `MOLT`
   + MOLA : MODIS Land Anomaly? => Aqua data
   + MOLT : MODIS Land Temperature? 
   + MOTA : MODIS Thermal Anomaly? 

8. Go down to the end of page
   + Record starts from 2000.02.24.

9. How to read the file name. 
From Modas Servieces: 
https://modaps.modaps.eosdis.nasa.gov/services/about/nomenclature.html

```
Generalized Filenaming Convention

MOD01.A2002032.1015.003.2002034184356.hdf
 
aaaaa  bbbbccc dddd eee fffffffffffff ggg
a) MODIS product short name, e.g. "MOD01" refers to the MODIS Level 1A Radiance product. "MOD" signifies Terra/MODIS, whereas "MYD" signifies Aqua/MODIS.

b) Year in which data was collected by the instrument, e.g. 2002.

c) Day on which data was collected by the instrument, given in Day of Year. For example, "032" is February 1st, i.e. the 32nd day of the year.

d) Time at which data was collected, given in Universal Time Coordinate (UTC) or Greenwich Mean Time (GMT).

e) Collection (version) number.

f) Production date and time, given in year, day-of-year, hours, minutes, and seconds, in the form yyyydddhhmmss.

g) File type extension, e.g. "hdf" is Hierarchical Data Format. All MODIS data are available in HDF format.

```
10. Okay, let us target to download 

URL : https://e4ftl01.cr.usgs.gov/MOLT/MOD21A1D.061/2021.10.28/
FILENAME : MOD21A1D.A2021301.h35v10.061.2021303035120.hdf 

#--------------------------------------------------------------

## 7. Coding

### Authentification
Accessing data throught EARTHDATA requires user registration.
https://urs.earthdata.nasa.gov

Just pick up username, password, e-mail address, and so on.
Nothing complicated. You will get an e-mal for a confirmation.
This __Username__ and __Password__ will be necessary in the
codign with Python. 


### Python Script

It took long time to reach, but the code itself is short.
Here is the whole code. 

'''
import pdb
import requests
import io
from pathlib import Path
import sys
import os


def set_cwd(CWE):
    if Path('.').cwd != CWD:
        os.chdir(CWD)


def get_modis(USERNAME, PASSWORD):

    URL = 'https://e4ftl01.cr.usgs.gov/MOLT/MOD11A1.061/2021.10.26/'
    FILENAME = 'MOD11A1.A2021299.h00v08.061.2021301153445.hdf'

    OUT_DIR = Path('../data3/')
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


if __name__ == '__main__':
    args = sys.argv

    if len(args) == 3:
        USERNAME = args[1]
        PASSWORD = args[2]

    CWD = '/Users/meg/git8/scr/'
    set_cwd(CWD)
    r = get_modis(USERNAME, PASSWORD)
    print(r.text)
    print(r.reason)


'''

### HDFView

To check up the contents of an HDF file that we will download to a
local machine, get `HDFView`.
https://portal.hdfgroup.org/display/support/Download+HDFView

   + You need to give exception permission in 'System Preference' on
     MacOSX at 'Security & Privacy' to run the app.


#--------------------------------------------------------------

## 8. To-Do

1. Look at the contents of HDF files closer
   + show images from python script
   + how to manipulate array data
   + `astropy`?

2. Study seach criterion. So that one can freely select
   + Munich-Augsburg area (or California/Turkey/Greece)
   + in favored time preriod. 

3. Try NRT (near real-time) data.
   + Scheculding.
   + AirFlow
   + PySpark

4. Try raw (but calibrated) image.
   + there is an interesting documents about ATBT.\
     __ATBD__ (Algorithm Theoretical Basis Documents)
     https://modis.gsfc.nasa.gov/data/atbd/

   + useful to make a calibration plan. 

'''
MODIS Calibrated Radiances
https://modis.gsfc.nasa.gov/data/dataprod/mod02.php

The Level 1B data set contains calibrated and geolocated at-aperture
radiances for 36 bands generated from MODIS Level 1A sensor counts
(MOD 01). The radiances are in W/(m2-µm-sr). In addition, reflectance
may be determined for the solar reflective bands (bands 1-19, 26)
through knowledge of the solar irradiance (e.g., determined from MODIS
solar-diffuser data, and from the target-illumination
geometry). Additional data are provided, including quality flags,
error estimates, and calibration data.
'''

5. Calculate temperature.
   + creats band-temperature templates. 

6. Alart system.
   + calculate the difference/anomaly, and raise the flag.

7. Frontend. 

8. VIIRS

9. Sentinel-2

#==============================================================
# END
#==============================================================


3 bands (29, 31, and 32 [what is the wavelength?])
  ASTER: radiative transfer
swath =  level 2 product
MOD21_L2 50min swath
MOD21A1D L3 1 km SIN Grid Day
MOD21A1N L3 1 km SIN Grid Night
MOD21A2 8-day L3 Global 1 km

(MOD14)

MOD14 : Thermal Anomalies. Just 2 bands 4 and 11 um 
MOD14A1 : Daily L3 Global 1 km ('L3' means level3a  )
MOD14A2 : 8-day L3 Global 1 km
MOD14   : 5-min L2 Swqth 1 km


2. We will focus on the Land Surface Temperature and
   Emissivity data of MODIS 
   https://modis.gsfc.nasa.gov/data/dataprod/
   
   - The short name of the data : MOD11A1
   - Daily
   - Levelt 3
   - global
   - 1 km resolution
     
   + retrieve from `EARTHDATA` above.


MODIS Calibrated Radiances
https://modis.gsfc.nasa.gov/data/dataprod/mod02.php

"The Level 1B data set contains calibrated and geolocated at-aperture
radiances for 36 bands generated from MODIS Level 1A sensor counts
(MOD 01). The radiances are in W/(m2-µm-sr). In addition, reflectance
may be determined for the solar reflective bands (bands 1-19, 26)
through knowledge of the solar irradiance (e.g., determined from MODIS
solar-diffuser data, and from the target-illumination
geometry). Additional data are provided, including quality flags,
error estimates, and calibration data."

MODIS/Terra Near Real Time (NRT) Land Surface Temperature/Emissivity
5-Min L2 Swath 1km

MOD11
MOD11A1 LST&E daily  L3 Global 1 km 
https://lpdaac.usgs.gov/products/mod11a1v061/ => access Data
https://icess.eri.ucsb.edu/modis/LstUsrGuide/usrguide_1dtil.html

MOD11A2 LST&E 8-day  L3 Global 1 km
MOD11A3 LST&E daily  L3 Global 6 km

MOD21 :  MODIS Land Surface Temperature and Emissivity (MOD21) (LST&E)
3 bands (29, 31, and 32 [what is the wavelength?])
  ASTER: radiative transfer
swath =  level 2 product
MOD21_L2 50min swath
MOD21A1D L3 1 km SIN Grid Day
MOD21A1N L3 1 km SIN Grid Night
MOD21A2 8-day L3 Global 1 km


MOD14 : Thermal Anomalies. Just 2 bands 4 and 11 um 
MOD14A1 : Daily L3 Global 1 km ('L3' means level3a  )
MOD14A2 : 8-day L3 Global 1 km
MOD14   : 5-min L2 Swqth 1 km

;---------
1. Data Pool
2. OPenDAP   : GUI base
3. Daac2Disk : short name
4. pydap     : cannot open session


Data Pool => like web directory
Thermal anomaly https://e4ftl01.cr.usgs.gov/MOTA/ => no 14A1
Land temperature  

OPeNDAP("Open-source Project for a Network Data Access Protocol"
OPenDAP
https://opendap.cr.usgs.gov/opendap/hyrax/MOD11A1.061/contents.html

http://opendap.cr.usgs.gov/opendap/hyrax/MOD11A1.061/h00v08.ncml?Latitude[47][50],Longitude[9][12]

https://lpdaac.usgs.gov/documents/603/DAAC2DiskUserGuide_20200313.pdf
Mac version does not run => canno 
=> yet another potal for data access
https://search.earthdata.nasa.gov/search?q=SENTINEL&ac=truehttps://search.earthdata.nasa.gov/search?q=SENTINEL&ac=true

DAAC
need to create a 'script' on the earthdata website, and use it as
an input file when you use DAAC.

./Daac2Disk_mac --shortname MOD11A1 --versionid 061 --browse --begin 2021-10-25 --end 2021-10-30 --bbox -116 33 -96 45.5 --output ./data

##  3. Convert the set with temperature map.



## 6. Tech Stack

- python
  + retreival
  + transform
  + visualization

+ do we need spark? 
  => probably not this time.



## 7. Coding

[Refrence] what kind of algorithms are used for the calibration and
the prepreocessing of data.

(MODIS) ATBD (Algorithm Theoretical Basis Documents)
https://modis.gsfc.nasa.gov/data/atbd/

There are several concerns.

+ registered?

+ optical depth?

+ filling factor?

+ graybody?

+ pseudo graybody?
  as the
  high temperature area is expected to be smaller than
  the low temprature area. This makes the apparent flame
  temperature cooler than the true temperature. 
  
+ speed.
  + a blackbody fitting at each pixel cost computational
    resources. Blackbody templates of each filter (=wavelength) should
    be prepared beforehand with grid of temperature.  and just take
    the one that show highest correlation.


#-----------------

it is almost funny that one cannot never reach the data server.
MODIS -> view all data -> Get started with Data -> Collection overview

daily per-pixel Land Surface Temperature and Emissivity (LST&E) with
1 kilometer (km) spatial resolution in a 1,200 by 1,200 km grid.
 
LST_Day_1km	Daytime Land Surface Temperature	Kelvin	16-bit unsigned integer	0	N/A	7500 to 65535	0.02	N/A

MOD11A1 061:
Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Land
Surface Temperature/Emissivity Daily (MOD11A1) Version 6.1.
The pixel temperature value is derived from the MOD11_L2 swath product.


okay let us focus on 11A1
Data Access


MOD14A1 v061 : 
The Terra Moderate Resolution Imaging Spectroradiometer (MODIS)
Thermal Anomalies and Fire Daily (MOD14A1) Version 6.1

mess: when you add a new tool, you did not deprecate the old one.
it is even hard which tool is the latest.

how to use pydap
https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+PyDAP
1. urllib2 => urllib
2. cookielib => cookiejar


Harmonized Landsat and Sentinel-2 (HLS) 
munich bounding box 47.64202,9.07351 49.92768,12.13283

and how to retrieve it? 

https://lpdaac.usgs.gov/product_search/?collections=Combined+MODIS&collections=Terra+MODIS&status=Operational&view=list&per_page=90&page=1

(ASTER GED) but from MODIS 
Principal Investigator: Glynn Hulley, Jet Propulsion Laboratory (JPL)

Using data from the Advanced Spaceborne Thermal Emission and
Reflection Radiometer (ASTER) on NASA's Terra spacecraft, NASA/JPL
derived the most detailed global emissivity map of the Earth, termed
the ASTER Global Emissivity Database (GED).

2. Retrieve satellite images from data server

- One small region with positive fire
+ lets try turkey this summer
- one region is fine, but all avaialble wagelength 






#========================================================

[Data Engineering]

- goal

- identify data source


seneinel 8 not yet? (2029)
sentinel 2 (15-30 days cycle
sentinel 1, 2,3, and 5P currently available

sentinel 3: VNIR (0.5-0.7 um) SWIR (1.4-3 um) <++++
(sentinel 3 bands) resolution 500m...

(copernicus API hub)
user guide https://scihub.copernicus.eu/twiki/do/view/SciHubUserGuide/BatchScripting?redirectedfrom=SciHubUserGuide.8BatchScripting


;---------------------------

MODIS VIIRS : 6 day cycle
MODIS 1 km resolution
VIIRS Thermal Hotspot
reported within 3 hours 15 minutes after the detection
;---------------------------
GeoMAC : no longer exist

LANDFIRE : before wildfire happens (risk management / danger prediction)
MTBS : after wildfire happened (severity)
600-1500K

(sentinel Data Access)
https://sentinel.esa.int/web/sentinel/sentinel-data-access

(Copernicus Open Access Hub)
https://scihub.copernicus.eu


(GWIS) data service
https://gwis.jrc.ec.europa.eu/applications/data-and-services


[Curren situation]
(GWID) (Global Wildfire Information System (GWIS) )
https://gwis.jrc.ec.europa.eu/apps/gwis_current_situation/index.html

(EFFIS) (The European Forest Fire Information System (EFFIS))
https://effis.jrc.ec.europa.eu
(Current Situation Viewer)

(Copernicus Emergency Management Service) (include flood) -> EFFIS
https://www.copernicus.eu/en/copernicus-services/emergency

#========================================================

[micro_course] => done

(first find out user name of the data owner)

how to list up all datasets (not only competition dataset)
kaggle d list -h
kaggle d list --user alexisbcook
kaggle d download alexisbcook/geospatial-learn-course-data

#========================================================

- wildwire detection

+ Herschel experience

+ experiment / calibration
  - filling facor
  - optical depth

  - different kinds of forest fire
    + desert
    + grass
    + bush
    + sparse forest
    + dense forest
    + short trees
    + tall trees
    + warm environment (soil)
    + cold environment (soil)
    + snow filed
    + no wind
    + windy
    + without smoke 
    + with smoke (high backgroun)
    + low altitude
    + high altitude

  - check first exsiting data
  
LANDFIRE : before wildfire happens (risk management / danger prediction)
MTBS : after wildfire happened (severity)

