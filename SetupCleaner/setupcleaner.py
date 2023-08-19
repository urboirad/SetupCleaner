import os
import pyglet
from pyglet import font
from pyglet import shapes
from pyglet.window import mouse
from pathlib import Path
from pprint import pprint

# Set up pyglet
window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
font.add_file('Assets/VCRosdNEUE.ttf')
VCRosdNEUE = font.load('VCRosdNEUE', 16)

# Variables
Cleaning = False
numExtensions = [1]
num = 0
for x in range(1, 1000):
    num += 1
    numExtensions.append(num)

# Classes
class Button():
    def __init__(self, x, y, width, height, hover, text, color, batch, button, visible):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.hover, self.text, self.color, self.batch, self.visible = hover, pyglet.text.Label(text, font_name='VCRosdNEUE', font_size=24, x=self.x + self.width // 2, y=self.y + self.height // 2, anchor_x='center', anchor_y='center'), color, batch, True
        self.button = shapes.Rectangle(self.x, self.y, self.width, self.height, self.color, self.batch)

    def draw(self):
        self.button.draw()
        self.text.draw()

# Search for installation files
possibleExtensions = ('setup.exe', 'Setup.exe', '-installer.exe', 'Installer.exe', '.msi', '.msm', '.msp', '.mst', '.msu', '.idt', '.cub', '.pcp', "-x64.exe", "-x86.exe", "-amd64.exe", "-x32.exe", "-amd32.exe", "-win64.exe", "-64-bit.exe",  "-32-bit.exe")

# Search for duplicate installation files
s = list(possibleExtensions)
for x in numExtensions:
    s.append("("+str(x)+").exe")
    s.append("."+str(x)+".exe")
possibleExtensions = tuple(s)

# Get Downloads folder
path = str(Path.home() / "Downloads")

# Get list of files
files = [x for x in os.listdir(path) if x.endswith(possibleExtensions)]
sw_files = [x for x in os.listdir(path) if x.startswith("setup")]
for x in sw_files:
    files.append(x)
print ("Files that will be deleted:")
pprint(files)

# Get size of files
filesSize = 0
for x in files:
    filesSize += os.path.getsize(os.path.join(path, x))
filesSize = round(filesSize/1048576)

# Functions
def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def CheckCollision(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 < x2 + w2 and x2 < x1 + w1 and y1 < y2 + h2 and y2 < y1 + h1

def delete_files():
    extneions = possibleExtensions
    path = get_download_path()
    files = [x for x in os.listdir(path) if x.endswith(extneions)]
    for x in files:
        os.remove(os.path.join(path, x))
    files = [x for x in os.listdir(path) if x.endswith(extneions)]

# Labels
title = pyglet.text.Label('Setup Cleaner', font_name='VCRosdNEUE', font_size=36, x=window.width // 2, y=450, anchor_x='center', anchor_y='center')
subTitle = pyglet.text.Label('Script By: RAD', font_name='VCRosdNEUE', font_size=18, x=window.width // 2, y=400, anchor_x='center', anchor_y='center')
size = pyglet.text.Label('Size: ' + str(filesSize) +'MB', font_name='VCRosdNEUE', font_size=18, x=10, y=60, anchor_x='left', anchor_y='center')
files_twbp = pyglet.text.Label('Files that will be deleted:', font_name='VCRosdNEUE', font_size=12, x=10, y=38, anchor_x='left', anchor_y='center')
filesList = pyglet.text.Label(str(files), font_name='VCRosdNEUE', font_size=12, x=10, y=20, anchor_x='left', anchor_y='center')
status = pyglet.text.Label('CLEANED', font_name='VCRosdNEUE', font_size=24, x=window.width // 2, y=200, anchor_x='center', anchor_y='center')

# Buttons
startButton = Button(window.width // 2 - 50, 200, 100, 50, False, "CLEAN", (55, 55, 255), batch, 0, True)

# Files List Movement
clk = pyglet.clock.get_default()
def callback(dt):
    if sum(len(i) for i in files) > 113:
        filesList.x -= 0.02
    if filesList.text == "Files deleted successfully!":
        filesList.x = 10
        
    if filesList.x < -window.width/2:
        filesList.x = 10
    
clk.schedule(callback)

# Draw
@window.event
def on_draw():
    window.clear()
    title.draw()
    subTitle.draw()
    size.draw()
    files_twbp.draw()
    filesList.draw()
    if not files:
        filesList.text = "There are no files to be deleted..."
    else:
        filesList.text = str(files)
    if startButton.visible:
        startButton.draw()
    else:
        status.draw()
        size.text = "Size: " + str(0) + "MB"
        filesList.text = "Files deleted successfully!"

# Mouse Input
@window.event
def on_mouse_press(x, y, button, modifier):
    if button == mouse.LEFT:
        if startButton.visible:
            if CheckCollision(x, y, 32, 32, startButton.x, startButton.y, startButton.width, startButton.height):
                delete_files()
                startButton.visible = False

pyglet.app.run()
