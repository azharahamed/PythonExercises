def alphabet_position(letter):
  char = letter.lower()
  return ord(char)-97

def rotate_character(char,rot):
  new_position = (alphabet_position(char)+rot)%26 if char.isalpha() else ord(char)
  return chr(new_position+97) if char.islower() else chr(new_position+65)  if char.isupper() else chr(new_position) 
  
def encrypt(text, rot):
  a_list = [char for char in text]
  return ''.join(rotate_character(item,rot) for item in a_list)

def main():
    # your main code (input and print statements)
    print(alphabet_position('z'))
    print(alphabet_position('Z'))
    print(rotate_character('%',13))
    print(encrypt('LaunchCode',13))
    print(encrypt('LaunchCode',1))
    print(encrypt('Hello, World!',5))
    
    message = input("\nType a message \n")
    rotate = int(input("Rotate by :\n"))
    print(encrypt(message,rotate))

if __name__ == "__main__":
    main()