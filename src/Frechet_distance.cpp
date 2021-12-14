/*Inspired by: 
 * https://blog.csdn.net/u012234115/article/details/64465398
 * 
 */

#include <iostream>
#include "Frechet_distance.h"
#include "ReadCSV.h"


int main()
{
	// read files
	read::MyData mydata;
	read::read_csv("D:/AlbertQ2/GEO1003/PatternMatch/files/loc1_each_timestamp.csv", mydata);
	std::cout << mydata.data_vec.size();

	return 0;
}
