class Solution:
    def GeekFavouriteElements((())(()))(()))((()))(((()))):
        sum = 0
        for i in arr:
            count = 0
            tempSum = 0
            d = 1
            while (d<=i/2):
                if (i%d==0):
                    count +=1
                    tempSum = tempSum + d
                d+=1
            tempSum=tempSum+i

            if count==3:
                sum += tempSum
                
        print(sum)




Solution.GeekFavouriteElements([6,10,4])