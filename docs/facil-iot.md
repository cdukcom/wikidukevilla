---
title: Fácil IoT manual
slug: /facil-iot
sidebar_position: 4
description: Complete operating manual for Fácil IoT 0.1.19.
last_update:
  date: 2026-11-06
  author: DukeVilla
---

# Fácil IoT operational manual

![Fácil IoT logo](/img/facil-iot-logo.png)

[Español](/docs/es/facil-iot) | English

[Family brochure (English)](https://www.duke-villa.com/api/datasheets/datasheets%2Fen%2Ffacil-iot%2FFacil_IoT_Family_Brochure.pdf) · [Ficha de familia (Español)](https://www.duke-villa.com/api/datasheets/datasheets%2Fes%2Ffacil-iot%2FBrochure_Familia_Facil_IoT.pdf)

**Current stable release:** `0.1.19`

**Reference appliance:** Protectli FW7225
**Manual scope:** operation, communities, devices, alarms, licenses, integrations, MESH WiFi, configuration, maintenance, and recovery.

**Living manual:** this online page is the current operational reference. It is updated in place.

:::info Living manual
Use this page for current procedures. Software releases link here; separate versioned manual copies are not maintained.
:::

## Product overview

Fácil IoT is a local-first control plane for communities, Sites, gateways, sensors, alarms, licenses, maps, integrations, and MESH WiFi. Local operation remains available during an Internet or central-service outage. Every displayed status must come from a live or persisted source; unavailable evidence is never replaced with sample data.

### Management architecture

- Fácil IoT provides the web interface, API, database, MQTT control plane, and signed lifecycle.
- Gateways and traDUKtors authenticate with unique MQTT identities and least-privilege topics.
- traDUKtor executes site-local Terminal Unit utilities and retains device secrets locally.
- The browser never receives signing keys, database access, or arbitrary radio command execution.

## Sign-in and navigation

Sign in with an individual account. Sessions expire after 30 minutes without pointer, keyboard, touch, or scroll activity. **Log out** closes the session.

The left navigation contains **Dashboard**, **Communities**, **Devices**, **Alarms**, **Maps**, **Licenses**, **Users**, **Integrations**, **MESH WiFi**, **Maintenance**, and **Settings**. Search and filters act on the current page only.

## Dashboard

Dashboard is the operational starting point.

- Summary cards show registered devices, online devices, devices with telemetry, and active alarms.
- **Operational status** shows installed release, management interface/IP, uptime, boot time, reset reason, hostname, and hardware.
- **Operational map** plots only persisted coordinates.
- **Alarms and event log** lists real events.
- **Recent devices** shows the latest real telemetry or a truthful offline state.

Use Dashboard after every update, restart, or network change.

## Communities

Communities are the top-level administrative and licensing boundary. Search and status filters narrow the list. Creation and editing record organization context, contact/location information where enabled, status, and notes.

A community contains Sites, users, devices, gateways, licenses, services, integrations, alarms, traDUKtors, and MESH nodes. Deactivation preserves history. Sites provide the physical or logical location used by devices and MESH equipment.

## Devices

The tabs separate hardware classes. **Refresh** retrieves live backend state; **Online only** hides assets without current evidence.

### LoRaWAN

Register hardware identity, approved model/profile, community, Site, and optional coordinates. License entitlement and radio connectivity are independent. Online state requires an uplink or heartbeat.

### BLE

Register the approved profile and unique hardware identifier. A gateway observation supplies telemetry but does not change ownership or Site assignment.

### Gateways

Register EUI, community/Site, enabled LoRaWAN/BLE services, and unique MQTT enrollment. Each service reports status independently. Editing metadata does not silently rotate credentials.

### traDUKtors

Register name, factory serial, community, management IP, MQTT management enablement, and MESH WiFi permission.

- **Check IP** performs platform-side reachability only.
- **Management OK** requires recent authenticated MQTT evidence.
- MESH work requires both management and MESH permission.

### Terminal Units

Register name, community, Site, manufacturer, serial, management IP, Telnet username/password, and assigned traDUKtor. Select the validated adapter for the equipment model and firmware. A manufacturer field or an IP address alone does not establish compatibility or authorize configuration writes.

The page separates **Configured** identity from **Detected** manufacturer, model, firmware, and serial. **Review** is enabled for mismatches. Confirm only after checking the equipment. Credentials are write-only and synchronized securely to the assigned traDUKtor.

## Alarms

The page summarizes open conditions and lists severity, alarm, community, state, and detection time.

- **Acknowledge** records operator awareness.
- **Resolve** closes the alarm with an audit event.
- **New route** creates notification automation.

### Notification routes

A route contains community, name, integration, recipient, optional sensor, comma-separated event types, severities, message template, and enablement. Empty sensor, event, or severity selections mean any matching value. Deleting a route does not delete its integration or alarm history.

## Maps

Maps uses OpenStreetMap and shows only verified stored coordinates. The legend distinguishes online, offline, and pending discovery. If tiles are unavailable, coordinates remain stored and the interface states that the background is unavailable.

## Licenses and services

Licenses are assigned by community and technology. LoRaWAN and BLE capacity, use, and validity are independent. Renewable services record service status and dates. A valid license authorizes use; it does not prove connectivity.

## Users

**New user** requests:

- **User**: starts with a lowercase letter and uses lowercase letters, numbers, period, underscore, or hyphen.
- **Role**: Administrator or Monitoring.
- **Display name** and optional **Email**.
- **Password**: at least 12 characters.

Administrators configure and maintain the appliance. Monitoring users have restricted operational access. **Delete** removes local access after confirmation.

## Integrations

Platform integrations show internal service state. Community integrations connect approved external services. Depending on provider, configure name, type, endpoint/account context, write-only secret/token, enablement, and community.

An enabled integration still needs a successful health check and a route or workflow. Gateway and traDUKtor MQTT identities remain per-device and are not replaced by a general integration.

## DVRCP remote access-device management

Fácil IoT centrally configures compatible access equipment through traDUKtor and DVRCP. It stores the assigned inventory and desired configuration, presents observed state for review, submits approved operations and displays verification results. traDUKtor executes the supported device operations locally through the validated adapter; network processing remains on the managed equipment.

![Generic DVRCP management architecture](/img/dvrcp-access-en.svg)

This workflow is not tied to a particular equipment brand. Compatibility and available actions depend on the model, firmware and adapter. When compatible equipment provides WiFi and captive-access support, its portal can be enabled and configured from Fácil IoT. WiFi and captive portals are optional; neither is required for basic remote device configuration.

## MESH WiFi: first routed-network setup

Fácil IoT defines the network and traDUKtor manages the assigned compatible access devices, called Terminal Units (TUs) in the interface, locally through DVRCP and the validated adapter. The following Headend/Access procedure applies to the routed profile that supports those roles. A routed MESH network can operate permanently **without a captive portal**. Captive Portal is optional and off by default; its activation and configuration are a separate commissioning stage.

Each traDUKtor supports a maximum of **10 Terminal Units: one Headend and nine Access units**. Commission the Headend first, verify it, and then commission the Access units. The Headend supplies the routed Internet exit and NAT through eth0. traDUKtor retains its own default gateway and installs specific return routes through the Headend.

### Before you start

Prepare the community and site, a registered traDUKtor with working authenticated MQTT management, and compatible access devices with a validated adapter, known management addresses and the credentials required by that adapter. Confirm that traDUKtor can initially reach the Headend on its management network. A route to a remote Access network cannot establish itself before its Headend path exists.

Use the current stable software on both products. Registration and role assignment are different operations: **Devices** registers equipment and its management settings; **MESH WiFi** assigns that equipment to the application and commissions its role. A detected identity mismatch must be reviewed before applying configuration.

### Step 1: Global - enable the application

1. Open **MESH WiFi**, then **Global**.
2. Enable the MESH WiFi service and click **Apply**.
3. Confirm that the application is enabled before proceeding to equipment selection.

Global controls the application. It does not replace the individual traDUKtor MQTT enrollment or automatically enable captive restrictions.

### Step 2: MESH traDUKtors - select local managers

1. Register and authorize the traDUKtor under **Devices > traDUKtors** if it is not already present. Complete its MQTT management setup.
2. Open **MESH WiFi > MESH traDUKtors** and add one or more of the already registered traDUKtors.
3. Confirm that the selected manager is available for the MESH application. On traDUKtor, DVRCP and the validated adapter for the selected equipment must be enabled for its supported operations.

Each traDUKtor has its own TU inventory and routed network. Always check the selector before assigning equipment or reviewing a map.

### Step 3: MESH Terminal Units - add the Headend first

1. Open **MESH Terminal Units** and select the intended traDUKtor.
2. Use **Open Terminal Units in Devices** to register the first TU and associate it with that traDUKtor. Enter its management address, manufacturer hint, and Telnet credentials.
3. Return to **MESH Terminal Units** and select that traDUKtor again.
4. Assign **Headend** to the first TU and click **Save role plan**. The Headend occupies node 1; Access units occupy nodes 2 through 10.
5. Open the Headend's **Configuration** and complete Step 4 before commissioning Access units.

The role selector chooses the target template. The node-order arrows order Access units; check the role plan before saving because node order participates in generated configuration. Saving a role plan alone does not prove that any device settings were applied.

### Step 4: Configuration - compare, apply, and confirm

The configuration dialog compares the **observed** device settings with the **target** for its role and site. Review the complete checklist, including the addressing, routing, services, and naming required by the selected template.

| Checklist state | Meaning and next action |
| --- | --- |
| Matches template | The observed value matches the target; no change is needed for that item. |
| Change required | The observed value differs; review the proposed target before applying. |
| Observation required | The original value was not observed. Do not assume that it matched or that its original value can be restored. |

1. Review the comparison. Use **Edit recommendation** only when the proposed settings need a deliberate adjustment. **Advanced actions** remains available for supported expert changes even when the normal checklist already matches.
2. When changes are required, click **Apply configuration** and confirm the reviewed operation. When everything already matches, the normal Apply action is gray and disabled.
3. Follow the progress indicators through dispatch, contact, loading, saving, saved-configuration confirmation, and operating verification. Wait for the actual result; storing a desired template is not proof of success.
4. After successful application and verification, click **Finish** to accept the changes and close the configuration session. Finish ends the session's rollback opportunity.
5. If you choose **Cancel** after changes were applied, read the rollback confirmation. It identifies the items that can be restored and those that will retain their new settings because an original value was unavailable. Confirming performs that restoration; dismissing the confirmation keeps the session open.

If an operation fails, review its reported result and restore or correct the affected items before continuing. A complete match and a completed confirmation are the commissioning goal. Keep the Headend reachable throughout this process.

### Step 5: Add and commission each Access unit

1. Once the Headend is configured and confirmed, register an Access TU under **Devices > Terminal Units** and associate it with the same traDUKtor.
2. Select the traDUKtor in **MESH Terminal Units**, assign **Access**, and save the role plan.
3. Open **Configuration**, review the Access target, apply required changes, wait for verification, and click **Finish**.
4. Repeat for each Access unit, up to nine. Check the intended node order and management addresses before applying each template.

This order establishes the Headend path before remote Access management depends on it. A confirmed Headend enables the routing workflow; confirmed Access configurations add their relevant networks to the routed plan. Do not skip configuration verification simply because a TU replies to a ping.

### Step 6: Routing - read the network snapshot

Open **Routing** and select the traDUKtor. The first snapshot loads automatically. There is no separate Verify button. The drawing shows the manager, Headend, Access connections, names, management IPs, and three simple states supplied by traDUKtor.

| State | OK means | If it is Not OK |
| --- | --- | --- |
| IP | traDUKtor reached the TU management address. | Check power, addressing, the Headend path, and the listed route. |
| Mgmt | The TU management session succeeded. | Check IP reachability, Telnet service, credentials, and identity. |
| Internet | A ping executed on that TU using its normal route reached Internet. | Check that TU's default route, Headend exit, NAT, and restrictions; an ICMP failure alone does not identify the cause. |

Internet is a device-level check, not a separate requirement for every interface. It does not prove client authentication or captive-portal enforcement. Unavailable or not-yet-tested evidence must not be read as a successful test. Offline TUs remain in the inventory with their last known identity and addressing; they are not deleted merely because they stop replying.

Below the drawing, **Static routes** lists each destination network, next hop, and reported installation state. **Saved** means traDUKtor confirmed permanent storage. **Active** without saved confirmation is not yet proof of restart persistence; **Pending** requires further review. These specific routes reach the remote networks through Headend eth0 without replacing traDUKtor's default gateway.

If the Headend configuration is incomplete, follow the configuration prompt and return to the previous step. If a commissioned TU is not OK, revisit its reachability and configuration before treating the network as ready. When all commissioned units show IP, Mgmt, and Internet OK and the required routes are saved, the routed-network milestone is complete. A user can stop here and operate without any captive portal.

### Routing refresh options

| Control or event | Behavior |
| --- | --- |
| Enter Routing or select a traDUKtor | Requests one snapshot automatically. |
| Refresh unchecked (default) | Keeps that snapshot unchanged, even if the page stays open for more than five minutes. |
| Interval selector | Defaults to 5 min; alternatives are 10 s, 30 s, and 1 min. Selecting an interval alone does not start refresh. |
| Refresh checked | Requests updated inventory at the selected interval and asks traDUKtor to use that temporary diagnostic interval. |
| Change interval while enabled | Updates the requested refresh interval. Requests do not overlap. |
| Uncheck Refresh | Stops periodic requests, releases the temporary interval, and keeps the last displayed snapshot. |
| Leave Routing, change manager, or close the browser | Ends the view's temporary refresh session. It does not remove TUs, configuration, or routes. |

traDUKtor normally scans its retained TU inventory at startup and every five minutes, independently of the browser. A live refresh session can temporarily request another interval. On release it returns to normal operation; if the browser disappears without releasing it, the temporary request expires automatically. Returning from a background browser view does not silently restart queries; re-enable Refresh or enter Routing again for a new snapshot.

The display is a diagnostic snapshot, not a continuous polling obligation. Choose shorter intervals only while observing commissioning or recovery, then disable Refresh when finished. Removing a TU or withdrawing a managed route requires an explicit Fácil IoT inventory or routing change. A controller outage, an offline TU, or closing this screen does not erase saved routes.

### Next stage: optional Captive Portal

When the equipment provides WiFi and the validated adapter supports captive access, enable and configure the optional portal from Fácil IoT. Keep **Captive Portal** off for an unrestricted routed network. Its global activation and policy configuration are a separate next milestone, after the routed network is stable. Existing device rules from previous manual tests may still restrict traffic; a green device-level Internet result does not validate a captive client's full browsing experience.

## Settings

### General

Configure application name, English language, time zone, date format, NTP enablement, primary NTP, and backup NTP. Accurate time is required for logs, certificates, release verification, and event correlation.

### Notifications

Channels include in-app, email, and WhatsApp when their integrations are active. Event toggles cover critical alarms, high-priority alarms, offline devices, and low battery.

### Appliance network

The primary interface alone installs the default gateway. Fields include hostname, DHCP/static IPv4, address, prefix, gateway, primary/secondary DNS, optional 802.1Q VLAN and VLAN ID, and IPv6 settings. Recovery LAN must not add another default route.

Network application requires confirmation, automatic backup, and rollback when validation fails. Keep direct recovery available.

## Maintenance

Maintenance exposes lifecycle status, signed updates, diagnostics/logs, backup and recovery, and previous-release state.

- **Last Release** checks the signed `stable` channel.
- **Last Beta** checks the signed `lab` channel.
- Browser upload accepts a signed `.fiot` package.
- Activation validates the package, backs up PostgreSQL, validates Compose, switches releases atomically, starts services, and runs health checks.
- Code rollback and database restoration are separate operations.

Keep power and network connected during activation. After return to login, confirm version, uptime, database content, live devices, MQTT management, and previous-release availability.

## MQTT equipment boundary

The protected broker uses separate identities and topic ACLs:

- Gateways use EUI-based enrollment for LoRaWAN/BLE traffic.
- traDUKtors use factory serial plus a unique credential.
- General traDUKtor management and MESH permission are separate.
- Serial or EUI is never accepted as a password.

Public MQTT uses TLS and authentication. Plain port 1883 is never exposed to the Internet.

## Backup and recovery

Create a PostgreSQL backup before release activation. Code rollback does not automatically restore database, certificates, secrets, or network settings. Maintain tested procedures for administrator recovery, code rollback, database restore, recovery LAN, and full appliance recovery.

Never remove persistent volumes or prune host-wide container data without identifying ownership and confirming a recoverable backup.

## Stable update acceptance

1. Record installed version and hardware.
2. Check **Last Release** and verify channel, size, signature, and version.
3. Install and observe progress.
4. Confirm service health and return to login.
5. Confirm version, uptime, database data, users, devices, MQTT, and previous release.
6. Repeat the routed MESH checks: management, confirmed configuration, saved return routes, and IP/Mgmt/Internet states for each commissioned TU.

## Security checklist

- Use individual accounts and least privilege.
- Use unique device MQTT credentials and topic ACLs.
- Keep time synchronized.
- Never publish secrets, private keys, customer data, or unsanitized logs.
- Back up before network, lifecycle, routing, or captive-policy changes.
- Treat every status as evidence for its named check only.
- Do not claim a radio changed until direct verification succeeds.

## Support information

Provide appliance release, hardware, hostname, uptime, boot reason, approximate failure time, affected community/Site, and sanitized logs. For MESH issues also provide traDUKtor serial/version, Terminal Unit serial/model/firmware, role, node position, and the failed job stage. Never include passwords, tokens, or private keys.
