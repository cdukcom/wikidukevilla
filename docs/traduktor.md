---
title: traDUKtor Lite manual
slug: /traduktor
sidebar_position: 3
description: Complete operating manual for traDUKtor Lite 0.2.31.
---

# traDUKtor Lite operational manual

![traDUKtor logo](/img/traduktor-logo.png)

**Current stable release:** `0.2.31`

**Reference hardware:** Olimex ESP32-POE-ISO-16MB-IND
**Manual scope:** installation, Translation, MESH WiFi, configuration, maintenance, backup, recovery, and troubleshooting.

[Download the PDF manual](/downloads/traduktor/traDUKtor_Lite_Operational_Manual_0.2.31.pdf)

:::info Living manual
This page is the current public manual. It is updated in place when validated behavior changes. The PDF records the stable release represented by this edition.
:::

## Product overview

traDUKtor Lite is a site-local protocol translator and controlled device-utility appliance. It translates approved industrial protocols and acts as the execution agent for Fácil IoT while keeping device credentials and vendor-specific commands at the site.

Only one primary application runs at a time:

- **Translation** runs up to five protocol-conversion lines.
- **MESH WiFi** reserves the runtime for Fácil IoT orchestration and Terminal Unit management.

Changing mode preserves the inactive application's saved configuration but stops its runtime services.

## First access and sign-in

Connect traDUKtor to a PoE network and open its management address. After factory reset, direct recovery uses `192.168.20.250/24`; configure the administration computer in the same subnet.

Sign in with an individual administrator account. Replace the default credential during commissioning. **Logout** closes the current session.

## Interface map

| Area | Views | Purpose |
| --- | --- | --- |
| Dashboard | System Status, Lines, MESH WiFi, Mgmt & VPN | Live operational evidence |
| Translation | Protocols, Lines | Operating mode, profiles, and protocol flows |
| MESH WiFi | Status and operating mode | Fácil IoT coordination and Terminal Units |
| Configuration | System, Network, Users, MQTT management | Persistent appliance settings |
| Maintenance | Firmware and files, Tools, Backup and files | Lifecycle, diagnostics, and recovery |

An unavailable or stopped value is never inferred. A green badge confirms only the check named by that badge.

## Dashboard

### System Status

- **Operational** means the web application and core runtime respond.
- **Auto-refresh every 10 seconds** updates live values without changing settings.
- **System** shows hostname, serial, firmware, uptime, time synchronization, and event count.
- **Ethernet** shows controller, link, address mode, MAC, IP, subnet, and gateway.
- **Restart diagnostics** identifies the last reset reason and current uptime.

### Lines

This view summarizes the five translation slots, their endpoints, saved state, runtime state, and counters. A saved line carries no traffic until it is **Running**.

### MESH WiFi

When MESH WiFi is active, the dashboard shows:

- authenticated **Management channel** to Fácil IoT;
- exclusive **Device mode**;
- local **Orchestration readiness**;
- persistent **Terminal Units** inventory.

Terminal Unit columns include name, serial, IP, configured manufacturer, detected model/part number, firmware, IP status, and Telnet management. IP reachability and authenticated Telnet are independent.

### Mgmt & VPN

This view reports the management uplink independently from optional VPN transport. Check destination, route, DNS, time/certificate prerequisites, and authenticated connection. A reachable broker is not necessarily an authenticated broker session.

## Translation

### Protocols

**Enable Translation** selects Translation as the primary application and stops MESH WiFi. Disabling it stops all lines but preserves profiles.

| Protocol | Principal profile settings |
| --- | --- |
| MQTT | Broker, port, TLS, client identity, username/password, publish/subscribe topics, QoS |
| Telnet | Remote host, TCP port, session role, bounded connection behavior |
| SSH | Host, port, username/password, client or server role |
| Modbus TCP | Client destination or local server endpoint, unit and mapping context |
| HTTP REST | URL, method, content behavior, request timing |

Profiles are reusable. Password fields are write-only; blank retains the saved secret. Stop every dependent line before changing a profile.

### Lines

1. Select **Create line** in an empty slot.
2. Enter **Line name**.
3. Select **Input protocol** and **Input profile**.
4. Select **Output protocol** and **Output profile**.
5. Save while stopped.
6. Start and verify state and counters.

Use **Stop** before editing or deleting. Delete removes the line, not shared profiles. If a line fails, check mode, line state, Ethernet/gateway/DNS, both profiles, remote services, credentials, TLS time, and the event log.

## MESH WiFi

### Architecture and operating mode

The validated path is:

