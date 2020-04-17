# OCR Research Project
![OCR Research Project](https://github.com/abhinandanarya06/OCR/blob/master/.res/OCR%20Research%20Project.jpg)
## Prerequisites
1. [Python 3.7.4](https://www.python.org/) Installed 
2. [OpenCV Python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) - Image Processing Library
3. [Tensorflow version 2.O Recommended](https://www.tensorflow.org/install) - Machine learning Library
```
pip install tensorflow==2.0rc1
            OR
pip3 install tensorflow==2.0rc1
```

## Assumption
1. The image given to the OCR program must have text place in approximately perfect horizontal line.
2. The text on image should be English as it supports English language.

## Quickstart
1. If you want to know how it works, please read the research notebook and wiki page.
2. Git clone this repository.
```
git clone https://github.com/abhinandanarya06/OCR.git
```
3. Open terminal in the current directory and change directory to OCR directory
```
cd OCR/
```
4. Place the images to ***sample_test_image*** directory from which you want to extract text.
5. run main.py
```
python main.py

     OR

python3 main.py
```

## Project Directory Overview
- OCR 
     - **[data](https://github.com/abhinandanarya06/OCR/tree/master/data)** contains others data directories of images of corresponding letters and common noise
         - **a**
         - **b**
         - :
         - :
         - **noise**
     - **[main.py](https://github.com/abhinandanarya06/OCR/blob/master/main.py)** is main start point of running the python project
     - **[ocr_help.py](https://github.com/abhinandanarya06/OCR/blob/master/ocr_help.py)** is OCR library that should be imported (imported in main.py) to use OCR functions
     - **[model.h5](https://github.com/abhinandanarya06/OCR/blob/master/model.h5)** is the tensorflow model which is to be used by **main.py**
     - **[Research Notebook on OCR.pynb](https://colab.research.google.com/github/abhinandanarya06/OCR/blob/master/Research_Notebook_on_OCR.ipynb)** is the notebook to understand how this OCR Project works

## Issues
1. Might not work on image having light colored text on dark background.
2. Might not work on some font styles of text on image
3. This OCR is not prepared to detect numbers and other characters as well. This feature addition is in development.
4. While running the research notebook and test it on pregiven sample images, you will find it not work good when image contain objects other than text contour.

## Important Message
This project is just research on OCR. From Reading and running the Research Notebook,
You will find there is some Issues. Issues indicated by me are mentioned in **Assumption** and **Issues** Section.
Hence this project is still in development and i am trying my best to minimise these issues.


* **Contribute** : If you have an idea to tackle these issues, I incourage you to contribute to this research project. You can use the dataset stored in data directory of the repository. 
* **Support** : If you find new issue, please let me know.
* **License** : This project is licensed under MIT

### *Happy Learning !*
