/*Inspired by: 
 * https://blog.csdn.net/u012234115/article/details/64465398
 * 
 */

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cstring>

#include "Frechet_distance.h"
#include "ReadCSV.h"

//using namespace std;


int main()
{
	// read files
	std::ifstream in_file("D:/AlbertQ2/GEO1003/PatternMatch/files/loc1_each_timestamp.csv", std::ios::in);
	std::string line_str;

	read::Data mydata;

	while (getline(in_file, line_str)) // read each line
	{
		std::stringstream ss(line_str);
		std::string str;
		std::vector<std::string> lineArray;

		while (getline(ss, str, ',')) { // for each line, split it with ','

			const char* p(str.data());
			float num((float)strtod(p, NULL)); // convert to float
			mydata.data_vec.emplace_back(num);
		}
		
	}
	std::cout << mydata.data_vec[2];

	return 0;
}
