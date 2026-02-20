# Background Remover

A **local background remover** in Python that lets you remove backgrounds from images **without uploading anything online**. Perfect for presentations, projects, or whenever you want your images to look **clean and professional**.

## Features
- Remove backgrounds from images locally.
- Import images from **clipboard** or **file**.
- Save images to **clipboard** or **file**.
- Configurable input/output behavior via `config.json`.
- Fully offline – no data is sent to third-party servers.
- Easy to use, but expandable for multiple images or a GUI.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/patriq128/Backround-Remover.git
   cd Backround-Remover
   ```
2. Install dependencies:
   ```bash
   pip install rembg pillow
   ```
3. On Linux, you need `xclip` to copy images to clipboard:
   ```bash
   sudo apt install xclip
   ```

## Usage
Run script:
```bash
python main.py
```
On the first run, you'll be prompted to set up configuration:
**Input:** clipboard, file, or ask every time.
**Save:** clipboard, file, or ask every time.

## Configuration
To change default behavior without input prompts every time:
```bash
python main.py --conf
```
This opens a configuration setup and saves your preferences to `config.json`.
