class LeadersArray:
    @staticmethod
    def leader_array(array):
        l = []
        n = len(array)
        for i in range(0, n):
            sub_array = array[i + 1:n]
            try:
                max_el = sub_array[0]
                for j in sub_array:
                    if j > max_el:
                        max_el = j
                if array[i] > max_el:
                    l.append(array[i])
            except:
                None

        l.append(array[n - 1])
        return l


obj=LeadersArray()
print(obj.leader_array(list(map(int,input("Enter the Array elements: ").split()))))
