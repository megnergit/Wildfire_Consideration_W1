# Wildfire Fast Alarming System - Is it feasible? 

## 1. Summary and Conclusion

The purpose of the text is to think through the feasibility of a
regional, fast, wildfire alarming-system that is based on the
monitoring from the space. We will first present an overview of the
current status of the field, including similar public systems working
now. The second half of the text is dedicated to the data engineering.
We will discuss what kind of data sources are available, and how we
can extract the data from there. We will perform an experiment on
retrieving the data from a MODIS server with a Python-base script (as
opposed to a manual, web/GUI-base download) with a proper
authentication.

My preliminary conclusions are that such a regional system would
suffer from one or two of the following problems. 

1. The telescope must be too big (~8m)
2. The number of satellites in the constellation is too many (> 6)
3. The size of the infrared array is too large and expensive (100k x 100k)
4. The area to be covered is too small and a regional government cannot
   fund the project. 

For the discussions behind the conclusion above,
jump to ## 9. System Design Considerations.

<!------------------------------------------------------------->
## 2. Overview

Here we present a research on the landscape of the state-of-the-art
wildfire alarming system. My expectations were that such systems are
already available, at multiple institutes in multiple industrialized
countries. Landsat, for instance, has been taking pictures for 50
years by now, and the wildfire is of the immediate interest not only
of the public but also of the business. After acute and repeating
threats in California, in Greece, in Australia, you would not have any
trouble to find a sponsor to finance a wildfire detection
program. However, it actually took me hours to reach such public
alarming systems on the web. Many of the projects that are related to
the forest/wildfire are not really for the detection, but either one
of the two below.

1. __Forecast :__ evaluate the wildfire threats from the amount of the
   dry vegetations (=fuel) that are prone to catch fire. The merit of
   such projects are to advise the authorities where to invest the
   money and the man power for the efficient preventions.
   
2. __Evaluation :__ of the aftermath of the fires. This is critically
   important for the insurance payments not only for individuals, but
   also for the agricultural industry.

At first, I was puzzled. The fast alarm would be a question that one
can monetize most easily. Why this topic looks almost circumvented?

My understanding after some research is that, indeed everbody wants to
tackle the fast alarm, but it is __technically highly challenging__,
or nearly impossible. The following is the line of thought.

1. __Wavelength :__ The temperature of the flames of the fire on wood
is 600-1500 K. The temperature range, if they are blackbody,
corresponds to the emitting power peaking at the wavelengths 2-5
um. This is __near__ to __thermal infrared__. The satellite imaging
has been traditionally performed in the visible wavelength (< 0.8 um),
in particular, for the military- and intelligence-purposes. There are
plethora of satellites on the sky, but only the minor fraction of them
are sensitive in the near-infrared, with even smaller fraction of them
to the thermal infrared. Infrared equipments/cameras/spectrometers set
much higher hurdles in terms of the cryogenics, which is not an issue
in the visible instruments.

2. __Spatial Resolution :__ In order to be effective in using the
satellite imagery for the fast alarm, i.e., the satellite imagery must
report a fire faster than the people on the ground would do --- the
spatial resolution is critical. In order to get a fire detected, the
fire must fill, or nearly fill, the whole one pixel of the
detector. Currently only a few newest satellites have the spatial
resolutions of ~10 m scale, with majority of them, 300 m to 1 km. If a
wildfire is 300 m wide, I suspect a ground-based technique could
report it faster.

3. __Temporal Resolution :__ I suspect this is the most critical issue
that makes the fast wildfire alarm-system from space nearly
impossible. We will discuss later, but observing the earth from the
geo-synchronous orbit is nearly impossible. The majority of the earth
observing systems are on the low earth orbit (height < 2000km). With a
tilted orbit, it takes at least a day, if not a week, that a satellite
can come back to one location again, and notices something is
different (=fire). The choice of the orbit is in a sense
intentional. A satellite project is funded by a country (US) or a
group of countries (EU). The satellites have to cover wide areas, and
if we would like to keep the spatial resolution high enough (therefore
cannot be in the high orbits), the satellite has to move around to
cover the entire area.

Because of the technical challenges discussed above, there is indeed
a gap to close with a __regional__, fast wildfire alarming system.  To
differentiate from existing systems, the service has to have
approximately the following specs. 

