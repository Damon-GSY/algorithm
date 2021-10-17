class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # 1. 遍历每一个domain
        # 2. 获取域名，倒序排列可能的所有域名
        # 3. 将每个可能的组合存在哈希表中
        temp = dict()
        for l in cpdomains:
            l = l.split(" ")
            count = int(l[0])
            domain = l[1]
            list_domain = domain.split(".")
            cur_domain = list_domain[-1]
            for i in range(len(list_domain)-1, -1, -1):
                if i != len(list_domain) - 1:
                    cur_domain = list_domain[i] + '.' + cur_domain
                if cur_domain not in temp.keys():
                    temp[cur_domain] = count
                else:
                    temp[cur_domain] += count
        result = []
        for k, v in temp.items():
            result.append(str(v) + ' ' + k)
        return result
