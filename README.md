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

## Some Sample Image Outputs

Project Freedom was utilized to create the following visualizations image mergings and audio transformations. For more information about these mergings, see the [Extended Report](/report/extended_report.pdf).

| ![Alt text](/assets/images/einstein.png)  | ![Alt text](/assets/images/monroe.png)  | ![Alt text](/samples/images/einstein_monroe.png) |
| ------------- | ------------- | ------------- |
| ![Alt text](/assets/images/rgb_einstein.png)  | ![Alt text](/assets/images/rgb_monroe.png)  | ![Alt text](/samples/images/rgb_einstein_monroe.png) |
| ![Alt text](/assets/images/einstein.png)  | ![Alt text](/samples/images/einstein_low15.png)  | ![Alt text](/samples/images/einstein_high15.png) |
| ![Alt text](/samples/audio/dog_bark_dry_waveform.png)  | ![Alt text](/samples/audio/cave_ir_waveform.png) | ![Alt text](/samples/audio/dog_bark_dry_convolve_cave_waveform.png) | 


## To Setup For Development

To setup for development, follow the same directions for installation listed above. 

To run unit tests, use:
```python3 -m unittest```

Currently, unit testing is minimal.

### Potential Development Opportunities

1. Make a similar processor class for video files, potentially with an application for hybridizing them similar to images.
2. It may be possible to create a hybridizer for audio files similar to the one for the images, though my testing was unsuccessful on this front.
3. Utilize machine learning to automatically detect the best methods to hybridize images and combine audio files.
4. Improve the robustness of the unit tests.



## Inspirations & Accredations:
The following resources inspired this project:
1. https://kryakin.site/am2/Stein-Shakarchi-1-Fourier_Analysis.pdf
2. https://jeremykun.com/2014/09/29/hybrid-images/
3. https://cmtext.indiana.edu/synthesis/chapter4_convolution.php#:~:text=Convolution%20is%20a%20method%20of,not%20share%20will%20be%20minimized.

The following resources were utilized during the development of this project:
1. https://pixabay.com/sound-effects/search/ir/
2. https://www.pygame.org/docs/
3. https://numpy.org/doc/stable/index.html
4. https://docs.scipy.org/doc/scipy/reference/main_namespace.html
5. https://ccrma.stanford.edu/~jos/st/Matrix_Formulation_DFT.html
6. https://en.wikipedia.org/wiki/Parseval%27s_theorem
7. https://users.metu.edu.tr/ccandan/pub_dir/Eig_Structure_DFT_IEEE_SPM_Column_March2011.pdf
8. https://vanhunteradams.com/FFT/FFT.html#The-Cooley-Tukey-FFT
9. https://faculty.washington.edu/seattle/physics541/%202010-Fourier-transforms/history-3.pdf
