# gets rarities and respective rates
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# link = "https://www.tcgplayer.com/content/article/Pok%C3%A9mon-TCG-Twilight-Masquerade-Pull-Rates/f3eea967-e5fb-4108-8655-bb1c89587628/?srsltid=AfmBOorOaR0oC4KNlXUpueOzj-qATtrQMxFVTQIie2E4e0RZkvgkELrX"
link = input("tcg pull rate link: ")
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

driver.get(link)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "author-bio")))

table = driver.find_elements(By.TAG_NAME, "table")
for t in table:
	tableText = t.text
	# print(tableText, "\n")
	if "Rarity" in tableText and "Pull Rate (95% Confidence Interval)" in tableText and "Rounded Pull Rate (Per X Packs)" in tableText:
		rateTable = (tableText.split("\n"))
		# print(rateTable)
		for i in rateTable[1:]:
			rarity, pullRate = None, None
			try:
				i = i[0:i.index(".")+3]
				i = i[::-1]
				firstSpace = i.index(" ")
				pullRate = float(i[0:firstSpace][::-1])
				rarity = i[firstSpace+1:][::-1]
			except:
				pass
			print(f"{rarity}: {pullRate}")
		break
	
driver.close()