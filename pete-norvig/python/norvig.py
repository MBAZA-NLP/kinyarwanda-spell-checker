import re
from collections import Counter
import json

file_path = './counter.json'

data = json.load(open(file_path, encoding='utf-8'))

WORDS = Counter(data)

# probability of a word in WORDS 
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

# get candidate with highest probability from a list
def correction(word): 
    "Most probable spelling correction for word."
    return sorted(candidates(word),key=P, reverse=True)

# create a new tuple that combines:
#   the word checked if it exists in dictionary WORDS
#   all the words in edits1; one letter away from the word, with checked if exists in dictionary WORDS
#   all the words in edits2; two letters away from the word, with checked if exists in dictionary WORDS
def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

# generate all words that appear in dictionary WORDS
def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

# splits: split word into left and right, left having from 0 to i and right the remaining
#   this is done for easier adding new letters in between 
#   example: hello = [('', 'hello'), ('h', 'ello'), ('he', 'llo'), ('hel', 'lo'), ('hell', 'o'), ('hello', '')]
#   inserting can be l='' and r='hello', insertion='ahello'

# CHECKING ONE EDIT AWAY FROM THE WORD
# deletes: removes a single letter from the word
#   this is done in case a user forgets a single letter from the word
#   example: hello = ['ello', 'hllo', 'helo', 'helo', 'hell']

# transposes: changes position of each letter in word
#   this is done in case one writes a letter in the wrong position
#   example: hello = ['ehllo', 'hlelo', 'hello', 'helol']

# replaces: replace each letter in the word one at a time by all 26 letters in alphabet
#   this is done in case one writes a wrong letter in a certain position
#   example: hello = ['aello', 'bello', 'cello', 'dello', 'eello', 'fello', 'gello', 'hello', 'iello', 'jello', 'kello', 'lello', 'mello', 'nello', 'oello', 'pello', 'qello', 'rello', 'sello', 'tello', 'uello', 'vello', 'wello', 'xello', 'yello', 'zello', 'hallo', 'hbllo', 'hcllo', 'hdllo', 'hello', 'hfllo', 'hgllo', 'hhllo', 'hillo', 'hjllo', 'hkllo', 'hlllo', 'hmllo', 'hnllo', 'hollo', 'hpllo', 'hqllo', 'hrllo', 'hsllo', 'htllo', 'hullo', 'hvllo', 'hwllo', 'hxllo', 'hyllo', 'hzllo', 'healo', 'heblo', 'heclo', 'hedlo', 'heelo', 'heflo', 'heglo', 'hehlo', 'heilo', 'hejlo', 'heklo', 'hello', 'hemlo', 'henlo', 'heolo', 'heplo', 'heqlo', 'herlo', 'heslo', 'hetlo', 'heulo', 'hevlo', 'hewlo', 'hexlo', 'heylo', 'hezlo', 'helao', 'helbo', 'helco', 'heldo', 'heleo', 'helfo', 'helgo', 'helho', 'helio', 'heljo', 'helko', 'hello', 'helmo', 'helno', 'heloo', 'helpo', 'helqo', 'helro', 'helso', 'helto', 'heluo', 'helvo', 'helwo', 'helxo', 'helyo', 'helzo', 'hella', 'hellb', 'hellc', 'helld', 'helle', 'hellf', 'hellg', 'hellh', 'helli', 'hellj', 'hellk', 'helll', 'hellm', 'helln', 'hello', 'hellp', 'hellq', 'hellr', 'hells', 'hellt', 'hellu', 'hellv', 'hellw', 'hellx', 'helly', 'hellz']

# inserts: inserts a new letter from the 26 alphabets between every left and right
#   this is done in case one adds an unnecessary word in a word
#   example: hello = ['ahello', 'bhello', 'chello', 'dhello', 'ehello', 'fhello', 'ghello', 'hhello', 'ihello', 'jhello', 'khello', 'lhello', 'mhello', 'nhello', 'ohello', 'phello', 'qhello', 'rhello', 'shello', 'thello', 'uhello', 'vhello', 'whello', 'xhello', 'yhello', 'zhello', 'haello', 'hbello', 'hcello', 'hdello', 'heello', 'hfello', 'hgello', 'hhello', 'hiello', 'hjello', 'hkello', 'hlello', 'hmello', 'hnello', 'hoello', 'hpello', 'hqello', 'hrello', 'hsello', 'htello', 'huello', 'hvello', 'hwello', 'hxello', 'hyello', 'hzello', 'heallo', 'hebllo', 'hecllo', 'hedllo', 'heello', 'hefllo', 'hegllo', 'hehllo', 'heillo', 'hejllo', 'hekllo', 'helllo', 'hemllo', 'henllo', 'heollo', 'hepllo', 'heqllo', 'herllo', 'hesllo', 'hetllo', 'heullo', 'hevllo', 'hewllo', 'hexllo', 'heyllo', 'hezllo', 'helalo', 'helblo', 'helclo', 'heldlo', 'helelo', 'helflo', 'helglo', 'helhlo', 'helilo', 'heljlo', 'helklo', 'helllo', 'helmlo', 'helnlo', 'helolo', 'helplo', 'helqlo', 'helrlo', 'helslo', 'heltlo', 'helulo', 'helvlo', 'helwlo', 'helxlo', 'helylo', 'helzlo', 'hellao', 'hellbo', 'hellco', 'helldo', 'helleo', 'hellfo', 'hellgo', 'hellho', 'hellio', 'helljo', 'hellko', 'helllo', 'hellmo', 'hellno', 'helloo', 'hellpo', 'hellqo', 'hellro', 'hellso', 'hellto', 'helluo', 'hellvo', 'hellwo', 'hellxo', 'hellyo', 'hellzo', 'helloa', 'hellob', 'helloc', 'hellod', 'helloe', 'hellof', 'hellog', 'helloh', 'helloi', 'helloj', 'hellok', 'hellol', 'hellom', 'hellon', 'helloo', 'hellop', 'helloq', 'hellor', 'hellos', 'hellot', 'hellou', 'hellov', 'hellow', 'hellox', 'helloy', 'helloz']

# function then returns a set for a combination of deletes, transposes, replaces and inserts
def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

# CHECKING TWO LETTER AWAY FROM THE WORD
#   this is done in case of 2 edits away form the word
#   done by applying edits1 to all words from a set resulting from the edits1 of the word
#   sample: hello = {'hxellok', 'eheglo', 'heelog', 'hglro', 'htdllo', 'helpmlo', 'hvellp', 'whellc', 'heyvlo', 'jhelyo', 'ghellgo', 'heyllk', 'hwelo', 'pellgo', 'hhllow', 'helvlqo', 'hellrqo', 'helqs'}
def edits2(word): 
    "All edits that are two edits away from `word`."
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))
