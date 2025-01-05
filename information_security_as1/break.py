import argparse
import re
from collections import Counter
from ciphers import decrypt_affine
from ciphers import decrypt_caesar
from ciphers import are_relatively_prime

with open("dictionary.txt", 'r') as file:
    dictionary= set(word.strip().lower() for word in file)

#nkrru se tgsk oy hayxg gtj o gs zxeotm zu atjkxyzgtj
#armmv pz sfpr dh inhef fso d fp kezdsx kv nsorehkfso

# python break.py caesar coded.txt
def break_caesar(ciphertext):
    real_text = ""
    max_word_count = 0

    for shift in range(1, 26):  # Shift from 1 to 25
        decrypted_text = decrypt_caesar(ciphertext, shift)
        word_count = count_valid_words(decrypted_text)

        if word_count > max_word_count:
            max_word_count = word_count
            real_text = decrypted_text

    return real_text


def count_valid_words(text):
    words = text.lower().split()
    return sum(1 for word in words if word in dictionary)


# python break.py affine coded.txt
def break_affine(ciphertext):
    real_text = ""
    max_word_count = 0
    for a in range(1, 26):
        if are_relatively_prime(a, 26):  # 'a' must be coprime with 26
            for b in range(26):
                decrypted_text = decrypt_affine(ciphertext, a, b)
                word_count = count_valid_words(decrypted_text)

                if word_count > max_word_count:
                    max_word_count = word_count
                    real_text = decrypted_text

    return real_text


# python break.py mono coded.txt
def break_mono(ciphertext):
    dict_file = "dictionary.txt"
    english_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    decrypt_message = {'A': "", 'B': "", 'C': "", 'D': "", 'E': "", 'F': "", 'G': "", 'H': "", 'I': "", 'J': "", 'K': "", 'L': "", 'M': "", 
                   'N': "", 'O': "", 'P': "", 'Q': "", 'R': "", 'S': "", 'T': "", 'U': "", 'V': "", 'W': "", 'X': "", 'Y': "", 'Z': ""}


    with open(dict_file, "r") as df:
        read_df = df.read().replace("\n"," ").upper()
        dict_words = re.split(r'[ ]', read_df)
    if (dict_words[-1] == ""):
        dict_words = dict_words[:-1]
 

    sorted_letter_count_message = ''.join([letter for letter, _ in Counter(ciphertext).most_common() if (not letter.isdigit() and letter.isalpha())])
    most_common_letter = sorted_letter_count_message[0]
    
    words = []
    words = (re.split(r'[ ]', text1))
    if (words[-1] == ""):
        words = words[:-1]
 

    # Tek harfli sadece harflerden oluşan kelimeler
    one_letter_words = [word for word in words if len(word) == 1 and not word.isdigit()]  

