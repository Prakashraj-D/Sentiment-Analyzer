1. Install Prerequisites

For Windows:

Python: Download and install from https://python.org
During install, check "Add Python to PATH".

VS Code: Download and install from https://code.visualstudio.com

Install Python extension from VS Code Extensions tab.



---

For Linux (Ubuntu/Debian):

Open terminal and run:

sudo apt update
sudo apt install python3 python3-pip -y
sudo apt install code -y  # If VS Code is installed via apt


---

2. Open the Project in VS Code

GUI Method (Windows/Linux):

Launch VS Code

Click File > Open Folder

Select the folder where your app.py file is located


Terminal Method:

cd path/to/your/project
code .


---

3. Create a Virtual Environment (Optional but Recommended)

Windows:

python -m venv venv
venv\Scripts\activate

Linux:

python3 -m venv venv
source venv/bin/activate

You’ll now see (venv) in your terminal, showing it’s active.


---

4. Install Required Python Libraries

If you have a requirements.txt:

pip install -r requirements.txt

Or manually:

pip install flask nltk

Also, in Python terminal or code, download the VADER lexicon:

import nltk
nltk.download('vader_lexicon')


---

5. Run the Flask App

Windows:

python app.py

Linux:

python3 app.py

Output will look like:

Running on http://127.0.0.1:5000/


---

6. Open in Browser

Go to http://127.0.0.1:5000
Use the interface to enter your text and see sentiment results.


---

7. Stop the App & Deactivate Virtual Env

To Stop Flask App:

Press Ctrl + C in terminal


To Exit Virtual Environment:

deactivate