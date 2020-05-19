# Quicksort Package (a sample package for CRI technical interview)
This python package contains only one function, the partition().

## Python Version Requirement
Please ensure your Python Version is at least 3.6.

## Quick overview of Quicksort
The quicksort is a divide-and-conquer sorting algorithm. <br/>
The main routine of quicksort is the partition routine. <br/>
The partition routine sorts the pivot element and returns the index of the sorted pivot element.

## Installation
Open a command prompt.

You can key in either one of the following:

1. py -3.6 -m pip install --index-url https://test.pypi.org/simple/ --no-deps quicksort-wc95

2. python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps quicksort-wc95

3. pip install -i https://test.pypi.org/simple/ quicksort-wc95==0.0.3

## Checking Installation 

In your command prompt either type:
1. python3

2. py -3.6

When you enter python's shell, type `from quicksort import partition` as shown in the image below.<br/>

This imports the partition submodule from the quicksort main module. <br/>

In addition, if installation works well, the import statement should work fine.<br/>

![Alt Text](images/img1.png)

## Testing the Partition Function
Now, we will call the partition function from the partition submodule.<br/>

And test if the function works. Follow the command as seen in the image below. <br/>

The image below simulates the 1st call to the partition function of quicksort. <br/>

Thus, 0 and len(lst) - 1 refer to the left and right pointers in the partition algorithm. <br/>

In addition, this routine uses the 1st element as the pivot. <br/>

![Alt Text](images/img2.png)

Notice that after 1 call to the partition routine, the index returned belong to pivot element 3.<br/>

Since, the pivot is now in index 2, elements from indices 0 to 1 are smaller than or equal to 3.
Elements from indices 3 and beyond are greater than 3.



