# Ohayo Network

> Live speed, your real exit IP and where each VPN tunnel exits — in the Mac menu bar. Per-app traffic, Wi-Fi details and a speed test. No account, no analytics.

Live download and upload speed, the country your traffic actually exits from, and — unusually — the location of every VPN tunnel separately. Split routing is visible at a glance.

[Get it on the Mac App Store](https://apps.apple.com/app/ohayo-network/id6787492543?mt=12) · macOS 14 or later · Apple silicon · one-time purchase, no subscription

## Ohayo Network in brief

- **Platform:** macOS 14 Sonoma or later
- **Processor:** Apple silicon (M1 or newer)
- **App type:** Menu-bar utility, no Dock icon
- **Availability:** Mac App Store · one-time purchase, no subscription
- **VPN and tunnels:** Any tunnel interface: WireGuard, IPsec, PPP and utun/tun-based clients such as OpenVPN
- **Per-app traffic:** Optional read-only content-filter system extension
- **Account:** Not required
- **Data collection:** None — no analytics, no ads, no backend
- **Languages:** English, Russian
- **Developer:** Ohayo Studio

### Made for

- Checking which country your VPN really exits from — per tunnel, even with several connected.
- Noticing at once when your exit IP or region changes: a VPN that dropped, or traffic taking a route you did not expect.
- Finding out which app is using your bandwidth and which servers it talks to.
- Watching live speed, Wi-Fi signal and data usage without opening a window.
- Running a quick Cloudflare speed test or a latency check from the menu bar.

## Features

Everything is read locally and updates the moment it changes — no background service, no calls home, no waiting for a refresh.

### Throughput, straight from the kernel

Download and upload come from the interface byte counters macOS keeps itself — no polling of other apps, no estimates. A live sparkline in the status bar, the full chart in the dashboard.

### Every tunnel, located separately

utun, WireGuard, IPsec — each active tunnel is geolocated over that interface, not over the default route. Split routing is flagged the moment part of your traffic leaves the country you expect.

### Exit IP and region

Country, city, ISP and ASN, with the flag in the status bar. Recent IP history, and your own labels: tag an exit as Home or Office VPN by country, city, ISP, ASN or IP.

### Per-app traffic

Live up and down per app, session totals, connection counts and remote endpoints. Top five in the popover, a sortable table in the dashboard. It runs on a macOS content-filter extension you add from Settings.

### Latency and a real speed test

Round-trip time and jitter for hosts you choose, plus an on-demand Cloudflare speed test with configurable duration, parallel streams and a data cap per phase.

### Wi-Fi, in detail

Network name, signal, channel, 802.11 standard, security and transmit rate — next to your local IP, MAC address and the DNS servers actually in use.

### Data usage on your own schedule

Cumulative totals for received and sent, with automatic resets — daily, weekly, monthly or never — and a manual reset whenever you want a clean count.

### The geolocation services are yours

Three key-less providers by default — each editable, switchable or removable. Add your own HTTPS endpoint by URL and JSON key paths, and pick which one is authoritative.

## Four screens: popover, dashboard, per-app traffic and settings

### The whole link, in one window

The dashboard stacks everything that matters into a single scroll: what you are connected through, where it comes out, how fast it is right now, and what a proper test says.

- Connection card: Wi-Fi, Ethernet or VPN — including the carrier underneath a tunnel
- Active tunnels, each with its own flag and exit
- Throughput chart and a Cloudflare speed test with ping, download and upload

### See which apps use the network

Every app that touches the network is listed live — with connection counts and the endpoints it talks to. It runs on a macOS content-filter system extension, installed from the app's own settings.

- Read-only: every flow is allowed, untouched — nothing is blocked, redirected or modified
- No payload is ever read; byte counts are aggregated in memory and written nowhere
- Remove the extension whenever you like; the rest of the app keeps working

### Every switch in one pane

Monitoring settings keep the controls together: how data usage resets, whether Wi-Fi details are read, and whether traffic is counted per app.

- Data usage resets daily, weekly, monthly or never — or clear it by hand right there
- Wi-Fi details are their own switch; macOS gates network names behind Location access
- The system extension installs and uninstalls here, with counting as a separate toggle

### The status bar, your way

Show a live sparkline, the two speeds, a compact label — with or without the flag of the country you are exiting from. It is a menu-bar app: no dock icon, no window in the way.

## We have no server. There is nothing for us to collect.

Ohayo Network has no account, no sign-in and no backend — everything it shows is measured on your Mac, by your Mac.

### Stays on your Mac

Throughput, per-app traffic, Wi-Fi details and your history of exits are computed and kept locally, in your own preferences.

### You choose who hears your IP

Geolocation, latency probes, the speed test and the map reach only the services you enable, always over HTTPS. Disable one and it is never contacted again.

### The filter reads no traffic

The content-filter extension allows every flow untouched, never inspects payload, and writes nothing to disk. It only counts bytes per app, in memory.

## FAQ

### Do I need a VPN for this to be useful?

No. Without a tunnel you get live speed, your exit IP and region, latency, Wi-Fi details, data usage and the speed test. If you do use one, each active tunnel is geolocated separately — that is what sets it apart from most menu-bar monitors.

### What is the system extension, and do I have to install it?

Per-app traffic is the only feature that needs it, and it is entirely optional — everything else works without it. It is a macOS content-filter extension: read-only, never blocking, never inspecting payload. You install it yourself, approve it in System Settings, and can uninstall it from the same panel at any time.

### Does it work on Intel Macs?

No — Ohayo Network is built for Apple silicon and requires macOS 14 Sonoma or later. If you need an Intel build, write to feedback@ohayo.by.

### Is it a subscription?

No. It is a one-time purchase on the Mac App Store, and updates to the version you bought arrive the usual way.

### Does monitoring slow my connection down?

No. Speed is read from counters the kernel already maintains, once a second. The content filter allows every flow immediately and only asks the kernel for cumulative byte counts — your traffic never routes through user space.

### What languages does it speak?

English and Russian, following your system language. If you need another language, write to feedback@ohayo.by.

## Links

- Web page: https://apps.ohayo.by/ohayo-network
- Russian version: https://apps.ohayo.by/ohayo-network/ru
- Mac App Store: https://apps.apple.com/app/ohayo-network/id6787492543?mt=12
- Support: https://legal.ohayo.by/network/support
- Privacy Policy: https://legal.ohayo.by/network/privacy
- feedback@ohayo.by
