# ECE480 Team11 Sound Identification 
# User Manual

**_Setting Up the Code_**

To begin, one must ensure that python version 3.11.0 or higher is installed on their
device. The code executes using python 3.11, which can be downloaded and installed from
pythons official website. Ensure that the correct version of the software is installed for your
corresponding operating system. Once this is finished, the repository then needs to either be
downloaded locally, or cloned from the github environment into one's local workspace. As a
side note, GitHub has an application named “GitHub Desktop” which can be downloaded
here. This software will quicken one's workflow, as it provides the same functionality for git
commands in the command line within its easy to understand GUI.
There are 3 branches outside of the “main” branch that should be noted. The “master”
branch contains all of the deployed code that is showcased and explained within this
document. Be sure you do not merge or edit code in this branch unless it is code that can
successfully build and run on another defined branch. There is another branch titled
“Yunpeng” in which this branch was used as the source branch for our application hosting
website known as “team11.fit”. It runs the same code that is on the master branch. Lastly,
there is a branch titled “Test”. This branch contains the same code as the previously
mentioned branches, plus extra python scripts dedicated to testing code locally. Simply run
the program and it will display the following output in the console:

    Serving Flask app 'api'
    Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    Running on all addresses (0.0.0.0)
    Running on http://127.0.0.1:5000
    Running on http://192.168.50.146:5000
    Press CTRL+C to quit

Click the first link which will pop up a window in your default browser:

    http://127.0.0.1:5000

From here you can test the edits to the code you have made. Once the testing procedure has
finished and the project builds successfully on either this branch, or another branch that is not
the master branch, feel free to merge this newly implemented code into the master branch.
Another method of testing can be done by executing the program as a desktop
application. In the file named “UI_Test.py”, all code there is documented such that one can
read and understand the workings of this test file. Just like before, you may run this program
and it will instead pop up a window that looks like this:

Although this looks different from the GUI above, it works the same as the GUI above. Some
key differences that you will see include the following:
- Option button in the top left corner of the application that allows you to either display
the dB level or not
- Negatively valued dB levels will display when a sound is heard.
- This is ok, as there can be two types of scales to define sound intensity.
Typically these values will range within range -inf [dB] → 3 [dB] +/-

This version of the application uses a module named “match_test.py” which functions the
same as the match module defined in the other branches, with only one extra function of
handling the recording of audio via some external input device such as a microphone. Be sure
that this file is edited if improvements/changes regarding the matching algorithm are made.
Once the desired results are achieved, be sure to implement this code within the “match”
module of the Test branch. Following this, you may merge the code from this branch into the
master branch (only if it builds properly, though!)
If one desires for the UI to be improved, look into the “index.html” file defined in the
“templates” directory of the repository. The file is clearly labeled and structured to
understand how a given portion of the website is displayed. Documentation on html scripting
as well as html formatting can be found through various sources such as YouTube, Wikipedia,

Geeksforgeeks, etc, so be sure to look into this prior to working on this file (if need be).
Note: PyCharm has a feature where one can edit an html file and view what the website
would look like without deploying the code to a server. In the top right corner of the code
window you should see a option bar with icons of ones available web browsers, in addition
to PyCharms built-in preview option:

If one would like to connect to the server which this application is running on for
debugging/logging purposes, you firstly need to download the Xshell software from here.
This software is essentially useful for the emulation of terminals via SSH protocol as well as
many other protocols. Once the software is installed, the following steps will allow you to get
into the server:

    ps -ef | grep api.py – Get process running on root (our server)
    
    kill #### – (Stop process ####) You can find #### by using the command above
    
    git fetch -all
    
    git reset –hard origin/xxxx – (xxxx is branch name) Update all codes in branch xxxx
    
    tail -n 100 nohup.out – Check the output logs

**_Application Use_**

To begin sound identification on one's device, open this link in any browser of choice
https://www.team11.fit/. It will open a window that looks like this while at the same time, ask
you for permission to utilize your microphone for sound detection:

To start the application, press the green, interactable ”Record” button in the middle of the
screen. This will then open a drop-down menu which will inform you that sound analysis has
begun.

The application informs you that the “loudness” or dB level of the sound will
appear once a sound is detected. In addition to this you will be informed by our application
when a sound is further from your or closer to you.

If you desire to stop seeing the analysis results, simply tap the slim white line next to
the “Sound Identification Results” text. Finally, if you wish to stop recording, simply click
the “Stop Record” button in the middle of the screen.