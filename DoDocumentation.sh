#!/bin/bash

doxygen Doxyfile;open Documentation/html/index.html;make -f Documentation/latex/Makefile;open Documentation/latex/refman.pdf





