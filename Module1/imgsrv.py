import time
import os

print("Image Service started...")

# Number of images available
NUM_IMAGES = 3

while True:
    time.sleep(1)
    
    try:
        with open('image-service.txt', 'r') as file:
            content = file.read().strip()
        
        # Check if content is a number
        if content and content.isdigit():
            number = int(content)
            
            # Use modulo to wrap around if number >= NUM_IMAGES
            image_index = number % NUM_IMAGES
            
            # Since images are 1.jpg, 2.jpg, 3.jpg, we need to add 1
            image_number = image_index + 1
            
            # Create path to image
            image_path = f"cs361/{image_number}.jpg"
            
            # Clear file and write image path
            with open('image-service.txt', 'w') as file:
                file.write(image_path)
            
            print(f"Received number: {number}, returning image: {image_path}")
    
    except FileNotFoundError:
        # Create file if it doesn't exist
        with open('image-service.txt', 'w') as file:
            file.write('')
    except Exception as e:
        print(f"Error: {e}")