# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Werror -g std=c++20

# For deleting the target 
TARGET_DEL = main.exe

# Source files

# Object files
OBJS = $(STCS:.cpp.o)

# Default rule to build and run the executable
all: $(TARGET) run

# Rule to link object filess into the target executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Rule to compile .cpp files into .o files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Rule to run the executablen
run: $(TARGET)
	$(TARGET)

# Clean rule to remove generated files
clean:
	del $(TARGET_DEL) $(OBJS)