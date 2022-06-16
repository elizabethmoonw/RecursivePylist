# pylist_test.py
# Prof. Lee (LJL2) and Elizabeth Moon (EM652)

""" Test cases """

from pylist_classes import Song, Mix
from pylist_classes import pprint_mix # In case you need to do some debugging prints.
import pylist
import inspect  # To print the name of a (test) function that is running
import copy # For checking whether Mixes were changed

##############################
# Set up some Songs and Mixes.
##############################

# In the below s_ variables are Songs.

# "s_" for Song, then the initials of the title.
s_dyc = Song("Dance Yrself Clean", "LCD Soundsystem")
s_lme = Song("Losing My Edge", "LCD Soundsystem")

lcd = Mix("LCD Soundsystem", [s_dyc, s_lme])

s_tmbtp = Song("This must be the place", "Talking Heads")
s_pk    = Song("Psycho Killer", "Talking Heads")
s_gib   = Song("Girlfriend is better", "Talking Heads")
s_oial  = Song("Once in a lifetime", "Talking Heads")
s_bdth  = Song("Burning Down the House", "Talking Heads")

th = Mix("why the big suit", [s_tmbtp, s_pk, s_gib, s_oial, s_bdth])

s_tmbtp2 = Song("This Must be the Place", "The Lumineers")
s_bdth2  = Song("Burning Down the House", "Tom Jones and the Cardigans")

# This Mix contains both a sub-Mix and two individual songs
th2 = Mix("Talking Heads Songs and Covers", [th, s_tmbtp2, s_bdth2])

# This Mix is a combo of two pre-existing Mixes.
m_recs = Mix("Recs from M", [th2, lcd])

s_ttabeftbou=Song("This Town Ain’t Big Enough for the Both of Us", "Sparks")
s_r    = Song("Redbone", "Childish Gambino")
s_batj = Song("Bennie and the Jets", "Elton John")
s_br   = Song("Bohemian Rhapsody", "Queen")

high = Mix("Songs in the key of Falsetto", [s_ttabeftbou, s_r, s_batj, s_br])

weird = Mix("Eccentrica",[high, m_recs])

s_an   = Song("Alles Neu", "Peter Fox")
s_wf   = Song("Wavin' Flag", "K'naan")
s_wywh = Song("Wish You Were Here", "Pink Floyd")
s_totw = Song("Top of the World", "Carpenters")
s_watd = Song("We Are the Dinosaurs", "The Laurie Berkner Band")
s_dgj  = Song("Der Glühwurm Julius", "Ute Rink")

bracy = Mix("Prof. Bracy's list", [s_an, s_wf, s_wywh, s_totw, s_watd, s_dgj])

s_sau = Song("Something About Us", "Daft Punk")
chris = Mix("Chris's list", [s_sau])

s_diat = Song("Desire is a Trap", "Bladee & Ecco2k")
s_n3c = Song("NOTHING 3V3R CHAN935", "Brainiac")

lifan = Mix("Lifan's list", [s_diat, s_n3c])

s_ab   = Song("Anomalie bleue", "L’Imperatrice")
s_l    = Song("Liability", "Lorde")
s_p    = Song("PPP", "Beach House")
s_vq   = Song("Veridis Quo", "Daft Punk")
s_gtaw = Song("Goodbye To A World", "Porter Robinson")
s_m    = Song("Mercy", "Max Richter")
s_ad   = Song("Aruarian Dance", "Nujabes")
s_gn   = Song("Good News", "Mac Miller")

gary  = Mix("Gary's list", [s_ab, s_l, s_p, s_vq, s_gtaw, s_m, s_ad, s_gn])

s_ba = Song("Broken Arrow", "Robbie Robertson")
s_ds = Song("Divorce Song", "Liz Phair")
s_np = Song("Nana Party (Chuang 2021 live version)",
            "OJM, Johan Gustafson, Fredrik Haggstam, Sebastian Lundberg, and Wang Tianfang")

llee= Mix("Prof. Lee's list", [s_ba, s_ds, s_np, lcd])

sad   = Mix("Sad songs", [s_l, s_p, s_gtaw, s_m, s_dyc, s_wywh, s_ds])
instr = Mix("instrumentals", [s_vq, s_m, s_ad])
elec  = Mix("electronic music", [s_vq, s_ab, s_gtaw])
hhr   = Mix("hip-hop/rap", [s_ad, s_gn])

cs1110picks = Mix("CS1110 picks", [chris, bracy, lifan, gary, llee])

###################
# Testing Functions
###################


# helper
def print_testing(start_or_end):
    """If start_or_end is 'start',
        print message about starting function that called this function
       If start_or_end is 'end'
        print message about ending function that called this function

    Precondition: start_or_end is either 'start' or 'end'"""
    caller = inspect.currentframe().f_back.f_code.co_name
    if start_or_end == 'start':
        print("Starting " + caller)
    elif start_or_end == 'end':
        print(caller + " seems to have passed (didn't crash/stop in the middle).")
        print("\n")

