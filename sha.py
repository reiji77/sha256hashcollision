import hashlib
from pathlib import Path
from itertools import product
import math


def calcSha256(text):
    dum = ''.join(text)
    return hashlib.sha256(dum.encode('utf-8')).hexdigest()


def calcLastNSame(realSha, fakeSha, matching):
    matching += 1
    
    if realSha[-matching:] == fakeSha[-matching:]:
        print(f"{matching} number of matching last")
        return True
    return False


def main():
    p1 = Path(__file__).with_name('fake.txt')
    fake_file = p1.open('r', encoding='utf-8')
    p2 = Path(__file__).with_name('real.txt')
    real_file = p2.open('r', encoding='utf-8')
    fake_text = fake_file.readlines()
    real_text = real_file.read()
    fake_file.close()
    real_file.close()
    realHash = hashlib.sha256(real_text.encode('utf-8')).hexdigest()
    print(f"real sha is {realHash}")
    fakeHash = calcSha256(fake_text)
    print(f"fake sha is {fakeHash}")
    matching = 0 
    
    for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a1 in product([True, False], repeat=27):
        spaceStatus = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a1]
        for i in range(0, 26):
            if spaceStatus[i]:
                if fake_text[i][-1] != ' ':
                    update = fake_text[i] + ' '
                    fake_text[i] = update
            else:
                if fake_text[i][-1] == ' ':
                    update = fake_text[i][:-1]
                    fake_text[i] = update
        if calcLastNSame(realHash, calcSha256(fake_text), matching):
                matching += 1
                com = input(f"last {matching} digits match. fakeSha: {calcSha256(fake_text)}. Press anything to continue")
                if matching == 5:
                    print(fake_text)
                    fake_adjusted = open('fake_adjusted.txt', 'w')
                    fake_adjusted.writelines(fake_text)
                    fake_adjusted.close()
                    return
                    


    



if __name__ == '__main__': 
    main()
