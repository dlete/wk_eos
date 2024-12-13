
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 60 | 15 | 45 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| leaf1 |  29 | 11 | 18 | NTP, Interface State, LLDP Topology, IP Reachability, BGP, Routing Table, Loopback0 Reachability |
| spine1 |  31 | 4 | 27 | NTP, LLDP Topology, IP Reachability, BGP, Routing Table, Loopback0 Reachability |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  2 | 0 | 2 |
| Interface State |  8 | 6 | 2 |
| LLDP Topology |  6 | 2 | 4 |
| IP Reachability |  6 | 2 | 4 |
| BGP |  14 | 2 | 12 |
| Routing Table |  16 | 2 | 14 |
| Loopback0 Reachability |  8 | 1 | 7 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 2 | spine1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 3 | leaf1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel11 - host11_leaf1_to_host11 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 4 | leaf1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel12 - host12_leaf3_to_host12 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 12 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet50/1 - remote: spine2_Ethernet1/1 | FAIL | Interface Down - N/A |
| 14 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2/1 - remote: leaf2_Ethernet49/1 | FAIL | Interface Down - N/A |
| 15 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3/1 - remote: leaf3_Ethernet49/1 | FAIL | Interface Down - N/A |
| 16 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4/1 - remote: leaf4_Ethernet49/1 | FAIL | Interface Down - N/A |
| 18 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet50/1 - Destination: spine2_Ethernet1/1 | FAIL | 100% packet loss |
| 20 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet2/1 - Destination: leaf2_Ethernet49/1 | FAIL | 100% packet loss |
| 21 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet3/1 - Destination: leaf3_Ethernet49/1 | FAIL | 100% packet loss |
| 22 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet4/1 - Destination: leaf4_Ethernet49/1 | FAIL | 100% packet loss |
| 25 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.0 | FAIL | Session state "Active" |
| 26 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.2 | FAIL | Session state "Idle" |
| 27 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.1 | FAIL | Session state "Active" |
| 28 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.65 | FAIL | Session state "Idle" |
| 29 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.129 | FAIL | Session state "Idle" |
| 30 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.193 | FAIL | Session state "Idle" |
| 31 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.1 | FAIL | Session state "Active" |
| 32 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.2 | FAIL | Session state "Active" |
| 33 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.129 | FAIL | Session state "Active" |
| 34 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.130 | FAIL | Session state "Active" |
| 35 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.131 | FAIL | Session state "Active" |
| 36 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.132 | FAIL | Session state "Active" |
| 38 | leaf1 | Routing Table | Remote VTEP address | 192.0.254.2 | FAIL | VTEP 192.0.254.2 is not in the routing table |
| 39 | leaf1 | Routing Table | Remote VTEP address | 192.0.254.3 | FAIL | VTEP 192.0.254.3 is not in the routing table |
| 40 | leaf1 | Routing Table | Remote VTEP address | 192.0.254.4 | FAIL | VTEP 192.0.254.4 is not in the routing table |
| 41 | spine1 | Routing Table | Remote VTEP address | 192.0.254.1 | FAIL | VTEP 192.0.254.1 is not in the routing table |
| 42 | spine1 | Routing Table | Remote VTEP address | 192.0.254.2 | FAIL | VTEP 192.0.254.2 is not in the routing table |
| 43 | spine1 | Routing Table | Remote VTEP address | 192.0.254.3 | FAIL | VTEP 192.0.254.3 is not in the routing table |
| 44 | spine1 | Routing Table | Remote VTEP address | 192.0.254.4 | FAIL | VTEP 192.0.254.4 is not in the routing table |
| 46 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.130 | FAIL | Lo0 192.0.255.130 is not in the routing table |
| 47 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.131 | FAIL | Lo0 192.0.255.131 is not in the routing table |
| 48 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.132 | FAIL | Lo0 192.0.255.132 is not in the routing table |
| 49 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.129 | FAIL | Lo0 192.0.255.129 is not in the routing table |
| 50 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.130 | FAIL | Lo0 192.0.255.130 is not in the routing table |
| 51 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.131 | FAIL | Lo0 192.0.255.131 is not in the routing table |
| 52 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.132 | FAIL | Lo0 192.0.255.132 is not in the routing table |
| 54 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.130 | FAIL | 100% packet loss |
| 55 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.131 | FAIL | 100% packet loss |
| 56 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.132 | FAIL | 100% packet loss |
| 57 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.129 | FAIL | 100% packet loss |
| 58 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.130 | FAIL | 100% packet loss |
| 59 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.131 | FAIL | 100% packet loss |
| 60 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.132 | FAIL | 100% packet loss |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 2 | spine1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 3 | leaf1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel11 - host11_leaf1_to_host11 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 4 | leaf1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel12 - host12_leaf3_to_host12 | FAIL | interface status: down - line protocol status: lowerLayerDown |
| 5 | leaf1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan100 - TENANT_A_BGP_TO_COMPUTE | PASS | - |
| 6 | leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 7 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 8 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 9 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - TEST_VRF_VTEP_DIAGNOSTICS | PASS | - |
| 10 | spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 11 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet49/1 - remote: spine1_Ethernet1/1 | PASS | - |
| 12 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet50/1 - remote: spine2_Ethernet1/1 | FAIL | Interface Down - N/A |
| 13 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1/1 - remote: leaf1_Ethernet49/1 | PASS | - |
| 14 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2/1 - remote: leaf2_Ethernet49/1 | FAIL | Interface Down - N/A |
| 15 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3/1 - remote: leaf3_Ethernet49/1 | FAIL | Interface Down - N/A |
| 16 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4/1 - remote: leaf4_Ethernet49/1 | FAIL | Interface Down - N/A |
| 17 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet49/1 - Destination: spine1_Ethernet1/1 | PASS | - |
| 18 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet50/1 - Destination: spine2_Ethernet1/1 | FAIL | 100% packet loss |
| 19 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet1/1 - Destination: leaf1_Ethernet49/1 | PASS | - |
| 20 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet2/1 - Destination: leaf2_Ethernet49/1 | FAIL | 100% packet loss |
| 21 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet3/1 - Destination: leaf3_Ethernet49/1 | FAIL | 100% packet loss |
| 22 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet4/1 - Destination: leaf4_Ethernet49/1 | FAIL | 100% packet loss |
| 23 | leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 24 | spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 25 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.0 | FAIL | Session state "Active" |
| 26 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.2 | FAIL | Session state "Idle" |
| 27 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.1 | FAIL | Session state "Active" |
| 28 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.65 | FAIL | Session state "Idle" |
| 29 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.129 | FAIL | Session state "Idle" |
| 30 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.193 | FAIL | Session state "Idle" |
| 31 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.1 | FAIL | Session state "Active" |
| 32 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.2 | FAIL | Session state "Active" |
| 33 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.129 | FAIL | Session state "Active" |
| 34 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.130 | FAIL | Session state "Active" |
| 35 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.131 | FAIL | Session state "Active" |
| 36 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.0.255.132 | FAIL | Session state "Active" |
| 37 | leaf1 | Routing Table | Remote VTEP address | 192.0.254.1 | PASS | - |
| 38 | leaf1 | Routing Table | Remote VTEP address | 192.0.254.2 | FAIL | VTEP 192.0.254.2 is not in the routing table |
| 39 | leaf1 | Routing Table | Remote VTEP address | 192.0.254.3 | FAIL | VTEP 192.0.254.3 is not in the routing table |
| 40 | leaf1 | Routing Table | Remote VTEP address | 192.0.254.4 | FAIL | VTEP 192.0.254.4 is not in the routing table |
| 41 | spine1 | Routing Table | Remote VTEP address | 192.0.254.1 | FAIL | VTEP 192.0.254.1 is not in the routing table |
| 42 | spine1 | Routing Table | Remote VTEP address | 192.0.254.2 | FAIL | VTEP 192.0.254.2 is not in the routing table |
| 43 | spine1 | Routing Table | Remote VTEP address | 192.0.254.3 | FAIL | VTEP 192.0.254.3 is not in the routing table |
| 44 | spine1 | Routing Table | Remote VTEP address | 192.0.254.4 | FAIL | VTEP 192.0.254.4 is not in the routing table |
| 45 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.129 | PASS | - |
| 46 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.130 | FAIL | Lo0 192.0.255.130 is not in the routing table |
| 47 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.131 | FAIL | Lo0 192.0.255.131 is not in the routing table |
| 48 | leaf1 | Routing Table | Remote Lo0 address | 192.0.255.132 | FAIL | Lo0 192.0.255.132 is not in the routing table |
| 49 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.129 | FAIL | Lo0 192.0.255.129 is not in the routing table |
| 50 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.130 | FAIL | Lo0 192.0.255.130 is not in the routing table |
| 51 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.131 | FAIL | Lo0 192.0.255.131 is not in the routing table |
| 52 | spine1 | Routing Table | Remote Lo0 address | 192.0.255.132 | FAIL | Lo0 192.0.255.132 is not in the routing table |
| 53 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.129 | PASS | - |
| 54 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.130 | FAIL | 100% packet loss |
| 55 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.131 | FAIL | 100% packet loss |
| 56 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.0.255.129 Destination: 192.0.255.132 | FAIL | 100% packet loss |
| 57 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.129 | FAIL | 100% packet loss |
| 58 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.130 | FAIL | 100% packet loss |
| 59 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.131 | FAIL | 100% packet loss |
| 60 | spine1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine1 - 192.0.255.1 Destination: 192.0.255.132 | FAIL | 100% packet loss |
