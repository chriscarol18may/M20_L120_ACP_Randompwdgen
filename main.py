import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits          # 0-9
    
    # Combine all character sets
    all_characters = lower + upper + digits
    
    # Ensure password contains at least one lower, upper, and digit
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length-3)
    
    # Shuffle the password to randomize character positions
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

# Example usage:
password_length = 12  # Desired password length
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)