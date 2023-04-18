
import socket
class DNSLookup:

    def __init__(self, domain):
        
        """
        Creates a new DNSLookup object for performing DNS lookups.
        Args:
            domain (str): The domain name to look up.
        """
        
        self.domain = domain
        
    def get_ip(self):
        """
        Performs a DNS lookup and returns the IP address(es) associated with the domain.
        Returns:
            list: A list of IP addresses associated with the domain.
        Raises:
            socket.gaierror: If the DNS lookup fails.
        """
        ip_addresses = []
        try:
            # Resolve the domain to one or more IP addresses
            ip_addresses = socket.getaddrinfo(self.domain, None, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            ip_addresses = [addr[4][0] for addr in ip_addresses]
        except socket.gaierror as e:
            print(f"DNS lookup failed: {e}")
        return ip_addresses
