// Copyright 2023 Arshia Eslami

#include<iostream>
#include<random>
using std::cin;
using std::cout;

int main() {
  cout << "hi";
  int n;
  int ans;
  cin >> n;
  int array[n];
  for ( int i = 0; i < n; ++i ) {
    cin >> array[i];
  }
  int target;
  cin >> target;
  for ( int i = 0; i < n; ++i ) {
    if ( array[i] == target ) {
      ans = i;
      break;
    }
  }
  cout << ans;

  return 0;
}



