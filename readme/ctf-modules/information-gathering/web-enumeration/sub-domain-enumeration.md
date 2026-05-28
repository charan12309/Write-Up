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

### DNS zone transfers

Brute forcing works well, but `AXFR` is faster when it is exposed.

A DNS zone transfer replicates records between name servers. If it is misconfigured, you may get the full zone file in one request.

### What a zone transfer is

A zone transfer is a full copy of the records in a DNS zone.

Authoritative servers use it to keep primary and secondary servers in sync. If access controls are loose, an unauthorized client can pull the same data.

![Diagram showing data transfer between secondary and primary servers. Includes steps: XML Request, XML Record, loop for retries, XML Report, and AOK (Acknowledgment).](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/144/ig_dns_zone_transfers_1.png)

Typical flow:

1. **AXFR request** — the secondary server requests a full transfer.
2. **SOA record** — the primary server returns the zone authority details.
3. **Record transfer** — the server sends records such as `A`, `AAAA`, `MX`, `CNAME`, and `NS`.
4. **Transfer complete** — the server signals the end of the transfer.
5. **Acknowledgment** — the secondary server confirms receipt.

### Why misconfigured transfers matter

Zone transfers are normal for DNS operations. The risk comes from weak access controls.

If any client can request `AXFR`, the server may disclose the entire zone. That gives you a high-value map of the target infrastructure.

Useful data often includes:

* `Subdomains` — hidden apps, staging hosts, admin panels, and internal naming patterns
* `IP addresses` — direct targets for scanning and service validation
* `Name server records` — authoritative infrastructure and possible hosting clues

#### Remediation

Modern DNS servers should allow transfers only to trusted secondary servers.

Misconfigurations still happen. That is why testing `AXFR` remains worth a quick check when scope allows.

{% hint style="warning" %}
Attempt zone transfers only when you have authorization.
{% endhint %}

### Testing with `dig`

Use `dig` to request a zone transfer from an authoritative server:

```bash
dig axfr @nsztm1.digi.ninja zonetransfer.me
```

This requests a full zone transfer for `zonetransfer.me` from `nsztm1.digi.ninja`.

If the server allows it, `dig` returns the full set of DNS records, including subdomains.

Example output:

```shell
impale7@htb[/htb]$ dig axfr @nsztm1.digi.ninja zonetransfer.me

; <<>> DiG 9.18.12-1~bpo11+1-Debian <<>> axfr @nsztm1.digi.ninja zonetransfer.me
; (1 server found)
;; global options: +cmd
zonetransfer.me.    7200    IN  SOA nsztm1.digi.ninja. robin.digi.ninja. 2019100801 172800 900 1209600 3600
zonetransfer.me.    300 IN  HINFO   "Casio fx-700G" "Windows XP"
zonetransfer.me.    301 IN  TXT "google-site-verification=tyP28J7JAUHA9fw2sHXMgcCC0I6XBmmoVi04VlMewxA"
zonetransfer.me.    7200    IN  MX  0 ASPMX.L.GOOGLE.COM.
...
zonetransfer.me.    7200    IN  A   5.196.105.14
zonetransfer.me.    7200    IN  NS  nsztm1.digi.ninja.
zonetransfer.me.    7200    IN  NS  nsztm2.digi.ninja.
_acme-challenge.zonetransfer.me. 301 IN TXT "6Oa05hbUJ9xSsvYy7pApQvwCUSSGgxvrbdizjePEsZI"
_sip._tcp.zonetransfer.me. 14000 IN SRV 0 0 5060 www.zonetransfer.me.
14.105.196.5.IN-ADDR.ARPA.zonetransfer.me. 7200 IN PTR www.zonetransfer.me.
asfdbauthdns.zonetransfer.me. 7900 IN   AFSDB   1 asfdbbox.zonetransfer.me.
asfdbbox.zonetransfer.me. 7200  IN  A   127.0.0.1
asfdbvolume.zonetransfer.me. 7800 IN    AFSDB   1 asfdbbox.zonetransfer.me.
canberra-office.zonetransfer.me. 7200 IN A  202.14.81.230
...
;; Query time: 10 msec
;; SERVER: 81.4.108.41#53(nsztm1.digi.ninja) (TCP)
;; WHEN: Mon May 27 18:31:35 BST 2024
;; XFR size: 50 records (messages 1, bytes 2085)
```

<br>
