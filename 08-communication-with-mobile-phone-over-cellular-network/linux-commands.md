# Linux Commands

This document contains the Linux commands used during the laboratory exercise on communication with a mobile phone over a cellular network using a Raspberry Pi.

> **Note:** IP addresses may differ between devices and network configurations. Users should check their own IP addresses before attempting to connect.

## 1. Network Configuration

### Check the IP Address

```bash
ip addr show wlan0
```

Displays the network configuration of the `wlan0` wireless interface, including its IP address.

Example output:

```text
inet 10.208.247.121/24 brd 10.208.247.255
```

### Test Network Connectivity

```bash
ping -c 4 google.com
```

Sends four ICMP packets to `google.com` to check network connectivity.

## 2. Wi-Fi Configuration

### Edit the Wi-Fi Configuration File

```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

Opens the Wi-Fi configuration file in the Nano text editor.

Example configuration:

```text
network={
    ssid="RPiHotspot"
    psk="YOUR_WIFI_PASSWORD"
}
```

Replace `YOUR_WIFI_PASSWORD` with the appropriate password for the network being used.

### Apply the Wi-Fi Configuration

```bash
sudo wpa_cli -i wlan0 reconfigure
```

Requests the wireless configuration to be reloaded for the `wlan0` interface.

## 3. SSH Configuration

### Enable the SSH Service at Startup

```bash
sudo systemctl enable ssh
```

Configures the SSH service to start automatically when the system boots.

### Start the SSH Service

```bash
sudo systemctl start ssh
```

Starts the SSH service immediately.

### Check SSH Service Status

```bash
systemctl status ssh
```

Displays the current status of the SSH service.

## 4. Network Management

### Check NetworkManager Status

```bash
systemctl status NetworkManager
```

Displays the current status of the NetworkManager service.

### Check the Wireless Interface

```bash
ip addr show wlan0
```

Displays the IP address and other network information associated with the wireless interface.

## 5. Start a Local HTTP Server

```bash
python3 -m http.server 8000
```

Starts a simple HTTP server on port `8000`, allowing other devices on the same reachable network to access files in the current directory through a web browser.

To access the server, use the Raspberry Pi's IP address:

```text
http://<RASPBERRY_PI_IP>:8000
```

Replace `<RASPBERRY_PI_IP>` with the actual IP address of the Raspberry Pi.

## Summary

These commands cover basic network configuration, Wi-Fi setup, SSH service management, network diagnostics, and hosting a simple HTTP server on a Raspberry Pi.