# Get a number between low and high
def prompt_for_number_in_range(low, high, prompt):
    assert low <= high
    while True:
        try:
            number = int(input("{} ({}-{}):".format(prompt, low, high)))
            if number < low or number > high:
                raise ValueError
            break
        except ValueError:
            print("Invalid selection")
    return number

# Prompt the user to select
def select_zotero_item(items: list[dict]) -> dict:
    for num, item in enumerate(items, start=1):
        print("{}. {} - {}".format(num,item['data']['title'], item['data']['creators'][0]['lastName']))
    item = prompt_for_number_in_range(1, len(items), "Select book")
    return items[item-1]

