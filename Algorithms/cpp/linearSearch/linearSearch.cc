// Copyright 2023 Arshia Eslami


#include<iostream>
#include<random>

using std::cin;
using std::cout;

int main(){
  cout << "hi"; 
  int n;
  cin >> n ;
  int array[n];
  for ( int i = 0; i < n; ++i ) {
    cin >> array[i]; 
  }

  for ( int i = 0; i < n; ++i ) {
    cout << array[i];
  }
  
  return 0;
}



