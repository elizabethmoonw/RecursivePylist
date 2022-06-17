# RecursivePylist 🎼🎵

People can make p(la)ylists or mixes by selecting individual songs and/or by combining other mixes. That means we can think of mixes as recursive data structures! 

## File pylist_classes.py defines these classes, but you don’t need to look at it. Here’s all you need to know...
1. A Song object has two attributes, title and artist, both non-empty strings. A call of the form Song(t, a) creates a new Song with title attribute set to t and artist attribute set to a.
2. A Mix object has two attributes, title and contents. title is a non-empty string. contents is a nonempty list, where each element is either a Song (not None) or a Mix. There should be no cycles/loops in the containment relationships of any of the contents of the Mixes reachable from a given Mix’s contents. A call of the form Mix(t, c) creates a new Mix with title attribute set to t and contents attribute set to c.
3. If you want to check whether an item x is a Song or a Mix, we’d like you to transition from using type(x)== Song (ditto Mix) to the following expression instead:
isinstance(x, Song)(ditto for Mix).

