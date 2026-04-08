#include "sensors.h"

#ifdef __mac__
#inlcude "mac/mac_sensors.cpp"

#elif __linux__
#include "linux/linux_sensors.cpp"

#endif

double get_battery_percent() {
  return 85.0;
}

int get_fan_speed_rpm() {
  return 1800;
}