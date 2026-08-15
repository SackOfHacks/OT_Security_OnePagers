# OT Security One-Pagers

Print-ready single-sheet references for OT/ICS protocols and the tradecraft around them.

Each one-pager takes a single protocol and puts the whole thing on one sheet: how it is
framed on the wire, what an attacker does with it, what a defender captures and matches
on, and how to tell routine traffic from the traffic that should start a ticket. The
audience is the person who needs the protocol detail at a glance — the analyst mid-hunt,
the responder on a bridge call, the assessor in a plant with no second monitor and no
internet — rather than someone with time to work through a 400-page specification.

## Contents

| Sheet | Protocol | Status |
|---|---|---|
| [CIP](./CIP/) | CIP / EtherNet/IP (ODVA) — service codes, object model, attack & defend | v1.0 |

More protocols are added the same way; the layout below is deliberately repeatable.

## What each one-pager gives you

Every sheet is built on the same skeleton, so once you have read one you know where to
look on the next:

- **One organising idea**, stated at the top — the sentence that makes the rest of the
  protocol decode itself. For CIP it is *"CIP is objects: every request is `<SERVICE>` on
  `<CLASS>:<INSTANCE>:<ATTRIBUTE>`."*
- **Where it lives** — specification volumes, encapsulation stack, ports, Purdue level
- **The wire format** — the structure an analyst actually has to decode, worked through
  a real example rather than described abstractly
- **The function/service reference** — the full table, colour-coded by what each one does
  to the physical process, not by what the specification calls it
- **Attacker playbook** — discover → enumerate → establish → manipulate → disrupt →
  persist, mapped to the ICS Kill Chain
- **Defender playbook** — copy-pasteable BPF, Zeek, Suricata and Wireshark syntax, plus
  the triage logic that turns a match into a disposition
- **Normal vs suspicious** — the baseline, so the sheet is usable by someone who has
  never seen the protocol before
- **Hardening** and **ATT&CK for ICS** technique mapping
- **Traps** — the specific ways analysts get this protocol wrong, called out in their own
  panel

## Files and formats

Each protocol directory carries the same three artifacts:

| Extension | Role |
|---|---|
| `.pptx` | Editable source and the source of truth — change, rebrand, extend |
| `.pdf` | Vector master for printing |
| `.png` | Screen use — wiki, Confluence, slide embed, chat |

Sheets are laid out for **18 × 24 in** at 300 dpi and also read fine on a monitor at
100% zoom, one panel at a time.

## How to use them

- **Print one** and put it on the wall of the SOC or the control-room office.
- **Hunt with it** — the defender panel is written so the capture filters and detection
  syntax can be lifted straight into a terminal or a rule.
- **Onboard with it** — hand it to an analyst who knows IT but not ICS, and it will get
  them through their first packet capture.
- **Brief with it** — the attacker panel maps cleanly onto how an intrusion in that
  protocol actually unfolds.

## Sourcing and accuracy

Values on these sheets are checked against primary sources — protocol dissector source
code, the specification or vendor developers' guide, and vendor programming manuals —
and the sources are named in the footer of each sheet. Where a technique has been seen in
a real intrusion, the malware family, activity group or advisory is cited. If you find
an error, an issue or a PR with the source to check against is welcome.

## Scope and use

Lab and reference material. Exercise the offensive content only against equipment you
are authorised to test — OT protocol writes move physical process, and a stop command on
a production controller is an outage, not a finding. These sheets contain no client data
and no material from any engagement.


## Licence

No licence file is set yet. Until one is added, treat these as all-rights-reserved:
use and print them freely, and ask before redistributing modified versions.
