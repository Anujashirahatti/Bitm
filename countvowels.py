def count_vowels(string):
    vowels="abedf"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
input_string='anuja'
vowels_count=count_vowels(input_string)
print(vowels_count)