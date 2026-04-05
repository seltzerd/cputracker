# CPU Tracker

`CPU Tracker` is a small local agent on Go that prints host metrics to the terminal every second.

At the moment the project collects:

- CPU usage
- RAM total and used
- Disk usage
- Hostname
- Timestamp
- CPU temperature, battery percentage, and fan speed through a small C++ layer

## Project Structure

```text
cputracker/
├── README.md
└── main/
    ├── cmd/tracker/main.go
    ├── cpuInfoCollect/
    ├── helpFuncs/
    ├── cpp/
    ├── go.mod
    └── go.sum
```

## Requirements

For a normal run you need:

- Go `1.25` or newer
- macOS with Xcode Command Line Tools installed
- a C/C++ toolchain available for `cgo`

If Xcode Command Line Tools are not installed yet:

```bash
xcode-select --install
```

## Quick Start

From the project root:

```bash
cd main
go run ./cmd/tracker
```

On the first run Go may download dependencies automatically.

To stop the agent, press `Ctrl + C`.

## Expected Output

The program prints a new metrics block roughly once per second:

```text
2026/04/05 03:33:01 AgentID: my-macbook
TimeStamp: 2026-04-05 03:33:01
MemoryTotal: 16384 MB
MemoryUsed: 9021 MB
CpuPercent: 12.5 %
DiskUsedPercent: 68.4 %
Temp: 50.00 C
Battery percent: 85.00
Fan speed (rpm): 1800
```

## Useful Commands

Run the app:

```bash
cd main
go run ./cmd/tracker
```

Build a binary:

```bash
cd main
go build -o tracker ./cmd/tracker
./tracker
```

Download dependencies in advance:

```bash
cd main
go mod download
```

## About the C++ Part

The Go app uses `cgo` and the files in [`main/cpp`](/Users/ivanlukanskiy/Desktop/cputracker/main/cpp) to get extra hardware metrics.

For the main app you do not need to run `cmake` manually: `go run` and `go build` compile the required C/C++ code automatically.

If you want to build the C++ library separately:

```bash
cd main/cpp
mkdir -p build
cd build
cmake ..
make
```

Important: right now [`main/cpp/sensors.cpp`](/Users/ivanlukanskiy/Desktop/cputracker/main/cpp/sensors.cpp) returns stub values (`50.0`, `85.0`, `1800`). So temperature, battery, and fan speed are placeholders until real sensor integration is implemented.

## Troubleshooting

If `go run` fails with a compiler error:

- make sure Go is installed: `go version`
- make sure Xcode Command Line Tools are installed
- run the command from [`main`](/Users/ivanlukanskiy/Desktop/cputracker/main), not from the repository root

If the app starts but sensor values look unreal:

- CPU, RAM, disk, hostname, and timestamp come from Go libraries
- temperature, battery, and fan speed currently come from stub C++ functions
