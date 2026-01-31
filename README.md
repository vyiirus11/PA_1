# PA_1

### FILES
`gale_shapley:` <br/>
`read_input:` <br/>
`verifier:` <br/>
`main.py:` <br/>

### TESTING | ERROR MAY OCCUR WITH OUTPUT TEXT FILE, SOLUTION BELOW
<ol>
<br>
<li>
After creating outpit file "exampleout.txt", go to bottom right corner of the exampleout.txt file and click on UTF-##

<div align="center">
<br>
      <img src="images/image.png" alt="Example" width="500">
    </div>     
</li>

<br>
<li>
Select Save with enconding

<div align="center">
<br>
      <img src="images/image2.png" alt="Example" width="500">
    </div> 
    </li>

<br>
<li>
Select UTF-8 (!!NOT BOM!!)

<div align="center">
<br>
      <img src="images/image3.png" alt="Example" width="500">
    </div> 
    </li>
    <br>
<li>    
Run verfier again
</li>
</ol>
<br>

### COMMANDS
1. input: 
```
python .\main.py match .\examplein.txt
```
2. output: 
```
python .\main.py match .\examplein.txt | Out-File -Encoding utf8 exampleout.txt
```
3. verifier: 
```
python .\main.py verify .\examplein.txt exampleout.txt
```
<br>
Helen Dang: 58380926<br/>
Carmel Norris: 99049562