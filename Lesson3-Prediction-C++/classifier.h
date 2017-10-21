#ifndef CLASSIFIER_H
#define CLASSIFIER_H
#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>

#define N_LABELS 3
#define N_VARS 4

using namespace std;

class GNB {
private:
  vector<string> possible_labels = {"left","keep","right"};

  double means[N_LABELS][N_VARS];
  double stds[N_LABELS][N_VARS];

  int getIndex(const string & label);

public:

	/**
  	* Constructor
  	*/
 	GNB();

	/**
 	* Destructor
 	*/
 	virtual ~GNB();

 	void train(vector<vector<double> > data, vector<string>  labels);

  	string predict(const vector<double>& observation);

};

#endif



