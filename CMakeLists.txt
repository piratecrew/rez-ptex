CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)
include(IlpHelpers)

set(ptex_version v${PTEX_VERSION})

set(url_ptex https://github.com/wdas/ptex.git)

ExternalProject_add(
    ptex
    GIT_REPOSITORY ${url_ptex}
    GIT_TAG ${ptex_version}
    PREFIX ptex
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND make -C ${PROJECT_BINARY_DIR}/ptex/src/ptex/src
    INSTALL_COMMAND ""
)

install(DIRECTORY 
    ${CMAKE_BINARY_DIR}/ptex/src/ptex/install/bin
    ${CMAKE_BINARY_DIR}/ptex/src/ptex/install/include
    ${CMAKE_BINARY_DIR}/ptex/src/ptex/install/lib
    DESTINATION .)

rez_install_files(
    cmake/ptex.cmake
    DESTINATION .
)
