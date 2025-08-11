# from rapidfuzz import fuzz
# import jaro
# import time

# s2 = "Amoonguss (Master Ball Pattern)"
# s1 = "Amoonguss"

# s = time.time()
# print(fuzz.ratio(s1, s2), time.time()-s)
# s = time.time()
# print(jaro.jaro_winkler_metric(s1, s2), time.time()-s)
# s = time.time()
# print(fuzz.token_set_ratio(s1, s2), time.time()-s)

#formats "{month} {day}, {year}" into ISO ("{year}-{month number}-{day number}")
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


test_dates = [
    "January 1, 2020",
    "February 29, 2020",
    "March 3, 1999",
    "April 30, 2001",
    "May 15, 2022",
    "June 9, 2010",
    "July 4, 1776",
    "August 31, 2021",
    "September 11, 2001",
    "October 31, 1995",
    "November 5, 1955",
    "December 25, 2023"]

for i in test_dates:
	print(stringDateToISO(i))