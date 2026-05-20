# Getting started

Use this page for first-pass concepts, common tools, and early service checks.

### Cheat sheets

| Cheat sheet                               | Focus                                          |
| ----------------------------------------- | ---------------------------------------------- |
| [Common ports](../cheat-sheets/page-3.md) | Default ports and quick service lookup         |
| [TMUX](../cheat-sheets/tmux.md)           | Session, window, and pane shortcuts            |
| [VIM](../cheat-sheets/vim.md)             | Fast editing and navigation                    |
| [Nmap](../cheat-sheets/nmap.md)           | Common scans, NSE scripts, and banner grabbing |
| [SMB](../cheat-sheets/smb.md)             | Share enumeration and access commands          |
| [SNMP](../cheat-sheets/snmp.md)           | `snmpwalk` and community string checks         |

## Foundations

### Shell

The shell takes user input and passes commands to the operating system to perform a specific function.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

### Port

Ports are virtual points where network connections begin and end.

They allow a computer to route different types of traffic simultaneously over a single network connection by mapping specific data streams to distinct software processes (e.g., SSH vs. web requests).

{% include "../../.gitbook/includes/protocol-comparison-tcp-vs....md" %}

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Web server

Software running on a host machine that directly handles HTTP/HTTPS traffic from a client browser over TCP ports 80 and 443.

It processes incoming requests, maps them to physical files, or hands them off to the application backend. This creates a large attack surface.

Attack surface breakdown:

Web Server Vulnerabilities and Web Application Flaws (OWASP Top 10)

{% embed url="https://owasp.org/Top10/2025/" %}

## Access and terminal tools

### Using SSH

Secure Shell is a network protocol that runs on port 22 by default and provides users a secure way to access a computer remotely.

SSH can use password authentication or public-key authentication with a public and private key pair.

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

### Using Netcat

Netcat, `ncat`, or `nc` is used to interact with TCP and UDP ports.

It can be used for many things during a pentest.

Its primary use is connecting to shells.

Netcat can connect to any listening port and interact with the service on that port.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Netcat can also be used to grab a banner from a target IP and port.

This is called banner grabbing.

Netcat can also be used to transfer files.

```bash
nc -nv <TARGET_IP> <TARGET_PORT>
```

