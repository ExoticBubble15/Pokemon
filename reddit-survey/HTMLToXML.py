#code from https://www.geeksforgeeks.org/python/parsing-and-converting-html-documents-to-xml-format-using-python/
from lxml import html, etree

with open("reddit-survey/surveyOptionsHTML.txt") as source:
	text = source.read()
	
	htmlDoc = html.fromstring(text)

	with open("reddit-survey/surveyOptionsXML.xml", "wb") as out:
		out.write(etree.tostring(htmlDoc))