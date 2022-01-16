import time
import random

def create_random_list (size):

    random_list = list(range(0,size))
    random.shuffle(random_list)

    return random_list

def bubbleSort(array):

    n = len(array)
    # we go through the list as many times ad there are elements
    for i in range(n):
        # we want the last pair of adjacent element to be(n-2,n-1)
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                #swap
                array[j],array[j+1],array[j]

def bucketSort(input_list):
    #find maximum value in the list and use length of the list tp determine which valuen the listoes into which bucket

    max_value = max(input_list)
    size = max_value/len(input_list)

    #create n empty buckets where n is equal to the length of the input list
    buckets_list=[]
    for x in range(len(input_list)):
        buckets_list.append([])

    # put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int(input_list[i]/size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list)-1].append(input_list[i])
     #sort elements within the buckets using insertion sort
    for z in range(len(input_list)):
        insertionSort(buckets_list[z])

    #concatenate buckets with sorted elements into a single list
    final_output =[]
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

def insertionSort(bucket):
    for i in range(1,len(bucket)):
        var = bucket[i] 
        j = i-1
        while (j >= 0 and var < bucket[j]):
            bucket[j+1] = bucket[j]
            j = j-1
        bucket[j+1] = var


ns = [10,100,1000,10000,100000]

time_bubble =[]
time_bucket = []

print("Running Time Bubble Sort")
for size in ns:
    abc = create_random_list(size)
    start_time = time.time()
    bubbleSort(abc)
    selesai = time.time() - start_time
    time_bubble.append(selesai)
    print(size, " : ", selesai, "detik")

print(" ")

print("Running Time Bucket Sort")
for i in ns:
    ghi = create_random_list(i)
    start_time = time.time()
    bucketSort(ghi)
    finish = time.time() - start_time
    time_bucket.append(finish)
    print(i, " : ",finish," detik ")

print(" ")

print("Running Insertion Sort")
for i in ns:
    ghi = create_random_list(i)
    start_time = time.time()
    insertionSort(ghi)
    finish = time.time() - start_time
    time_bucket.append(finish)
    print(i, " : ",finish," detik ")
