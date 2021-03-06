INCLUDE(ExternalProject)
SET(OPTIONAL_ARGS
    "-DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}"
    "-DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}"
    "-DCMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}"
    "-DCMAKE_C_FLAGS=${CMAKE_C_FLAGS}"
     "-Dprotobuf_WITH_ZLIB=ON"
     "-DZLIB_ROOT:FILEPATH=${ZLIB_ROOT}"
      ${EXTERNAL_OPTIONAL_ARGS})

SET(OPTIONAL_CACHE_ARGS "-DZLIB_ROOT:STRING=${ZLIB_ROOT}")
SET(PROTOBUF_REPO "https://gitee.com/berlinfog/protobuf.git")
SET(PROTOBUF_TAG "v3.1.0")
IF(USE_TENSORFLOW)
    SET(PROTOBUF_TAG "v3.5.0")
ENDIF()
SET(PROTOBUF_SOURCES_DIR ${THIRD_PARTY_PATH}/protobuf)
SET(PROTOBUF_INSTALL_DIR ${THIRD_PARTY_PATH})

ExternalProject_Add(
    extern_protobuf
    ${EXTERNAL_PROJECT_LOG_ARGS}
    DEPENDS             extern_zlib
    GIT_REPOSITORY      ${PROTOBUF_REPO}
    GIT_TAG             ${PROTOBUF_TAG}
    PREFIX              ${PROTOBUF_SOURCES_DIR}
    CONFIGURE_COMMAND   cd <SOURCE_DIR> && ${CMAKE_COMMAND} -DCMAKE_SKIP_RPATH=ON
                        -Dprotobuf_BUILD_TESTS=OFF
                        -DCMAKE_POSITION_INDEPENDENT_CODE=ON
                        -DCMAKE_INSTALL_PREFIX=${PROTOBUF_INSTALL_DIR}
                        -DCMAKE_INSTALL_LIBDIR=lib ./cmake
    BUILD_COMMAND       cd <SOURCE_DIR> && make -j8 && make install
    UPDATE_COMMAND      ""
    INSTALL_COMMAND     ""
)

add_custom_command(TARGET extern_protobuf POST_BUILD
    COMMAND cp ${PROTOBUF_INSTALL_DIR}/bin/protoc ${PROTOBUF_INSTALL_DIR}/lib
)
