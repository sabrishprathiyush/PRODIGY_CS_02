from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
   
    image = Image.open(input_image_path)
    image_array = np.array(image)

 
    encrypted_array = image_array ^ key


    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_image_path)

    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):

    encrypted_image = Image.open(input_image_path)
    encrypted_array = np.array(encrypted_image)

   
    decrypted_array = encrypted_array ^ key

    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_image_path)

    print(f"Image decrypted and saved to {output_image_path}")


if __name__ == "__main__":
    key = 123  

  
    encrypt_image('input.jpg', 'encrypted.png', key)


    decrypt_image('encrypted.png', 'decrypted.png', key)
