from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sqlite3

#formats "{month} {day}, {year}" into ISO ("{year}-{month number}-{day}" with necessary preceeding 0's)
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def stringDateToISO(date):
	date = date.split(" ")
	monthNumber = str(MONTHS.index(date[0])+1)
	dayNumber = date[1][:date[1].index(",")]

	if len(monthNumber) < 2:
		monthNumber = f"0{monthNumber}"
	if len(dayNumber) < 2:
		dayNumber = f"0{dayNumber}"
	return f"{date[2]}-{monthNumber}-{dayNumber}"

db = "pokemonTCG.db"
connection = sqlite3.connect(db)
cursor = connection.cursor()

link = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_Trading_Card_Game_expansions"
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

tables = driver.find_elements(By.TAG_NAME, "table")
whiteFlareException = False #special case
for table in tables:
	try:
		rows = table.find_elements(By.TAG_NAME, "tr")
		seriesTitle = rows[1].find_elements(By.TAG_NAME, "a")[2].text #this is problematic in the case that the first expansion set of a series is not the base set
		if seriesTitle == "Mega Evolution": #stopping point
			break
		elif seriesTitle in ["Sword & Shield", "Scarlet & Violet"]: #only include SWSH and SV
			print(seriesTitle)
			cursor.execute(f"INSERT INTO Series VALUES (\"{seriesTitle}\")")
			expansionCount = 0
			for setRow in rows[1:]:
				#['set #', 'symbol' (empty string), 'logo' (empty string), 'expansion name', 'expansion type', '# cards', 'release date', 'abbreviation']
				cols = setRow.find_elements(By.TAG_NAME, "td")
				if not whiteFlareException:
					expansionTitle = cols[3].text
					if expansionTitle == "Scarlet & Violet—Black Bolt":
						whiteFlareException = True
					releaseDate = stringDateToISO(cols[6].text)
				else:
					expansionTitle = "Scarlet & Violet—White Flare"
				print(f"{seriesTitle}, {expansionTitle}, {releaseDate}")
				cursor.execute(f"INSERT INTO Expansion VALUES (\"{seriesTitle}\", \"{expansionTitle}\", \"{releaseDate}\")")
				expansionCount += 1
			print(expansionCount, "\n")
	except Exception as e:
		print(e)
		pass

connection.commit()
driver.close()