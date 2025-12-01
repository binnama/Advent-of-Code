
#include <fstream>
#include <fileReader.h>

// The arrow starts at 50
// Need to count everytime the is 0 at the end of a step
// Need to split each line in the code into L/R and the number
// L = negative rotation
// R = positive rotation

// If the number passes 0 while moving left (negative), 
// the number continues to tick down from 99
// Same if the number increases past 99, next is 0


int readFile(cost string& filePath)
{
    ifstream file(filePath);

    if (file.is_open())
    {
        while (getline(file, line_))
        {

        }
    }

}