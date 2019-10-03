class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        answer = []
        domain_dict = {}

        def parse_domain(domain):
            sub_domains = []
            new_sub_domains = ''
            for sub_domain in domain.split('.')[::-1]:
                new_sub_domains = sub_domain + new_sub_domains
                sub_domains.append(new_sub_domains)
                new_sub_domains = '.' + new_sub_domains
            return sub_domains

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)
            for sub_domain in parse_domain(domain):
                if sub_domain in domain_dict:
                    domain_dict[sub_domain] += count
                else:
                    domain_dict[sub_domain] = count

        for key, value in domain_dict.items():
            answer.append('{} {}'.format(value, key))

        return answer
