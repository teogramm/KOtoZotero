import sys


def info_show_processing_file(filename: str):
    print("Processing {}".format(filename))

def info_show_import_successful():
    print("Import completed for book.")

def error_file_does_not_exist(filename: str):
    print("{} does not exist or is inaccessible.".format(filename), file=sys.stderr)


# Get a number between low and high or a string
def prompt_for_number_in_range_or_text(low, high):
    assert low <= high
    user_input = input("Enter a number between {} and {} or enter a different search term: ".format(low, high))
    return user_input


def prompt_for_text() -> str:
    user_input = input("No books were found. Enter a different search term: ")
    return user_input


# Prompt the user to select an item or to enter a custom term in order to redo the search
# Returns a dict if the user selects an item or a string if the user enters a different term
# to redo the search
def select_zotero_item(items: list[dict]) -> dict | str:
    for num, item in enumerate(items, start=1):
        try:
            author_last_name = item['data']['creators'][0]['lastName']
        except IndexError:
            author_last_name = ""
        # Show index and book name
        book_display = "{}. {}".format(num, item['data']['title'])
        # Additionally add author name if it exists
        if author_last_name:
            book_display += " - " + author_last_name
        print(book_display)
    if len(items) == 0:
        return prompt_for_text()
    else:
        selection = prompt_for_number_in_range_or_text(1, len(items))
        try:
            # Try to interpret the selection as an index for an item
            index = int(selection) - 1
            return items[index]
        except (IndexError, ValueError):
            # Either the user has not entered a number, or they have entered a number not corresponding to a selection.
            return selection
