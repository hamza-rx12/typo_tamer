str1 = "ac"
str2 = "abc"

class min_dist:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.dist_mtrx = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
        self.back_trc = []
        
        for i in range(len(str1)+1):
            self.dist_mtrx[0][i] = i
            if len(str2)+1 > i:
                self.dist_mtrx[i][0] = i

        for i in range(1,len(str2)+1):
            for j in range(1,len(str1)+1):
                if str2[i-1] == str1[j-1]:
                    self.dist_mtrx[i][j] = self.dist_mtrx[i-1][j-1]
                else: 
                    a = self.dist_mtrx[i-1][j-1]
                    b = self.dist_mtrx[i][j-1]
                    c = self.dist_mtrx[i-1][j]
                    self.dist_mtrx[i][j] = min(a+2,b+1,c+1)

    def dist(self):
        return self.dist_mtrx[-1][-1]

    # def backtrace(self):

    
min_d = min_dist(str1,str2)


for i in min_d.dist_mtrx:
    print(i)
print(min_d.dist())

    


# str1, str2 = (str1,str2) if len(str1) >= len(str2) else (str2,str1)
# dist = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
 

# for i in range(len(str1)+1):
#     dist[0][i] = i
#     if len(str2)+1 > i:
#         dist[i][0] = i

# for i in range(1,len(str2)+1):
#     for j in range(1,len(str1)+1):
#         if str2[i-1] == str1[j-1]:
#             dist[i][j] = dist[i-1][j-1]
#         else: 
#             a = dist[i-1][j-1]
#             b = dist[i][j-1]
#             c = dist[i-1][j]
#             dist[i][j] = min(a+2,b+1,c+1)
