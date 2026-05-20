# Nmap

Use this page as a quick command reference for common Nmap tasks.

### Common scans

```
nmap 10.129.42.253              # quick scan
nmap -sV -sC -p- IP             # full version scan
nmap -sV -sC -p 21,22,80 IP    # scan specific ports
nmap -sU IP                     # UDP scan
```

### NSE scripts

```
nmap --script <script-name> IP
nmap --script ftp-anon IP          # check anonymous FTP
```

```
nmap --script vuln IP              # check known vulns
nmap --script ftp-anon IP          # anonymous FTP check
nmap --script http-enum IP         # web enumeration
nmap --script smb-vuln-ms17-010 IP # EternalBlue check
```

### Banner grabbing

```
nmap -sV --script=banner IP 
nc -nv IP PORT                 # manual banner grab
```
