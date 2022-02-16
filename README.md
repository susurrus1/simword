# simword

## Description

A game where you have to guess a secret word based on semantic
similarity.  This code is based on the Semantle game
(https://semantle.novalis.org/).

## Installation

Requires the following python libraries:

Library		tested with version
gensim		3.8.1

## Usage:

At the command prompt, type:

python simword.py


The first time you run the script, it may need to download the model
(currently, this is set to "glove-wiki-gigaword-200" and requires 252
MB of disk space).  You can enter as many guesses as you like, and to
give up just enter:

...

as your guessed word.

## Known bugs/limitations

Sometimes the random word picked by the script is not found in the
model vocabulary, which causes the code to crash.  If that happens,
you can just relaunch it.
