# Function to get sum of digits 
def getSum(n):  
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

# Print out the number which is equal to the square of sum of its digits

for number in range(50,201):
    numSum=getSum(number)
    numSumSquare=numSum**2
    if (numSumSquare == number):
        print(number)