from utils import *
from config import *

def guitar_to_ukulele(guitar_tabs: list, song_name: str):
    """ Convert guitar tabs to ukulele tabs, and poop the ukulele scheme to a .txt file """

    # Get the strings of the uku and the guitar
    guitar_strings = get_strings_from_base_notes(guitar_base_notes, guitar_frets_num)
    ukulele_strings = get_strings_from_base_notes(ukulele_base_notes, ukulele_frets_num)

    # Convert the tabs to the numbers that represent the different notes on the guitar
    song_note_nums = song_to_nums(guitar_tabs, guitar_strings)

    # Convert the guitar note numbers, to ukulele tabs
    song_tabs_uku = nums_to_song_tabs(song_note_nums, ukulele_strings)

    # Create a printable ukulele tabs scheme
    song_tabs_scheme = song_tabs_to_scheme(song_tabs_uku, 4)

    # Poop the ukulele tabs scheme to a .txt file
    tabs_scheme_to_txt_file(song_name, song_tabs_scheme)

    print("FML I'M OUT")

if __name__ == "__main__":
    guitar_to_ukulele(the_bad_touch_tabs, "The_Bad_Touch")