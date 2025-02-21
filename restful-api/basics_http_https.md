### Main differences between HTTP and HTTPS

_HTTP_ sends plain text requests and response
_HTTPS_ sends encrypted requests and response using **_TLS (SSL)_** - TLS uses a technology called **public key cryptography**: Public key cryptography, also known as asymmetric cryptography, uses two separate keys instead of one shared one: a public key and a private key. Public key cryptography is an important technology for Internet security.
HTTP doesn't verify that a person or a machine is who they claim to be **_(Authentication)_**
SSL certificate helps in authenticating clients. If a client's private key matches with the public keys in a website certificate, it proves that the server is actually the legitimate host of the website. This prevents or helps block a number of attacks that are possible when there is no authentication, such as:

- [On-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/)
  - An on-path attacker places themselves in between victims and the services they are trying to reach, often for the purposes of stealing data. On-path attackers place themselves between two devices (often a web browser and a [web server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)) and intercept or modify communications between the two. The attackers can then collect information as well as impersonate either of the two agents. In addition to websites, these attacks can target email communications, [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) lookups, and public WiFi networks. Typical targets of on-path attackers include [SaaS](https://www.cloudflare.com/learning/cloud/what-is-saas/) businesses, [ecommerce businesses](https://www.cloudflare.com/ecommerce/), and users of financial apps.
- [DNS hijacking](https://www.cloudflare.com/learning/dns/dns-security/)
  - In DNS hijacking, the attacker redirects queries to a different domain name server. This can be done either with malware or with the unauthorized modification of a DNS server. Although the result is similar to that of DNS spoofing, this is a fundamentally different attack because it targets the [DNS record](https://www.cloudflare.com/learning/dns/dns-records/) of the website on the nameserver, rather than a resolver’s cache.
- [BGP hijacking](https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/)
  - BGP hijacking is a malicious rerouting of Internet traffic that exploits the trusting nature of BGP, the routing protocol of the Internet. BGP hijacking is when attackers maliciously reroute Internet traffic. Attackers accomplish this by falsely announcing ownership of groups of [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), called IP prefixes, that they do not actually own, control, or route to. A BGP hijack is much like if someone were to change out all the signs on a stretch of freeway and reroute automobile traffic onto incorrect exits.
- [Domain spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)
  - Domain spoofing involves faking a website name or email name so that unsecure or malicious websites and emails appear to be safe. Domain spoofing is when cyber criminals fake a website name or email domain to try to fool users. The goal of domain spoofing is to trick a user into interacting with a malicious email or a phishing website as if it were legitimate. Domain spoofing is like a con artist who shows someone fake credentials to gain their trust before taking advantage of them.

In addition, the SSL certificate is digitally signed by the certificate authority that issued it. This provides confirmation that the server is who it claims to be.

### Structure of an HTTP request and response

![HTTP-Request-response](https://mdn.github.io/shared-assets/images/diagrams/http/messages/http-message-anatomy.svg)  
Both requests and responses share a similar structure:

1. A _start-line_ is a single line that describes the HTTP version along with the request method or the outcome of the request.
2. An optional set of _HTTP headers_ containing metadata that describes the message. For example, a request for a resource might include the allowed formats of that resource, while the response might include headers to indicate the actual format returned.
3. An empty line indicating the metadata of the message is complete.
4. An optional _body_ containing data associated with the message. This might be POST data to send to the server in a request, or some resource returned to the client in a response. Whether a message contains a body or not is determined by the start-line and HTTP headers.

The start-line and headers of the HTTP message are collectively known as the _head_ of the requests, and the part afterwards that contains its content is known as the _body_.

### List of common HTTP methods and status code

Method: **HEAD** - Description: requests the metadata of a resource in the form of header - Use cases: Performance optimization, Security, User experience
Method: **POST** - Description: sends data to the server - Use case: you want to insert the data of a new Employee who has just joined the company
Method **DELETE** - Description: asks the server to delete a specified resource - Use case: you want to delete Employee

More informations: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

Status code: **201** - Description: Created - Scenario: request has been fulfilled, resulting in the creation of a new resource
Status code: **304** - Description: Not modified - Scenario: This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.
Status code: **507** - Description: Insufficient storage - Scenario: The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.

More informations: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages
