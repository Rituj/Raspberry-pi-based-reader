# Raspberry-pi-based-reader
Since this project runs on the raspberry pi board,it has some other hardware reuirements too,which include:1.Pi camera module 2.Breadboard 3.Male to female wires 4.A speaker 5.A switch or button
The Pi camera clicks the picture and saves it in the defined location from where it is passed as an argument in the main code.
I have used opencv and pytesseract for image filtering and text extraction respectively and the python gtts module for text to speech conversion,so these libraries are also a prerequisite to run the project.
The main code can be tested as a standalone code by passing an image as an argument from the command line.
I have also provided a sample image for the same.
