# Power Racing Series Score Extraction

No interface or error handling yet. Be careful with what you type because it doesn't know how to deal with typos and will throw errors at you and fail.

Ignore "extract-and-score" for now. I figured out where I was screwing up but haven't had time to fix it yet.

---
## Using It

### Requirements

* Python 3. Not making it compatible with Python 2 because I don't want to.
* Pandas. Because handling dataframes is more convenient than handling CSVs directly.
* If you don't want to/can't install Python and Pandas, [PythonAnywhere](http://www.pythonanywhere.com) will work. It has the necessary stuff installed, but you will need an internet connection

### Setup

* No installation, no UI, hope you like typing.
* Export HTML file(s) and save into the same folder as my scripts unless you like typing out file locations (the UI version will fix this).

### Running scripts

* Run ```process_html.py```. Follow directions.
* You now have a CSV file with the car names, rankings, and race points for that race.
* To add up points from multiple races, run ```combine_races.py``` and it will give you a CSV combining all the races you fed it with points added up for the weekend
---
## Known Issues

* I haven't done anything about points for races with more than 20 cars. That will be fixed soon - probably by Wednesday morning. If you want it fixed more quickly, please send me an exported HTML file for a race with more than 20 cars. 
* It's ugly and not well documented right now.
---
## Future goals

* Functionality without installing Python and Pandas
* Better interface and error handling
* For next season, use this as the groundwork for a Django-based tool to maintain a persistent database of points and other race data.
