class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = {}

        for cpdomain in cpdomains:
            times, domain = cpdomain.split(" ")
            times = int(times)
            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                if subdomain not in mp:
                    mp[subdomain] = times
                else:
                    mp[subdomain] += times
        answer = []
        for key, val in mp.items():
            answer.append(str(val)+" "+key)
        
        return answer