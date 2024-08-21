#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        string expr;
        cin >> expr;

        string modifiedExpr;
        for (int i = 0; i < expr.length(); i++) {
            if (islower(expr[i])) {
                modifiedExpr += expr[i];
            } else {
                modifiedExpr += expr[i + 1];
                modifiedExpr += expr[i];
                i++;
            }
        }

        cout << modifiedExpr << endl;
    }

    return 0;
}
