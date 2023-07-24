import csv
import glob
import os
import sys
from typing import List

import more_itertools
from pyzotero.zotero import Zotero
from kotozotero.ui import select_zotero_item, error_file_does_not_exist, info_show_processing_file, info_show_import_successful

from kotozotero.globals import *

zot = Zotero(user_id, 'user', api_key)


def search_book(book_name: str):
    return zot.top(q=book_name, itemType="book")


def get_zotero_item_from_name(book_name: str) -> dict:
    while True:
        results = search_book(book_name)
        item_or_string = select_zotero_item(results)
        if type(item_or_string) is dict:
            item = item_or_string
            break
        else:
            book_name = item_or_string
    return item


# Import the notes in the given csv file
def import_notes(csv_file):
    # Get the name of the csv file the keep only the book name
    # We assume the name of the csv file contains the author and book name separated by a hyphen
    book_parts = os.path.splitext(os.path.basename(csv_file))[0].split('-')
    # If the name is not in the format Author - Book just use the name of the csv file.
    if len(book_parts) < 2:
        book_name = book_parts[0]
    else:
        book_name = book_parts[1]
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


# Returns the paths of the csv files which contain the notes.
def get_files_to_import() -> List[str]:
    return sys.argv[1:]


def main():
    check_if_envvars_are_set()
    files = get_files_to_import()
    for csv_file in files:
        if os.access(csv_file, os.R_OK):
            info_show_processing_file(csv_file)
            import_notes(csv_file)
            info_show_import_successful()
        else:
            # If the file does not exist print an error
            error_file_does_not_exist(csv_file)


if __name__ == "__main__":
    main()
