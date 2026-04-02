package collect

import (
	help "cpu_tracker/helpFuncs"
	"time"

	"github.com/shirou/gopsutil/mem"
)

func Collect() *help.FromAgent {
	m, _ := mem.VirtualMemory()

	data := &help.FromAgent{
		AgentID:       "agent-1",
		Timestamp:     time.Now(),
		MemoryTotalMB: int(m.Total / 1024 / 1024),
	}
	return data

	// total := m.Total / 1024 * 1024
	// used := m.Used / 1024 * 1024

}
