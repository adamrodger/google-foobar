# please excuse me, I'm a C# and Rust developer with only minor Python experience :D
# let's give it a go though!

MAP = {
    'a': "100000", 'n': "101110",
    'b': "110000", 'o': "101010",
    'c': "100100", 'p': "111100",
    'd': "100110", 'q': "111110",
    'e': "100010", 'r': "111010",
    'f': "110100", 's': "011100",
    'g': "110110", 't': "011110",
    'h': "110010", 'u': "101001",
    'i': "010100", 'v': "111001",
    'j': "010110", 'w': "010111",
    'k': "101000", 'x': "101101",
    'l': "111000", 'y': "101111",
    'm': "101100", 'z': "101011",
    ' ': "000000"
}

def solution(s):
    mapped = []
    
    for c in s:
        if c.isupper():
            # upper-case escape string
            mapped.append("000001")
        mapped.append(MAP[c.lower()])
    
    return "".join(mapped)
    
if __name__ == "__main__":
    assert solution("The quick brown fox jumps over the lazy dog") == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"