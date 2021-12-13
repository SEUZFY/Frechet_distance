// Frechet_distance.cpp: 定义应用程序的入口点。
//

#include "Frechet_distance.h"

//#include <iostream>
//#include <string>
//#include <vector>
//#include <fstream>
//#include <sstream>

#include "ReadCSV.h"

using namespace std;


int main()
{
	// 写文件
	/*
	ofstream outFile;
	outFile.open("data.csv", ios::out); // 打开模式可省略
	outFile << "name" << ',' << "age" << ',' << "hobby" << endl;
	outFile << "Mike" << ',' << 18 << ',' << "paiting" << endl;
	outFile << "Tom" << ',' << 25 << ',' << "football" << endl;
	outFile << "Jack" << ',' << 21 << ',' << "music" << endl;
	outFile.close();*/

	// 读文件
	ifstream inFile("D:/AlbertQ2/GEO1003/PatternMatch/files/loc1_each_timestamp.csv", ios::in);
	string lineStr;
	vector<vector<string>> strArray;
	while (getline(inFile, lineStr))
	{
		// 打印整行字符串
		//cout << lineStr << endl;
		// 存成二维表结构
		stringstream ss(lineStr);
		string str;
		vector<string> lineArray;
		// 按照逗号分隔
		while (getline(ss, str, ',')) {
			cout << str << " \n";
			lineArray.emplace_back(str);
		}
		strArray.emplace_back(lineArray);
	}
	cout << strArray[186][0];

	/*while (!strArray.empty()) {
		cout << strArray.back() << " ";
		strArray.pop_back();
	}*/
	return 0;
}
/*
————————————————
版权声明：本文为CSDN博主「踏莎行hyx」的原创文章，遵循CC 4.0 BY - SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https ://blog.csdn.net/u012234115/article/details/64465398*/
