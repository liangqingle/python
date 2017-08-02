#-*- coding:utf-8 -*-
'''
1 插入排序
2 选择排序
3 冒泡排序
4 堆排序
5 快速排序 
6 归并排序 
7 计数排序
8 基数排序
9 桶排序
'''
def insertsort(source):
    '''
        插入排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    
    sourcesize = len(source)
    lastindex = sourcesize - 1
    startindex = 0
    
    for i in range(1,sourcesize):
        tmp = source[i]
        for j in range(i, startindex, -1):
            if source[j] < source[j-1]:
                source[j], source[j-1] = source[j-1],source[j]
            else:
                break
        source[j-1]=tmp
            
    target =  source
    return target


def selectionsort(source):
    '''
        选择排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source

    sourcesize = len(source)
    lastindex = sourcesize-1
    startindex = 0

    for i in range(sourcesize):
        minindex = i
        for j in range(i, sourcesize):
            if source[minindex] > source[j]:
                minindex = j
        source[minindex], source[i] = source[i], source[minindex]        

    target =  source
    return target


def bubblesort(source):
    '''
        冒泡排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    
    sourcesize = len(source)
    lastindex = sourcesize - 1
    startindex = 0

    while sourcesize > 0:
        for i in range(sourcesize-1):
            if source[i] > source[i+1]:
                source[i], source[i+1] = source[i+1], source[i]
        sourcesize = sourcesize - 1    

    target =  source
    return target


def heapsort(source):
    '''
        堆排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    
    

    target =  source
    return target


def quicksort(source):
    '''
        快速排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    target =  source
    return target


def mergesort(source):
    '''
        归并排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    target =  source
    return target


def countingsort(source):
    '''
        计数排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    target =  source
    return target


def radixsort(source):
    '''
        基数排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    target =  source
    return target


def bucketsort(source):
    '''
        桶排序算法
    '''
    if source is None or len(source) == 0 or len(source) == 1:
        return source
    target =  source
    return target


print(insertsort([10,9,8,7,6,5,4,3,2,1]))    
print(selectionsort([10,9,8,7,6,5,4,3,2,1]))    
print(bubblesort([10,9,8,7,6,5,4,3,2,1]))    
