---
title: Fácil IoT manual
slug: /facil-iot
sidebar_position: 4
description: Complete operating manual for Fácil IoT 0.1.18.
---

# Fácil IoT operational manual

![Fácil IoT logo](/img/facil-iot-logo.png)

**Current stable release:** `0.1.18`

**Reference appliance:** Protectli FW7225
**Manual scope:** operation, communities, devices, alarms, licenses, integrations, MESH WiFi, configuration, maintenance, and recovery.

[Download the PDF manual](/downloads/facil-iot/Facil_IoT_Operational_Manual_0.1.18.pdf)

:::info Living manual
This page is the current public manual and is updated in place. The PDF records the stable release represented by this edition.
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

Register name, community, Site, manufacturer, serial, management IP, Telnet username/password, and assigned traDUKtor. The current manufacturer list begins with **Astra Wireless** and can grow as new utility adapters are implemented.

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

## MESH WiFi

Fácil IoT is the desired-state control plane; traDUKtor is the site-local execution agent. The MESH workspace has **Global**, **MESH traDUKtors**, **MESH Terminal Units**, **Routing**, and **Captive Portal** tabs.

### Global

Global settings define deployment-wide addressing, naming, policy defaults, and captive-service context used when generating plans. Changes here are desired-state inputs and do not directly reconfigure a radio.

### MESH traDUKtors

Select the traDUKtor responsible for a Site. Readiness requires authenticated MQTT, MESH permission, compatible firmware, retained inventory, and local reachability prerequisites. A traDUKtor can manage up to ten Terminal Units.

### MESH Terminal Units

Select a traDUKtor and assign exactly one **Headend** plus up to nine **Access** nodes.

- Node 1 is always the Headend.
- Access nodes occupy positions 2 through 10.
- Up/down arrows reorder Access routing position.
- **Save role plan** persists roles and order.
- **Configuration** remains disabled until the role plan is saved.

The Headend provides upstream/default-gateway access. Access nodes extend service through the MESH backhaul. Replacing the Headend moves the replacement to node 1.

### Configuration review

The configuration window has two columns:

- **Current configuration**: read-only normalized evidence from the Terminal Unit.
- **Recommended configuration**: complete role template generated by Fácil IoT.

Sections cover internal switching, management path, Ethernet/WiFi/MESH interfaces, default gateway, routes, ACL, firewall, NAT, DHCP, LLDP, and other required service state. Collapsible sections keep the comparison compact.

**Edit recommendation** requires acknowledgement that advanced Astra Wireless expertise is needed. **Apply changes** submits a bounded job to traDUKtor. **Cancel** makes no changes.

:::warning Level 3 status
Stable releases validate management Levels 1 and 2. Full Level 3 application is controlled work until arbitrary starting configurations can be read, transitioned, and verified without losing management.
:::

### Routing

Routing uses the saved node order to build the tree from the Headend upstream interface toward Access nodes. It must identify default gateway, per-node MESH addresses, downstream networks, next hops, conflicts, missing return routes, loops, and unreachable management paths.

Review every route before application. The visual order is operational input, not decoration.

### Captive Portal

Captive Portal defines the client network, DHCP range/options, DNS/portal destination, quarantine behavior, temporary approval, NAT, ACL, and firewall policy. The intended outcome is that unauthenticated clients reach only required services and the portal; authorized clients follow approved Internet policy.

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
6. Repeat critical operational checks for MESH Levels 1 and 2.

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
