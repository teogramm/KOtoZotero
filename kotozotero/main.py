import csv
import glob
from typing import List

import more_itertools
from pyzotero.zotero import Zotero
from ui import select_zotero_item

from globals import *

zot = Zotero(user_id, 'user', api_key)


def search_book(book_name: str):
    return zot.top(q=book_name)


def get_zotero_item_from_name(book_name: str):
    results = search_book(book_name)
    while len(results) < 1:
        book_name = input("Book {} not found. Make sure it exists in your Zotero library or enter an alternative "
                          "search term: ".format(book_name))
        results = search_book(book_name)
    return select_zotero_item(results)


# Import the notes in the given csv file
# We assume the name of the csv file contains the author and book name separated by a hyphen
def import_notes(csv_file):
    # Get the name of the csv file the keep only the book name
    book_name = os.path.splitext(csv_file)[0].split('-')[1]
    item = get_zotero_item_from_name(book_name)
    parent_book_id = item['key']
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        # Skip header row
        next(reader, None)
        notes = []
        for note in reader:
            # Create a note item
            new_note = zot.item_template('note')
            # The highlight is in the second to last column and the note (if any) is in the last column
            new_note['note'] = note[-2]
            if note[-1]:
                new_note['note'] += "\n" + note[-1]
            notes.append(new_note)
        # You can only create 50 items per call
        for chunk in more_itertools.chunked(notes, 50):
            zot.create_items(chunk, parentid=parent_book_id)

## Returns the paths of the csv files which contain the notes.
def get_files_to_import() -> List[str]:
    return glob.glob("in/*.csv")


if __name__ == "__main__":
    files = get_files_to_import()
    for csv_file in files:
        import_notes(csv_file)
