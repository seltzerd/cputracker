package main

import (
	collect "cpu_tracker/cpuInfoCollect"
	"fmt"
	"log"
	"os"
	"sync"
	"time"
	// _ "help/helpFuncs"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(1)

	q := make(chan os.Signal, 1)

	go func() {
		defer wg.Done()

		t := time.NewTicker(1 * time.Second)
		defer t.Stop()

		for {
			select {
			case <-t.C:
				res := fmt.Sprint(collect.Collect())
				log.Println(res)
			case <-q:
				log.Printf("quit")
			}
		}
	}()

	wg.Wait()
}
