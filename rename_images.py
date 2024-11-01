import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog

# Function to get the letter from the user
def get_letter():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    letter = simpledialog.askstring("Input", "Enter the letter to add at the end of each image file:")
    return letter

# Function to ask the user for the folder path
def get_folder_path():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
    return folder_path

# Function to show confirmation dialog
def show_confirmation(images):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    count = len(images)  # Get the number of images
    message = f"{count} images will be renamed.\n\nDo you want to proceed with renaming these images?"
    return messagebox.askyesno("Confirm Renaming", message)


# Ask the user for the letter
letter = get_letter()

# Check if the user canceled the input
if letter is None:
    messagebox.showinfo("No letter entered. Exiting...")
    exit()

# Ask the user for the folder path
folder_path = get_folder_path()

# Check if a valid folder path was selected
if not folder_path:
    messagebox.showinfo("Info", "No folder selected. Exiting...")
else:
    # List to hold image files to be renamed
    images_to_rename = []

    # Iterate over all the files in the selected directory
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images_to_rename.append(filename)

    # Check if there are any images to rename
    if not images_to_rename:
        messagebox.showinfo("No image files found in the selected directory.")
    else:
        # Show confirmation dialog
        if show_confirmation(images_to_rename):
            # Rename the files
            for filename in images_to_rename:


                # Create the new filename by adding the letter before the file extension
                #separate file from extension
                file_name, file_extension = os.path.splitext(filename)

                #delete last 10 char
                truncated_name = file_name[:-10] if len(file_name) > 10 else file_name

                #rename file after changes
                new_name = f"{truncated_name}{letter}{file_extension}"

                try:
                    # Rename the file
                    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
                except Exception as e:
                    print(f"Error renaming '{filename}': {e}")

            messagebox.showinfo("All images have been renamed.")
        else:
            messagebox.showinfo("Renaming canceled.")
