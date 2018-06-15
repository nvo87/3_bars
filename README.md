# Closest bars

This program define the smallest, biggest and closest bar using json file with bars data collection [(download bars.json)](https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json)

# How to start

Script requires you Python 3.5
Start on Linux

```bash

$ python bars.py <filepath/to/.json>
```
For example, 
```bash

$ python bars.py bars.json
```
You have to put json file with bars data to script folder. You may download example from [here](https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json) or find it in [data.mos.ru)](https://data.mos.ru/).
then enter your geo-position (longitude and latitude, e.c. 38.5 and 55.1)

bars.py returns:
```
The biggest bar - Sportbar Red Mashine
The smallest one - Bar Spring
The closest one - Taverna

```

Start on windows is the same

For more information, type
```bash

$ python bars.py -h
```

# Projects aims

It's study project on devman - [DEVMAN.org](https://devman.org)

Main goal is to study lambda functions and json handling 
