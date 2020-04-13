# OCR Research Project
###### using OpenCV and Tensorflow

## Prerequisites
1. Python 3.7.4 Installed 
2. OpenCV Python - Image Processing Library
3. Tensorflow 2.0 - Machine learning Library

## Assumption
1. The image given to the OCR program must have text appear horizontally.
2. The text on image should be English as it supports English language.

## User Guide
1. Git clone this repository.
```
git clone https://github.com/abhinandanarya06/OCR.git
```
2. Go to Research Notebook and run cells as instructed. You can also test it on notebook itself.
3. After complete Notebook runned, saved OCR model file ***model.h5*** will appear in the repo directory.
4. Place the images to ***test*** directory from which you want to extract text.
5. run main.py

## Project Directory Overview
- OCR 
     - **data** contains others data directories of images of corresponding letters and common noise
         - **a**
         - **b**
         - :
         - :
         - **noise**
     - **main.py** is main start point of running the python project
     - **ocr_help.py** is OCR library that should be imported (imported in main.py) to use OCR functions
     - **Research Notebook on OCR.pynb** is the notebook to understand how this OCR Project works
     - **research_notebook_on_ocr.py** is just python file version of above mentioned notebook that can be run instead of the notebook

## Issues
1. Might not work on image having light colored text on dark background.
2. Might not work on some font styles of text on image
3. This OCR is not prepared to detect numbers and other characters as well. This feature addition is in development.

## Important Message
This project is just research on OCR. From Reading and running the Research Notebook,
You will find there is some faults. Faults indicated by me are Some Wrong Text Character 
Prediction by the model and others mentioned in **Assumption** and **Issues** Section.
Hence this project is still in development and i am trying my best to minimise these faults.

I incourage you to contribute to this project. You can use the dataset stored in data directory of the repository.

# *Thank You !*
