# Project Freedom

![Build Status](https://github.com/Sn00pyW00dst0ck/project_freedom/actions/workflows/pipeline.yml/badge.svg?event=push)
![Reports Build Status](https://github.com/Sn00pyW00dst0ck/project_freedom/actions/workflows/latex-build.yml/badge.svg?event=push)

Project Freedom is a easy to use CLI program that
users can interact with in order to perform their own experiments
with the Fast Fourier Transform (FFT) and related operations on both images and audio files.

Basic filtering operations are supported for images and audio, and
there are numerous ways to visualize how the files have changed
and preview those changes.

This project is implemented in Python, and supports building on
Python versions 3.9-3.12 (though it was only tested on version 3.12).
It relies on Numpy, Matplotlib, Scipy, and PyGame.

## To Use

Ensure that a Python version between 3.9 and 3.12 is installed and that 
the pip package manager is installed. 

To install this program, execute the following commands from a terminal on 
a Linux machine:
```git clone https://github.com/Sn00pyW00dst0ck/Carpool-Creator.git```
```cd project_freedom```
```pip3 install -r requirements.txt```

To run the program, execute the following command from within a Linux terminal 
in the root of the repository:
```python3 ./src/main.py```

Then, follow the prompts within the terminal to experiment with the FFT. 

Do not, under ANY circumstances, run this program from anywhere other than the 
root directory of the repository; otherwise files may be read from invalid locations
causing the program to crash. 

While this program *should* work on a Windows machine, it was developed for and tested on
Linux in Python version 3.12 and that is the environment to expect best results for.

## To Setup For Development

To setup for development, follow the same directions for installation listed above. 

To run unit tests, use:
```python3 -m unittest```

Currently, unit testing is minimal.

### Potential Development Opportunities

1. Make a similar processor class for video files.
2. Utilize machine learning to automatically detect the best methods to hybridize images and combine audio files.
3. Improve the robustness of the unit tests.
