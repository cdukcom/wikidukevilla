---
title: traDUKtor Lite manual
slug: /traduktor
sidebar_position: 3
description: Complete operating manual for traDUKtor Lite 0.2.32.
last_update:
  date: 2026-11-06
  author: DukeVilla
---

# traDUKtor Lite operational manual

![traDUKtor logo](/img/traduktor-logo.png)

[Español](/docs/es/traduktor) | English

[Family brochure (English)](https://www.duke-villa.com/api/datasheets/datasheets%2Fen%2Ftraduktor%2FtraDUKtor_Family_Brochure.pdf) · [Ficha de familia (Español)](https://www.duke-villa.com/api/datasheets/datasheets%2Fes%2Ftraduktor%2FBrochure_Familia_traDUKtor.pdf)

**Current stable release:** `0.2.32`

**Reference hardware:** Olimex ESP32-POE-ISO-16MB-IND
**Manual scope:** installation, Translation, DVRCP, configuration, maintenance, backup, recovery, and troubleshooting.

**Living manual:** this online page is the current operational reference. It is updated in place.

:::info Living manual
Use this page for current procedures. Software releases link here; separate versioned manual copies are not maintained.
:::

## Product overview

traDUKtor Lite is a site-local protocol translator and controlled device-utility appliance. It translates approved industrial protocols and acts as the execution agent for Fácil IoT while keeping device credentials and vendor-specific commands at the site.

Only one primary application runs at a time:

- **Translation** runs up to five protocol-conversion lines.
- **DVRCP** reserves the runtime for Fácil IoT orchestration and Terminal Unit management.

Changing mode preserves the inactive application's saved configuration but stops its runtime services.

## First access and sign-in

Connect traDUKtor to a PoE network and open its management address. After factory reset, direct recovery uses `192.168.20.250/24`; configure the administration computer in the same subnet.

Sign in with an individual administrator account. Replace the default credential during commissioning. **Logout** closes the current session.

## Interface map

| Area | Views | Purpose |
| --- | --- | --- |
| Dashboard | System Status, Lines, DVRCP, Mgmt & VPN | Live operational evidence |
| Translation | Protocols, Lines | Operating mode, profiles, and protocol flows |
| DVRCP | Status and operating mode | Fácil IoT coordination and Terminal Units |
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

### DVRCP

DVRCP provides the control workflow for remotely configuring **compatible access equipment** from Fácil IoT through traDUKtor. Fácil IoT defines inventory, desired configuration and approved actions; traDUKtor executes supported operations locally through validated device adapters and returns observed results. It is independent of a particular equipment brand, but support must be validated for the model, firmware and adapter. It does not make an arbitrary IP device compatible automatically.

![Generic DVRCP management architecture](/img/dvrcp-access-en.svg)

WiFi is optional. When the managed equipment provides WiFi and the validated integration supports captive access, its portal can be enabled and configured from Fácil IoT. Network functions and access enforcement remain on the equipment. A routed access network can operate without a captive portal.

When DVRCP is active, its status tab shows:

- authenticated **Management channel** to Fácil IoT;
- exclusive **Device mode**;
- local **Orchestration readiness**;
- persistent **Terminal Units** inventory.

Terminal Unit columns include name, serial, management IP, route/output, next hop, manufacturer, model, firmware, and the three states **IP**, **Mgmt**, and **Internet**. The inventory section below explains each state and the autonomous five-minute scan.

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

## DVRCP

DVRCP provides the control workflow for remotely configuring **compatible access equipment** from Fácil IoT through traDUKtor. Fácil IoT defines inventory, desired configuration and approved actions; traDUKtor executes supported operations locally through validated device adapters and returns observed results. It is independent of a particular equipment brand, but support must be validated for the model, firmware and adapter. It does not make an arbitrary IP device compatible automatically.

![Generic DVRCP management architecture](/img/dvrcp-access-en.svg)

WiFi is optional. When the managed equipment provides WiFi and the validated integration supports captive access, its portal can be enabled and configured from Fácil IoT. Network functions and access enforcement remain on the equipment. A routed access network can operate without a captive portal.

### Architecture and operating mode

Fácil IoT defines the assigned inventory and desired device configuration. traDUKtor executes site-local utilities through the enabled, validated device adapter and reports results through authenticated MQTT over TLS. The routed-network workflow includes reading, comparing, applying, saving, and verifying supported templates. Headend and Access roles apply only when the selected device profile implements that topology.

**Enable DVRCP** stops Translation and its running lines without deleting their saved configuration. It is available after **Managed by Fácil IoT** is configured and connected. The installed device adapter can be enabled or disabled under DVRCP; disabling it stops its device-specific operations without deleting the retained inventory. The Fácil IoT application is named **MESH WiFi**; the local execution service is named **DVRCP**.

### Fácil IoT coordination and commissioning order

Enter the Fácil IoT host/IP and port, and authorize the factory serial in Fácil IoT. The MQTT identity is separate from TU Telnet credentials. In Fácil IoT, enable MESH WiFi, add the registered manager, and commission node 1 as Headend before Access nodes 2 through 10. The validated routed profile supports up to ten compatible units per traDUKtor: one Headend and up to nine Access units. Do not assume this topology or every operation is supported by a different device profile.

Use the [Fácil IoT first-time routed-network procedure](/docs/facil-iot#mesh-wifi-first-routed-network-setup) for the complete menu sequence. Compare each target with the observed device, apply required changes, wait for verification, and accept with **Finish**. Saving a desired role plan alone does not configure the device.

### Persistent inventory and autonomous checks

Open **Dashboard > DVRCP**, then **Terminal Units**, to inspect the retained inventory. traDUKtor checks assigned TUs at startup and normally every **300 seconds (5 min)**. It updates reachable TUs with current IP, authenticated management, identity, addressing, and device-level Internet results. It executes one bounded Internet ping on each reachable, managed TU using the device's normal route; it does not require a separate Internet test from every interface.

A TU that becomes unreachable remains listed. Its last known name, serial, manufacturer, model, firmware, and management address are retained rather than erased by an incomplete observation. Current reachability and management evidence are reported separately from historical metadata. Fácil IoT explicitly synchronizes additions, changes, and removals; an offline device is not a deletion request.

| Column | Meaning |
| --- | --- |
| Name / Serial | Assigned equipment identity, reconciled with the detected device. |
| Management IP | Address traDUKtor uses to reach that TU. |
| Route / Output | Actual lookup: directly connected, specific route, or default route, and outgoing interface. |
| Next hop | Next address used to reach the target; for a direct target, the target itself. |
| Manufacturer / Model / Firmware | Last observed equipment identity and software. |
| IP | OK after a successful reachability check; Unreachable when there is no reply; Awaiting before evidence is available. |
| Mgmt | OK after management succeeds; Awaiting when management has not succeeded or IP is unavailable. |
| Internet | OK after the TU's normal-route Internet test succeeds; Unreachable after failure; Awaiting when no current test can be completed. |

Mgmt uses the authenticated Telnet result, rather than requiring a second ping back to traDUKtor. Internet indicates reachability from the TU itself; it does not certify browsing from every client subnet or captive-portal enforcement. A manufacturer mismatch requires explicit review in Fácil IoT before configuration writes.

### Inventory utility and temporary live refresh

The DVRCP inventory utility returns a consolidated snapshot of retained TUs, current health evidence, management paths, and routes. Fácil IoT uses that response to build its Routing diagram instead of scheduling separate per-interface diagnostic jobs for every screen refresh.

Fácil IoT requests one snapshot automatically when Routing is opened or a manager is selected. With **Refresh** unchecked it keeps that view fixed; traDUKtor still performs its normal five-minute local scan. Enabling Refresh requests a temporary interval of **10 s, 30 s, 1 min, or 5 min**. Disabling it, leaving Routing, or closing the browser releases the temporary request. If the browser disappears unexpectedly, its request expires and normal scanning resumes. Closing the view does not delete any inventory or routes.

### Permanent return routes - destination-specific routing

traDUKtor installs specific destination networks through **Headend eth0** while preserving its independently configured default gateway. This is the routed-network path used by the stable release. The Headend routes Access traffic and provides the Internet exit through NAT on eth0.

Fácil IoT sends the confirmed routing plan after Headend commissioning and updates it as Access configurations are confirmed. Installed routes are stored compactly and persist across power loss, restarts, and loss of Fácil IoT. They remain until an explicit controller update changes or withdraws them; inventory refresh sessions do not own these permanent routes.

Check the reported storage state. A route active only in memory is not yet confirmed permanent. A saved acknowledgement confirms persistence; diagnose a storage error before relying on restart recovery. **Configuration > Network** changes to management IP or gateway are saved separately and require a reboot as stated by the interface. Save successfully before rebooting.

### Device adapters and safe configuration

The validated device adapter exposes the capabilities supported by that equipment. These can include identity, health, configuration, interfaces, routing, switching, ACL, firewall, NAT, DHCP, WiFi and neighbor evidence. Do not assume that every adapter exposes every utility. Configuration writes use allow-listed operations and target-specific verification. Detection alone never authorizes a write.

Progress is reported while a reviewed configuration is applied and verified. In Fácil IoT, **Finish** confirms the completed session. **Cancel** offers a rollback of items with known original values and identifies items that will retain their new values. Do not assume an unobserved original value can be reconstructed.

### Optional captive access

A complete routed network works without a captive portal. Captive Portal is off by default, and its global activation and policy setup belong to the next commissioning stage. Enable and configure captive policies from Fácil IoT only after confirming device and adapter support. Existing experimental client restrictions must not be confused with an already commissioned captive service. Device-level IP, Mgmt, and Internet checks do not validate client authorization.

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
