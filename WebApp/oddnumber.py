# Largest Odd Number in String
# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

# A substring is a contiguous sequence of characters within a string.

def OddNumber(num):
    largest_odd = [0]
    print(len(largest_odd))
    if int(num)%2 != 0:
        for i in num:
            
            if int(i)%2 != 0:
                print( "is odd number")
                
            #     for j in len(largest_odd):
                odd = largest_odd.append(i)
                print(odd)    
            #         largest_odd.append(i)
            #         # print(odd)
            # print(largest_odd)
        # print(num)
    elif int(num)%2 == 0:
        for i in num:
            if int(i)%2 != 0:
                print( "is odd number")
                
            #     for j in len(largest_odd):
                    
                odd = largest_odd.append(i)
                print(odd)
            # print(largest_odd)
        print("There is no odd value there")

        
OddNumber("553")
    