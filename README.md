## HepStruja -- bez struje

Tired of checking when is a planned outage in your town? - No more!

This project relies on Pushbullet!

### Installation

1. Register on https://www.pushbullet.com/
2. Download Pushbullet app
3. Generate token
4. Adjust the `electro.py` according to your town.
 - install requirements with `pip install -r requirements.txt` 
5. Create a crontab entry, e.g. `0 8 * * * /usr/bin/python3 /home/pi/bez_struje/electro.py`