# pySerial for network devices

This is a template for automating sending commands via console and extracting the output into a text file.
Some parts of the code is from https://github.com/ktbyers/pynet/blob/master/serial/cisco_serial.py

Note that the code reads from the console after every command instead of all at once after inputting every command is because there is a limit to the number of bytes readable in one go (I think, after multiple tests).


Sample output can be seen from the test.txt file
