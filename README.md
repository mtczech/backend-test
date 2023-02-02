# backend-test

How to download and run the code for this app:

Step 1: Open up the command prompt/terminal and navigate to the folder that you would like to place the program into.

Step 2: Run the following command in the command prompt/terminal: git clone https://github.com/mtczech/backend-test.git. This will download the program from the Github repository, including the data to be read in.

Step 3: Navigate to the folder backend-test that has just been placed in your current directory. 

Step 4: Once you are in the backend-test folder, you are free to run the code! You can do so by putting in the command python fetchbackendtest.py <XXXX>, where <XXXX> is the number of points you want to distribute.

-----------------------------------------------------------------------------------------------------

Notes: This code makes a lot of assumptions about what you are doing with it. These include:

* The first assumption was that there will always be three values in the CSV, and that these three values will be in this order: ('payer', 'points', 'timestamp'). If there are any extra values, they will be ignored.

* Another assumption made was that the times will always be in the form 'YYYY-MM-DDTHH:mm:SSZ', where YYYY is the year, MM is the month, DD is the day, HH is the hour, mm is the minute, and SS is the second.

* Third assumption: Only one number is put into the command line, and this number is an integer.

* Final assumption: The file being put in will always be named 'samplebackend.csv'.

If any of these assumptions are broken, that is undefined behavior. However, if you want to put new data into the function, you can do so by either changing the data in the 'samplebackend.csv' file or changing the file itself. If you change the file itself, make sure it is in the same place with the same name, and the data is correctly formatted.
