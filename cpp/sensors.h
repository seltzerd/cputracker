#pragma once

#ifdef __cplusplus
extern "C" {
#endif

  double get_cpu_temp();
  double get_battery_percent();
  int get_fan_speed_rpm();

#ifdef __cplusplus
}
#endif