#include <fstream>
#include <string>
#include <vector>
#include <glob.h>

double get_cpu_temp() {
  std::string path = "/sys/class/hwmon/hwmon*/temp*_input";
  glob_t glob_result;
  glob("/sys/class/hwmon/hwmon*/temp*_input", GLOB_TILDE, NULL, &glob_result);
  
  double mx_temp = 0.0;
  for (int i = 0; i < glob_result.gl_pathc; i++) {
    std::ifstream file(glob_result.gl_pathv[i]);
    double temp = 0.0;
    if (file >> temp) {
      if (temp > mx_temp) {
        mx_temp = temp;
      }
    }
  }
  globfree(&glob_result);
  return mx_temp / 1000.0;
}

