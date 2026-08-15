# OT Security One-Pagers

**One protocol. One sheet. Everything you need to attack it, defend it, and not get fooled by it.**

Print-ready single-sheet references for OT/ICS protocols and the tradecraft around them —
built for the analyst mid-hunt, the responder with a packet capture open, and the assessor
standing in a plant with no second monitor and no internet.

<p align="center">
  <a href="./CIP/CIP_EtherNetIP_Attack_Defend_Poster.pdf">
    <img src="./CIP/CIP_EtherNetIP_Attack_Defend_Poster.png" width="720"
         alt="CIP / EtherNet/IP Attack &amp; Defend one-pager">
  </a>
  <br>
  <em>CIP / EtherNet/IP — click for the full-resolution PDF</em>
</p>

## The sheets

| Sheet | Protocol | Formats | Status |
|---|---|---|---|
| [**CIP**](./CIP/) | CIP / EtherNet/IP (ODVA) — service codes, object model, attack & defend | [PDF](./CIP/CIP_EtherNetIP_Attack_Defend_Poster.pdf) · [PNG](./CIP/CIP_EtherNetIP_Attack_Defend_Poster.png) · [PPTX](./CIP/CIP_EtherNetIP_Attack_Defend_Poster.pptx) | v1.0 |

More protocols land the same way. The layout is deliberately repeatable — read one sheet and
you know where to look on every sheet after it.

## What's on a sheet

Ten panels, always in the same order:

| # | Panel | What you get |
|---|---|---|
| 🎯 | **The one idea** | The single sentence that makes the rest of the protocol decode itself. For CIP: *"CIP is objects — every request is `<SERVICE>` on `<CLASS>:<INSTANCE>:<ATTRIBUTE>`."* |
| 1 | **Where it lives** | Spec volumes, encapsulation stack, ports, Purdue level |
| 2 | **The wire format** | The structure you actually have to decode, worked through a real example |
| 3 | **Session & connection chain** | How a conversation gets established — and where it isn't authenticated |
| 4 | **Service / function codes** | The full table, colour-coded by *what it does to the physical process*, not by what the spec calls it |
| 5 | **High-value objects** | What an attacker goes looking for, and why |
| 6 | **Attacker playbook** | discover → enumerate → establish → manipulate → disrupt → persist, mapped to the ICS Kill Chain |
| 7 | **Defender playbook** | Copy-pasteable BPF, Zeek, Suricata and Wireshark syntax, plus the triage logic behind them |
| 8 | **Normal vs suspicious** | The baseline — so the sheet works for someone who has never seen the protocol |
| 9–10 | **Hardening + ATT&CK for ICS** | Concrete controls and technique IDs |
| ⚠️ | **Traps** | The specific ways analysts get this protocol wrong, called out in their own panel |

## Formats

| File | Use it for |
|---|---|
| `.pptx` | Editable source of truth — fork it, restyle it, extend it |
| `.pdf` | Vector master for printing |
| `.png` | Screen use — wiki, slide embed, chat |

Laid out for **18 × 24 in at 300 dpi**. Also reads fine on a monitor at 100% zoom,
one panel at a time.

## How people use them

- 🖨️ **Print one** and tape it to the SOC wall or the control-room office door.
- 🔎 **Hunt with it** — the defender panel is written so the filters and detection syntax
  lift straight into a terminal or a rule file.
- 🎓 **Onboard with it** — hand it to an analyst who knows IT but not ICS and it will carry
  them through their first industrial packet capture.
- 🗣️ **Brief with it** — the attacker panel maps onto how an intrusion in that protocol
  actually unfolds, in the order it unfolds.

## Accuracy

Values are checked against primary sources: protocol dissector source code, the published
specification or vendor developers' guide, and vendor programming manuals. Sources are named
in the footer of every sheet. Where a technique has been seen in the wild, the malware family,
activity group or advisory is cited by name.

Spotted something wrong? **Open an issue with the source to check against, or send a PR.**
Corrections to hex values, service semantics and detection syntax are especially welcome —
so are requests for the next protocol.

## ⚠️ Use responsibly

Lab and reference material. Exercise the offensive content only against equipment you are
authorised to test. OT protocol writes move physical process — a stop command on a production
controller is an outage, not a finding.

## Licence

No licence file is set yet. Until one lands, treat these as all rights reserved: use them and
print them freely, and please ask before redistributing modified versions.
