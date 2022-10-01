from bs4 import BeautifulSoup
import pandas as pd 
import logging

logging.basicConfig(filename='assignment.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)
logging.info("Logger Started")

def convertToCsv():
   try:
      # read the xml
      with open('data.xml', 'r') as f:
         file = f.read() 
      soup = BeautifulSoup(file, 'xml')
      
      # extracting texts from each requested tags and storing the data in a list, Except ID as there seems to be an issue with the ID Tag
      # Column 1
      eachFullNm = soup.find_all('FullNm')
      FullNm =[]
      for name in eachFullNm:
         FullNm.append(name.text)
      logging.info("Contents of tag FullNm Extracted ")

      # Column 2
      eachClssfctnTp = soup.find_all('ClssfctnTp')
      ClssfctnTp =[]
      for clssfct in eachClssfctnTp:
         ClssfctnTp.append(clssfct.text)
      logging.info("Contents of tag ClssfctnTp Extracted ")

      # Column 3
      eachIssr = soup.find_all('Issr')
      Issr =[]
      for issr in eachIssr:
         Issr.append(issr.text)
      logging.info("Contents of tag Issr Extracted ")

      # Column 4
      eachCmmdtyDerivInd = soup.find_all('CmmdtyDerivInd')
      CmmdtyDerivInd =[]
      for cmmdtyDerivInd in eachCmmdtyDerivInd:
         CmmdtyDerivInd.append(cmmdtyDerivInd.text)
      logging.info("Contents of tag CmmdtyDerivInd Extracted ")

      # Column 5
      eachNtnlCcy = soup.find_all('NtnlCcy')
      NtnlCcy =[]
      for ntnlCcy in eachNtnlCcy:
         NtnlCcy.append(ntnlCcy.text)
      logging.info("Contents of tag NtnlCcy Extracted ")
         
      # Combining the lists to form a Data Frame
      df = pd.DataFrame(list(zip(FullNm, ClssfctnTp, CmmdtyDerivInd, NtnlCcy, Issr)), columns =["FullNm","ClssfctnTp","CmmdtyDerivInd","NtnlCcy","Issr"]) 
      logging.info("DataFrame Created")
      
      # Converting the Data Frame to CSV
      df.to_csv('SteelEye.csv')
      logging.info("CSV Created")
      
      return "XML Successfully Converted to CSV"
   
   except:
      return "Conversion of XML to CSV Unsuccessful"


if __name__ == "__main__":
   convertToCsv()