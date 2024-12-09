""" from django.shortcuts import render
from django.http import JsonResponse
import numpy as np

# Import encryption functions
from .aes import aes_encrypt, aes_decrypt

def index(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text')
        key = request.POST.get('key')
        action = request.POST.get('action')

        if len(text) != 16 or len(key) != 16:
            result = "Both text and key must be 16 characters long."
        else:
            if action == 'encrypt':
                encrypted_text, perm = aes_encrypt(text, key)
                request.session['perm'] = perm.tolist()  # Store permutation in session
                result = f"Encrypted: {encrypted_text}"
            elif action == 'decrypt':
                perm = np.array(request.session.get('perm'))  # Retrieve permutation
                try:
                    decrypted_text = aes_decrypt(text, key, perm)
                    result = f"Decrypted: {decrypted_text}"
                except Exception as e:
                    result = f"Decryption failed: {e}"

    return render(request, 'encryption/index.html', {'result': result})
 """
""" from django.shortcuts import render
import numpy as np
import random
import string
from .aes import aes_encrypt, aes_decrypt

# Function to generate a random 16-character key
def generate_random_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Function to generate a random permutation
def generate_random_permutation():
    return np.random.permutation(256).tolist()  # Convert to list for JSON serialization

def index(request):
    # Default values
    random_key = generate_random_key()
    random_perm = generate_random_permutation()
    encrypted_text = ''
    decrypted_text = ''

    if request.method == 'POST':
        action = request.POST.get('action')
        text = request.POST.get('text', '')
        key = request.POST.get('key', random_key)

        # Retrieve permutation from session, convert back to numpy array
        perm = request.session.get('perm', random_perm)
        perm = np.array(perm)  # Convert list back to numpy array

        if action == 'encrypt' and len(text) == 16:
            # Encrypt the text
            encrypted_text, perm = aes_encrypt(text, key)
            request.session['perm'] = perm.tolist()  # Store as list for session storage
        elif action == 'decrypt':
            try:
                decrypted_text = aes_decrypt(text, key, perm)
            except Exception as e:
                decrypted_text = f"Error: {e}"

    return render(request, 'encryption/index.html', {
        'random_key': random_key,
        'random_perm': random_perm,
        'encrypted_text': encrypted_text,
        'decrypted_text': decrypted_text
    })
 """
from django.shortcuts import render
import numpy as np
from .aes import aes_encrypt, aes_decrypt

# Fixed permutation (provided in the problem statement)
FIXED_PERMUTATION = [
    63, 16, 124, 24, 20, 51, 234, 60, 217, 101, 83, 128, 34, 220, 227, 25, 72, 167, 133, 243, 8, 70, 82, 111, 14, 201,
    33, 52, 21, 17, 193, 196, 165, 241, 103, 197, 239, 108, 96, 198, 211, 48, 231, 244, 181, 178, 7, 28, 139, 140, 13,
    45, 149, 212, 78, 59, 114, 203, 174, 164, 225, 37, 97, 141, 253, 145, 135, 184, 131, 106, 195, 121, 74, 240, 40,
    65, 3, 182, 119, 42, 12, 255, 169, 229, 98, 170, 223, 102, 125, 1, 226, 61, 22, 26, 186, 122, 188, 77, 242, 84,
    247, 112, 32, 31, 46, 238, 152, 107, 116, 172, 237, 245, 117, 126, 56, 202, 214, 10, 176, 105, 153, 95, 154, 81,
    146, 110, 192, 207, 18, 99, 2, 147, 87, 183, 30, 85, 187, 136, 163, 75, 138, 129, 252, 88, 148, 89, 156, 100, 118,
    246, 130, 168, 151, 199, 194, 50, 236, 224, 210, 127, 228, 80, 158, 11, 71, 150, 4, 67, 62, 104, 204, 137, 35, 9,
    132, 215, 38, 250, 166, 41, 179, 160, 134, 190, 208, 185, 15, 115, 36, 68, 200, 232, 248, 54, 155, 90, 58, 249, 92,
    191, 162, 157, 175, 251, 159, 189, 44, 123, 0, 6, 5, 113, 55, 66, 29, 222, 206, 235, 213, 57, 177, 180, 219, 254,
    221, 47, 205, 53, 86, 49, 27, 43, 109, 73, 69, 120, 91, 233, 79, 94, 216, 143, 64, 76, 19, 144, 23, 161, 173, 218,
    39, 209, 230, 93, 171, 142
]

def index(request):
    # Initialize variables
    encrypted_text = ''
    decrypted_text = ''
    error_message = None

    if request.method == 'POST':
        action = request.POST.get('action')
        text = request.POST.get('text', '')
        key = request.POST.get('key', '')

        # Validate the key length (must be 16 characters)
        if len(key) != 16:
            error_message = "Secret key must be exactly 16 characters long."
        else:
            # Convert fixed permutation to numpy array
            perm = np.array(FIXED_PERMUTATION)

            if action == 'encrypt' and len(text) == 16:
                # Encrypt the text
                encrypted_text = aes_encrypt(text, key, perm)
            elif action == 'decrypt':
                try:
                    # Decrypt the text
                    decrypted_text = aes_decrypt(text, key, perm)
                except Exception as e:
                    error_message = f"Error during decryption: {e}"

    return render(request, 'encryption/index.html', {
        'encrypted_text': encrypted_text,
        'decrypted_text': decrypted_text,
        'error_message': error_message
    })
