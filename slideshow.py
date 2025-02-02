import os
import time
from PIL import Image, ImageTk
from screeninfo import get_monitors
import tkinter as tk

# Configuration
image_path = r"D:\Pictures\ComfyUIFlux"  # Use raw string
total_width, total_height = (3743, 2375)
# new_width, new_height = (nw, nh)
monitor_x_offset = -1034
monitor_y_offset = -1090
slideshow_interval = 5
images = []
image_index = 0

def load_and_resize_image(image_path, width, height): # , max_width, max_height
    """Loads an image and resizes it to the specified dimensions."""
    try:
        image = Image.open(image_path)

        # Calculate the scaling factors
        width_ratio = total_width / image.width
        height_ratio = total_height / image.height
        scale = min(width_ratio, height_ratio)

        # Calculate new dimensions
        new_width = int(image.width * scale)
        new_height = int(image.height * scale)

        image = image.resize((new_width, new_height), Image.LANCZOS)
        return image
    except FileNotFoundError:
        print(f"Image not found: {image_path}")
        return None
    except IOError:
        print(f"Error reading image: {image_path}")
        return None
    except Exception as e:
        print(f"Error loading image: {image_path} - {str(e)}")
        return None

def display_image(image_path, root, canvas):
    """Displays an image on the canvas."""
    image = load_and_resize_image(image_path, total_width, total_height)
    if image:
        photo_image = ImageTk.PhotoImage(image)
        # Calculate center coordinates
        x = (total_width - image.width) // 2
        y = (total_height - image.height) // 2
        canvas.create_image(x, y, anchor=tk.NW, image=photo_image) 
        canvas.image = photo_image 

def slideshow():
    """Cycles through images in a slideshow."""
    global image_index 

    if image_index >= len(images):
        image_index = 0  # Loop back to the first image

    display_image(images[image_index], root, canvas) 
    root.update() 
    time.sleep(slideshow_interval)

    image_index += 1 
    root.after(slideshow_interval * 1000, slideshow)  # Schedule the next slide

# Create Tkinter root window
root = tk.Tk()
root.overrideredirect(True) # Remove title bar and borders
root.attributes('-fullscreen', False)
root.geometry(f'{total_width}x{total_height}+{monitor_x_offset}+{monitor_y_offset}') 
root.configure(bg='black')
root.bind('<Escape>', lambda e: root.destroy())

# Create canvas object and pack it into the root window
canvas = tk.Canvas(root, width=total_width, height=total_height, bg='black') # Backgound color
canvas.pack()

def run_slideshow(image_path, slideshow_interval):

    global images
    try:
        # Load all image files in the folder
        images = [os.path.join(image_path, file) 
                  for file in os.listdir(image_path) 
                  if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        # print(images) # Print the formatted list (for verification)

        root.after(0, slideshow) # Start the slideshow after the root window is initialized
        root.mainloop() # loops the slideshow
    except Exception as e:
        print(f'Failed to start slideshow: {str(e)}')

if __name__ == '__main__':
    run_slideshow(image_path, slideshow_interval)