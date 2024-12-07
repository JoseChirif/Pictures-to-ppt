import os
import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser
import sys


def relative_route_to_file(path_to_folder, file):
    """
    Returns the relative path to a file, accounting for whether the application 
    is running in a PyInstaller bundle or a standard script environment.

    Args:
        path_to_folder (str): The folder path where the file is located.
        file (str): The name of the file.

    Returns:
        str: The complete relative path to the specified file.
    """
    if hasattr(sys, '_MEIPASS'):
        # Running as a PyInstaller bundle, use _MEIPASS to locate files
        route = os.path.join(sys._MEIPASS, path_to_folder, file)
    else:
        # Running as a regular script, use standard relative path
        route = os.path.join(path_to_folder, file)
    
    return route



def working_directory():
    """
    Returns the path to the project's parent directory. If the script is bundled into an executable, it returns the executable's directory.

    Args:
        None

    Returns:
        str: Path to the parent directory of the project or the directory of the executable if running as a bundled application.
    """
    if hasattr(sys, 'frozen'):
        # If the script is bundled into an executable, it returns the directory of the executable.
        directory = os.path.dirname(sys.executable)
    else:
        # If running as a normal script, it returns the parent directory of the project
        directory = os.path.abspath(os.path.join(__file__, *(['..'] * 3)))
    
    return directory  # Returns the directory



def show_message(title, message):
    """
    Displays a message in a popup window using tkinter. If the message is a DataFrame, it converts it to a string.

    Args:
        title (str): The title of the popup window.
        message (str or pd.DataFrame): The message to display. If a DataFrame is provided, it will be converted to a string.

    Returns:
        None: This function does not return anything.

    Raises:
        None: This function does not raise any exceptions.
    """
    # Create a hidden window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    # Display the message in a popup window
    messagebox.showinfo(title, message)
    # Close the window after the message is closed
    root.destroy()
    


def show_options(header_text, *args):
    """
    Displays an options window with a dynamic number of buttons based on the provided options.
    Upon selecting an option, returns the index (1-based) of the selected option.
    If canceled, closes only the options window without affecting other windows.

    Args:
        header_text (str): The text displayed at the top of the window.
        *args (str): Variable number of option texts for buttons.

    Returns:
        int: The selected option (1-based index) or None if canceled.
    """
    def cancel_current_operation():
        """
        Cancels the operation and closes only the current options window.
        """
        nonlocal result
        result = None
        options_window.destroy()

    def select_option(option_number):
        """
        Handles the selection of an option.

        Args:
            option_number (int): The 1-based index of the selected option.
        """
        nonlocal result
        result = option_number
        options_window.destroy()

    # Create the options window
    options_window = tk.Toplevel()
    options_window.title("Pictures to PPT")
    options_window.iconbitmap("assets/icon.ico")  # Update the path as needed

    # Variable to store the result of the selection
    result = None

    # Handle the close (X) button of the window
    options_window.protocol("WM_DELETE_WINDOW", cancel_current_operation)

    # Frame for organizing the header text
    frame_header = tk.Frame(options_window)
    frame_header.pack(fill="x", pady=5)

    # Centered text at the top of the window
    lbl_header = tk.Label(
        options_window,
        text=header_text,
        font=("Arial", 10, "bold"),  # Font size 10, bold style
        anchor="center",
        padx=20
    )
    lbl_header.pack(pady=15)  # Top/bottom margin

    # Create buttons dynamically for each option
    for i, option in enumerate(args, start=1):
        button = tk.Button(
            options_window,
            text=option,
            font=("Arial", 10),  # Font size 10
            padx=20,  # Horizontal padding inside the button
            pady=10,  # Vertical padding inside the button
            command=lambda opt=i: select_option(opt),
            cursor="hand2"
        )
        button.pack(pady=5, padx=20)  # Spacing between buttons

    # Cancel button
    cancel_button = tk.Button(
        options_window,
        text="Cancel",
        font=("Arial", 10),
        bg="#F06D22",
        command=cancel_current_operation,
        padx=20,  # Horizontal padding inside the button
        pady=10,  # Vertical padding inside the button
        cursor="hand2"
    )
    cancel_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    # Wait for the user to select an option or cancel
    options_window.grab_set()  # Makes the window modal
    options_window.wait_window()  # Pauses execution of this function until the window is closed

    return result



