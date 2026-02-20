print("Loading...")
from rembg import remove
from PIL import Image, ImageGrab
import io
import tkinter as tk
from tkinter import filedialog
import subprocess
import json
import sys
import os

root= tk.Tk()
root.withdraw()

if not os.path.exists("config.json"):
    with open("config.json", "w") as config_file:
        config_data = {
            "input": 3,
            "save": 3,
            "first_run": False
        }
        json.dump(config_data, config_file)

with open("config.json", "r") as config_file:
    config_data = json.load(config_file)
input_option = config_data.get("input", "3")
save_monkey = config_data.get("save", "3")
first_run = config_data.get("first_run")

# I want to die
def main():

    if input_option == "1":
        ask = "1"
    elif input_option == "2":
        ask = "2"
    else:
        ask = input("Do you want import image from 1.clipboard or 2.file ?")

    if ask == "1":
        input_image = ImageGrab.grabclipboard()
    elif ask == "2":
        files = filedialog.askopenfilenames(
            title="Select Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )  
        input_image = Image.open(files[0])
    else:
        print("Invalid option. Please choose 1 or 2.")
    output_image = remove(input_image)

    if save_monkey == "1":
        save_option = "1"
    elif save_monkey == "2":
        save_option = "2"
    else:
        save_option = input("Do you want save the image to the 1.clipboard or 2.file ?")

    if save_option == "1":
        output = io.BytesIO()
        output_image.save(output, format="PNG")
        image_data = output.getvalue()
        output.close()
        process = subprocess.Popen(
            ['xclip', '-selection', 'clipboard', '-t', 'image/png'],
            stdin=subprocess.PIPE
        )
        process.communicate(image_data)
        print("Image saved to clipboard.")
    elif save_option == "2":
        save_path = input("Enter the path to save the image: ")
        output_image.save(save_path)
        print("Image saved to", save_path)
    else:
        print("Invalid option. Please choose 1 or 2.")

def config():
    print("Welcome to the configuration setup!")
    input_ask = input("DO you want to input from 1.clicpboard or 2.file or 3.ask_everytime ?")
    save_ask = input("DO you want to save to 1.clicpboard or 2.file or 3.ask_everytime ?")
    config_data = {
        "input": input_ask,
        "save": save_ask,
        "first_run": True
    }
    with open("config.json", "w") as config_file:
        json.dump(config_data, config_file)
    print("Configuration saved to config.json")

if "--conf" in sys.argv:
    config()
else:
    if first_run:
        main()
    else:
        print("Welcome for the first time! Let's set up the configuration.")
        config()
