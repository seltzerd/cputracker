package main

import (
	collect "cpu_tracker/cpuInfoCollect"
	"fmt"
	"log"
	"sync"
	// _ "help/helpFuncs"
)

func main() {

	var wg sync.WaitGroup

	wg.Add(1)

	go func() {
		defer wg.Done()
		res := fmt.Sprint(collect.Collect())
		log.Println(res)
	}()
	wg.Wait()
}
