# Simplified DES Cryptanalysis Simulation

This project contains a Python script that demonstrates a simplified version of the Data Encryption Standard (DES) cipher and shows how to break it using differential cryptanalysis. It’s designed for educational purposes to help students understand how block ciphers work and how cryptanalysis can find secret keys. The code is simple and uses an 8-bit block cipher with a single S-box, unlike the real DES, which is more complex.

## What This Code Does

* **Cipher Simulation** : The code implements a basic block cipher that encrypts 8-bit plaintexts using an 8-bit key over two rounds, similar to how DES works but much simpler.
* **Differential Cryptanalysis** : It shows how to use differential cryptanalysis, a technique to recover part of the secret key (the second subkey) by analyzing pairs of plaintexts and their ciphertexts.
* **Educational Goal** : Helps students learn about Feistel networks, S-boxes, and how cryptanalysts exploit patterns to break encryption.

## Prerequisites

To run this code, you need:

* **Python 3** : Any recent version of Python (e.g., Python 3.8 or higher) will work.
* A basic text editor or Python IDE (like VS Code, PyCharm, or IDLE).
* No external libraries are required; the code uses only standard Python.

## How to Run the Code

1. **Save the Code** :

* Copy the Python code into a file named `des_cryptanalysis.py` (or any name you prefer, but make sure it ends with `.py`).

1. **Run the Script** :

* Open a terminal or command prompt.
* Navigate to the folder containing `des_cryptanalysis.py`.
* Run the command:
  ```bash
  python des_cryptanalysis.py
  ```
* The script will:
  * Encrypt three pairs of plaintexts using a secret key (`10100111`).
  * Print the plaintexts and their ciphertexts.
  * Perform differential cryptanalysis to recover the second subkey (`0111`).
  * Output the recovered subkey.

1. **Expected Output** :

* You’ll see plaintext-ciphertext pairs for three sets of inputs.
* The script will test possible subkeys and print which ones work.
* At the end, it should print: `Recovered subkey2: 0111`.

## How the Code Works

### Part 1: The Simplified DES Cipher

The cipher takes an 8-bit plaintext (e.g., `00000000`) and an 8-bit key (e.g., `10100111`) and encrypts the plaintext over two rounds. Here’s how it works:

* **XOR Function** : Combines two binary strings by comparing each bit. If the bits are the same (`0` and `0`, or `1` and `1`), it outputs `0`; if different, it outputs `1`.
* **S-box** : A lookup table that takes a 4-bit input and produces a 4-bit output, adding nonlinearity to the cipher (like a secret codebook).
* **F-function** : XORs part of the plaintext with a subkey, then passes it through the S-box.
* **Round Function** : Splits the 8-bit plaintext into two 4-bit halves (left and right), processes them using the F-function, and swaps them in a Feistel structure.
* **Encryption** : Runs two rounds, using two 4-bit subkeys derived from the 8-bit key.
* **Oracle** : Pretends to be the encryption system, using a fixed secret key (`10100111`) to encrypt inputs.

### Part 2: Differential Cryptanalysis

Differential cryptanalysis finds the secret key by studying how differences in plaintexts lead to differences in ciphertexts. The code:

* Chooses pairs of plaintexts that differ in a specific way (e.g., `00000000` and `00000010`, differing in one bit).
* Encrypts these pairs to get ciphertexts.
* Analyzes the ciphertext differences to guess the second subkey (`subkey2`).
* Tests all possible 4-bit subkeys (16 options) and keeps those that match the expected pattern.
* Narrows down the subkeys until only one remains, which should be `0111`.

### Key Concepts

* **Feistel Network** : The cipher splits data into two halves and processes them alternately, a common design in block ciphers like DES.
* **S-box** : A critical component that makes the cipher hard to break by mixing bits in a nonlinear way.
* **Differential Cryptanalysis** : A method to break ciphers by looking at how input differences affect output differences, revealing key information.

## Example Output

When you run the script, you’ll see something like:

```
Plaintext: 00000000
Ciphertext: 01100100
Plaintext: 00000010
Ciphertext: 00110000
...
delta f2: 0110
Trying subkey2: 0000
Trying subkey2: 0001
...
0111 is a possible subkey2
Recovered subkey2: 0111
```

This shows the encryption process and the attack narrowing down to the correct subkey.

## Diagram of Simplified DES Cryptanalysis

[diagram of simplified des cryptanalysis](https://github.com/RadinRavankhah/DES-Cryptanalysis-Python-Simulation/blob/main/des_cryptanalysis_diagram.png)

## Tips for Students

* **Experiment** : Try changing the plaintext pairs or the secret key in the `oracle_encrypt` function to see how the attack behaves.
* **Debugging** : The `print` statements show intermediate steps. Study them to understand how the subkey is recovered.
* **Learn the S-box** : Look at the `sbox_dict` to see how it maps inputs to outputs. Try computing its differential distribution (how input differences lead to output differences).
* **Limitations** : This is a toy cipher, not real DES. Real DES uses 64-bit blocks, 56-bit keys, and 8 S-boxes, making it much harder to break.

## Limitations

* The cipher is very simplified (8-bit instead of 64-bit, one S-box instead of eight).
* The attack assumes specific differences and may not work for all S-boxes or keys without modification.
* No input validation, so ensure inputs are 8-bit binary strings (e.g., `00000000`).

## Further Learning

* Read about DES and Feistel networks in cryptography textbooks or online resources.
* Explore real differential cryptanalysis attacks on DES to see how they scale up.
* Try modifying the S-box or adding more rounds to see how it affects the attack.
