#!/usr/bin/env python3

import sys

from itertools import product

if len(sys.argv) < 2:
    print(
        "Missing arguments. Usage:  $ url_generator.py mydomain.com domain2.org etc.net"
    )

lookup = {
    "a": ["ａ", "𝐚", "𝖺", "𝚊", "ɑ", "а"],
    "b": ["𝐛", "𝖻", "𝚋", "Ƅ", "Ь", "Ꮟ", "ᖯ"],
    "c": ["ｃ", "ⅽ", "𝐜", "𝖼", "𝗰", "𝚌", "ᴄ", "ϲ", "ⲥ", "с", "𐐽"],
    "d": ["ⅾ", "𝐝", "𝖽", "𝚍", "ԁ", "Ꮷ", "ᑯ", "ꓒ"],
    "e": ["℮", "ｅ", "𝐞", "𝖾", "𝚎", "е"],
    "f": ["𝐟", "𝖿", "𝚏", "ꬵ"],
    "g": ["ｇ", "ℊ", "𝐠", "𝗀", "𝚐", "ɡ"],
    "h": ["ｈ", "𝐡", "𝗁", "𝚑", "һ", "հ"],
    "i": ["ｉ", "ⅰ", "𝐢", "𝖎", "𝗂", "𝗶", "𝚒", "і", "Ꭵ"],
    "j": ["ｊ", "𝐣", "𝔧", "𝗃", "𝚓", "ϳ", "ј"],
    "k": ["𝐤", "𝗄", "𝚔", "ᴋ", "ĸ", "κ", "𝛋", "ⲕ", "к"],
    "l": ["Ɩ", "ⅼ", "𝐥", "𝔩", "𝗅", "Ⲓ", "ﺎ", "ﺍ", "ߊ", "ⵏ", "ꓲ", "𐊊", "𐌉"],
    "m": ["m"],
    "n": ["𝐧", "𝗇", "𝚗", "ᴨ", "п", "ո"],
    "o": ["൦", "๐", "໐", "𝐨", "𝗈", "𝚘", "ᴏ", "ο", "ⲟ", "о", "ჿ", "օ", "ဝ", "𐐬"],
    "p": ["⍴", "ｐ", "𝗉", "𝚙", "𝛒", "р"],
    "q": ["𝐪", "𝗊", "𝚚", "ԛ", "զ"],
    "r": ["𝐫", "𝗋", "𝚛", "ꭇ", "ꭈ", "ᴦ", "г"],
    "s": ["𝐬", "𝗌", "𝚜", "ꜱ", "ѕ", "𐑈"],
    "t": ["𝐭", "𝗍", "𝚝"],
    "u": ["𝐮", "𝗎", "𝚞", "ս"],
    "v": ["∨", "ｖ", "ⅴ", "𝐯", "𝗏", "𝚟", "ᴠ", "ν", "ѵ"],
    "w": ["w"],
    "x": ["ｘ", "ⅹ", "𝐱", "𝗑", "𝚡", "х"],
    "y": ["ｙ", "𝐲", "𝗒", "𝚢", "ʏ", "у"],
    "z": ["𝐳", "𝗓", "𝚣", "ᴢ"],
}


# print out substitute urls
for url in sys.argv[1:]:
    segments = url.split(".")
    iterables = []
    for letter in segments[0]:
        iterables.append(lookup[letter] if letter in lookup else [letter])
    for permutation in product(*iterables):
        domain = "".join(permutation)
        if segments[1:]:
            domain += "." + ".".join(segments[1:])
        print(domain)
