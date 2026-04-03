package collect

import (
	help "cpu_tracker/helpFuncs"
	"fmt"
	"math"
	"os"
	"time"

	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/mem"
)

func Collect() string {
	// loc, _ := time.LoadLocation("Europe/Moscow")
	// moscowTime := time.Now().In(loc)
	hostname, _ := os.Hostname()
	m, _ := mem.VirtualMemory()
	cpu, _ := cpu.Percent(time.Second, false)
	d, _ := disk.Usage("/")
	// er := fmt.Sprintf("Error with marshal")

	data := &help.FromAgent{
		AgentID:         hostname,
		Timestamp:       time.Now().Local().Format("2006-01-02 15:04:05"),
		MemoryTotalMB:   int(m.Total / 1024 / 1024),
		MemoryUsedMB:    int(m.Used / 1024 / 1024),
		CpuPercent:      math.Round(cpu[0]*100) / 100,
		DiskUsedPercent: math.Round(d.UsedPercent*100) / 100,
	}
	// bytes, err := json.Marshal(data)

	res := fmt.Sprintf("AgentID: %+v\nTimeStamp: %+v\nMemoryTotal: %+v MB\nMemoryUsed: %+v MB\nCpuPercent: %+v %%\nDiskUsedPercent: %+v %%\n", data.AgentID, data.Timestamp, data.MemoryTotalMB, data.MemoryUsedMB, data.CpuPercent, data.DiskUsedPercent)

	return res
	// total := m.Total / 1024 * 1024
	// used := m.Used / 1024 * 1024
}
