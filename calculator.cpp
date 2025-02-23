#include <iostream>

using namespace std;

int main() {
    cout << "hello world" << endl;
    int number1, number2, val;
    char calc;

    printf("---C++ CALCULATOR---\n");
    printf("Enter your first number: ");
    scanf("%d", &number1);
    printf("Enter your operator: ");
    scanf(" %c", &calc);
    printf("Enter your second number: ");
    scanf("%d", &number2);

    if (calc == '+') {
        val = number1 + number2;
    } else if (calc == '-') {
        
        val = number1 - number2;
    } else if (calc == '/') {
        val = number1 / number2;
    } else if (calc == '*') {
        val = number1 * number2;
    } else {
        printf("invalid operator, please restart code.\n");
        return 1; // Exit with error
    }

    printf("%d\n", val);
    return 0;

}

