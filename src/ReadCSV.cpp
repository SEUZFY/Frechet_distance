#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cstring>

#include "ReadCSV.h"

void read::read_csv(const char* path, MyData& mydata)
{
	std::ifstream in_file(path, std::ios::in);
	std::string line_str;

	while (getline(in_file, line_str)) // read each line
	{
		std::stringstream ss(line_str);
		std::string str;

		while (getline(ss, str, ',')) { // for each line, split it with ','
			const char* p(str.data());
			float num((float)strtod(p, NULL)); // convert to float
			mydata.data_vec.emplace_back(num);
		}

	}
}
