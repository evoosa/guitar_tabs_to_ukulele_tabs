from config import *


def note_to_num(full_note: tuple):
    """ (note, pitch) => num """
    note = full_note[0]
    pitch = full_note[1]
    num = base_notes.index(note) + 12 * (pitch - 1)
    return num


def num_to_note(num: int):
    """ num => (note, pitch) """
    note = base_notes[num % 12]
    pitch = num // 12 + 1
    return [note, pitch]


def get_strings_from_base_notes(strings_base_notes: list, frets_num: int):
    """ Generate list of notes numbers, for each string, from it's base note """
    strings = []
    for base_note in strings_base_notes:
        base_note_num = note_to_num(base_note)
        string = range(base_note_num, base_note_num + frets_num + 2)
        strings.append(string)
    return strings


def string_loc_to_num(strings, string_loc: tuple):
    """
    Convert string location => (string_num, location)
    to note number
    """
    string = strings[string_loc[0] - 1]
    note_num = string[string_loc[1]]
    return note_num


def song_to_nums(song: list, strings: list):
    """ Convert a song to it's notes numbers """
    return [string_loc_to_num(strings, string_loc) for string_loc in song]


def nums_to_song(song_notes_nums: list, strings: list):
    """ Convert note_nums to a song - strum locations on the instrument """

    song_tabs = []

    # get the lowest note in the song
    song_lowest_note_num = list(set(song_notes_nums))[0]

    # get the lowest note in the ukulele
    instrument_lowest_notes = [string[0] for string in strings]
    print(instrument_lowest_notes)
    instrument_lowest_note_num = list(set(instrument_lowest_notes))[0]
    print(instrument_lowest_note_num)

    # if the lowest note in the guitar is lower than the one in the ukulele:
    if song_lowest_note_num < instrument_lowest_note_num:
        diff = instrument_lowest_note_num - song_lowest_note_num
        song_notes_nums = [num + ((diff // 12 + 1) * 12) for num in song_notes_nums]

    # convert the note_nums in the song, to the locations in the ukulele
    for note_num in song_notes_nums:
        closest_string = None
        smallest_diff = 1000000
        for i in range(len(instrument_lowest_notes)):
            inst_note = instrument_lowest_notes[i]
            note_diff = note_num - inst_note
            if note_diff >= 0:
                if note_diff < smallest_diff:
                    smallest_diff = note_diff
                    closest_string = i + 1

        song_tabs.append((closest_string, strings[closest_string - 1].index(note_num)))

    return song_tabs

guitar_strings = get_strings_from_base_notes(guitar_base_notes, guitar_frets_num)
ukulele_strings = get_strings_from_base_notes(ukulele_base_notes, ukulele_frets_num)
song_note_nums = song_to_nums(the_bad_touch_tabs, guitar_strings)
print(nums_to_song(song_note_nums, ukulele_strings))
