# CPU Tracker

A lightweight Go agent that collects and logs system resource metrics every second.

## What it does

Collects the following metrics from the host machine:
- **CPU usage** (%)
- **RAM** — total and used (MB)
- **Disk usage** (%)
- **Hostname** (used as Agent ID)
- **Timestamp**

## Project structure

```
golang/
├── cmd/tracker/main.go           # Entry point
├── cpuInfoCollect/collectData.go # Metrics collection logic
├── helpFuncs/modles.go           # Data models
├── go.mod
└── go.sum
```

## Requirements

- Go 1.21+
- [gopsutil](https://github.com/shirou/gopsutil)

## Run

```bash
cd golang
go run cmd/tracker/main.go
```

## Output example

```
AgentID: my-macbook
TimeStamp: 2026-04-03 14:22:01
MemoryTotal: 16384 MB
MemoryUsed: 9021 MB
CpuPercent: 12.5 %
DiskUsedPercent: 68.4 %
```

Metrics are printed to stdout every second via `log.Println`.

## Models

`FromAgent` — data collected by the agent (used internally and for future API transport).

`ToSwift` — model for sending data to a Swift client (online status, last seen time).

UPDATE SOON...
