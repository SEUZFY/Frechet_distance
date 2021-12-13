

// Read from the csv file and store the two columns: one is x-axis and the other is y-axis


#ifndef _READ_CSV_
#define _READ_CSV_
#include <vector>

namespace read {

	/*
	struct Line {
		// structure that stores each line
		float x_axis; // the first column, stands for the x-axis
		float y_axis; // the second column, stands for the y-axis

		Line(float& x, float& y) :
			x_axis(x), y_axis(y) {}
	};*/

	struct Data {
		std::vector<float> data_vec;

		Data(int& nrows) {
			data_vec.reserve(nrows);
		}

		Data(){}

	};

}


#endif

