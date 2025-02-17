class min_dist:
    def __init__(self, from_, to_, del_cost=1, ins_cost=1, rep_cost=2, priority={"delete": 1, "insert": 2, "replace": 3}):
        self.str1 = to_
        self.str2 = from_
        self.del_cost = del_cost
        self.ins_cost = ins_cost
        self.rep_cost = rep_cost
        self.priority = priority
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
                    a = self.dist_mtrx[i-1][j-1] + self.rep_cost                    
                    b = self.dist_mtrx[i][j-1] + self.del_cost
                    c = self.dist_mtrx[i-1][j] + self.ins_cost
                    self.dist_mtrx[i][j] = min(a,b,c)

    def dist(self):
        return self.dist_mtrx[-1][-1]


    def backtrace(self):
        i, j = len(self.str2), len(self.str1)



        

        def add_operation(operation,place):
            i, j = place
            x = "" if i == -1 else self.str2[i] 
            y = "" if j == -1 else self.str2[j]

            self.back_trc.append({
                "operation": operation, 
                "letters": (x, y)
            })

        while i > 0 or j > 0:
            x = self.dist_mtrx[i][j]

            # Safe access with float('inf') as fallback
            a = self.dist_mtrx[i-1][j-1] if i > 0 and j > 0 else float('inf')
            b = self.dist_mtrx[i][j-1] if j > 0 else float('inf')
            c = self.dist_mtrx[i-1][j] if i > 0 else float('inf')
            



            operations = [
                    {"cond": i > 0 and x == c + self.del_cost, "oper": "delete", "cost":self.del_cost},
                    {"cond": j > 0 and x == b + self.ins_cost, "oper": "insert", "cost":self.ins_cost},
                    {"cond": i > 0 and j > 0 and x == a + self.rep_cost, "oper": "replace", "cost":self.rep_cost}
                ]
        
            # sort on priority of operations (in general when the cost is the same)
            operations = sorted(operations, key = lambda op: self.priority[op["oper"]])

            # sort on cost of operations (overwrite the previous sort. cost >> priority)
            operations = sorted(operations, key = lambda op: op["cost"])

            
            
            # the keep operation costs nothing so it's always of high priority 
            if i > 0 and j > 0 and self.str2[i-1] == self.str1[j-1]:
                add_operation("keep", [i-1, j-1])
                i -= 1
                j -= 1

            else:
                for oper in operations:
                    match oper["oper"]:
                        case "delete":
                            if oper["cond"]:
                                add_operation("delete", [i-1, -1])
                                i -= 1
                                break
                        case "insert":
                            if oper["cond"]:
                                add_operation("insert", [-1, j-1])
                                j -= 1
                                break
                        case "replace":
                            if oper["cond"]:
                                add_operation("replace", [i-1, j-1])
                                i -= 1
                                j -= 1
                                break



            # # update the conditions
            # for i in len(operations):
            #     if operations[i]["oper"] == "delete":
            #         operations[i]["cond"] = j > 0 and x == b + self.del_cost
            #     elif operations[i]["oper"] == "insert":
            #         operations[i]["cond"] = j > 0 and x == b + self.ins_cost
            #     elif operations[i]["oper"] == "replace":
            #         operations[i]["cond"] = i > 0 and j > 0 and x == a + self.rep_cost
                
            
        # print(cost)
        return self.back_trc[::-1]  # Reverse

    

source = "almma"
target = "amza"
min_d = min_dist(source, target, del_cost=20,priority={"delete": 0, "insert": 1, "replace": 3}) #, del_cost=1, ins_cost=1


print(f"source: {source}\t target: {target}")
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









            # if i > 0 and x == c + self.ins_cost:
            #     add_operation("delete", [i-1, -1])
            #     i -= 1

            # elif j > 0 and x == b + self.del_cost:
            #     add_operation("insert", [-1, j-1])
            #     j -= 1

            # else:  # Replace (Least favored)
            #     add_operation("replace", [i-1, j-1])
            #     i -= 1
            #     j -= 1