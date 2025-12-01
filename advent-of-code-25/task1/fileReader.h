#include <string>

#ifndef FILEREADER_H
#define FILEREADER_H

namespace 
{
    public:
        int readFile(const string& filePath);

    private:
        string line_;
        int currentNumber_;
        int zeroCount_;
}


#endif // FILEREADER_H
