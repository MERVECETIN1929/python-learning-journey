def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                  "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morse_code_sets = set()
    for x in words:
        morse_code_word = str()
        for y in x:
            # ord(y)-ord("a") y harfinin hangi sıradaki mors codune denk geleceğini belirtir.
            morse_code_word += morse_code[ord(y)-ord("a")]
        morse_code_sets.add(morse_code_word)
    return len(morse_code_sets)


print(uniqueMorseRepresentations(["a"]))
