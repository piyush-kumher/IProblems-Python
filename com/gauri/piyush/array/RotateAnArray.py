#!/usr/bin/python

# Reversal algorithm for right rotation of an array
# Given an array, right rotate it by k elements.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3

#First Approach.. though this uses extra uses, can also be done in same array with for loop

list = list[::-1] #reverse the array

firstSection = list[0:k] #take first k elements
firstSection.reverse()   # reverse it
secondSection = list[k:] # take last remaining elements
secondSection.reverse() # reverse last elements

list[0:k] = firstSection
list[k:] = secondSection

print list


#Second approach

def rotate_elements(input_list, k):
    dummy_array = [0] * len(input_list)
    i = 0;
    while i < len(input_list):
        m = i + k
        if m >= len(input_list):
            m -= len(input_list)
        dummy_array[m] = input_list[i]
        i += 1
    return dummy_array

print rotate_elements(list1, k)


