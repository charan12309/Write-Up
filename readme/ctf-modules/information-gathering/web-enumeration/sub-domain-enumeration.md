# Sub Domain Enumeration

Subdomains extend the main domain and often expose separate applications or services.

Examples include `blog.example.com`, `shop.example.com`, and `mail.example.com`.

### Why subdomains matter

Subdomains often expose assets that are not linked from the main site.

Common examples:

* `Development and Staging Environments` — may run weaker controls or older code
* `Hidden Login Portals` — may expose admin panels or internal access points
* `Legacy Applications` — may still run outdated and vulnerable software
* `Sensitive Information` — may expose files, data, or configuration details

### Subdomain enumeration

`Subdomain enumeration` is the process of identifying and listing subdomains for a target domain.

From a DNS perspective, subdomains are usually represented by `A` or `AAAA` records. They may also use `CNAME` records to point to other hosts.

There are two main approaches.

#### Active subdomain enumeration

This approach interacts directly with the target's DNS infrastructure.

One method is a `DNS zone transfer`. A misconfigured server may expose the full zone. This is uncommon, but still worth testing when allowed.

Another common method is `brute-force enumeration`. This tests a list of possible names against the target domain. Tools such as `dnsenum`, `ffuf`, and `gobuster` automate this process with common or custom wordlists.

#### Passive subdomain enumeration

This approach uses external data sources and avoids direct interaction with the target's DNS servers.

Useful sources include:

* `Certificate Transparency (CT) logs` — certificates often list subdomains in the SAN field
* `Search engines` — operators such as `site:` can reveal indexed subdomains
* `Online DNS databases` — many services aggregate DNS data from multiple sources

Passive methods are quieter. Active methods are usually more complete. Combining both gives better coverage.

### Subdomain brute-forcing

`Subdomain brute-force enumeration` tests pre-defined names against the target domain to find valid subdomains.

This usually follows four steps:

1. `Wordlist selection`
   * `General-purpose` — common names such as `dev`, `staging`, `blog`, `mail`, `admin`, and `test`
   * `Targeted` — names based on the target's industry, stack, or naming patterns
   * `Custom` — names built from intelligence gathered during recon
2. `Iteration and querying`
   * Append each word to the root domain, such as `dev.example.com`
3. `DNS lookup`
   * Query each candidate and check whether it resolves
4. `Filtering and validation`
   * Keep valid results and confirm whether the host is live or useful

### Common tools

| Tool                                                    | Description                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------- |
| [dnsenum](https://github.com/fwaeytens/dnsenum)         | Comprehensive DNS enumeration tool with brute-force support |
| [fierce](https://github.com/mschwager/fierce)           | Recursive subdomain discovery with wildcard detection       |
| [dnsrecon](https://github.com/darkoperator/dnsrecon)    | DNS reconnaissance with multiple discovery modes            |
| [amass](https://github.com/owasp-amass/amass)           | Broad subdomain discovery with strong data source coverage  |
| [assetfinder](https://github.com/tomnomnom/assetfinder) | Lightweight subdomain discovery tool                        |
| [puredns](https://github.com/d3mondev/puredns)          | Fast brute-force resolution and filtering                   |

### DNSEnum

`dnsenum` is a command-line tool written in Perl for DNS reconnaissance and subdomain discovery.

Key functions include:

* `DNS Record Enumeration` — retrieves records such as `A`, `AAAA`, `NS`, `MX`, and `TXT`
* `Zone Transfer Attempts` — tests discovered name servers for `AXFR`
* `Subdomain Brute-Forcing` — tests candidate names from a wordlist
* `Google Scraping` — looks for subdomains indexed in search results
* `Reverse Lookup` — finds domains associated with an IP address
* `WHOIS Lookups` — gathers registration and ownership details

This example enumerates subdomains for `inlanefreight.com` with a SecLists wordlist:

```bash
dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -r
```

Command breakdown:

* `dnsenum --enum inlanefreight.com` — sets the target domain and enables common enumeration options
* `-f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt` — uses the SecLists wordlist for brute force
* `-r` — enables recursive brute forcing against discovered subdomains

Example output:

```shell
impale7@htb[/htb]$ dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt

dnsenum VERSION:1.2.6

-----   inlanefreight.com   -----

Host's addresses:
__________________

inlanefreight.com.                       300      IN    A        134.209.24.248

[...]

Brute forcing with /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt:
_______________________________________________________________________________________

www.inlanefreight.com.                   300      IN    A        134.209.24.248
support.inlanefreight.com.               300      IN    A        134.209.24.248
[...]

done.
```

<br>
