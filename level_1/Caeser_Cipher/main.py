alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else :
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

import art
print(art.logo)


flag = 1
while flag :
  direction = input("Encode or Decode : ").lower()
  text = input("Enter message :")
  shift = int(input("Shift amount: "))
  shift = shift % 26
    
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  check = input("Would you like to try again? (y/n)").lower()
  if check == "n" :
    flag = 0

