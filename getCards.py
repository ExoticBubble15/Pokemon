from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

link = "https://www.tcgplayer.com/categories/trading-and-collectible-card-games/pokemon/price-guides/sv06-twilight-masquerade?srsltid=AfmBOorq2nlLlF6Muig2hAV-yDJyQ-GL6jAfwJFAdi5-6Xy0Tcigv0UY"
# link = input("tcg pull price guide link: ")
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

driver.get(link)
#expand to get full list
expand = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/section[2]/section[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]")))
expand.click()

setTitle = driver.find_element(By.TAG_NAME, "h1").text
setTitle = setTitle.split("\n")[1]
setTitle = setTitle[setTitle.index(": ")+2:setTitle.index(" Price Guide")]

evens = driver.find_elements(By.CLASS_NAME, "is-even")
odds = driver.find_elements(By.CLASS_NAME, "is-odd")
rarities = {}
for row in [evens, odds]:
	for elem in row:
		#['image' (empty string), 'product name', 'printing', 'condition', 'rarity', 'number', 'market price', 'add to cart']
		cols = elem.find_elements(By.TAG_NAME, "td")
		cardTitle, cardRarity = cols[1].text, cols[4].text
		if cardRarity in rarities:
			rarities[cardRarity].append(cardTitle)
		else:
			rarities[cardRarity] = [cardTitle]
		
driver.quit()