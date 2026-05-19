# Getting started

***

### Common Terms&#x20;

#### Shell :

The shell is a program that takes the input from the user and passes these commands to OS (Operating System) to perform a specific function.

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### Port:

Ports are virtual points where network connections begin and end.

They allow a computer to route different types of traffic simultaneously over a single network connection by mapping specific data streams to distinct software processes (e.g., SSH vs. web requests).

{% include "../../.gitbook/includes/protocol-comparison-tcp-vs....md" %}

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### Web Server :

Software running on a host machine that directly handles HTTP/HTTPS traffic from a client browser over TCP ports 80 and 443.

It processes incoming requests, maps them to physical files, or hands them off to the application backend and it has a huge attack surface.

Attack Surface Breakdown:

Web Server Vulnerabilities and Web Application Flaws (OWASP Top 10)

{% embed url="https://owasp.org/Top10/2025/" %}

### Common Tools&#x20;

#### Using SSH :

Secure Shell is a network protocol that runs on port 22 by default and provides users a secure way to access a computer remotely.

SSH can be configured with password authentication or passwordless using public-key authentication using public/private key-pair.

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### Using Netcat :

Netcat, ncat or nc is used to interact with TCP/UDP Ports.

It can be used for many things during a pentest.

Its primary usage is for connecting to shells.

Netcat can be used to connect to any listening port and interact with the service on that port

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Netcat can be used this way to obtain the banner running on that Port and IP.

This is called as Banner Grabbing.

Netcat can also be used to transfer files.

```
nc -nv <Target_IP> <Target_Port>
```

Then there is also Socat which is called as Netcat on steriods.A [standalone binary](https://github.com/andrew-d/static-binaries) of `Socat` can be transferred to a system after obtaining remote code execution to get a more stable reverse shell connection.

Socat also supports forwarding ports and connecting to serial devices.



1. **Port Forwarding :**

When you hack a target network, you often find a central server (like a database) that is completely hidden from the internet behind a firewall.

You cannot talk to it directly.

But if you have already compromised the public web server sitting right next to it, you can tell that web server: _"Take any traffic I send to you on Port X, and automatically forward it to the hidden database on Port Y."_



2. **Connecting to Serial Devices :**

* Serial Devices: Physical hardware components (like routers, IoT devices, or microchips) that transmit data sequentially, one bit at a time.
* Security Purpose: Involves physically opening a device's casing, connecting a cable directly to diagnostic pins on the circuit board (like UART), and using tools to read raw data or drop straight into a root command line without a network connection and password.

#### TMUX :

Terminal multiplexers, like `tmux` or `Screen`, are great utilities for expanding a standard Linux terminal's features, like having multiple windows within one terminal and jumping between them.&#x20;

[https://tmuxcheatsheet.com/](https://tmuxcheatsheet.com/)

#### VIM:

Vim is a great text editor that can be used for writing code or editing text files on Linux systems.&#x20;

[https://vimsheet.com/](https://vimsheet.com/)

