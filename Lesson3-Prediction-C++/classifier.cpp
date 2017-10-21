#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <numeric>
#include <map>
#include <cmath>
#include "classifier.h"

using namespace std;

double gaussian_prob(double obs, double mu, double sigma) {
  double num = (obs - mu) * (obs - mu);
  double denum = 2. * sigma * sigma;
  double norm = 1. / sqrt(M_PI * denum);
  return norm * exp(-num / denum);
}

vector<double> preprocess(vector<double> vars) {
  //vars[0]=fmod(vars[0], 4.);
  return vars;
}

/**
  * Constructor
  */
GNB::GNB() = default;

/**
 	* Destructor
 	*/
GNB::~GNB() = default;

int GNB::getIndex(const string &label) {
  for (int i = 0; i < N_LABELS; i++) {
    if (label == possible_labels[i]) {
      return i;
    }
  }
  return -1;
}

void GNB::train(vector<vector<double> > data, vector<string> labels) {
  // Sort datapoints per variable and labels
  vector<double> points[N_LABELS][N_VARS];
  for (int n = 0; n < data.size(); n++) {
    int label = getIndex(labels[n]);
    const vector<double> &measurement = preprocess(data[n]);

    for (int j = 0; j < N_VARS; j++) {
      points[label][j].push_back(measurement[j]);
    }
  }

  // Calculate mean and variances for each variable and label
  for (int i = 0; i < N_LABELS; i++) {
    for (int j = 0; j < N_VARS; j++) {
      const vector<double> &v = points[i][j];

      double sum = std::accumulate(v.begin(), v.end(), 0.0);
      double mean = sum / v.size();

      double sq_sum = std::inner_product(v.begin(), v.end(), v.begin(), 0.0);
      double stdev = std::sqrt(sq_sum / v.size() - mean * mean);

      means[i][j] = mean;
      stds[i][j] = stdev;
    }
  }
}

string GNB::predict(const vector<double>& observation) {
  vector<double> vars = preprocess(observation);

  // Calculate probability for each class
  double probs[N_LABELS];
  for (int i = 0; i < N_LABELS; i++) {
    double prob = 1.;
    for (int j = 0; j < N_VARS; j++) {
      prob *= gaussian_prob(vars[j], means[i][j], stds[i][j]);
    }
    probs[i] = prob;
  }

  // Find largest probability
  int max_label = 0;
  double max_prob = probs[0];
  for (int i = 1; i < N_LABELS; i++) {
    if(probs[i]>max_prob) {
      max_prob=probs[i];
      max_label=i;
    }
  }

  cout << max_prob << endl;
  // Return associated label
  return possible_labels[max_label];
}
