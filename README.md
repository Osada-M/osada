# osada 0.1


## Install

`pip install osada`


## Description

This is a module for my own use.  
It has some useful features to solve what I usually find troublesome. Please use it if you like.  

The functions are as follows.
- Colored print
- Generation of sequence

If I'm writing Python and find it annoying, I'll add function more.


## Usage

- Import
```
import osada
```

- Colored print  
```
osada.cprint("hello!", "orange", "white")
```

```
print(f"The three primary colors of light are \
{osada.colored('red', color='red')}, \
{osada.colored('green', color='green')}、\
{osada.colored('blue', color='blue')}.")
```
