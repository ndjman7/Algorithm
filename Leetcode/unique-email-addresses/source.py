class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        parsed_emails = []
        unique_emails = []
        for email in emails:
            name, domain = email.split('@')
            parsed_emails.append({'name': name, 'domain': domain})

        for parsed_email in parsed_emails:
            name = parsed_email['name'].split('+')[0]
            name = name.replace('.', '')
            unique_emails.append(name+'@'+parsed_email['domain'])

        return len(set(unique_emails))
