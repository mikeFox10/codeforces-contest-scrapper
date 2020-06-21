# Codeforces input and output contest scrapper
## Get all input and output test cases of codeforces contest in files .txt

### Requirements
- Python 3

```
$ pip3 install beautifulsoup4
$ pip3 install request
```

### Configuration

Edit config constants in cf_scrapper.py
```
configPath = "/home/user/" # Directory for save TC contest
pathToTemplate = None # Optional - path to template file Example: /home/io.cpp
```
### Run

```
$ python3.8 cf_scrapper.py
Enter contest id: 
```

Enter contest id

*** Ej. 1370 is contest id in https://codeforces.com/contest/1370/problems URL

Ready to solve contest
