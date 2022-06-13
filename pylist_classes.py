# pylist_classes.py
# Prof. Lee, LJL2, Mar 2022

"""Defines classes Song and Mix, plus a pretty-print function pprint_mix().
"""

class Song:
    """Instance attributes:
        * title [non-empty string]: title of this Song.
        * artist [non-empty string]: name of artist(s) or group.

       Class variable: (CS1110 will cover these later.)
        * all_songs: list of all Songs that have been created.
    """
    all_of_em = [] # Will contain all Songs that are created

    def __init__(self, t, a):
        """A new Song with title `t` and artist `a`.

        Preconditions:
            t: non-empty string
            a: non-empty string
        """
        self.title = t
        self.artist = a
        Song.all_of_em.append(self)

    def __eq__(self, other):
        return (isinstance(other, Song) and
                self.title == other.title and
                self.artist == other.artist)

    def __lt__(self, other):
        """Sort by artist, then by title"""
        assert isinstance(other, Song)
        return self.artist < other.artist or \
            (self.artist == other.artist and self.title < other.title)

    def __repr__(self):
        return "Song '"+self.title+"' by "+self.artist

class Mix:
    """Instance Attributes:
        * title [non-empty string]: title of this Mix.
        * contents [non-empty list]: each element is either a Song (not None)
            or a Mix.  No cycles/loops in the containment relationships of
            any of the contents of the Mixes reachable from a given Mix's
            contents.

       Class variable: (CS1110 will cover these later.)
        * all_mixes: list of all Mixes that have been created
    """
    all_of_em = []

    def __init__(self, t, c):
        """A new Mix with title `t` and contents `c`.

        Preconditions:
            t: non-empty string
            c: non-empty list.  Each element is either a Song (not None) a
              or a Mix.
        """
        self.title = t
        self.contents = c
        Mix.all_of_em.append(self)

    def __eq__(self, other):
        return (isinstance(other, Mix) and
                self.title == other.title and
                self.contents == other.contents)

    def __lt__(self, other):
        """Sort by title."""
        assert isinstance(other, Mix)
        return self.title < other.title

    def __repr__(self):
        """Printout uses indents to indicate sub-items."""
        return pprint_mix_helper(self, '  ')


def pprint_mix(m):
    """Pretty-print Mix `m`.  Returns None.

    Example: In a4_test, pretty-printing Mix `weird` would print the following:

    Mix 'Eccentrica' with contents:
      Mix 'Songs in the key of Falsetto' with contents:
        Song 'This Town Ain’t Big Enough for the Both of Us'
        Song 'Redbone'
        Song 'Bennie and the Jets'
        Song 'Bohemian Rhapsody'
      Mix 'Recs from M' with contents:
        Mix 'Talking Heads Songs and Covers' with contents:
          Mix 'why the big suit' with contents:
            Song 'This must be the place'
            Song 'Psycho Killer'
            Song 'Girlfriend is better'
            Song 'Once in a lifetime'
            Song 'Burning Down the House'
          Song 'This Must be the Place'
          Song 'Burning Down the House'
        Mix 'LCD Soundsystem' with contents:
          Song 'Dance Yrself Clean'
          Song 'Losing My Edge'

    which reflects that
    `weird` contains:
      Mix `high`
      and Mix `m_recs` which contains:
         Mix `th2` which contains
            Mix `th`
         and Mix `lcd`

    """
    print(pprint_mix_helper(m, '  '))


# STUDENTS: Note that this is an example of a recursive function for Mixes!
def pprint_mix_helper(m, prefix):
    """Returns a string representing Mix `m`, with each content item
        indented one `prefix` in for each level of nesting.

    Preconditions:
      m is a Mix (not None).
      `prefix` is a string. Expected to be something like a tab (\t) or spaces.
    """
    out = "Mix '"+m.title+"' with contents:\n"
    for item in m.contents:
        if isinstance(item, Song):
            out += prefix+"Song '"+item.title+ "'\n"
        else:
            assert isinstance(item, Mix), "Bad item in contents, namely, "+repr(item)

            # Create a list of the lines in the item, so that each line
            # can have `prefix` added to its beginning.
            itemlines = pprint_mix_helper(item, prefix).strip().split("\n")
            for line in itemlines:
                out += (prefix+line+"\n")
    return out
