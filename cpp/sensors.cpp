#include "sensors.h"

#ifdef __mac__
#include "mac/mac_sensors.cpp"

#elif __linux__
#include "linux/linux_sensors.cpp"

#endif

int get_fan_speed_rpm() {
  return 1800;
}