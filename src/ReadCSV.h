

// Read from the csv file and store the two columns: one is x-axis and the other is y-axis


#ifndef _READ_CSV_
#define _READ_CSV_

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

namespace read {

	struct Line {
		// structure that stores each line
		float x_axis; // the first column, stands for the x-axis
		float y_axis; // the second column, stands for the y-axis

		Line(float& x, float& y) :
			x_axis(x), y_axis(y) {}
	};

	struct Data {
		std::vector<Line> data;

		Data(int& nrows) {
			data.reserve(nrows);
		}

		Line* get_line(int& row) {
			return (row >= 0 && row < data.size()) ? (&data[row]) : nullptr;
		}

	};

}


#endif

