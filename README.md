# OT Security One-Pagers

**One protocol. One sheet. Everything you need to attack it, defend it, and not get fooled by it.**

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/licence-CC%20BY%204.0-blue.svg" alt="Licence: CC BY 4.0"></a>
  <img src="https://img.shields.io/badge/sheets-19-brightgreen.svg" alt="19 sheets published">
  <img src="https://img.shields.io/badge/print-18%20%C3%97%2024%20in%20%40%20300%20dpi-orange.svg" alt="Print size 18 by 24 inches at 300 dpi">
  <img src="https://img.shields.io/badge/source-editable%20.pptx-lightgrey.svg" alt="Editable PPTX source included">
  <img src="https://img.shields.io/badge/commercial%20use-permitted-success.svg" alt="Commercial use permitted">
</p>

<p align="center">
  <a href="#find-your-sheet"><img src="./assets/series_banner.jpg" width="100%"
     alt="The tops of all nineteen OT Security One-Pager sheets, laid out by domain"></a>
</p>

You have a packet capture open, a protocol you half-remember, and no time to read a
four-hundred-page specification. **Each sheet is the one page you need: what the protocol is,
what every function code does to the physical process, how an attacker uses it, and the exact
filter that catches them.**

Nineteen industrial protocols — the grid, the PLC families, field instruments and safety
systems, building automation and smart meters — on the same ten-panel layout. Learn where to
look on one sheet and you know where to look on all of them.

