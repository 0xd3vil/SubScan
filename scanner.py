import dns.resolver

def scan_subdomains(domain):
    subdomains = []
    try:
        answers = dns.resolver.query(domain, 'NS')
        for rdata in answers:
            subdomain = str(rdata).strip('.')
            subdomains.append(subdomain)
    except Exception:
        pass
    return subdomains

if __name__ == '__main__':
    domain = input('Enter the domain to scan: ')
    subdomains = scan_subdomains(domain)
    print('Subdomains:', subdomains)