1. High cadence in monitoring (15 minutes ideal, longest one hour of
   intervals). The satellites must be watching a same area
   continuously, or have to come back frequent enough. The operation
   would be expensive, and indeed suits for micro satellite systems.

2. Thermal wavelength (> 3 um) sensitivity. The longer the wavelength,
   the lower the temperature a heat source could be to get
   caught. This means that the lead time of the flame detection will
   be shorter. One can also live with 2.2 um, which is enough to catch
   the fire of the temperature 1500 K.

3. Spatial resolution should not be significantly worse than 10 m.
   This will be set by the compromises among

    - height of the satellite orbit
    - size of the detector
    - area to cover

Just a quick calculation. In order to cover Attica (a region in Greece
where Athen is located. About 84 km wide) with 10 m pixel scale, the
detector must be 8400 px times 8400 px large. If we are to use ultra
resolution technique (using half-pixel shifts to attain twice higher
resolution), still need 4k x 4k infrared detector. It costs minimum
200k Euro, and more, if we include readout electronics, drivers,
cryogenics (heatsinks) and so on.

1) __Geostationary Orbit__\
The orbit is 36000 km above the ground. The angular resolution needed
to resolve 10 m on the ground is, 10m/36000 km / (1/3600*3.14/180) =
0.05 arcsec, or 50 mas. To achieve this angular resolution at 2.2 um,
the satellite has to have a telescope with a diameter of about 8-m.
That is impossible.

2) __20-cm Telescope__\
We shal set the size of the telescope 20-cm. The diffraction-limited
angular-resolution of the telescope is 2 arcsec at 2.2 um. The maximum
height that this satellite can go, while still resolving 10 m on the
ground, is 10 / (1/3600*3.14/180) = 2.1 x 10^6 m = 2100 km.
This is a medium earth orbit, and the orbital period is about 130 min.

3) __Low Earth Orbit__\
The satellite can be on the low earth
orbit. This is the orbit where Landsats and ISS are working. The
orbital period at 350 km above the ground is 91 min. If a certain
place on the earth has to be covered every 15 min, at least
6-satellites are necessary in the constellation.

<!-------------------------------------------------------------->

## 3. Existing Similar Services in Public

The following two would be the similar public services that report
wildfires as fast as possible.

