cmake_minimum_required(VERSION 3.22)
project(computacao_distribuida C)

set(CMAKE_C_STANDARD 11)

#add_executable(computacao_distribuida
#        lab01/client.c
#        lab01/server.c)

add_executable(client lab01/client.c)
add_executable(server lab01/server.c)