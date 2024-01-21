# Batch Image Compressor
## Setting up the Project
 
This will walk you through setting up the project environment.

**Prerequisites:**

- Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))

**Steps:**

1. **Install `pip`** (if not already installed):

   - Open a terminal or command prompt.
   - Check if `pip` is installed: `pip --version`
   - If not installed, download `get-pip.py` from [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)
   - Run the script: `python get-pip.py`

2. **Install `venv`** (if not already installed):

   - `pip install venv`

3. **Create a virtual environment:**

   - Navigate to the project directory in your terminal.
   - Create the virtual environment:
     ```bash
     python -m venv env
     ```
   - Activate the virtual environment:
     - **Windows:** `env\Scripts\activate.bat`
     - **Linux/macOS:** `source env/bin/activate`

4. **Install dependencies:**

   - **Using a `requirements.json` file:**
     ```bash
     pip install -r requirements.json
     ```
   - **Alternatively, install directly from `requirements.txt`:**
     ```bash
     pip install -r requirements.txt
     ```

**You're now ready to start working on the project!** 

**Additional notes:**

- If you encounter issues, consult the official documentation for `pip` and `venv`.
- Consider using a code editor or IDE with Python support for a smoother development experience.

## Installing the CLI
Simply copy the executable file to scripts folder in your system and assign a path environment variable to it .

Then simply call the script from the command line using the following command

```bash
batch_comp -h
```
This will show the help menu for the script and the various options that can be used with it indicating that it was successfully installed


## CLI usage
This cli uses a list of simple arguments that can be used to compress images in a folder or a single image or a list of images and save them in a folder . The folder is called 'output' 

|  Option |Type| Usage and explanation  |
| ------------ | ------------ | ------------ |
| -F  |String|Used to compress/convert images from a folder , it will create an output folder in the directory itself called 'output'   |
|-f|String|Used to compress/convert images from a list of images , the path must be absolute in this version of the release , will create an 'output' folder in the directory of the first image provided in the list|
|-q|Integer|Specifies the quality of the conversion, the value ranges from 1-100 , a lower value gives a smaller file but with diminished quality. It is 40 by default|
|-t|String| This specifies the type of the output file, it is 'jpg' by default |
|-r|Boolean[True/False]|Specifies if the output folder must be replaced by a new batch of compressed files|