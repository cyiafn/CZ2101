import time
import random
from time import process_time
import os
import logging
import copy
logging.basicConfig(filename='log.log', level=logging.INFO)


def insertionSort(f, l):

    global ar
     
    # Traverse through 1 to len(arr)
    compare = 0
    for i in range(f, l + 1):
 
        key = ar[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= f and key < ar[j]:
            compare += 1
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = key
    
    return compare

def hybridMergeSort(f, l):
    #global ar variable so that we can actually modify the array
    global ar
    
    #check for threshhold for S insertion sort
    if (l - f) + 1 <= int(os.environ["s"]):
        compare = insertionSort(f, l)
        return compare

    #middle point, + init key comparison key1,key2
    mid = int((l - f) / 2) + f
    key1 = 0
    key2 = 0
    #less than 1 means only 1 element
    if l - f < 1:
        return 0
    
    # if more than 2 eles do merge sort
    elif (l - f > 1):
        key1 = hybridMergeSort(f, mid)
        key2 = hybridMergeSort(mid + 1, l)
        
    #merge left right
    key3 = merge(f, l)
    comparisons = key1 + key2 + key3
    

    return comparisons



def mergeSort(f, l):
    #global ar variable so that we can actually modify the array
    global ar
    #middle point, + init key comparison key1,key2
    mid = int((l - f) / 2) + f
    key1 = 0
    key2 = 0
    #less than 1 means only 1 element
    if l - f < 1:
        return 0
    # if more than 2 eles do merge sort
    elif (l - f > 1):
        key1 = mergeSort(f, mid)
        key2 = mergeSort(mid + 1, l)
        
    #merge left right
    key3 = merge(f, l)
    comparisons = key1 + key2 + key3
    

    return comparisons



def merge(f, l):
    #global ar variable so that we can actually modify the array
    global ar
    #middle point
    mid = int((l - f) / 2) + f
    #less than 0 means 1/ no keys
    if l - f  < 1:
        return 0
    comp = 0
    #alternative to pointer by keeping track of indexes
    leftFirst, rightFirst, fixedIndexStart = f, mid + 1, l + 1 
    while True:
        #merge func
        if ar[leftFirst] < ar[rightFirst]:
            comp += 1
            popped = ar.pop(leftFirst)
            ar.insert(l, popped)
            rightFirst -= 1
            fixedIndexStart -= 1
        elif ar[leftFirst] > ar[rightFirst]:
            comp += 1
            popped = ar.pop(rightFirst)
            ar.insert(l,popped)
            fixedIndexStart -= 1
        elif ar[leftFirst] == ar[rightFirst]:
            comp += 1
            popped = ar.pop(leftFirst)
            ar.insert(l,popped)
            rightFirst -= 1
            popped = ar.pop(rightFirst)
            ar.insert(l,popped)
            fixedIndexStart -= 2
        if leftFirst == rightFirst or rightFirst == fixedIndexStart:
            while fixedIndexStart > f:
                popped = ar.pop(f)
                ar.insert(l, popped)
                fixedIndexStart -= 1
            break
        elif leftFirst == rightFirst and rightFirst == fixedIndexStart:
            break
    return comp
    

def generateRandomArray(k, rang):
    ar = []
    for i in range(k):
        ar.append(random.randrange(rang))
    return ar


    
if __name__ == "__main__":

    elements = [10,50,100,500,1000,5000,10000,50000]
    
    ranges = [99, 99, 999, 999, 9999, 9999, 99999, 99999]
    for element in range(0, len(elements)):
        for s in range(1,100):
            print(str(elements[element]) + " elements for S: " + str(s))
            os.environ["s"] = str(s)
            sortingTimeAr = []
            mergeKeys = []
            mergeHybridKeys = []
            sortingTimeHybrid = []
            for i in range(5):
                ar = generateRandomArray(elements[element], ranges[element])
                ar1 = copy.deepcopy(ar)
                t0 = time.process_time()
                compare = mergeSort(0, len(ar) - 1)
                sortedTime = time.process_time() - t0
                sortingTimeAr.append(sortedTime)
                mergeKeys.append(compare)

                ar = ar1
                t0 = time.process_time()
                compare = hybridMergeSort(0, len(ar) - 1)
                sortedTime = time.process_time() - t0
                sortingTimeHybrid.append(sortedTime)
                mergeHybridKeys.append(compare)


            print("=========================================")
            logging.info("===========================================")
            logging.info(str(elements[element]) + " elements for S: " + str(s))
            logging.info("Average sorted time for merge sort: {:.7f}".format(sum(sortingTimeAr)/len(sortingTimeAr)))
            logging.info("Average key compare for merge sort: {:.1f}".format(sum(mergeKeys)/len(mergeKeys)))
            logging.info("Average sorted time for hybrid sort: {:.7f}".format(sum(sortingTimeHybrid)/len(sortingTimeHybrid)))
            logging.info("Average key compare for hybrid sort: {:.1f}".format(sum(mergeHybridKeys)/len(mergeHybridKeys)))
            print("Average sorted time for merge sort: {:.7f}".format(sum(sortingTimeAr)/len(sortingTimeAr)))
            print("Average key compare for merge sort: {:.1f}".format(sum(mergeKeys)/len(mergeKeys)))
            print("Average sorted time for hybrid sort: {:.7f}".format(sum(sortingTimeHybrid)/len(sortingTimeHybrid)))
            print("Average key compare for hybrid sort: {:.1f}".format(sum(mergeHybridKeys)/len(mergeHybridKeys)))
