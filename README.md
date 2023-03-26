# Zoom Automation Script
This script is designed to automate the process of joining Zoom meetings for users who attend meetings at regular intervals. It uses the **"schedule"** library to schedule and join meetings automatically.

## Prerequisties
Before running this script, you must have the following installed on your computer:

* Python (version 3.7 or higher)
* **"schedule"** library

You can install the **"schedule"** library by running the following command:

<pre><code> pip install schedule </code></pre>

## Usage
To use this script, you must define a function for each class that you attend, and then schedule it to run at the appropriate times using the **"schedule"** library.

To define a function for a class, you can use the following template:

<pre><code> def class_name():
  print("Opening Zoom Meeting for XXX101") 
  open_link("{ZOOM LINK YOUR COURSE}") 
</code></pre>

Replace **"class_name"** with the name of the class, and enter the code necessary to join the Zoom meeting for that class.

To schedule the function to run at a specific time, you can use the **"schedule.every().day.at()"** method. For example, to schedule the **"class_name"** function to run every Monday at 9:00 AM, you can use the following code:

<pre><code> schedule.every().monday.at("9:00").do(class_name) </code></pre>

Replace **"9:00"** with the appropriate start time for your class, and **"class_name"** with the name of the function you defined for that class.

Repeat this process for each class that you attend, scheduling each function to run at the appropriate times using the **"schedule"** library.

## Automation for Windows User
1- Open Notepad or any other text editor.
2- Copy and paste the following code:

<pre><code> @echo off
python "{Your root directory}\automation.py"
pause </code></pre>

3- Replace **"{Your root directory}"** with the actual directory path where your **"automation.py"** script is located. For example, if your **"automation.py"** file is located in the **"C:\Users\username\Desktop\Zoom directory"**, the code should look like this:

<pre><code> @echo off
python "C:\Users\username\Desktop\Zoom\automation.py"
pause </code></pre>

4- Save the file with a .bat extension. For example, you can name the file **"zoom.bat"**.

To run this batch file on Windows startup, you need to add it to the startup folder. Here are the steps:
* Press the Windows key + R to open the Run dialog box.
* Type **"shell:startup"** and press Enter. This will open the Startup folder.
* Copy the **"zoom.bat"** file to this folder.
* Restart your computer to test if the batch file runs on startup.
Once you have completed these steps, the **"automation.py"** script will run automatically every time you start your computer.
