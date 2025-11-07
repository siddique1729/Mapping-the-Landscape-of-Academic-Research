import time
import random

print("PRNG Service started...")

while True:
    time.sleep(1)
    
    try:
        with open('prng-service.txt', 'r') as file:
            content = file.read().strip()
        
        if content == "run":
            # Generate random number
            random_number = random.randint(0, 1000)
            
            # Clear file and write random number
            with open('prng-service.txt', 'w') as file:
                file.write(str(random_number))
            
            print(f"Generated random number: {random_number}")
    
    except FileNotFoundError:
        # Create file if it doesn't exist
        with open('prng-service.txt', 'w') as file:
            file.write('')
    except Exception as e:
        print(f"Error: {e}")