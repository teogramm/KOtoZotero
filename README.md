# KOtoZotero

A tool to import notes extracted from KOReader into Zotero.

## Limitations
You have to add the books to your Zotero library before running this script.

## Quickstart
0. Export the notes using [KOHighlights](https://github.com/noembryo/KoHighlights/). Export
one CSV file per book. Make sure the books already exist in your Zotero library.
1. Install the requirements from requirements.txt
```pip install -r requirements.txt```
2. You need your Zotero user ID, which is available [here](https://www.zotero.org/settings/keys).
3. In addition, you need an API key from [here](https://www.zotero.org/settings/keys/new).
4. Set the ```ZOT_LIB_ID```  and ```ZOT_KEY ``` environment variables to your
user  ID and API Key (obtained in steps 3 and 4).
5. Run the program, giving the csv files as arguments.

```
ZOT_LIB_ID=123456 ZOT_KEY=<key> python3 -m kotozotero path/to/Book1.csv path/to/Book2.csv
```

## License

The program is licensed under GPLv3.
