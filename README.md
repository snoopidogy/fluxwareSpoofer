# 🚫 HWID Spoofer – Permanent Hardware ID Changer for Windows 🛠️  
![Platform](https://img.shields.io/badge/platform-windows-blue.svg)  
![License](https://img.shields.io/badge/license-educational-red.svg)  
![Language](https://img.shields.io/badge/language-C++-brightgreen.svg)

> ⚠️ **Disclaimer:** This tool is intended **strictly for educational and research purposes**.  
> Permanent spoofing of hardware identifiers may violate software terms or laws.  
> Use responsibly and ethically. Misuse is your sole responsibility.

---

## 📚 Overview

The **HWID Spoofer** is a powerful Windows tool that permanently changes your system’s hardware identifiers, including BIOS serials, motherboard info, disk volume IDs, and MAC addresses. It is designed for developers, security researchers, and students who want to understand how hardware binding works in licensing, anti-cheat, and system security.

---

## 🚀 Key Features

✅ Permanent spoofing of multiple hardware identifiers  
✅ Supports BIOS UUID & Serial modification  
✅ Baseboard (Motherboard) information patching  
✅ Disk Volume Serial number rewriting  
✅ MAC address change at the registry level (persistent after reboot)  
✅ Modular and extensible C++ codebase  
✅ Command-line interface with fine-grained spoof control  
✅ Detailed logs and debug output  

---

## 🔧 Spoofed Components

| Component           | Method Used                     | Persistence                  |
|---------------------|--------------------------------|-----------------------------|
| BIOS Serial         | WMI & Firmware Registry Patch  | Permanent (requires reboot) |
| Baseboard Info      | Registry & WMI Patch           | Permanent                   |
| Disk Volume ID      | Volume Serial rewrite           | Permanent                   |
| MAC Address         | Registry NDIS Driver Mod        | Permanent (reboot applied)  |
| CPU ID (emulated)   | Software Layer Override         | Permanent                   |

---

## 📦 Installation & Usage

1. Clone the repository:  
   ```bash
   git clone https://github.com/snoopidogy/fluxwareSpoofer.git
