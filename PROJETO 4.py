import random
import time

#lista
def createList():
    l = []
    for i in range (20000):
        l.append(random.randint(0,5000))
    return l

#bubbleSort
def bubbleSort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
    return lista

#insertionSort
def insertionSort(lista): 
    for index in range(1, len(lista)):
        value = lista[index]
        i = index -1 
        while i>=0:
            if value < lista[i]:
                lista[i+1] = lista[i]
                lista[i] = value
                i = i - 1
            else:
                break
    return lista
        
#shellSort
def shellSort(lista):
    gap = len(lista)//2
    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista [i]
            j = i
            while j>= gap and lista[j-gap] > temp:
                lista[j] = lista[j-gap]
                j = j-gap
            lista[j] = temp
        gap = gap//2
    return lista

#quickSort
def quickSort(alist):
       quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

#mergeSort
def mergeSort(lista):
    if len(lista) > 1:
        listaEsq = lista[:len(lista)//2]
        listaDir = lista[len(lista)//2:]
    
        mergeSort(listaEsq)
        mergeSort(listaDir)
        
        i = 0
        j = 0
        k = 0
        while i < len(listaEsq) and j < len(listaDir):
            if listaEsq[i] < listaDir[j]:
                lista[k] = listaEsq[i]
                i+=1
            else:
                lista[k] = listaDir[j]
                j+=1
            k+=1
        
        while i <len(listaEsq):
            lista[k] = listaEsq[i]
            i+=1
            k+=1
            
        while j <len(listaDir):
            lista[k] = listaDir[j]
            j+=1
            k+=1


lista = createList()

listabs = lista.copy() 
listais = lista.copy() 
listass = lista.copy() 
listaqs = lista.copy() 
listams = lista.copy() 

tb1 = time.time()
(bubbleSort(listabs))
tb2 = time.time()
print("Bubble Sort:", tb2 - tb1)

ti1 = time.time()
insertionSort(listais)
ti2 = time.time()
print("Insertion Sort:",ti2 - ti1)

ts1 = time.time()
shellSort(listass)
ts2 = time.time()
print("Lista Shell Sort:",ts2 - ts1)

tq1 = time.time()
quickSort(listaqs)
tq2 = time.time()
print("Lista Quick Sort", tq2 - tq1)

tm1 = time.time()
mergeSort(listams)
tm2 = time.time()
print("Lista Merge Sort:", tm2 - tm1)

