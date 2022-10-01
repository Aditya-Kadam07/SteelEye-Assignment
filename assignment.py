from bs4 import BeautifulSoup
import pandas as pd 


with open('data.xml', 'r') as f:
	file = f.read() 

soup = BeautifulSoup(file, 'xml')

eachFullNm = soup.find_all('FullNm')
FullNm =[]
for name in eachFullNm:
   FullNm.append(name.text)

eachClssfctnTp = soup.find_all('ClssfctnTp')
ClssfctnTp =[]
for clssfct in eachClssfctnTp:
   ClssfctnTp.append(clssfct.text)

eachIssr = soup.find_all('Issr')
Issr =[]
for issr in eachIssr:
   Issr.append(issr.text)

eachCmmdtyDerivInd = soup.find_all('CmmdtyDerivInd')
CmmdtyDerivInd =[]
for cmmdtyDerivInd in eachCmmdtyDerivInd:
   CmmdtyDerivInd.append(cmmdtyDerivInd.text)

eachNtnlCcy = soup.find_all('NtnlCcy')
NtnlCcy =[]
for ntnlCcy in eachNtnlCcy:
   NtnlCcy.append(ntnlCcy.text)

df = pd.DataFrame(list(zip(FullNm, ClssfctnTp, CmmdtyDerivInd, NtnlCcy, Issr)), columns =["FullNm","ClssfctnTp","CmmdtyDerivInd","NtnlCcy","Issr"]) 
df.to_csv('data.csv')



