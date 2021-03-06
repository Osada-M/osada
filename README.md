# osada 0.1


## Install

```
pip install osada
```


## Description

This is a module for my own use.  
It has some useful features to solve what I usually find troublesome. Please use it if you like.  

The functions are as follows.
- Colored print
- Generation of sequence

If I'm writing Python and find it annoying, I'll add function more.


## Usage

```
import osada
```

- ## Colored print

### `osada.cprint(string, color, background, end, bloom, **kwarg)`
```
osada.cprint("hello!", "orange", "white")

# # The writing below is the same as the sentence above
# osada.cprint("hello!", "ff8844", "ffffff")
# osada.cprint("hello!", color="ff8844", background="ffffff")
```
<img width="139" alt="cprint_0" src="https://user-images.githubusercontent.com/76993392/148169485-80423778-bef0-4325-92e5-e2396077e6cc.png">

### `osada.colored(string, color, background, bloom)`
```
print(f"The three primary colors of light are \
{osada.colored('red', color='red')}, \
{osada.colored('green', color='green')}、\
{osada.colored('blue', color='blue')}.")
```
<img width="849" alt="colored_0" src="https://user-images.githubusercontent.com/76993392/148169519-b6791b7b-8353-438f-971f-3d803d513771.png">

- ## Generation of sequence

### `osada.array(inf, sup, number)`  
inf : start number  
sup : end number  
number : element count  
```
osada.array(1, 2, 2)
# [1.0, 2.0]

osada.array(1, 2, 5)
# [1.0, 1.25, 1.5, 1.75, 2.0]

osada.array(1, 2, 11)
# [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7000000000000002, 1.8, 1.9, 2.0]
```


### `osada.randomArray(inf, sup, number, isint)`  
inf : start number  
sup : end number  
number : element count  
isint : is integer value
```
osada.randomArray(0, 1, 5)
# [0.8081470327591642, 0.8900165197747789, 0.3057814178026007, 0.005010722833622361, 0.7636094070498007]

osada.array(1, 10, 10, True)
# [5, 8, 2, 10, 9, 4, 10, 3, 5, 6]
```