# Tek harfli kelimeleri say
    if one_letter_words:
        counter = Counter(one_letter_words)
        most_common_letter_1, frequency_1 = counter.most_common(1)[0]  # En çok geçen harf ve sayısı


    word_count_2 = Counter()
    word_count_3 = Counter()
    word_count_4 = Counter()
    word_count_ing = Counter()
    word_count_ty = Counter()
    
    for word in words:
        if (len(word) == 3) and not word.isdigit():  
            word_count_3[word] += 1
        if (len(word) == 2) and not word.isdigit(): 
            word_count_2[word] += 1
        if (len(word) == 4) and not word.isdigit(): 
            word_count_4[word] += 1
        if (len(word) > 3) and not word.isdigit(): 
            word_count_ing[word[-3:]] += 1
        if (len(word) > 2) and not word.isdigit(): 
            word_count_ty[word[-2:]] += 1


    # A ile başlayan 3 harfli kelimeler
    A_words = Counter({word: count for word, count in word_count_3.items() if word.startswith(most_common_letter_1)})
 
    # and bulma kısmı
    most_common_word_3, frequency_3 = A_words.most_common(1)[0]  # A ile başlayan ve en fazla geçen 3 harfli kelime ve frekansı
    A = most_common_word_3[0]
    N = most_common_word_3[1]
    D = most_common_word_3[2]
    E = most_common_letter

    decrypt_message[most_common_word_3[0]] = "A"
    decrypt_message[most_common_word_3[1]] = "N"  
    decrypt_message[most_common_word_3[2]] = "D"  

    # the bulma kısmı
    The_word = Counter({word: count for word, count in word_count_3.items() if (word.endswith(E) and not word.startswith(A))})
    tofind_The, frequency_The = The_word.most_common(1)[0]
    T = tofind_The[0]
    H = tofind_The[1]

    decrypt_message[tofind_The[0]] = "T"
    decrypt_message[tofind_The[1]] = "H"  
    decrypt_message[tofind_The[2]] = "E" 

    
    # to bulma kısmı
    T_words = Counter({word: count for word, count in word_count_2.items() if word.startswith(T)})
    tofind_To, frequency_To = T_words.most_common(1)[0]
    O = tofind_To[1]

    decrypt_message[tofind_To[1]] = "O"


    # of bulma kısmı
    O_words = Counter({word: count for word, count in word_count_2.items() if word.startswith(O)})
    tofind_of, frequency_of = O_words.most_common(1)[0]
    F = tofind_of[1]

    decrypt_message[tofind_of[1]] = "F"

    # with bulma kısmı
    word_with = Counter({word: count for word, count in word_count_4.items() if (word[2]==T and word[3]==H)})
    tofind_with,frequency_with = word_with.most_common(1)[0]
    W = tofind_with[0]
    I = tofind_with[1]

    decrypt_message[tofind_with[0]] = "W"
    decrypt_message[tofind_with[1]] = "I"

    # are bulma kısmı
    word_are = Counter({word: count for word, count in word_count_3.items() if (word[0] == A and word[2] == E)})
    tofind_are, frequency_are = word_are.most_common(1)[0]
    R = tofind_are[1]

    decrypt_message[tofind_are[1]] = "R"

    # from bulma kısmı
    word_from = Counter({word: count for word, count in word_count_4.items() if (word[2] == O and word[0] == F and word[1] == R)})
    if len(word_from) != 0:
        tofind_from, frequency_from = word_from.most_common(1)[0]
        M = tofind_from[3]
        
        decrypt_message[tofind_from[3]] = "M"

    # -ing bulma kısmı
    word_ing = Counter({word: count for word, count in word_count_ing.items() if (word.startswith(I) and word[1] == N)})
    tofind_ing, frequency_ing = word_ing.most_common(1)[0]
    G = tofind_ing[2]

    decrypt_message[tofind_ing[2]] = "G"
    
        
    not_found_letters_alph = list(english_frequency)
    not_found_letters_text = list(sorted_letter_count_message)
    
    for x in decrypt_message.keys():
        if decrypt_message[x] != "":
            not_found_letters_alph.remove(decrypt_message[x])
            not_found_letters_text.remove(x)
  

    for word in words:
        count = 0
        for letter in word:
            if letter not in not_found_letters_text:
                count += 1      # how many letters has already found in the word
        

        if len(word) * 0.8 <= count < len(word):
            missing_letters = []
            missing_letters_index = []
            decrypted_word = list(word)
            
            for i in range(len(decrypted_word)):
                decrypted_char = decrypt_message.get(decrypted_word[i], decrypted_word[i])  # decryption
                if decrypted_char != "":  # Eğer karşılık boş değilse
                    decrypted_word[i] = decrypted_char  
                else:
                    missing_letters.append(decrypted_word[i])
                    missing_letters_index.append(i)
            
            
            len_missing_letters = len(missing_letters)

            for i in range(len_missing_letters):
                miss_letter = missing_letters[i]
                miss_index = missing_letters_index[i]
                miss_alph_ind = not_found_letters_text.index(miss_letter)
                decrypted_word[miss_index] = not_found_letters_alph[miss_alph_ind]
                if ''.join(decrypted_word) in dict_words:
                    
                    decrypt_message[miss_letter] = not_found_letters_alph[miss_alph_ind]
                    not_found_letters_alph.pop(miss_alph_ind)
                    not_found_letters_text.pop(miss_alph_ind)
                    if len_missing_letters - 1 == i:
                        break
                    
                else:     
                    if miss_alph_ind > 0:
                        decrypted_word[miss_index] = not_found_letters_alph[miss_alph_ind-1] 
                        if ''.join(decrypted_word) in dict_words:
                            decrypt_message[miss_letter] = not_found_letters_alph[miss_alph_ind-1]
                            not_found_letters_alph.pop(miss_alph_ind-1)
                            not_found_letters_text.pop(miss_alph_ind)
                            if len_missing_letters - 1 == i:
                                break
                        else:
                            if miss_alph_ind > 1:
                                decrypted_word[miss_index] = not_found_letters_alph[miss_alph_ind-2] 
                                if ''.join(decrypted_word) in dict_words:
                                    decrypt_message[miss_letter] = not_found_letters_alph[miss_alph_ind-2]
                                    not_found_letters_alph.pop(miss_alph_ind-2)
                                    not_found_letters_text.pop(miss_alph_ind)
                                    if len_missing_letters - 1 == i:
                                        break
                                else: 
                                    if miss_alph_ind < len(not_found_letters_alph) - 1:
                                        decrypted_word[miss_index] = not_found_letters_alph[miss_alph_ind+1] 
                                        if ''.join(decrypted_word) in dict_words:
                                            decrypt_message[miss_letter] = not_found_letters_alph[miss_alph_ind+1]
                                            not_found_letters_alph.pop(miss_alph_ind+1)
                                            not_found_letters_text.pop(miss_alph_ind)
                                            if len_missing_letters - 1 == i:
                                                break
                                        else:
                                            if miss_alph_ind < len(not_found_letters_alph) - 2:
                                                decrypted_word[miss_index] = not_found_letters_alph[miss_alph_ind+2] 
                                                if ''.join(decrypted_word) in dict_words:
                                                    decrypt_message[miss_letter] = not_found_letters_alph[miss_alph_ind+2]
                                                    not_found_letters_alph.pop(miss_alph_ind+2)
                                                    not_found_letters_text.pop(miss_alph_ind)
                                                    if len_missing_letters - 1 == i:
                                                        break
                                                                                                                       

    with open(args.file, "r") as fl:
        open_file = fl.read()

    open_file_list = list(open_file)

    # Her bir karakteri kontrol et ve değiştirme işlemi yap
    for i in range(len(open_file_list)):
        if not open_file_list[i].isdigit() and open_file_list[i].isalpha():  # Sayı değilse ve harfse
            character = open_file_list[i]
            decrypted_char = decrypt_message.get(open_file_list[i].upper(), open_file_list[i])  # decryption
            if decrypted_char != "":                # Eğer karşılık boş değilse
                open_file_list[i] = decrypted_char  # Değiştir
                if character.isupper():
                    open_file_list[i] = decrypted_char.upper()  # Büyük harf ise büyük yap
                else:
                    open_file_list[i] = decrypted_char.lower()  

    # Listeyi tekrar stringe dönüştür
    open_file = ''.join(open_file_list)

    return open_file
    



parser = argparse.ArgumentParser(prog="ciphers",description="decrypt ciphers")

parser.add_argument("cipher", help="Choose cipher: caesar, affine, mono")
parser.add_argument("file", help="Input file containing the text")

args = parser.parse_args()


with open(args.file, "r") as f_mono:
    text = re.sub(r'[.,;:!?()\'\"[\]{}<>]', '', f_mono.read()).upper()
    text1 = text.replace("\n"," ")

with open(args.file, "r") as f_other:
    text2 = f_other.read()


if args.cipher == "caesar":
    with open('break_caesar.txt', 'w') as file:
        file.write(break_caesar(text2))

elif args.cipher == "affine":
    with open('break_affine.txt', 'w') as file:
        file.write(break_affine(text2))

elif args.cipher == "mono":
    with open("break_mono.txt", "w") as new_file:
        new_file.write(break_mono(text))


