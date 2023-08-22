![setupCleaner_logo](https://github.com/urboirad/SetupCleaner/assets/97897450/70760984-0454-48ca-b3ca-07bbe1054133)

# Quick Description
Python script with GUI (made with Pyglet) that searches for installation/setup files and deletes them.

# Install
1. Download latest release
2. Extract folder
3. Extract the SetupCleaner folder from SetupCleaner.rar
4. In the "SetupCleaner" folder you can find the setupcleaner.exe file.

# How it works
1. Searches through the user's download folder for files ending with file extensions listed in the "possibleExtenions" list.
2. Generates a list of the installation files picked up.
3. Looks through the generated list of files and removes files that shouldn't be there. (These could be images that have words like "setup" in the their name).
4. GUI using the Pyglet library is created showing the list of files along with a handy CLEAN button. (This list can also be seen in the terminal)


# Full Code Breakdown
**Imports:**
The code starts by importing various modules from Pyglet, os, sys, pathlib, and pprint. These modules are used for GUI rendering, file and directory operations, and pretty-printing.

**Pyglet Setup:**
The script sets up a Pyglet window and a graphics batch for rendering. It also loads a custom font for the interface and an image (logo) to be displayed.

**Button Class:**
Defines a class named Button for creating GUI buttons. Each button has attributes like position, size, color, label, and visibility. The draw method of this class renders the button and its label on the GUI.

**File Extension Lists:**
Lists of possible installation file extensions and bad file extensions are defined. These are used for filtering and identifying files to be cleaned.

**Directories and Files:**
The script determines the user's Downloads folder path and lists files in the folder that match the possible installation file extensions. It also identifies files starting with "setup" and adds them to the list. Files with bad extensions are excluded. The list of files to be deleted is printed to the console.

**File Sizes:**
The script calculates the total size of the files to be deleted in megabytes.

**Functions:**
get_assets_folder(): This function returns the path to the "assets" folder.
get_download_path(): Gets the user's Downloads folder path.
CheckCollision(): Checks if two rectangles (used for collision detection) intersect.
delete_files(): Deletes the files matching possible installation file extensions from the Downloads folder.
Labels: Several Pyglet text labels are defined, including the size of files, a list of files to be deleted, and a status label. These labels display information on the GUI.

**Buttons (Class):**
Defines the Clean button using the Button class. This button is used to trigger the cleaning process.

**Files List Movement:** 
A callback function scheduled using Pyglet's clock. This function moves the files list to the left to accommodate long file lists.

**Drawing:**
The on_draw() event handler draws the interface on the window. It includes the logo, labels, and buttons. If there are no files to delete, it updates the text of the files list label.

**Mouse Input:**
The on_mouse_press() event handler responds to left mouse button clicks. If the start button is clicked, it triggers the delete_files() function and hides the start button.