def check_presentation_exists(ppt_path):
    """
    Checks if a PowerPoint file already exists in the working directory.
    If it exists, asks the user whether to replace it.

    Args:
        ppt_path (str): Full path to the PowerPoint file.

    Returns:
        bool: True if the file can be replaced or does not exist, False if the replacement is declined.
    """
    if os.path.exists(ppt_path):
        choice = show_options(f"The presentation '{os.path.basename(ppt_path)}' already exists.\nDo you want to replace it?", "Yes", "No")
        if choice == 1:  # Yes
            return True
        else:  # No or canceled
            return False
    return True



## FUNCTIONS FOR MAIN MENU
def open_web_page(*links):
    """
    Attempts to open a list of web links in the default web browser. For each link,
    it checks if the URL is accessible before opening it. Stops at the first successful link.

    Args:
        *links (str): One or more URLs to open.

    Returns:
        None
    """
    for link in links:
        try:
            # Perform a GET request to check if the link is accessible
            response = requests.get(link, timeout=5)
            if response.status_code == 200:
                webbrowser.open(link)
                print(f"Opening: {link}")
                break  # Stop if the link was successfully opened
            else:
                print(f"The link {link} is not available, status code: {response.status_code}")
        except requests.ConnectionError:
            print(f"Connection error while checking {link}. The link might not exist.")
        except requests.Timeout:
            print(f"Timeout expired while checking {link}.")
        except requests.RequestException as e:
            print(f"Error while checking {link}: {e}")
    else:
        print("No links could be opened.")
        

def adjust_text(event, *args, margin):
    """
    Adjusts the text wrapping length for given labels based on the available width minus a specified margin.

    Args:
        event: The triggering event, typically a window resize event.
        *args: Variable number of label widgets to adjust.
        margin (int): The margin to subtract from the label width for text wrapping.

    Returns:
        List of labels with updated wraplength configurations (optional).
    """
    updated_labels = []
    for label in args:
        # Adjust the text wrapping length to the available width minus the margin
        new_wraplength = label.winfo_width() - margin
        if new_wraplength > 0:  # Ensure the new wrap length is positive
            label.config(wraplength=new_wraplength)
            updated_labels.append(label)  # Store updated label

    return updated_labels  # Return the list of updated labels


# FUNCTIONS TO EXECUTE SCRIPTS

class DirectExecutionExit(Exception):
    """Custom exception to handle script exit without closing the Tkinter menu."""
    pass

def exit_if_directly_executed():
    """
    Raises an exception that can be caught to stop the script.
    
    Args:
        None
        
    Returns:
        None
    """
    raise DirectExecutionExit("The script was stopped.")



def execute_script_src(script):
    """
    Executes the corresponding script.

    Args:
        script (str): The name of the script to execute.

    Returns:
        None: This function does not return any value. It only executes the script and handles errors.
    """
    try:
        # Attempt to import and execute the corresponding script
        module = __import__(f'src.{script}', fromlist=['create_presentation'])
        module.create_presentation()  # Call the function create_presentation with no arguments

    except DirectExecutionExit as e:
        print(f"The script was stopped: {e}")
    except ImportError as e:
        print(f"Error importing the script '{script}': {e}")
    except AttributeError as e:
        print(f"The script '{script}' does not have a 'main' function: {e}")
    except Exception as e:
        print(f"An error occurred while executing the script '{script}': {e}")



def run_picture_center():
    """
    Executes the 'Imagen_to_ppt - Picture center' script

    Returns:
        None: This function does not return any value. It only calls the execute_script_src function.
    """
    execute_script_src('Imagen_to_ppt - Picture center')
    
    
def run_picture_covering_panoramic_slide():
    """
    Executes the 'Imagen_to_ppt- Picture covering panoramic slice' script

    Returns:
        None: This function does not return any value. It only calls the execute_script_src function.
    """
    execute_script_src('Imagen_to_ppt- Picture covering panoramic slice')


def run_picture_in_panoramic_slide():
    """
    Executes the 'Imagen_to_ppt- Picture in panoramic slice' script

    Returns:
        None: This function does not return any value. It only calls the execute_script_src function.
    """
    execute_script_src('Imagen_to_ppt- Picture in panoramic slice')