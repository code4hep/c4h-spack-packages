# Pythia8 is built with Autotools and installs no CMake package config, so this
# module locates its header and library (via CMAKE_PREFIX_PATH) and creates the
# Pythia8::Pythia8 imported target.

find_path(PYTHIA8_INCLUDE_DIR
    NAMES Pythia8/Pythia.h
    PATH_SUFFIXES include
)

find_library(PYTHIA8_LIBRARY
    NAMES pythia8
    PATH_SUFFIXES lib lib64
)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Pythia8 DEFAULT_MSG
    PYTHIA8_LIBRARY PYTHIA8_INCLUDE_DIR)

if(Pythia8_FOUND AND NOT TARGET Pythia8::Pythia8)
    add_library(Pythia8::Pythia8 UNKNOWN IMPORTED)
    set_target_properties(Pythia8::Pythia8 PROPERTIES
        IMPORTED_LOCATION "${PYTHIA8_LIBRARY}"
        INTERFACE_INCLUDE_DIRECTORIES "${PYTHIA8_INCLUDE_DIR}"
    )
endif()

mark_as_advanced(PYTHIA8_INCLUDE_DIR PYTHIA8_LIBRARY)