def test_songs_in():
    print_testing('start')

    # For testing some repeat handling
    fake_song = Song("Fake Song", "Fakers")
    fake_song2 = Song("Fake Song", "Fakers")
    pl_pseudo_repeats = Mix('Repeated names but not objects', [fake_song, fake_song2])

    for testcase in [
                    # elements are pairs: a Mix and expected answer
                    [chris, [s_sau]],
                    [llee, [s_dyc, s_lme, s_ds, s_np, s_ba]],
                    [m_recs,[s_dyc, s_lme, s_bdth, s_gib, s_oial, s_pk, s_tmbtp,
                         s_tmbtp2, s_bdth2]],
                    [weird,[s_r, s_batj, s_dyc, s_lme,
                            s_br, s_ttabeftbou, s_bdth, s_gib, s_oial, s_pk,
                            s_tmbtp, s_tmbtp2, s_bdth2]],
                    [cs1110picks, [s_p, s_diat, s_n3c, s_totw, s_sau, s_vq,
                                    s_wf, s_dyc, s_lme, s_ds, s_l, s_ab, s_gn,
                                    s_m, s_ad, s_np, s_an, s_wywh, s_gtaw, s_ba,
                                    s_watd, s_dgj]],
                    # The next bunch test various types of repeats.
                    #   1. contents has first repeats
                    [Mix('duplicates1', [s_np, s_np]),
                        [s_np]],
                    #   2. overlapping Mixes in contents
                    [Mix('duplicates2', [llee, weird]),
                        [s_r, s_batj, s_dyc, s_lme, s_ds, s_np, s_br, s_ba,
                         s_ttabeftbou, s_bdth, s_gib, s_oial, s_pk, s_tmbtp,
                         s_tmbtp2, s_bdth2]],
                    #   3. one contents Mix is subset of other
                    [Mix('duplicates3', [gary, instr]),
                        [s_p, s_vq, s_l, s_ab, s_gn, s_m, s_ad, s_gtaw]],
                    #   4. distinct objects with same names and artists
                    [pl_pseudo_repeats, [fake_song]]]:

        m = testcase[0]
        expected = testcase[1]
        print("\tTrying Mix '"+m.title+"'")

        m_copy = copy.deepcopy(m) # Copy to check that no changes happened

        result = a4.songs_in(m)

        assert result == sorted(result), "Error: output isn't sorted."
        assert result == expected, \
            ("Error: expected\n\t"+repr(expected)+"\nbut got\n\t"+repr(result))
        assert m_copy == m, "Error: songs_in changed contents of input."

    print_testing('end')


def test_basic_mixes():
    print_testing('start')

    for testcase in [
        # elements are pairs: a Mix, and expected output
        [instr, [instr]],
        [bracy, [bracy]],
        [th2, [th]],
        [m_recs, sorted([th, lcd])],
        [weird, sorted([th, lcd, high])],
        [cs1110picks, sorted([chris, bracy, lifan, gary, lcd])]]:

        m = testcase[0]
        expected = testcase[1]
        print("\tTrying Mix '"+m.title+"', will remove duplicates for you.")

        m_copy = copy.deepcopy(m) # Copy to check for no changes

        result = a4.basic_mixes(m)
        result_no_dups = [] # Construct deduplicated version
        for r in result:
            if r not in result_no_dups:
                result_no_dups.append(r)

        assert result == sorted(result), "Error: output isn't sorted."
        assert result_no_dups == expected, \
            ("Error: expected\n\t"+repr(expected)+"\nbut got\n\t"+repr(result_no_dups))
        assert m_copy == m, "Error: playlists_with changed contents of input."

    print_testing('end')



def test_mixes_with():
    print_testing('start')

    lotsa_mixes = [cs1110picks, chris, bracy, lifan, gary, llee, sad, instr,
                    elec, hhr, weird, high, m_recs, th2, th, lcd]

    for testcase in [
        # elements are triples: a Song, a list of Mixes, expected output
        [s_ad, [hhr], [hhr.title]],
        [s_vq, [instr,elec], sorted([instr.title, elec.title])],
        [s_ad, [sad, elec],[]],
        [s_ad, [hhr, elec], [hhr.title]],
        [s_ad, [sad, instr, elec, hhr], sorted([instr.title, hhr.title])],
        [s_m, [cs1110picks], sorted([cs1110picks.title, gary.title])],
        [s_m, [cs1110picks, sad], sorted([cs1110picks.title, gary.title, sad.title])],
        [s_bdth, [weird], sorted([weird.title, m_recs.title, th2.title, th.title])],
        [s_bdth, [weird, th], sorted([weird.title, m_recs.title, th2.title, th.title])],
        [s_bdth, lotsa_mixes, sorted([weird.title, m_recs.title, th2.title, th.title])]]:

        s = testcase[0]
        mlist = testcase[1]
        expected = testcase[2]
        print("\tTrying Song '"+s.title+"', length "+str(len(mlist))+
            " list of Mixes starting with '"+mlist[0].title+"'")

        mlist_copy = copy.deepcopy(mlist) # Copy to check for no changes

        result = a4.mixes_with(s, mlist)

        assert result == sorted(result), "Error: output isn't sorted."
        assert result == expected, \
        ("Error: expected\n\t"+repr(expected)+"\nbut got\n\t"+repr(result))
        assert mlist_copy == mlist, "Error: mixes_with changed contents of input."

    print_testing('end')


if __name__ == '__main__':

    test_songs_in()
    test_basic_mixes()
    test_mixes_with()

    print("If you ran all three test functions and nothing crashed, things look good! (But consider more testing beyond what we provided...)")
