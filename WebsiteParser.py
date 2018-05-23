from xml.dom import minidom
import mysql.connector
import sys
import re
import glob, os

def insert(cursor, a1, a2, a3, a4, a5, a6):
     query = 'INSERT INTO weather(state,city,weather,temp,humidity,pres) VALUES (%s,%s,%s,%s,%s,%s)'
     cursor.execute(query, (a1,a2,a3,a4,a5,a6))

DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

for file in glob.glob("*.xhtml"):
     doc = minidom.parse(file)
     degr = doc.getElementsByTagName("h1")[1]
     degrData = degr.firstChild.data
     degrRegex = re.findall(r'\d{0,2}[^F\°]',degrData)
          
     cond = doc.getElementsByTagName("h4")[2]
          
     city = doc.getElementsByTagName("a")[10]
     cityData = city.firstChild.data
     cityRegex = re.findall(r'[A-Za-z\s]*[^\/\,A-Z]', cityData)
     state = doc.getElementsByTagName("a")[10]
     stateData = state.firstChild.data
     stateRegex = re.findall(r'[A-Z][A-Z]',stateData)
     if not (stateRegex):
          pens = doc.getElementsByTagName("h2")[1]
          pensData = pens.firstChild.data
          pensRegex = re.findall(r'[A-Z][A-Z]',pensData)
          stateRegex = pensRegex
     elif (stateRegex[0] == 'NW'):
          stateRegex[0] = 'AZ'

     if (cityRegex[0] == 'NWS Phoenix'):
          cityRegex[0] = 'Phoenix'
               
          
     print("STATE:%s,StateCity:%s, Degrees:%s, Condition:%s" % (stateRegex[0],cityRegex[0], degrRegex[0],
                                             cond.firstChild.data))
     a1 = stateRegex[0]
     a2 = cityRegex[0]
     a3 = cond.firstChild.data
     a4 = degrRegex[0]
     table = doc.getElementsByTagName("table")
     for j in table[0].getElementsByTagName("tbody"):
          for x in j.getElementsByTagName("tr"):
               bold = x.getElementsByTagName("b")[0]
               one = x.lastChild.firstChild.data
               if bold.firstChild.data == "Humidity":
                    number1 = re.findall(r'\d{0,2}[^\%]',one)
                    a5 = number1[0]
                    print("humidity:%s" % (number1[0]))
	            
               elif bold.firstChild.data == "Barometer":
                    number = re.findall(r'\d{2}\.\d{2}|\d{2}',one)
                    print("pressure:%s" % (number[0]))
                    a6 = number[0]
     try:
          cnx = mysql.connector.connect(host='localhost', user='root', password='password', database='weather')
          cursor = cnx.cursor()
     
          insert(cursor, a1, a2, a3, a4, a5, a6)
          cnx.commit()
     except mysql.connector.Error as err:
          print(err)
     finally:
          cnx.close()


