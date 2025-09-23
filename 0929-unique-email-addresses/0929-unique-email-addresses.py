class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        counter = 0
        seen = set()
        for email in emails:
            local, domain = email.split("@")
            local_plus = local.split("+")[0]
            local_val = "".join(local_plus.split("."))

            url = local_val + "@"+domain 
            print(url)
            if url not in seen:
                seen.add(url)
                counter += 1
                
        return counter

