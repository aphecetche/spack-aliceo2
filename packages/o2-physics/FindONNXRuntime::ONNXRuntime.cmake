find_package(PkgConfig)

pkg_check_modules(ONNXRuntime REQUIRED IMPORTED_TARGET libonnxruntime)

if (PkgConfig::ONNXRuntime)
   add_library(ONNXRuntime::ONNXRuntime ALIAS PkgConfig::ONNXRuntime)
endif()

find_package_handle_standard_args(ONNXRuntime::ONNXRuntime
    REQUIRED_VARS ONNXRuntime_FOUND)
