# Cipher_Breaker
 
1.	Part 1: Cipher Implementation 

a)	Caesar Cipher
•	encrypt_caesar(plaintext, shift): This function shifts the alphabet by the number of positions specified by the shift entered in the terminal and performs the encryption by changing the plaintext according to the corresponding shifted letters.

•	decrypt_caesar(plaintext, shift): This function decrypts a message that was encrypted using the Caesar cipher by shifting the letters of the alphabet based on the given shift value. To do this, we use the previously written encrypt_caesar(plaintext, shift) function. The shift value is recalculated by subtracting it from 26, which is the length of the English alphabet. This effectively reverses the encryption and decrypts the message.

b)	Affine Cipher
encrypt_affine(plaintext, shift): 

decrypt_affine(plaintext, shift): 



c)	Mono-alphabetic Substitution Cipher
encrypt_mono(plaintext, shift): 

decrypt_mono(plaintext, shift): 




2.	Part 2: Cryptanalysis

a)	Caesar Cipher
•	break_caesar(ciphertext): This function calls the decrypt_caesar function for all shift values from 1 to 25. It checks the number of valid words in each solution using the count_valid_words function. The solution with the highest word count is stored and saved to a file.

b)	Affine Cipher
•	break_affine(ciphertext): This function takes values of “a” between 1 and 25 and checks for values that have a greatest common divisor (gcd) of 1 with 26. For each “a”, it tries values of “b” from 0 to 25. It calls the decrypt_affine function from ciphers.py that we already defined and checks the number of valid words in each solution.
•	are_relatively_prime(a,b): This function calculates whether two numbers are relatively prime using the Euclidean algorithm.
•	count_valid_words(text): This function converts the text to lowercase, splits it into words, and checks if each word exists in the previously loaded set of words (dictionary).

c)	Mono-alphabetic Cipher
•	break_mono(ciphertext): This function decrypts a text encrypted with a mono-alphabetic substitution cipher. We use a dictionary-type variable called decrypted_message, which stores the mapping of each letter in the ciphertext to its corresponding letter in the English alphabet as we discover them. Punctuation marks and newline characters are removed when reading the encrypted text, and each word is stored in a list called words.

We base our frequency analysis on the standard letter frequency of the English language, which is "ETAOINSHRDLCUMWFGYPBVKJXQZ". We assume that “E” is the most frequently used letter in any long text. Using this assumption, we try to identify as many letters as possible. Next, we identify “a” by finding the most common letter among single-letter words. After that, we look for three-letter words like “and” and “the”, using certain limitations. For the word “from,” if it doesn’t appear in the text, we simply skip it. By this process, we aim to decrypt thirteen letters. As each letter is discovered, the corresponding variables are updated. The process order to find thirteen letter is below:
 ![image](https://github.com/user-attachments/assets/17488543-ed73-4477-83ea-5e2118e92026)


The letters that are not yet identified are listed as their equivalents in the English alphabet under not_found_letters_alph = ['S', 'L', 'C', 'U', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'], and the corresponding encrypted letters are listed in not_found_letters_text = ['L', 'S', 'X', 'E', 'N', 'H', 'W', 'C', 'A', 'B', 'P', 'J', 'M'] based on frequency analysis.

The expression (if len(word) * 0.8 <= count < len(word)) is used to verify that the word being checked contains enough known letters (at least 80%) while still leaving some letters unknown. Using the known letters, the encrypted word is partially decrypted, and any unknown letters are added to a list. In not_found_letters_text, we match the encrypted letters with their potential equivalents in not_found_letters_alph, and check if the decrypted word exists in dictionary.txt. If the frequencies don’t match, we check the letters directly adjacent in the frequency order. If it still doesn’t match, we check two positions to the left and right. We stop there, assuming that the letter frequency of a long text won’t deviate significantly from the standard. This process continues until every letter in the word is known.





