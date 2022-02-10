import datetime
import requests
from pushbullet import Pushbullet
from bs4 import BeautifulSoup

pb = Pushbullet("<GENERATED_TOKEN>")
seek_town = "NOVI" # keyword to appear in town list 

today = datetime.date.today().strftime("%d.%m.%Y")
tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
d = tomorrow

# found this out at: https://www.hep.hr/ods/bez-struje/19
area = "varazdin"
unit = "109"
url = f"https://www.hep.hr/ods/bez-struje/19?dp={area}&el={unit}&datum={d}"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="home")

towns = results.find_all("div", class_="grad")
times = results.find_all("div", class_="kada")

result = []
for town, time in zip(towns, times):
   town = town.text.strip()
   time = time.text.strip()
   if seek_town in town:
      result.append((town, time))

if result:
   pb.push_note("HEP", f"{result}")