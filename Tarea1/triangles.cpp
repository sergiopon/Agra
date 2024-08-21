#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    while (true) {
        int n;
        cin >> n;
        if (n == 0) break;

        vector<long long> arcs(n); // Usar long long para evitar desbordamientos
        for (int i = 0; i < n; i++) {
            cin >> arcs[i];
        }

        vector<long long> cum_arc(n + 1);
        for (int i = 1; i <= n; i++) {
            cum_arc[i] = cum_arc[i - 1] + arcs[i - 1];
        }

        long long count = 0;
        for (int i = 0; i < n; i++) {
            long long base = arcs[i];
            unordered_map<long long, int> freq;
            for (int j = i + 1; j < i + n; j++) {
                long long diff = cum_arc[j % n + 1] - cum_arc[i];
                if (diff == base * 3) {
                    count++;
                }
                freq[diff]++;
            }
        }

        cout << count << endl;
    }
    return 0;
}