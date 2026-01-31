# PA_1
matching and verifying


Task C: graphing: matplotlib, pyplot

read-input.py

gale-shapley.py

Testing
examplein.txt
exampleout.txt

ERROR MAY OCCUR WITH OUTPUT TEXT FILE, SOLUTION BELOW:
1. after creating exampleout.txt, go to bottom right corner of the exampleout.txt file and click on UTF-##
(images/image.png")
2. Select Save with enconding 
3. Select UTF-8 (!!NOT BOM!!)
4. Run verfier again

Commands
1. python .\main.py match .\examplein.txt
2. python .\main.py match .\examplein.txt | Out-File -Encoding utf8 exampleout.txt
3. python .\main.py verify .\examplein.txt exampleout.txt

Helen Dang: 58380926 