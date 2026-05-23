# Network Enumeration with Nmap

## Syntax <a href="#syntax" id="syntax"></a>

Syntax of nmap is simple and looks like this :&#x20;

```
nmap <scan types> <options> <target>
```

```
impale7@htb[/htb]$ nmap --help

<SNIP>
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
<SNIP>
```

the TCP-SYN scan (`-sS`) is one of the default settings unless we have defined otherwise and is also one of the most popular scan methods. This scan method makes it possible to scan several thousand ports per second. The TCP-SYN scan sends one packet with the SYN flag and, therefore, never completes the three-way handshake, which results in not establishing a full TCP connection to the scanned port.

* If our target sends a `SYN-ACK` flagged packet back to us, Nmap detects that the port is `open`.
* If the target responds with an `RST` flagged packet, it is an indicator that the port is `closed`.
* If Nmap does not receive a packet back, it will display it as `filtered`. Depending on the firewall configuration, certain packets may be dropped or ignored by the firewall.

Example:

```
impale7@htb[/htb]$ sudo nmap -sS localhost

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-11 22:50 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000010s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5432/tcp open  postgresql
5901/tcp open  vnc-1

Nmap done: 1 IP address (1 host up) scanned in 0.18 seconds
```



## Host Enumeration

### Host Discovery

In case of an internal pen test, we need to check what are all the systems that are online so that we can work with them. The most effective host discovery method is to use **ICMP echo requests**, which we will look into.



**Scan Network Range**

```
impale7@htb[/htb]$ sudo nmap 10.129.2.0/24 -sn -oA tnet | grep for | cut -d" " -f5

10.129.2.4
10.129.2.10
10.129.2.11
10.129.2.18
10.129.2.19
10.129.2.20
10.129.2.28

```

<figure><img src="../../../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

* `10.129.2.0/24`: This targets the entire local subnet—all 256 possible IP addresses (from `.0` to `.255`).
* `-sn` (No Port Scan): This is critical. It tells Nmap: _"Just knock on the door to see if someone answers. Do not try to scan their ports yet."_ This works primarily by sending an ICMP Echo Request (a ping). If the machine replies, it's alive.
* `-oA tnet` (Output All Formats): As the text highlights, always log your scans. This flag creates three distinct files in your directory: `tnet.nmap` (human-readable), `tnet.gnmap` (grepable), and `tnet.xml`.

This method only works if host firewalls allow ICMP traffic.

When standard host discovery fails, you have to drop the `-sn` ping sweep and manually probe specific ports (like port 80 for web or port 445 for SMB) to see if the TCP handshake forces the machine to reveal itself.



#### Scan IP List <a href="#scan-ip-list" id="scan-ip-list"></a>

During an internal pen test, we can be provided with a set of IP's to work with...

Pre defined list of IP's:

```
impale7@htb[/htb]$ cat hosts.lst

10.129.2.4
10.129.2.10
10.129.2.11
10.129.2.18
10.129.2.19
10.129.2.20
10.129.2.28
```

Command to use:

```
impale7@htb[/htb]$ sudo nmap -sn -oA tnet -iL hosts.lst | grep for | cut -d" " -f5

10.129.2.18
10.129.2.19
10.129.2.20
```

<figure><img src="../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

Remember, this may mean that the other hosts ignore the default **ICMP echo requests** because of their firewall configurations. Since `Nmap` does not receive a response, it marks those hosts as inactive.<br>

### Scan Multiple IPs <a href="#scan-multiple-ips" id="scan-multiple-ips"></a>

It can also happen that we have to scan a small part of the network and then we can do this as an alternative to the prev one:

```
impale7@htb[/htb]$ sudo nmap -sn -oA tnet 10.129.2.18 10.129.2.19 10.129.2.20| grep for | cut -d" " -f5

10.129.2.18
10.129.2.19
10.129.2.20
```



If these IP addresses are next to each other, we can also define the range in the respective octet.

```
impale7@htb[/htb]$ sudo nmap -sn -oA tnet 10.129.2.18-20| grep for | cut -d" " -f5

10.129.2.18
10.129.2.19
10.129.2.20
```



### Scan Single IP <a href="#scan-single-ip" id="scan-single-ip"></a>

Before we scan a single host for open ports and its services, we first have to determine if it is alive or not. For this, we can use the same method as before.

```
impale7@htb[/htb]$ sudo nmap 10.129.2.18 -sn -oA host 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-14 23:59 CEST
Nmap scan report for 10.129.2.18
Host is up (0.087s latency).
MAC Address: DE:AD:00:00:BE:EF
Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
```

