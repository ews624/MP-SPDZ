# CMake generated Testfile for 
# Source directory: /home/ethan/Documents/GitHub/MP-SPDZ/cmake-3.24.1
# Build directory: /home/ethan/Documents/GitHub/MP-SPDZ/cmake-3.24.1
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
include("/home/ethan/Documents/GitHub/MP-SPDZ/cmake-3.24.1/Tests/EnforceConfig.cmake")
add_test([=[SystemInformationNew]=] "/home/ethan/Documents/GitHub/MP-SPDZ/cmake-3.24.1/bin/cmake" "--system-information" "-G" "Unix Makefiles")
set_tests_properties([=[SystemInformationNew]=] PROPERTIES  _BACKTRACE_TRIPLES "/home/ethan/Documents/GitHub/MP-SPDZ/cmake-3.24.1/CMakeLists.txt;896;add_test;/home/ethan/Documents/GitHub/MP-SPDZ/cmake-3.24.1/CMakeLists.txt;0;")
subdirs("Source/kwsys")
subdirs("Utilities/std")
subdirs("Utilities/KWIML")
subdirs("Utilities/cmlibrhash")
subdirs("Utilities/cmzlib")
subdirs("Utilities/cmcurl")
subdirs("Utilities/cmnghttp2")
subdirs("Utilities/cmexpat")
subdirs("Utilities/cmbzip2")
subdirs("Utilities/cmzstd")
subdirs("Utilities/cmliblzma")
subdirs("Utilities/cmlibarchive")
subdirs("Utilities/cmjsoncpp")
subdirs("Utilities/cmlibuv")
subdirs("Source")
subdirs("Utilities")
subdirs("Tests")
subdirs("Auxiliary")