__GWID__
[Global Wildfire Information System](https://gwis.jrc.ec.europa.eu/apps/gwis_current_situation/index.html)\
__EFFIS__
[The European Forest Fire Information System](https://effis.jrc.ec.europa.eu)


<!-------------------------------------------------------------->

## 4. Satellites and Projects

What kind satellites are available as a resource of the wildfire
detection? It is by no means simple to get a good overview of the 
current and the historical missions that have long lineage by now. 
We needed the following informations  for each.

- name 
- start of operation/ end of operation /if it is in operation
- bands / near-infrared covered? (2.2 um)/thermal infrared covered? (>3 um)
- spatial resolution
- temporal resolution
- is Europe covered?
- is data publicly available?
- is data flux-calibrated?
- is data available in (near) real time? 

After some research, we found that the followings are the relevant
satellites for our mission, which are currently in operation, are
working in the infrared, and their data is publicly available.

### US : Earth-Observing System

__MODIS__ [MODerate resolution Imaging Spectroradiometer](https://nifc.maps.arcgis.com/home/item.html?id=b8f4033069f141729ffb298b7418b653)
- Consists of two satellites
  + Terra (looking at lands, EOS-AM) shortname of data MOD*
  + Aqua (looking at oceans, EOS-PM) shortname of data MYD* 
- Mid-infrared available (< 14um)
- Spatial resolution 500m to 1 km.
- Global coverage every 1 to 2 days

__VIIRS__ [Visible Infrared Imaging Radiometer Suite](https://nifc.maps.arcgis.com/home/item.html?id=dece90af1a0242dcbf0ca36d30276aa3)
- Mid-infrared available (< 13 um)
- Spatial resolution 375m to 750m.
- Global coverage every 1 to 2 days
- Can catch thermal hotspots

### EU: Sentinel project (formally known as 'Copernicus')

__Sentinel 2__ 
- Wavelength up to 2.2 um
- Spatial resolution 10-60m

__Sentinel 3__
- Wavelength up to 11 um (SLSTR)
- Spatial resolution 500 - 1km

Other Sentinels are either not on the sky yet, or do not have infrared
sensitivity. Most hopeful future addition is __Sentinel 8__, which has
high spatial resolution and infrared sensitivity, but the launch is not
planned before 2029.

__Conclusions:__\
As a proof of concept, we will see if we can retrieve MODIS data from
its data server by a Python script (as opposed to a manual web-based
GUI).

<!--------------------------------------------------------------> 
## 5. Data Access 

### First I need to vent

The data access in the earth observation industry is a mess. In
particular in the US. The reasons are the following.

1. Too much money to fund new projects.  
2. Old projects are not deprecated.  
3. Two many governmental agencies in play \
   (ocean, land-, geo-, space, civil-, agri-, intel- and more).

The result is too many redundant systems where it is not even clear
which one is the latest. I do understand researchers do not like to
close the working systems at their local institutes. However, offering
(and keeping the maintenance of) perl/shell-script-base systems to the
public just dilutes already sparse man power even sparser. One can see
numerous non-working solutions still on their web sites with
half-minded maintenance status.

### Data Servers

There are somehow lots of outlets for same data. The followings are
only the small fraction of them, as I encountered on the way.

#### US
- [__Earthdata__](https://lpdaac.usgs.gov/products/mod11a1v006/) (USGS)
  + One can learn which MODIS data to use for a project.

- [__MODIS Data Products__](https://modis.gsfc.nasa.gov/data/dataprod/)

- [__LANCE__](https://lance4.modaps.eosdis.nasa.gov/modis/) Land, Atmosphere Near-real-time Capability for EOS (NASA)
   + MODIS-NRT1 (Terra) [MODIS-NRT2 is Aqua]
   + [NRT](https://nrt4.modaps.eosdis.nasa.gov/archive/allData/61/MOD11_L2/Recent)  (near real time. 3-5 hours)

- [__MODAPS Services__](https://modaps.modaps.eosdis.nasa.gov/services/about/nomenclature.html)
   + Just too many of them.
   + Documentation is good. 

#### EU

- [__Sentinel Data Access__](https://sentinel.esa.int/web/sentinel/sentinel-data-access)

- [__Copernicus Open Access Hub__](https://scihub.copernicus.eu)

- [__GWIS__](https://gwis.jrc.ec.europa.eu/applications/data-and-services)
   Global Wildfire Information System (GEO + Copernicus)
   + Data already reduced to text tables. 
   + No raw images. 

- [__HLS__](https://hls.gsfc.nasa.gov)
   Harmonized Landsat and Sentinel-2

__Conclusions:__
1. We will concentrate on MODIS data, and its data products
  - Calibrated and reduced, instead of raw images
  - Images, instead of tabulated data.
2. Download it from the internet from python script
   (not with GUI).

<!-------------------------------------------------------------->

## 6. Identify Available Files and What We Need

### Goal of data engineering

Originally, I wanted to finish until 5 in the To-Do list at the 
end of this report (=calculating the temperature pixel by pixel), 
but it took me too long to get the latest status of the field. 
Here I will concentrate on extracting the data. We will first 
identify which files we need.

###  What datasets are available, and which one we need

MODIS data consists of numerous [product
lines](https://modis.gsfc.nasa.gov/data/dataprod/). Just picking up a few
products that are related to the wildfire and the surface 
temperature of the land,

(MOD11) MODIS Land Surface Temperature and Emissivity (LST&E)
  + Bands 31 and 32.
  - MOD11A1 LST&E daily level3 Global 1 km 
  - MOD11A2 LST&E 8-day level 3 Global 1 km
  - MOD11_L2 Daily 5-min level 2 swath 1 km

  - [Data Access](https://lpdaac.usgs.gov/products/mod11a1v061/) 
  - [User Guide](https://icess.eri.ucsb.edu/modis/LstUsrGuide/usrguide_1dtil.html)

(MOD21) MODIS Land Surface Temperature and Emissivity (MOD21) (LST&E)
  Difference from MOD11
   - Bands 29, 31, 32
   - 3-5 K bias in MOD11 is corrected
   - Full radiation transfer implemented (from ASTER project)

   - MOD21A1D LST&E daily level-3 Global 1 km Day
   - MOD21A1N LST&E daily level-3 Global 1 km Night
   - MOD21A2 LST&E 8-day level 3 Global 1 km
   - MOD21_L2 Daily 5-min level 2 swath 1 km

(MOD14) MODIS Thermal Anomalies -- Active Fire

    - 4 and 11 um radiance. Just 2 bands
    - MOD14A1 : daily level 3 global 1 km 
    - MOD14A2 : 8-day level 3 global 1 km
    - MOD14   : 5-min level 2 swath 1 km

### File types

   Which file type we should retrieve? 
   
   - `NetCDF` (Network Common Data Form)
     + standard in the earth observing community
   - `NcML` represents metadata part of `NetCDF` in `xml`
   - `HDF4` and `HDF5` (Hierarchical Data Format)
     + I do not understand the differences from NetCDF
     + It also has `xml` representation. 
   
__Conclusion:__\
   1. MOD11A1.
   2. MOD21A1 is better.
   3. MOD14A1 will make  a 'test set' to our experiments
      that provides 'ground truth' of the presence of
      the wildfire. 
   4. Let us look at HDF files first. 

--------------------------------------------------------------
## 7. Data Access Points

There are at least 7 different ways to retrieve MODIS MOD21A1 data 
rom its server.

1. Data Pool : this leads users to LP DAAC (LP: Land Process)

2. NASA Earthdata Search : GUI base => drop

3. Daac2Disk : a small data-transfer program available on here
   https://lpdaac.usgs.gov/tools/daac2diskscripts/
   The program takes care of authentication. 

   (User Manual)
   https://lpdaac.usgs.gov/documents/202/DAAC2DiskUserGuide_QSeQHbQ.pdf

   + On MacOSX, we need to set a special permission in 'System Preference'
     -> 'Security & Privacy' to download the script and run it locally.
   + Make the program executable by `chmod +x Daac2Dick_mac'

   Need 'shortname' to search the files, but could not find the
   definition of them.
   

4. LDOPE : Land Data Operational Products Evaluation
   https://lpdaac.usgs.gov/tools/ldope/

   + On MacOSX, we need to set a special permission in 'System
   Preference' -> 'Security & Privacy' to download the installer.
 
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
    - could not open a session

7. Python/requests 
   https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+Python
    - cannot open a session in the original presentation, but 
    - can work around.

__Conclusion:__\ 
1. Get to MODIS Data products https://modis.gsfc.nasa.gov/data/dataprod/
2. Click on MOD21.
3. Select MOD21A1D
4. 'ACCESS DATA' at a menu-bar under the banner.
5. Data Pool (just to get the  directory and the file name)
6. 'Launch Data Pool' (in the banner)
7. Choose the directory `MOLT`
   + MOLA : MODIS Land Anomaly? => Aqua data
   + MOLT : MODIS Land Temperature? 
   + MOTA : MODIS Thermal Anomaly? 

8. Go down to the end of the page
   + Record starts from 2000.02.24.

9. See MODAPS Services to learn what the file names mean.
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
10. Okay, let us target the following file.   

```
URL : https://e4ftl01.cr.usgs.gov/MOLT/MOD21A1D.061/2021.10.28/
FILENAME : MOD21A1D.A2021301.h35v10.061.2021303035120.hdf 
```

--------------------------------------------------------------
## 8. Coding

### Authentication

Accessing data through Earthdata requires a user registration.
https://urs.earthdata.nasa.gov
Just pick up a username, a password, and your e-mail address.  Nothing
complicated. You will get a confirmation e-mail.  The __Username__ and
__Password__ will be used in the authentication in the Python script
below.


### Python Script

It took me long to reach here, but the code itself is short.
Here is the entire code.

'''
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

### How to run the demo

```
> python3 exp_modis1.py [USERNAME] [PASSWORD]

```
Replace `[USERNAME]` and `[PASSWORD]` with your own.

### HDFView

To check the contents of an HDF file that we download to the local
machine, get a quick HDF viewer, `HDFView`.

https://portal.hdfgroup.org/display/support/Download+HDFView

   + On MacOSX we need to set a permission at 'System Preference'
    -> 'Security & Privacy' to run the app.

I can see the metadata, but it is not clear if any imaging data
is attached. 
     
--------------------------------------------------------------
## 9. System Design Considerations

### Hardware

1. None of the existing satellites are fully optimized for a fast
   alarming of the wildfire. There are many systems for the forecasting
   (warning) and the evaluation (of the damage), but not the detection
   of it.

2. Possible specifications of such a system:

   + temporal resolution 10-15 min.
   + spatial resolution 10 m
   + temperature sensitivity 600-1500 K which is 2 to 5 um
     in the wavelength.

   This is in the order of difficulty to suffice. 

3. Need near-infrared sensitivity (2.2 um) to detect the blackbody
  radiation of the temperature 1500 K. If possible, thermal infrared (>
  3um 1000K) is desired.

4. Wide-format infrared detector array necessary. Minimum 4k by 4k.

5. Geostationary orbit is impossible because of the spatial
   resolution needed for looking from over there. Either 
   in the medium (>2000 km) or the low earth 
   (200-2000 km) orbits are realistic. 

6. At a medium earth orbit at 2000 km above the ground, a telescope
   with 20-cm diameter would suffice to resolve 10 m on the ground
   with a diffraction-limited angular-resolution. Required telescope
   diameter becomes smaller with the height of the orbit.

7. The higher the orbit, the simultaneous coverage of the land is
   larger (depending on the size of the detector installed, though). 
   Germany spans about 1000 km across. Need a fast telescope even on the
   medium earth orbit to cover the whole land.

8. The higher the orbit, need a larger infrared detector array. If one
   would like to resolve 80 km x 80 km area (about Munich-Augsburg
   distance) with 10 m resolution, we need 8k x 8k infrared detector
   array. One quadrant (4k x 4x) would cost 200k Euro.

9. The orbital periods of the low and the medium earth orbits do not
   differ too much (the radius of the earth is dominant), and are
   90-130 min. Depending on the required temporal resolution, a
   constellation of the satellites with more than 6 machines is
   necessary.

### Software

10. A blackbody/graybody fitting at each pixel costs computing
    resources. Band-flux templates for grids of temperatures to
    quickly calculate a cross-correlation would make the data
    processing faster.

11. Potential challenges in building a data analysis system are

   - Optical depths of the flames
   - Filling factors of the flames
   - Varying filling factors with flames with temperature (=wavelength)

   All can tweak the true temperature of the fire. 

12. Calibration documents for MODIS data is available on the internet.
    They should be useful for building an in-house calibration system 
    as well.

### Data Pipeline Experiment

1. Satellites that have closest specifications with what we have in
   mind are MODIS and VIIRS (from US) and Sentinel-2 and -3 (from EU)

2. Data access system in the earth observing community is a mess.

3. Non-GUI path of the retrieval of MODIS Data goes as follows.

  - Go to 'Data Pool' of NASA Earthdata webpage to identify the file
    and its location.

  - Register yourself as a user on Earthdata to get an username and
    password for the authentication.

  - Use Python package `requests` to retrieve the data. Need an
    authentication.

  - Use `HDFView` to see if a HDF file is correctly retrieved.


--------------------------------------------------------------

## 10. To-Do

1. Look at the contents of HDF files closer
   - show images with Python script
   - find how to manipulate array data
   - `astropy`?

2. Study how to set search criteria so that we can freely select
   the files we want. Such as

   - Munich-Augsburg area (or California/Turkey/Greece), 
   - In our favored time priod. 

3. Try NRT (near real-time) data.

   - Retrieve with scheduling.
   - `AirFlow`
   - `PySpark`

4. Try raw (but flux-calibrated) images.
   - there is an interesting documents about ATBT.\
     __ATBD__ (Algorithm Theoretical Basis Documents)
     https://modis.gsfc.nasa.gov/data/atbd/

   - Useful to make a calibration plan. 

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

5. Calculate the temperatures.
   - Create band-temperature templates. 

6. Alert system.
   - calculate the difference/anomaly, and raise the flag.

7. Frontend. 

8. VIIRS

9. Sentinel-2

==============================================================
# END

