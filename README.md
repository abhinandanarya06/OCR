# OCR Research Project
###### using OpenCV and Tensorflow

## Prerequisites
1. OpenCV Python - Image Processing Library
2. Tensorflow 2.0 - Deep learning Library

## Assumption
1. The image given to the OCR program must have text appear horizontally.
2. The text on image should be English as it supports English language.

## User Guide
1. Go to Research Notebook and run cells as instructed. You can also test it on notebook itself.
2. After complete Notebook runned, Download saved OCR model ***model.h5***.
3. Place the saved model file in local OCR directory cloned from this repo.
4. Place the images from which text to be extracted
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

## Important Message
This project is just research on OCR. From Reading and running the Research Notebook,
You will find there is some faults. Faults indicated by me are Some Wrong Text Character 
Prediction by the model and others mentioned in **Assumption** Section.
Hence this project is still in development and i am trying my best to minimise these faults.

I incourage you to contribute in this project.

# *Thank You !*
