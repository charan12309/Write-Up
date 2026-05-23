---
description: Identify open ports, services, and scan states with Nmap.
---

# Host and Port Scanning

After we have found out that our target is alive, we want to get a more accurate picture of the system.

The information we need includes:

* Open ports and their services
* Service versions
* Information the services provide
* Operating system

Nmap can report six different states for a scanned port:

<figure><img src="../../../../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

### Discovering open TCP ports

By default, `Nmap` scans the top 1000 TCP ports with the SYN scan (`-sS`).

This SYN scan is set only to default when we run it as root because of the socket permissions required to create raw TCP packets.

Otherwise, the TCP scan (`-sT`) is performed by default.

This means that if we do not define ports and scanning methods, these parameters are set automatically.

We can define the ports one by one (`-p 22,25,80,139,445`), by range (`-p 22-445`), by top ports (`--top-ports=10`) from the `Nmap` database that have been signed as most frequent, by scanning all ports (`-p-`), but also by defining a fast port scan, which contains the top 100 ports (`-F`).

### Scanning top 10 TCP ports

<figure><img src="../../../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

We see that we only scanned the top 10 TCP ports of our target, and `Nmap` displays their state accordingly.

If we trace the packets `Nmap` sends, we will see the `RST` flag on `TCP port 21` that our target sends back to us.

To have a clear view of the SYN scan, we disable the ICMP echo requests (`-Pn`), DNS resolution (`-n`), and ARP ping scan (`--disable-arp-ping`).

### Trace the packets

```bash
impale7@htb[/htb]$ sudo nmap 10.129.2.28 -p 21 --packet-trace -Pn -n --disable-arp-ping

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:39 CEST
SENT (0.0429s) TCP 10.10.14.2:63090 > 10.129.2.28:21 S ttl=56 id=57322 iplen=44  seq=1699105818 win=1024 <mss 1460>
RCVD (0.0573s) TCP 10.129.2.28:21 > 10.10.14.2:63090 RA ttl=64 id=0 iplen=40  seq=0 win=0
Nmap scan report for 10.129.2.28
Host is up (0.014s latency).

PORT   STATE  SERVICE
21/tcp closed ftp
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
```

<figure><img src="../../../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

We can see from the SENT line that we (`10.10.14.2`) sent a TCP packet with the `SYN` flag (`S`) to our target (`10.129.2.28`). In the next RCVD line, we can see that the target responds with a TCP packet containing the `RST` and `ACK` flags (`RA`). `RST` and `ACK` flags are used to acknowledge receipt of the TCP packet (`ACK`) and to end the TCP session (`RST`).

Request

<figure><img src="../../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

Response

<figure><img src="../../../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

