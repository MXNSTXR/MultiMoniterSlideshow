# **MultiMoniterSlideshow**

This Python script creates a fullscreen slideshow of images on your secondary monitor(s).

**Features**

* Displays images from a specified folder in a fullscreen slideshow on a secondary monitor.
* Resizes images to fit the screen while maintaining aspect ratio.
* Configurable slideshow interval.

**Requirements**

* Python 3.x
* Pillow (PIL Fork)
* screeninfo
* tkinter

**Installation**

1. Install the required libraries using pip:

```bash
pip install pillow screeninfo tkinter
```

**Usage**

1. Save the script as `slideshow.py`.
2. Edit the following configuration variables in the script:

    * `image_path`: The path to the folder containing your wallpaper images.
    * `total_width` and `total_height`: The desired width and height of the slideshow (in pixels).
    * `monitor_x_offset` and `monitor_y_offset`: The offset coordinates of the secondary monitor (in pixels, negative values allowed).
    * `slideshow_interval`: The time interval (in seconds) between slide transitions.

3. Run the script from the command line:

```bash
python slideshow.py
```

**Notes**

* The script uses the `screeninfo` library to detect your secondary monitor. If you have multiple secondary monitors, the script may not display the slideshow on the desired one. You may need to adjust the `monitor_x_offset` and `monitor_y_offset` values to position the slideshow correctly.
* The script currently supports image formats like JPG, JPEG, PNG, and GIF.

**Customization**

* You can modify the `display_image` function to add additional image processing or effects.
* You can add support for additional image formats by modifying the image loading logic.

**Contributing**

Pull requests and suggestions are welcome!
```
Please let me know if you have any other questions and tips, this is my first python program I've ever made.
