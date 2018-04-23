
# coding: utf-8

# In[2]:


arr = [2,6,25,6,5,10]
print("UNSORTED:")
print(arr)
for i in range(1, len(arr)):
 
        check = arr[i]
        j = i-1
        while j >=0 and check < arr[j] :
                arr[j+1] = arr[j]
                j = j-1
        arr[j+1] = check
print("SORTED:")
print(arr)


# In[3]:


#Create a list of unsorted numbers
arr = [2,6,25,6,5,10]
#Print the unsorted list to screen
print("UNSORTED:")
print(arr)
#Create a for loop that iterates through each element in the list from 1 to the length of the list
for i in range(1, len(arr)):
        #create a variable called check to store the selected element in the list
        check = arr[i]
        #create a variable called j to store the position of the selected element in the list minus 1
        j = i-1
        #create a while loop that checks if j is greater than or equal to 0 and if check is less than the element held in list in posistion j
        while j >=0 and check < arr[j] :
                #set the element in position j+1 to store the element currently in position j
                arr[j+1] = arr[j]
                #decrement the variable j by 1
                j = j-1
        #set the element in position j+1 to hold the value held by check
        arr[j+1] = check
#Print the sorted list to screen
print("SORTED:")
print(arr)

