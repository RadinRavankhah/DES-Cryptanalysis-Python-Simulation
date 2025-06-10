def xor(t1: str, t2: str) -> str:
    res = ""
    for i in range(len(t1)):
        res += '0' if t1[i] == t2[i] else '1'
    return res

def sbox(input: str) -> str:
    sbox_dict = {
        '0000': '1110', '0001': '0100', '0010': '1101', '0011': '0001',
        '0100': '0010', '0101': '1111', '0110': '1011', '0111': '1000',
        '1000': '0011', '1001': '1010', '1010': '0110', '1011': '1100',
        '1100': '0101', '1101': '1001', '1110': '0000', '1111': '0111'
    }
    return sbox_dict[input]

def f_func(r: str, subkey: str) -> str:
    return sbox(xor(r, subkey))

def round_func(text: str, subkey: str) -> str:
    l, r = text[:4], text[4:]
    return r + xor(l, f_func(r, subkey))

def encrypt(text: str, key: str) -> str:
    subkey1, subkey2 = key[:4], key[4:]
    res = round_func(round_func(text, subkey1), subkey2)
    return res

# Simulate encryption oracle (in practice, query the system)
def oracle_encrypt(plaintext: str) -> str:
    secret_key = "10100111"  # Example key 10100111
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {encrypt(plaintext, secret_key)}")
    return encrypt(plaintext, secret_key)

# Differential cryptanalysis attack
# pairs = [("00000000", "00000001"), ("00000100", "00000101"), ("00001000", "00001001")]
pairs = [("00000000", "00000010"), ("00000100", "00000110"), ("00001000", "00001010")]
ciphertexts = [(oracle_encrypt(p1), oracle_encrypt(p2)) for p1, p2 in pairs]

candidates = set(range(16))  # All possible subkeys: 0 to 15
for (c1, c2) in ciphertexts:
    delta_c = xor(c1, c2)
    # print(delta_c)
    delta_r2 = delta_c[4:]
    delta_f2 = xor("0010", delta_r2)
    print("delta f2:",delta_f2)
    l2, l2_prime = c1[:4], c2[:4]
    new_candidates = set()
    for k2 in candidates:
        k2_str = format(k2, '04b')
        print(f"Trying subkey2: {k2_str}")
        if xor(sbox(xor(l2, k2_str)), sbox(xor(l2_prime, k2_str))) == delta_f2:  # delta_f2 is the difference between r2 and r2_prime, minus the differential we added.
            # so if the condition above is true over the full loop, that means this k2_str, is causing the same difference in the sbox, for all the pairs
            new_candidates.add(k2)
            print(k2_str, "is a possible subkey2")
    candidates = candidates.intersection(new_candidates)
    if len(candidates) == 1:
        break

subkey2 = format(candidates.pop(), '04b')
print(f"Recovered subkey2: {subkey2}")  # Should print "0111" for our example