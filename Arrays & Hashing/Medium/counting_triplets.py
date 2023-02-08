# Counting Triplets

# Given an array, find the number of distinct indices whereby the sum of numbers are divisible by d. Note we assume that an index starts at 1

# Example:
# Input = [3,3,4,7,8]
# Output = 3
# Explanation : [3,3,4] with indices 1,2,3 is a solution as 10 is divisible by 5
#               [3,4,8] with indices 1,3,5 is a solution as 15 is divisible by 5
#               [3,4,8] with indices 2,3,5 is a solution as 15 is divisible by 5



def countingTriplets(arr, d) : 
    
    '''
        idea - Using an index mapping to store the occurences of each number, checking if the sum of any three numbers is divisible by M, and store the value.
    '''
    count = 0
      
    # Storing frequencies of all remainders when divided by d. 
    freq = [0] * d 
    for i in range(0,len(arr)) : 
        arr[i] = arr[i] % d 
        freq[arr[i]] = freq[arr[i]] + 1
      
    for i in range(0,d) : 
        for j in range(i,d) : 
              
            # including i and j in the sum of rem, we calculate the remainder required to make the sum divisible by d 
            rem = (d - (i + j) % d) % d 
              
            # if the required number is  less than j, we skip as we  have already calculated for that value before. arrs j here starts with i and rem is less than j. 
            if (rem < j) : 
                continue
                  
            # Case where thrice of a number is divisible by d
            if (i == j and rem == j) : 
                count = count + freq[i] * (freq[i] - 1) * (freq[i] - 2) / 6
                  
                  
            # Case where twice of a number added with another number is divisible by d
            
            elif (i == j) : 
                count = count +(freq[i] * (freq[i] - 1) * freq[rem] / 2) 
       
            elif (i == rem) : 
                count = count + freq[i] * (freq[i] - 1) * freq[j] / 2
            elif (rem == j) : 
                count = count + freq[j] * (freq[j] - 1) * freq[i] / 2
                
       
            # case where all three numbers sump up to be divisible by d; we increment the current count with the product of their frequencies
            else : 
                count = count + freq[i] * freq[j] * freq[rem] 
              
    return int(count) 
    

if __name__ == '__main__':
    arr = [3,3,4,7,8]
    d = 5
    
    print(countingTriplets(arr,d))
    