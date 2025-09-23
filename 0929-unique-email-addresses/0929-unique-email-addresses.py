class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        counter = 0
        seen = set()
        for email in emails:
            local, domain = email.split("@")
            local_val = ""
            for c in local:
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    local_val += c
            url = local_val + "@"+domain 
            print(url)
            if url not in seen:
                seen.add(url)
                counter += 1
                
        return counter

