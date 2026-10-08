# MACMap – Adaptive MAC Learning and Network Fault Analysis System

## 📌 Project Overview

MACMap is a Python-based software simulation designed to demonstrate how a network switch learns MAC addresses and uses the learned information to forward Ethernet frames within a Local Area Network (LAN).

In an Ethernet network, a switch maintains a dynamic MAC address table. When a frame enters the switch, the switch examines the source MAC address and associates it with the incoming port. When another frame is received, the switch checks the destination MAC address in its table and forwards the frame through the appropriate port.

MACMap simulates this process in a simple and understandable way without requiring physical networking hardware.

The project also provides additional monitoring features to identify MAC address movement and inactive or stale MAC table entries.

---

## 🎯 Objectives

The main objectives of MACMap are:

- To simulate MAC address learning in an Ethernet switch.
- To maintain a dynamic MAC address table.
- To demonstrate Ethernet frame forwarding.
- To simulate flooding when a destination MAC address is unknown.
- To detect MAC address movement between switch ports.
- To identify stale or inactive MAC table entries.
- To record important network events during simulation.
- To provide a simple way to understand Layer 2 switching.
- To demonstrate basic network fault-analysis concepts.
- To help students understand switch behavior through software simulation.

---

## 💡 Problem Statement

In a computer network, switches need to learn the location of devices before they can efficiently forward Ethernet frames.

Learning switch concepts using physical networking equipment can be difficult for beginners because it requires additional hardware and configuration.

A MAC address table is also dynamic. Devices may appear on different ports, and old MAC table entries may remain inactive for some time.

Therefore, a simple software-based system is required to demonstrate:

1. How MAC addresses are learned.
2. How Ethernet frames are forwarded.
3. How unknown destination addresses are handled.
4. How MAC address movement can be detected.
5. How inactive MAC entries can be identified.

MACMap addresses these requirements through a Python-based simulation.

---

## 🚀 Proposed Solution

MACMap provides a simulated Ethernet switching environment where users can add devices, associate MAC addresses with switch ports, send Ethernet frames, view the MAC address table, check stale entries, and monitor network events.

The system stores information such as:

- MAC address
- Switch port
- Last-seen time

When an Ethernet frame is processed, the source MAC address is learned and associated with the incoming port.

The destination MAC address is then searched in the MAC address table.

If the destination is known, the frame is forwarded toward the corresponding port.

If the destination is unknown, the system simulates flooding behavior.

The system also checks whether an already learned MAC address appears on another port. Such a change is recorded as a MAC movement event.

Inactive entries can be identified using the configured timeout period.

---

# 🏗️ System Architecture

The basic architecture of MACMap is:

```text
+----------------------+
|     End Devices      |
+----------+-----------+
           |
           v
+----------------------+
| Ethernet Frame       |
| Generator            |
+----------+-----------+
           |
           v
+----------------------+
| MAC Learning Module  |
+----------+-----------+
           |
           v
+-------------------------------+
| Dynamic MAC Address Table     |
| MAC Address                   |
| Port                          |
| Last Seen                     |
+---------------+---------------+
                |
                v
+-------------------------------+
| Frame Forwarding Module       |
+---------------+---------------+
                |
                v
+-------------------------------+
| Network Event / Fault         |
| Analysis Module               |
+---------------+---------------+
                |
                v
+-------------------------------+
| Visualization / Results      |
+-------------------------------+