1. Fácil IoT to traDUKtor through authenticated MQTT over TLS.
2. traDUKtor directly to Terminal Units through Telnet.

**Enable MESH WiFi** stops Translation and its running lines. It is unavailable until **Managed by Fácil IoT** is configured and connected. MESH WiFi reserves the profiles and capacity needed for orchestration.

### Fácil IoT coordination

Enter the Fácil IoT host/IP and port. The factory serial identifies traDUKtor; authorize that serial in Fácil IoT first. The management credential is separate from all Terminal Unit credentials.

### Persistent Terminal Units

Fácil IoT synchronizes up to ten desired records. Each record contains name, serial, manufacturer hint, management IP, Telnet user, and Telnet password. traDUKtor retains inventory across restarts and reports configured identity separately from detected evidence.

The selected manufacturer is a hint. A vendor adapter validates the response and reports manufacturer, model, firmware, and serial. A mismatch requires explicit review in Fácil IoT.

### Astra Wireless utility set

The stable vendor adapter is Astra Wireless. Bounded utilities collect identity, health, complete paginated `config show`, interfaces, routing, MINT/MESH, switching, ACL, firewall, NAT, DHCP, WiFi, and LLDP evidence.

Remote commands through the Headend may accelerate neighbor observation. Configuration writes use a direct target Telnet session whenever possible and require target-specific verification.

### Captive access status

The runtime can list quarantined clients and temporary approvals. Quarantine blocks navigation; an approval allows the displayed client for the displayed interval. These states support the future captive-portal policy and do not replace final routing/firewall rules.

## Configuration

### System

Configure hostname and local identity. Factory serial is read-only. Restart when the interface says that a saved change requires it.

### Network

Select DHCP or static IPv4 and configure address, prefix, default gateway, and DNS. Use one valid default gateway. Keep recovery access while changing the management path.

### Users

Create or update unique local users. New passwords contain 10 to 63 characters. The current administrator password authorizes access changes.

### MQTT management

Configure management enablement, broker, port, TLS trust, and the appliance credential issued by Fácil IoT. Confirm synchronized time, save, and verify **Connected**. Never install a broker private key or CA private key on traDUKtor.

## Maintenance

### Firmware and files

- **Last Release** checks signed `stable` firmware.
- **Last Beta** checks signed `lab` firmware.
- **Install** verifies application, hardware, channel, version, length, SHA-256, and ECDSA signature before writing the inactive bank.
- **Rollback to previous firmware** changes bank and restarts; saved configuration, passwords, and certificates remain.
- **Manual firmware upload** accepts a signed compatible binary.

Keep power and Ethernet connected. After restart, confirm the active bank is **Validated**.

### Tools

Run bounded ping, DNS, route, connectivity, time, and service diagnostics. Sanitize output before external sharing.

### Backup and files

- **Replication template** exports reusable behavior without identity, management network, or secrets. Import leaves lines and MESH stopped.
- **Configuration backup** preserves appliance-specific settings without exporting secrets. Preview before restore.
- **System radiography** exports sanitized identity, firmware, reset, network, service, and event evidence for support.

Review all imported settings before restart or service activation.

### Restart and factory reset

**Restart** retains data and applies saved configuration. **Restore factory settings** erases configuration, accounts, and secrets, then returns to `192.168.20.250/24`.

:::danger Factory reset
Factory reset is destructive. Confirm recovery connectivity and an approved backup before continuing.
:::

## Stable update acceptance

1. Record version, bank, IP, and mode.
2. Check **Last Release** and verify the offered version.
3. Install to the inactive bank.
4. Verify restart, Ethernet, time, MQTT, and selected mode.
5. Verify retained lines or Terminal Unit inventory.
6. Test one real translation flow or Telnet-managed Terminal Unit.
7. Confirm the new bank is validated and rollback remains available.

## Level 3 safety contract

A Headend or Access template is a target, not an assumption. A safe job reads and retains current state, establishes management first, calculates an ordered allow-listed plan, applies it, verifies interfaces/routes/services, and stops or restores on failure. The browser never submits arbitrary vendor CLI.

## Security checklist

- Use stable firmware unless a controlled test requires beta.
- Use unique users and device credentials.
- Never expose plaintext MQTT or Terminal Unit Telnet to the Internet.
- Keep time synchronized for TLS.
- Back up before network, mode, firmware, or radio changes.
- Do not power off during firmware write, restart, or factory reset.
- Never publish credentials, private addresses, or unsanitized radiography.

## Support information

Provide serial, firmware, active bank, reset reason, operating mode, approximate failure time, and sanitized system radiography. Never include passwords, tokens, or private keys.
