package collect

import (
	help "cpu_tracker/helpFuncs"
	"encoding/json"
	"log"
	"time"

	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/mem"
)

func Collect() string {
	m, _ := mem.VirtualMemory()
	cpu, _ := cpu.Percent(time.Second, false)
	d, _ := disk.Usage("/")
	// er := fmt.Sprintf("Error with marshal")

	data := &help.FromAgent{
		// AgentID:       "agent-1",

		Timestamp:       time.Now(),
		MemoryTotalMB:   int(m.Total / 1024 / 1024),
		MemoryUsedMB:    int(m.Used / 1024 / 1024),
		CpuPercent:      cpu[0],
		DiskUsedPercent: d.UsedPercent,
	}
	bytes, err := json.Marshal(data)

	if err != nil {
		log.Fatal(err)
	}
	str := string(bytes)
	return str
	// total := m.Total / 1024 * 1024
	// used := m.Used / 1024 * 1024
}