> [!TIP]
> **New — November 2026: sixteen sheets in one drop**, from IEC-104 and IEC 61850 to TriStation,
> HART-IP and smart meters. **[Find yours →](#find-your-sheet)**

## Why people keep them open

- 🎯 **The one idea up front.** Every sheet opens with the single sentence that makes the
  protocol decode itself — *"Select and Execute are the same message, one bit apart."*
- 🔴 **Colour-coded by physical consequence.** Function codes are coloured by what they do to the
  plant (read, enumerate, set a value, operate a breaker, stop a CPU), not by what the
  specification calls them.
- 🟢 **Detection you can paste.** BPF, Zeek, Suricata and Wireshark syntax that lifts straight
  into a terminal or a rule file, plus the one highest-value query for that protocol.
- ⚠️ **The traps get their own callout.** The point index that names no breaker, the second
  identity your firewall never sees, the parser that silently is not installed.
- 📚 **Checked, not paraphrased.** Every Wireshark filter was tested against a real Wireshark
  build; every value is traced to a specification, dissector or vendor manual, named on the
  sheet.
- ✏️ **Editable and free to use.** The `.pptx` source is included, and the licence is CC BY 4.0,
  commercial use permitted.

## Find your sheet

### 🔌 By what you see on the wire

Port or EtherType in a capture, firewall log or Shodan result → the sheet that decodes it.

| You see | It is probably | Sheet |
|---|---|---|
| `502/tcp` | Modbus TCP | [Modbus](./Modbus/) |
| `44818/tcp`, `2222/udp` | EtherNet/IP + CIP | [CIP](./CIP/) |
| `20000/tcp` or `/udp` | DNP3 | [DNP3](./DNP3/) |
| `2404/tcp` | IEC 60870-5-104 | [IEC-104](./IEC104/) |
| `102/tcp` | **two candidates** — Siemens S7comm / S7comm-Plus, or IEC 61850 MMS; the S7comm sheet shows how to tell them apart | [S7comm](./S7comm/) · [61850 MMS](./IEC61850-MMS/) |
| EtherType `0x88B8` / `0x88BA` | IEC 61850 GOOSE / Sampled Values (R-GOOSE / R-SV ride UDP) | [GOOSE & SV](./IEC61850-GOOSE/) |
| `4712/tcp`, `4713/udp` | IEEE C37.118 synchrophasors | [C37.118](./C37.118/) |
| `9600/udp` or `/tcp` | Omron FINS | [FINS](./FINS/) |
| `48898/tcp`, `48899/udp` | Beckhoff ADS / AMS | [ADS / AMS](./ADS/) |
| EtherType `0x88A4` | EtherCAT (a panel on the ADS sheet) | [ADS / AMS](./ADS/) |
| EtherType `0x8892`, `34964/udp` | PROFINET RT / DCP, PNIO-CM | [PROFINET](./PROFINET/) |
| `4840/tcp` | OPC UA (`opc.tcp`) | [OPC UA](./OPCUA/) |
| `135/tcp` + dynamic RPC to an OPC server | OPC Classic / DA over DCOM (a panel on the OPC UA sheet) | [OPC UA](./OPCUA/) |
| `5094/tcp` or `/udp` | HART-IP | [HART-IP](./HART-IP/) |
| `1502/udp` | TriStation (Triconex safety controller) | [TriStation](./TriStation/) |
| `4000/tcp` or `/udp` | Emerson ROC Plus | [ROC Plus](./ROC-Plus/) |
| `47808/udp` (`0xBAC0`) | BACnet/IP | [BACnet](./BACnet/) |
| `1911/tcp`, `4911/tcp` | Niagara Fox (a panel on the BACnet sheet) | [BACnet](./BACnet/) |
| `3671/udp`, multicast `224.0.23.12` | KNXnet/IP | [KNXnet/IP](./KNX/) |
| `1153/tcp` or `/udp` | ANSI C12.22 smart meters | [ANSI C12.22](./C12.22/) |
| `4059/tcp` or `/udp` | DLMS/COSEM smart meters | [DLMS/COSEM](./DLMS/) |

Ports are conventions, not guarantees: gateways, serial converters and vendors move them. Each
sheet's panel 1 lists the variants, and its traps callout says what a non-standard port means.

### 🏭 By vendor or kit on site

| If the site runs… | Start with |
|---|---|
| Rockwell / Allen-Bradley (ControlLogix, CompactLogix) | [CIP](./CIP/) |
| Siemens (S7-300/400/1200/1500, TIA Portal, ET 200) | [S7comm](./S7comm/) · [PROFINET](./PROFINET/) |
| Schneider Electric (Modicon, Triconex) | [Modbus](./Modbus/) · [TriStation](./TriStation/) |
| Omron (Sysmac NJ/NX, CJ/CS) | [FINS](./FINS/) |
| Beckhoff (TwinCAT, EtherCAT) | [ADS / AMS](./ADS/) |
| Emerson (ROC800, FloBoss flow computers) | [ROC Plus](./ROC-Plus/) |
| Protection relays and RTUs (SEL, GE, Hitachi Energy, Siemens SIPROTEC) | [DNP3](./DNP3/) · [IEC-104](./IEC104/) · [61850 MMS](./IEC61850-MMS/) · [GOOSE & SV](./IEC61850-GOOSE/) |
| PMUs and phasor data concentrators (openPDC, SEL) | [C37.118](./C37.118/) |
| Smart transmitters, asset-management systems, WirelessHART gateways | [HART-IP](./HART-IP/) |
| Building management (Tridium Niagara, Johnson Controls, Honeywell) | [BACnet](./BACnet/) |
| Lighting, blinds and room control (KNX / ETS) | [KNXnet/IP](./KNX/) |
| Utility AMI head-ends and meters | [ANSI C12.22](./C12.22/) (North America) · [DLMS/COSEM](./DLMS/) (Europe and elsewhere) |
| Historians, MES and SCADA integration layers | [OPC UA](./OPCUA/) |

### 🦠 By incident, malware or advisory

When an advisory names a family, this is the sheet that shows what it did on the wire.

| Named in the advisory | What it used | Sheet |
|---|---|---|
| **Industroyer** (Kyiv, 2016) | IEC-104 module, IEC 61850 MMS module | [IEC-104](./IEC104/) · [61850 MMS](./IEC61850-MMS/) |
| **Industroyer2** (Ukraine, April 2022) | IEC-104 only, target IOAs compiled in | [IEC-104](./IEC104/) |
| **CosmicEnergy** (2023) | IEC-104 | [IEC-104](./IEC104/) |
| **TRITON / TRISIS** (2017) | TriStation, against a Triconex safety controller | [TriStation](./TriStation/) |
| **Stuxnet** (Natanz, 2010) | S7comm via a trojanised STEP 7 library | [S7comm](./S7comm/) |
| **FrostyGoop / BUSTLEBERM** (Lviv, January 2024) | Modbus TCP against heating controllers | [Modbus](./Modbus/) |
| **PIPEDREAM / INCONTROLLER** (2022) | Omron module over FINS, an OPC UA module, CODESYS reach | [FINS](./FINS/) · [OPC UA](./OPCUA/) · [ADS / AMS](./ADS/) |
| **2021 German building-automation lockout** (CVE-2023-4346) | KNX device keys set by an intruder | [KNXnet/IP](./KNX/) |

### 🧭 By the job in front of you

- **"I've been handed a PCAP."** Match ports and EtherTypes with the [wire table](#-by-what-you-see-on-the-wire),
  then go straight to panel 7 on that sheet: capture filter, parser, and the triage questions in
  order.
- **"I'm hunting in a substation."** [DNP3](./DNP3/) or [IEC-104](./IEC104/) for the SCADA link,
  [61850 MMS](./IEC61850-MMS/) for the station bus, [GOOSE & SV](./IEC61850-GOOSE/) for the process
  bus, [C37.118](./C37.118/) for wide-area monitoring.
- **"Is this command normal?"** Panel 8 (normal vs suspicious) on each sheet is the baseline,
  written for someone who has never seen the protocol before.
- **"I need detection content."** Panel 7 has paste-ready BPF, Zeek, Suricata and Wireshark syntax,
  and says plainly where a Zeek parser or Wireshark dissector does not exist, because a missing
  parser looks exactly like a quiet network.
- **"I'm writing the assessment report."** Panel 9 gives hardening controls and panel 10 the
  ATT&CK for ICS technique IDs, with the in-the-wild citation.
- **"I'm teaching an IT analyst OT."** Start with [Modbus](./Modbus/) (simplest), then [DNP3](./DNP3/)
  and [IEC-104](./IEC104/) as a matched pair. Practise against real captures in
  [ICS-PCAP-Challenges](https://github.com/SackOfHacks/ICS-PCAP-Challenges), which covers every
  protocol here.

## All nineteen sheets

Every sheet ships as an editable **PPTX**, a vector **PDF** for print and a 300 dpi **PNG** for
screens. **Preview** opens a quick 800 px look before you download.

| Sheet | Domain | The one idea | Get it |
|---|---|---|---|
| [**DNP3**](./DNP3/) | Grid | Select arms the point, Operate fires it — and neither message asks who you are | [PDF](./DNP3/DNP3_Attack_Defend_Poster.pdf) · [PNG](./DNP3/DNP3_Attack_Defend_Poster.png) · [PPTX](./DNP3/DNP3_Attack_Defend_Poster.pptx) · [preview](./assets/DNP3_Attack_Defend_Poster_thumb.jpg) |
| [**IEC-104**](./IEC104/) | Grid | Select and Execute are the same message, one bit apart | [PDF](./IEC104/IEC104_Attack_Defend_Poster.pdf) · [PNG](./IEC104/IEC104_Attack_Defend_Poster.png) · [PPTX](./IEC104/IEC104_Attack_Defend_Poster.pptx) · [preview](./assets/IEC104_Attack_Defend_Poster_thumb.jpg) |
| [**61850 MMS**](./IEC61850-MMS/) | Grid | Control is not a protocol verb — it is a Write to a named object | [PDF](./IEC61850-MMS/IEC61850_MMS_Attack_Defend_Poster.pdf) · [PNG](./IEC61850-MMS/IEC61850_MMS_Attack_Defend_Poster.png) · [PPTX](./IEC61850-MMS/IEC61850_MMS_Attack_Defend_Poster.pptx) · [preview](./assets/IEC61850_MMS_Attack_Defend_Poster_thumb.jpg) |
| [**GOOSE & SV**](./IEC61850-GOOSE/) | Grid | The subscriber obeys the highest state number it has seen | [PDF](./IEC61850-GOOSE/IEC61850_GOOSE_SV_Attack_Defend_Poster.pdf) · [PNG](./IEC61850-GOOSE/IEC61850_GOOSE_SV_Attack_Defend_Poster.png) · [PPTX](./IEC61850-GOOSE/IEC61850_GOOSE_SV_Attack_Defend_Poster.pptx) · [preview](./assets/IEC61850_GOOSE_SV_Attack_Defend_Poster_thumb.jpg) |
| [**C37.118**](./C37.118/) | Grid | A data frame is just numbers until CFG-2 names them — and CFG-2 is handed to anyone who asks | [PDF](./C37.118/C37118_Synchrophasor_Attack_Defend_Poster.pdf) · [PNG](./C37.118/C37118_Synchrophasor_Attack_Defend_Poster.png) · [PPTX](./C37.118/C37118_Synchrophasor_Attack_Defend_Poster.pptx) · [preview](./assets/C37118_Synchrophasor_Attack_Defend_Poster_thumb.jpg) |
| [**CIP**](./CIP/) | PLC | Every request is a `<SERVICE>` on a `<CLASS>:<INSTANCE>:<ATTRIBUTE>` | [PDF](./CIP/CIP_EtherNetIP_Attack_Defend_Poster.pdf) · [PNG](./CIP/CIP_EtherNetIP_Attack_Defend_Poster.png) · [PPTX](./CIP/CIP_EtherNetIP_Attack_Defend_Poster.pptx) · [preview](./assets/CIP_EtherNetIP_Attack_Defend_Poster_thumb.jpg) |
| [**Modbus**](./Modbus/) | PLC | Four data banks and one byte of intent — no users, no passwords, no sessions | [PDF](./Modbus/Modbus_Attack_Defend_Poster.pdf) · [PNG](./Modbus/Modbus_Attack_Defend_Poster.png) · [PPTX](./Modbus/Modbus_Attack_Defend_Poster.pptx) · [preview](./assets/Modbus_Attack_Defend_Poster_thumb.jpg) |
| [**S7comm**](./S7comm/) | PLC | The function byte is the whole exploit — `0x29` halts the CPU | [PDF](./S7comm/S7comm_Attack_Defend_Poster.pdf) · [PNG](./S7comm/S7comm_Attack_Defend_Poster.png) · [PPTX](./S7comm/S7comm_Attack_Defend_Poster.pptx) · [preview](./assets/S7comm_Attack_Defend_Poster_thumb.jpg) |
| [**FINS**](./FINS/) | PLC | Two bytes at a fixed offset — `04 02` stops the PLC, no password asked | [PDF](./FINS/Omron_FINS_Attack_Defend_Poster.pdf) · [PNG](./FINS/Omron_FINS_Attack_Defend_Poster.png) · [PPTX](./FINS/Omron_FINS_Attack_Defend_Poster.pptx) · [preview](./assets/Omron_FINS_Attack_Defend_Poster_thumb.jpg) |
| [**ADS / AMS**](./ADS/) | PLC | The route is the whole authentication | [PDF](./ADS/Beckhoff_ADS_Attack_Defend_Poster.pdf) · [PNG](./ADS/Beckhoff_ADS_Attack_Defend_Poster.png) · [PPTX](./ADS/Beckhoff_ADS_Attack_Defend_Poster.pptx) · [preview](./assets/Beckhoff_ADS_Attack_Defend_Poster_thumb.jpg) |
| [**PROFINET**](./PROFINET/) | PLC | The station name is the address — and it is a writable field | [PDF](./PROFINET/PROFINET_Attack_Defend_Poster.pdf) · [PNG](./PROFINET/PROFINET_Attack_Defend_Poster.png) · [PPTX](./PROFINET/PROFINET_Attack_Defend_Poster.pptx) · [preview](./assets/PROFINET_Attack_Defend_Poster_thumb.jpg) |
| [**OPC UA**](./OPCUA/) | PLC / integration | "Encrypted" is not "authenticated" — two independent switches, both commonly off | [PDF](./OPCUA/OPC_UA_Attack_Defend_Poster.pdf) · [PNG](./OPCUA/OPC_UA_Attack_Defend_Poster.png) · [PPTX](./OPCUA/OPC_UA_Attack_Defend_Poster.pptx) · [preview](./assets/OPC_UA_Attack_Defend_Poster_thumb.jpg) |
| [**HART-IP**](./HART-IP/) | Field | Command 40 freezes the 4-20 mA loop at a value the DCS believes | [PDF](./HART-IP/HART-IP_Attack_Defend_Poster.pdf) · [PNG](./HART-IP/HART-IP_Attack_Defend_Poster.png) · [PPTX](./HART-IP/HART-IP_Attack_Defend_Poster.pptx) · [preview](./assets/HART-IP_Attack_Defend_Poster_thumb.jpg) |
| [**TriStation**](./TriStation/) | Safety | The keyswitch is the only authentication the protocol has | [PDF](./TriStation/TriStation_Attack_Defend_Poster.pdf) · [PNG](./TriStation/TriStation_Attack_Defend_Poster.png) · [PPTX](./TriStation/TriStation_Attack_Defend_Poster.pptx) · [preview](./assets/TriStation_Attack_Defend_Poster_thumb.jpg) |
| [**ROC Plus**](./ROC-Plus/) | Oil & gas | Opcode 181 writes any parameter — including the flow constants custody transfer is billed on | [PDF](./ROC-Plus/ROC_Plus_Attack_Defend_Poster.pdf) · [PNG](./ROC-Plus/ROC_Plus_Attack_Defend_Poster.png) · [PPTX](./ROC-Plus/ROC_Plus_Attack_Defend_Poster.pptx) · [preview](./assets/ROC_Plus_Attack_Defend_Poster_thumb.jpg) |
| [**BACnet**](./BACnet/) | Building | Every write carries a priority — 1 beats the operator's 8 | [PDF](./BACnet/BACnet_Attack_Defend_Poster.pdf) · [PNG](./BACnet/BACnet_Attack_Defend_Poster.png) · [PPTX](./BACnet/BACnet_Attack_Defend_Poster.pptx) · [preview](./assets/BACnet_Attack_Defend_Poster_thumb.jpg) |
| [**KNXnet/IP**](./KNX/) | Building | A GroupValue_Write names a function, not a device — and carries no sender | [PDF](./KNX/KNXnetIP_Attack_Defend_Poster.pdf) · [PNG](./KNX/KNXnetIP_Attack_Defend_Poster.png) · [PPTX](./KNX/KNXnetIP_Attack_Defend_Poster.pptx) · [preview](./assets/KNXnetIP_Attack_Defend_Poster_thumb.jpg) |
| [**ANSI C12.22**](./C12.22/) | Metering | A Write is a procedure call — and one procedure opens the service switch | [PDF](./C12.22/ANSI_C1222_Attack_Defend_Poster.pdf) · [PNG](./C12.22/ANSI_C1222_Attack_Defend_Poster.png) · [PPTX](./C12.22/ANSI_C1222_Attack_Defend_Poster.pptx) · [preview](./assets/ANSI_C1222_Attack_Defend_Poster_thumb.jpg) |
| [**DLMS/COSEM**](./DLMS/) | Metering | Disconnecting a household is one ACTION — class 70, method 1 | [PDF](./DLMS/DLMS_COSEM_Attack_Defend_Poster.pdf) · [PNG](./DLMS/DLMS_COSEM_Attack_Defend_Poster.png) · [PPTX](./DLMS/DLMS_COSEM_Attack_Defend_Poster.pptx) · [preview](./assets/DLMS_COSEM_Attack_Defend_Poster_thumb.jpg) |

**Read them in pairs.** Four pairs cross-reference each other on purpose, so reading one makes
the other decode on sight: **DNP3 ↔ IEC-104** (North American and European grid SCADA),
**61850 MMS ↔ GOOSE & SV** (the two halves of one standard), **BACnet ↔ KNXnet/IP** (the two
building buses) and **ANSI C12.22 ↔ DLMS/COSEM** (North American and European metering).

## What's on every sheet

Ten panels, always in the same place, always in the same order:

| | Panel | | Panel |
|---|---|---|---|
| 🎯 | **The one idea** — the sentence that decodes the rest | 6 | **Attacker playbook** — discover → enumerate → manipulate → disrupt → cover tracks |
| 1 | **Where it lives** — variants, stack, ports, Purdue level | 7 | **Defender playbook** — capture, parse, detect, triage, the one query |
| 2 | **The data model** — what the protocol addresses, mapped to the process | 8 | **Normal vs suspicious** — the baseline |
| 3 | **The wire format** — the frame, field by field | 9 | **Hardening** — concrete controls and the standards behind them |
| 4 | **Function codes** — the full table, coloured by physical consequence | 10 | **ATT&CK for ICS** — technique IDs and what has been seen in the wild |
| 5 | **The high-value targets** — the two details an attacker goes looking for | ⚠️ | **Traps** — the ways analysts get this protocol wrong |

Laid out for **18 × 24 in at 300 dpi**: print one for the SOC wall or the control-room door. It
also reads fine on a monitor at 100% zoom, one panel at a time.

## Accuracy

Values are checked against primary sources: the published specification or vendor developers'
guide, protocol dissector source, and vendor programming manuals. Every Wireshark display filter
on a sheet was checked against the field list of Wireshark 4.6.10. Every Zeek reference says
whether the parser is mainline, a CISA/INL ICSNPP package, or absent. Malware and incidents are
named only where they genuinely used the protocol; where nothing has been seen in the wild, the
sheet says so and cites the defining research instead.

<details>
<summary><b>Sources, sheet by sheet</b></summary>

- **CIP** — the Wireshark ENIP/CIP dissectors, the ODVA developers guide, Rockwell's Logix 5000 Data Access manual.
- **Modbus** — the Wireshark Modbus dissector (`packet-mbtcp.c`), the Modbus Organization Application Protocol Specification v1.1b3.
- **DNP3** — IEEE 1815-2012, the DNP Users Group object library, the Wireshark DNP3 dissector, CISA/INL ICSNPP-DNP3.
- **IEC-104** — IEC 60870-5-104 and -101, IEC 62351-3/-5, the Wireshark `iec60870_104` / `iec60870_asdu` dissectors, the community ICSNPP-IEC104 parser.
- **61850 MMS / GOOSE & SV** — IEC 61850-7-2/-8-1/-9-2, IEC 61850-90-5, IEC 62351-6, ISO 9506, the Wireshark `mms`, `goose`, `sv` and `rgoose` dissectors.
- **C37.118** — IEEE C37.118.1/.2-2011, the Wireshark `synphasor` dissector, CISA ICSNPP-Synchrophasor.
- **S7comm** — the Wireshark `s7comm` / COTP / TPKT dissectors, ICSNPP-S7comm (including its S7comm-Plus tables, since Wireshark has no mainline S7comm-Plus dissector), Biham et al. "Rogue7" (Black Hat USA 2019).
- **FINS** — the Wireshark `omron` dissector, Omron W227, ICSNPP-Omron-FINS.
- **ADS / AMS** — the Wireshark `ams` and `ecat` dissectors, Beckhoff InfoSys, the ETG EtherCAT specification.
- **PROFINET** — the Wireshark `pn_dcp` / `pn_rt` / `pn_io` dissectors, the PI specification family, ICSNPP-PROFINET.
- **OPC UA** — OPC UA Parts 4 and 6, the Wireshark `opcua` dissector (service NodeIds checked against its value table).
- **HART-IP** — HCF_SPEC-085, the Wireshark `hart_ip` dissector, ICSNPP-HART-IP.
- **TriStation** — the Nozomi Networks TriStation dissector. There is no mainline Wireshark or Zeek parser, and the sheet says so.
- **ROC Plus** — the Emerson ROC Plus Protocol Specifications Manual via the CISA/INL ICSNPP-ROCplus parser. There is no mainline Wireshark dissector.
- **BACnet / KNXnet/IP** — ANSI/ASHRAE 135, the KNX Standard v2.1, the Wireshark `bvlc` / `bacnet` / `bacapp` and `knxip` / `cemi` dissectors, ICSNPP-BACnet (KNX has no Zeek parser).
- **ANSI C12.22 / DLMS/COSEM** — ANSI C12.22/C12.19/C12.18/C12.21, IEEE 1703/1377, IEC 62056 (Green and Blue Books), the Wireshark `c1222`, `dlms` and `cosem` dissectors, ICSNPP-C1222.

</details>

Spotted something wrong? **Open an issue with the source to check against, or send a PR.**
Corrections to hex values, service semantics and detection syntax are especially welcome.

## Not finding your protocol?

The set was checked against all 28 OT protocols in
[ICS-PCAP-Challenges](https://github.com/SackOfHacks/ICS-PCAP-Challenges). Several live as a
panel on the sheet they belong with, rather than on a sheet of their own.

<details>
<summary><b>Where the other protocols went, and why</b></summary>

| Protocol | Where it is | Why |
|---|---|---|
| S7comm-Plus | panel on **[S7comm](./S7comm/)** | same port, transport, discovery and defender syntax; the difference is one protocol-ID byte and the Rogue7 story |
| IEC 61850 Sampled Values, R-GOOSE / R-SV | on **[GOOSE & SV](./IEC61850-GOOSE/)** | same publisher/subscriber model and the same replay-and-injection attack class; R-GOOSE is GOOSE made routable |
| OPC DA (OPC Classic over DCOM) | panel on **[OPC UA](./OPCUA/)** | on the wire it is Windows DCE/RPC + DCOM, so the attack and defence story is Windows RPC, and OPC UA is its successor |
| EtherCAT | panel on **[ADS / AMS](./ADS/)** | a machine-level Layer-2 bus that nobody taps and no NSM parser covers; ADS is the routable way in |
| Niagara Fox | panel on **[BACnet](./BACnet/)** | proprietary, with no published specification; what can be verified is the banner and the exposure |
| Ethernet POWERLINK | no sheet | a machine-internal real-time bus with no IP routing, no NSM parser and no public threat history |
| LonTalk (ISO/IEC 14908) | no sheet | a declining building installed base, normally reached through a Niagara or BACnet gateway that has a sheet |
| LS XGT FEnet | no sheet | single-vendor and regional; open an issue if you run it |

</details>

**Next up**, in no fixed order: MELSEC / SLMP · CODESYS runtime · ICCP / TASE.2 · PCCC / DF1 ·
GE-SRTP · BSAP. [Open an issue](https://github.com/SackOfHacks/OT_Security_OnePagers/issues) to
push one up the list or nominate another. Requests decide what gets drawn next, and if a sheet
saved you an hour, a ⭐ is the other signal that reaches me.

## Use them, fork them, build on them

[**CC BY 4.0**](./LICENSE). Print them, hand them out, put them in a deck, take them into a
client engagement or a paid training room. The only condition is credit:

> OT Security One-Pagers — https://github.com/SackOfHacks/OT_Security_OnePagers — CC BY 4.0

If you extend or restyle a sheet, say what you changed. To add a sheet, drop
`<PROTOCOL>/<Name>_Attack_Defend_Poster.{pdf,png,pptx}` into a new directory, render an 800 px
thumbnail to `assets/<Name>_Attack_Defend_Poster_thumb.jpg`, add a row to the index and the
lookup tables, and bump the badge. Keep the ten-panel order: the layout only works if every
sheet keeps it.

> [!WARNING]
> **Lab and reference material.** Exercise the offensive content only against equipment you are
> authorised to test. OT protocol writes move physical process: a stop command is an outage, a
> coil write is an output changing state, a DNP3 Operate is a breaker, and anything written to
> a safety controller sits between a process upset and an injury.

<details>
<summary><b>Release log</b></summary>

| Date | What landed |
|---|---|
| 2026-11-20 | **Sixteen sheets**: IEC-104, S7comm & S7comm-Plus, Omron FINS, IEC 61850 MMS, IEC 61850 GOOSE & SV, OPC UA, Beckhoff ADS / AMS, BACnet, KNXnet/IP, PROFINET, HART-IP, TriStation, ROC Plus, ANSI C12.22, DLMS/COSEM and IEEE C37.118, all v1.0. README rebuilt around finding the right sheet |
| 2026-11-20 | CIP and DNP3 re-rendered: one callout on each ran past its border. Wording tightened, no technical value changed |
| 2026-09-21 | **DNP3 v1.0**: object library, three-sublayer frame anatomy, the CROB and the IIN |
| 2026-09-21 | Repo checks and a strict-allowlist `.gitignore` |
| 2026-09-12 | CC BY 4.0 licence |
| 2026-09-03 | **Modbus v1.0**: four data banks, function codes, FC 8 diagnostics, the 4xxxx addressing trap |
| 2026-08-15 | **CIP / EtherNet/IP v1.0**: service codes, object model, connection chain |

</details>
