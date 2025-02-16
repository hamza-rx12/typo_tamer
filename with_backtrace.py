class min_dist:
    def __init__(self, from_, to_):
        self.str1 = to_
        self.str2 = from_
        m, n = len(self.str1), len(self.str2)
        self.dist_mtrx = [[0 for _ in range(m+1)] for _ in range(n+1)]
        self.back_trc = []
        
        for i in range(max(m,n)+1):
            if m+1 > i : self.dist_mtrx[0][i] = i
            if n +1 > i : self.dist_mtrx[i][0] = i

        for i in range(1,n+1):
            for j in range(1,m+1):
                if self.str2[i-1] == self.str1[j-1]:
                    self.dist_mtrx[i][j] = self.dist_mtrx[i-1][j-1]
                else:
                    a = self.dist_mtrx[i-1][j-1]
                    b = self.dist_mtrx[i][j-1]
                    c = self.dist_mtrx[i-1][j]
                    self.dist_mtrx[i][j] = min(a+2,b+1,c+1)

    def dist(self):
        return self.dist_mtrx[-1][-1]


    def backtrace(self):
        i, j = len(self.str2), len(self.str1)

        while i > 0 and j > 0:
            x = self.dist_mtrx[i][j]

            # Check then access
            a = self.dist_mtrx[i-1][j-1] if i > 0 and j > 0 else float('inf')
            b = self.dist_mtrx[i][j-1] if j > 0 else float('inf')
            c = self.dist_mtrx[i-1][j] if i > 0 else float('inf')

            # Keep 
            if self.str2[i-1] == self.str1[j-1]:
                self.back_trc.append({
                    "operation": "keep", 
                    "letters": (self.str2[i-1], self.str1[j-1])
                })
                i -= 1
                j -= 1

            # Remove
            elif x == c + 1:
                self.back_trc.append({
                    "operation": "delete",
                    "letters": (self.str2[i-1], "")
                })
                i -= 1

            # Insert
            elif x == b + 1:
                self.back_trc.append({
                    "operation": "insert",
                    "letters": ("", self.str1[j-1])
                })
                j -= 1

            # Replace: least favoured 
            else:
                self.back_trc.append({
                    "operation": "replace",
                    "letters": (self.str2[i-1], self.str1[j-1])
                })
                i -= 1
                j -= 1

        # Delete the rest
        while i > 0:
            self.back_trc.append({
                "operation": "delete",
                "letters": (self.str2[i-1], "")
            })
            i -= 1

        # Insert the rest
        while j > 0:
            self.back_trc.append({
                "operation": "insert",
                "letters": ("", self.str1[j-1])
            })
            j -= 1

        return self.back_trc[::-1]  # Reverse

    

source = "aaabc"
target = "aaaac"
min_d = min_dist(source, target)


print(f"str1: {source}\t str2: {target}")
for i in min_d.dist_mtrx:
    print(i)
print(min_d.dist())
for i in min_d.backtrace():
    print(i)




    # def backtrace(self):
    #     i, j = len(self.str2), len(self.str1)

    #     while i > 0 or j > 0 :
    #         x = self.dist_mtrx[i][j]
    #         a = self.dist_mtrx[i-1][j-1]
    #         b = self.dist_mtrx[i][j-1]
    #         c = self.dist_mtrx[i-1][j]

    #         if self.str2[i-1] == self.str1[j-1] :
    #             self.back_trc.append({
    #                 "operation":"keep", 
    #                 "letters": (self.str2[i-1], self.str1[j-1])})
    #             i -= 1
    #             j -= 1

    #         else :

    #             if x == b + 1 : 
    #                 self.back_trc.append({
    #                     "operation":"delete", 
    #                     "letters": (self.str2[i-1], "")})

    #                 i -= 1
                
    #             elif x == c + 1 :
    #                 self.back_trc.append({
    #                     "operation":"insert", 
    #                     "letters": ("", self.str1[j-1])})
    #                 j -= 1
                
    #             else :
    #                 self.back_trc.append({
    #                     "operation":"replace", 
    #                     "letters": (self.str2[i-1], self.str1[j-1])})
    #                 i -= 1
    #                 j -= 1

    #     return self.back_trc