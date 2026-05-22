---
description: How to balance guided study with black-box practice.
---

# Practice strategy

Use this page to build a practice routine that creates real penetration testing skill.

### Guided vs exploratory learning

Do not study in one mode only.

Switch between guided work and black-box practice.

#### Guided learning

Use this for new tools, protocols, and attack paths.

This mode is structured.

You read the theory, see a working example, and reproduce it in a lab.

Why it matters:

* builds strong fundamentals
* explains why the target is vulnerable
* reduces blind tool usage

#### Exploratory learning

Use this for realism and problem solving.

This mode gives you a target with little or no guidance.

You must enumerate, triage, and build your own path forward.

Why it matters:

* sharpens your methodology
* forces independent thinking
* prepares you for messy real targets

#### Best way to combine both

Learn a concept in a guided lab first.

Then apply it on a black-box machine or CTF challenge immediately.

That loop turns theory into repeatable skill.

{% hint style="info" %}
Use guided learning to understand a tool deeply.

Use exploratory practice to prove you can still use it without instructions.
{% endhint %}

### External practice resources

Use local vulnerable targets when you want fast, repeatable practice.

Good options:

* [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — modern web app practice for web flaws and APIs
* [Metasploitable 2](https://sourceforge.net/projects/metasploitable/) and [Metasploitable 3](https://github.com/rapid7/metasploitable3) — intentionally vulnerable VMs for service enumeration and exploitation
* [DVWA](https://github.com/digininja/DVWA) — classic web app lab with adjustable difficulty

Run them in a local hypervisor such as VirtualBox or VMware.

### High-value walkthroughs and mentors

Use retired-box walkthroughs to compare methodology, not just copy steps.

Recommended references:

* [IppSec](https://www.youtube.com/@IppSec) — detailed retired-machine walkthroughs with strong troubleshooting habits
* [0xdf hacks stuff](https://0xdf.gitlab.io/) — text walkthroughs with strong post-root analysis and defensive context

### Next step after Academy-style study

Move into beginner-friendly live targets as soon as possible.

Start with Starting Point and guided Tracks on the Hack The Box platform.

Then practice on classic introductory machines such as `Lame`, `Nibbles`, `Shocker`, and `Jerry`.

These targets are useful for building comfort with outdated services such as Samba, Apache, and Tomcat.

### Key takeaway

Do not rely on one writeup for a retired machine.

Compare multiple walkthroughs for the same box.

Each operator uses different shortcuts, tooling, and decision rules.

That comparison helps you build your own style.
