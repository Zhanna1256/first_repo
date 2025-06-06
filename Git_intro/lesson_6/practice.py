# 1
# text = "Hello world"
# found = False
# for char in text:
#     if char.isupper():
#         print(f"Первая заглавная буква {char}")
#         found = True
#         break
# if not found:
#     print("Нет заглавных букв")


# 2
# text = "!!!Hello !!! world!!!"
# while len(text)> 0 and text[-1]=="!":
#     text = text[:-1]
# print(text)



# while text.endswith("!"):
#     text = text[:-1]
# print(text)

# 3
# text = "Python 3.13 is awesome in 2025"
# result = ""
# for char in text:
#     if not char.isdigit():
#         result += char
# print(result)

# 4
# text = "Hello world 23232 1321 brother "
# vowels = "aeiouy"
# vowels_count = 0
# consonant_count = 0
# for char in text:
#     if char.isalpha():
#         if char.lower() in vowels:
#             vowels_count += 1
#         else:
#             consonant_count += 1
# print(f"Согласных = {consonant_count}, гласных = {vowels_count}")


# 5

# text = "This is a simple Python string example"
# words = text.split()
# for word  in words:
#     if len(word) >4:
#         print(word)
    
# 6

animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра"]
unique_animals = []
counts = []

for animal in animals:
    if animal not in unique_animals:
        unique_animals.append(animal)
        counts.append(1)
    else:
        index = unique_animals.index(animal)
        counts[index] += 1 
for i in range(len(unique_animals)):
    print(f"{unique_animals[i]}: {counts[i]}")

