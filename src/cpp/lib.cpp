#include <iostream>

extern "C" void showNumbers(int n1, int n2) {
    int n3 = n1 + n2;
    printf("the sum is: %d\n", n3);
}

extern "C" void subNumbers(int n1, int n2) {
    int n3 = n1 - n2;
    printf("the sub is: %d\n", n3);
}