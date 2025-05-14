# SYN Flood Tool

A simple Python-based tool to perform a basic SYN flood attack for educational and testing purposes.

> ⚠️ **Disclaimer**: This tool is intended for authorized security testing and educational use only. Unauthorized use against systems you do not own or have explicit permission to test is illegal and unethical.

---

## 🚀 Features

- Randomized source IP addresses and ports
- Packet crafting using Scapy
- Customizable target IP, port, and packet count

---

## 🛠 Requirements

- Python 3.x
- [Scapy](https://scapy.readthedocs.io/)

Install dependencies:

```bash
pip install scapy
```

> On some systems, you may need administrative/root privileges to send raw packets.

---

## ⚙️ Usage

Run the script:

```bash
python syn_flood_tool.py
```

Follow the interactive prompt:

- Enter the target IP address
- Enter the target port
- Enter the number of packets to send

---

## 📁 File Structure

```
syn_flood_tool.py  # Main script
README.md          # Project documentation
LICENSE            # MIT License
```

---

## 🧪 Example Output

```text
[*] 목표의 IP : 192.168.1.10
[*] 목표의 Port : 80
[*] 보낼 패킷의 갯수 : 100
공격 실행...

[*] 전체 송신 패킷 수 : 100
```

---

## 🙋 Author

- Email: gump71036969@gmail.com

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
