# SteelEye-Assignment

The test requirements mentioned were very vague, So i manually downloaded the XML file.

The main code file is assignment.py

The program is coded in Python3 and requires following Libraries. 
* BeautifulSoup : to read xml
* pandas : to create csv
* logging : to create logs

Code reads the xml file, extracts and creates CSV of the following:
* FinInstrmGnlAttrbts.FullNm
* FinInstrmGnlAttrbts.ClssfctnTp
* FinInstrmGnlAttrbts.CmmdtyDerivInd
* FinInstrmGnlAttrbts.NtnlCcy
* Issr

Logging added : assignment.log

Generated csv added : SteelEye.csv

pydoc added : assignment.html

The XML file downloaded is also added : data.xml.zip


# Todo
Need AWS account credentials from SteelEye for AWS S3 bucket storage in order to perform Step 5 of the assignment.
