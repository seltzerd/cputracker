package help

import "time"

type FromAgent struct {
	AgentID         string  `json:"agent_id"`
	Timestamp       string  `json:"timestamp"`
	CpuPercent      float64 `json:"cpu_percent"`
	MemoryUsedMB    int     `json:"memory_used_mb"`
	MemoryTotalMB   int     `json:"memory_total_mb"`
	DiskUsedPercent float64 `json:"disk_used_percent"`
}

type ToSwift struct {
	AgentID       string    `json:"agent_id"`
	Online        bool      `json:"online"`
	CpuPercent    float64   `json:"cpu_percent"`
	MemoryUsedMB  int       `json:"memory_used_mb"`
	MemoryTotalMB int       `json:"memory_total_mb"`
	LastSeen      time.Time `json:"last_seen"`
}
