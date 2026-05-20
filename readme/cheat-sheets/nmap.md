# Nmap

Use this page as a quick command reference for common Nmap tasks.

Use this when you need to find open ports, identify services, or run quick NSE checks.

### Common scans

```bash
nmap <TARGET_IP>                      # quick scan
nmap -sV -sC -p- <TARGET_IP>         # full version scan
nmap -sV -sC -p 21,22,80 <TARGET_IP> # scan specific ports
nmap -sU <TARGET_IP>                  # UDP scan
```

### NSE scripts

```bash
nmap --script <SCRIPT_NAME> <TARGET_IP>
nmap --script ftp-anon <TARGET_IP>     # check anonymous FTP
```

```bash
nmap --script vuln <TARGET_IP>              # check known vulns
nmap --script ftp-anon <TARGET_IP>          # anonymous FTP check
nmap --script http-enum <TARGET_IP>         # web enumeration
nmap --script smb-vuln-ms17-010 <TARGET_IP> # EternalBlue check
```

### Banner grabbing

```bash
nmap -sV --script=banner <TARGET_IP>
nc -nv <TARGET_IP> <TARGET_PORT>          # manual banner grab
```

### Aggressive scan

```bash
nmap -A -p<TARGET_PORT> <TARGET_IP>
```
