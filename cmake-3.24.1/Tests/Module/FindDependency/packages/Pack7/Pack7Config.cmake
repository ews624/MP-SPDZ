if(NOT Pack7_FOUND)
  set(Pack7_FOUND 1)
  add_library(Pack7::Pack7 INTERFACE IMPORTED)
  set_property(TARGET Pack7::Pack7 PROPERTY INTERFACE_COMPILE_DEFINITIONS HAVE_PACK7)
endif()

foreach(module ${Pack7_FIND_COMPONENTS})
  if(module STREQUAL "Comp1")
    add_library(Pack7::Comp1 INTERFACE IMPORTED)
    set_property(TARGET Pack7::Comp1 PROPERTY INTERFACE_COMPILE_DEFINITIONS HAVE_PACK7_COMP1)
    set_property(TARGET Pack7::Comp1 PROPERTY INTERFACE_LINK_LIBRARIES Pack7::Pack7)
    set(Pack7_Comp1_FOUND 1)
  endif()
endforeach()