Then there is also Socat, often called Netcat on steroids. A [standalone binary](https://github.com/andrew-d/static-binaries) of `Socat` can be transferred to a system after remote code execution to get a more stable reverse shell.

Socat also supports forwarding ports and connecting to serial devices.

1. **Port forwarding**

When you hack a target network, you often find a central server (like a database) that is completely hidden from the internet behind a firewall.

You cannot talk to it directly.

But if you have already compromised the public web server sitting right next to it, you can tell that web server: _"Take any traffic I send to you on port X, and automatically forward it to the hidden database on port Y."_

2. **Connecting to serial devices**

* **Serial devices**: Physical hardware components like routers, IoT devices, or microchips that transmit data sequentially, one bit at a time.
* **Security purpose**: Involves opening a device's casing, connecting a cable directly to diagnostic pins on the circuit board like UART, and using tools to read raw data or drop into a root command line without a network connection or password.

### TMUX

Terminal multiplexers, like `tmux` or `Screen`, are great utilities for expanding a standard Linux terminal's features, like having multiple windows within one terminal and jumping between them.

{% embed url="https://tmuxcheatsheet.com/" %}

### VIM

Vim is a great text editor that can be used for writing code or editing text files on Linux systems.

{% embed url="https://vimsheet.com/" %}

## Service enumeration

### Nmap

Nmap is used to scan ports and let us know the services that are running.

Basic Nmap scan. This checks the 1,000 most common ports and runs a TCP scan by default:

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

```bash
nmap <TARGET_IP>
```

We can use the `-sC` parameter to specify that `Nmap` scripts should be used to try and obtain more detailed information. The `-sV` parameter instructs `Nmap` to perform a version scan. In this scan, Nmap will fingerprint services on the target system and identify the service protocol, application name, and version. The version scan is underpinned by a comprehensive database of over 1,000 service signatures. Finally, `-p-` tells Nmap that we want to scan all 65,535 TCP ports.

<br>

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

```bash
nmap -sV -sC -p- <TARGET_IP>
```

* `-sV` → version detection
* `-sC` → run default scripts
* `-p-` → scan all 65,535 ports

### Nmap scripts

Specifying `-sC` will run many useful default scripts against a target, but there are cases when running a specific script is required.

```bash
nmap --script <SCRIPT_NAME> <TARGET_IP>
nmap --script ftp-anon <TARGET_IP>          # check anonymous FTP
```

```bash
nmap --script vuln <TARGET_IP>              # check known vulns
nmap --script ftp-anon <TARGET_IP>          # anonymous FTP check
nmap --script http-enum <TARGET_IP>         # web enumeration
nmap --script smb-vuln-ms17-010 <TARGET_IP> # EternalBlue check
```

## Attacking Network Services

### Banner grabbing

**Fingerprinting** = identifying exactly what is running on a target.

Like a human fingerprint — unique to each person. Every service leaves identifying information.

**Banner grabbing is one way to fingerprint:**

```bash
# Using Nmap
nmap -sV --script=banner <TARGET_IP>

# Using Netcat manually
nc -nv <TARGET_IP> 21

# Response:
220 (vsFTPd 3.0.3)
→ FTP server, version 3.0.3
```

Generic info → "FTP is running"\
Fingerprinted → "vsFTPd 3.0.3 is running"

Generic → can't find specific exploits\
Fingerprinted → Google "vsFTPd 3.0.3 CVE"\
→ find backdoor vulnerability\
→ exploit it

### FTP

`Nmap` scan of the default port for FTP (21) reveals the vsftpd 3.0.3 installation that we identified previously. Further, it also reports that anonymous authentication is enabled and that a `pub` directory is available.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### SMB

SMB (Server Message Block) is a prevalent protocol on Windows machines that provides many vectors for vertical and lateral movement. `Nmap` has many scripts for enumerating SMB, such as [smb-os-discovery.nse](https://nmap.org/nsedoc/scripts/smb-os-discovery.html), which will interact with the SMB service to extract the reported operating system version.

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

```bash
nmap -A -p<TARGET_PORT> <TARGET_IP>
```

This is an aggressive scan.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

#### Why This Matters in Pentesting

The text is demonstrating the progression of enumeration. You start by finding an open port (`445`), then you use specialized tools (NSE scripts or `-A` flags) to pull the banners and exact software versions. Once you have those precise versions (e.g., _Windows 7 SP1_ or _Samba 4.6.2_), you can cross-reference them against public vulnerability databases to find specific, actionable exploits like EternalBlue.<br>

### Shares

* **SMB (Server Message Block)**: Protocol used to share folders and files remotely.
* **Security risk**: Shares frequently expose sensitive data like hardcoded passwords.
* **Tool (`smbclient`)**: Used to enumerate and interact with SMB shares from the command line.
  * `-L` lists all available shares on the target host.
  * `-N` suppresses the password prompt and forces an anonymous connection attempt.

Listing available shares:

```bash
smbclient -N -L \\\\<TARGET_IP>
```

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

After finding a non-default share like `users`, we attempt to connect to it.

```bash
smbclient \\\\<TARGET_IP>\\<SHARE_NAME>
```

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

If this fails, we need to find valid credentials elsewhere and then try again.

```bash
smbclient -U <USERNAME> \\\\<TARGET_IP>\\<SHARE_NAME>
```

After this, the tool asks for a password. Once inside the `smb: \>` prompt, it functions similarly to a basic FTP or Linux shell.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

We can now use the `get` command to download the `passwords.txt` file.

### SNMP

* **SNMP (ports 161/162 TCP/UDP)**: Used for device management.
* **Versions 1 and 2c**: Insecure. They rely on unencrypted plaintext community strings instead of passwords.
* **Default danger**: Default strings are almost always `public` for read or `private` for write.
* **Pentest value**: Leaks running processes, internal routing tables, and exact software versions.

#### `snmpwalk`

```bash
snmpwalk -v 2c -c public <TARGET_IP> 1.3.6.1.2.1.1.5.0
```

* `snmpwalk`: A tool that sends sequential requests to "walk" through a device's management data tree.
* `-v 2c`: Specifies that it is using SNMP version 2c (the insecure, plaintext version).
* `-c public`: Supplies `public` as the community string (password).
* `<TARGET_IP>`: The target IP address.
* `1.3.6.1.2.1.1.5.0`: This OID points directly to the system's hostname.

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

If the community string fails, use `onesixtyone` to brute-force it.

```bash
onesixtyone -c dict.txt <TARGET_IP>
```

* `onesixtyone`: A highly efficient, multi-threaded scanner built specifically to brute-force SNMP community strings.
* `-c dict.txt`: Passes a text file containing a dictionary of common community strings (e.g., `public`, `private`, `internal`, `manager`, `cisco`).

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

### Web Enumeration

