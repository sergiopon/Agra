#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    int S, W, C, K, M;
    while (cin >> S >> W >> C >> K >> M) {
        int total_time = 0;
        int total_resource = 0;
        int robots = 0;
        int next_robot_time = M;

        priority_queue<int, vector<int>, greater<int>> work_queue;

        while (total_resource < 10000) {
            // Construir robots
            if (robots < K && total_time >= next_robot_time) {
                robots++;
                next_robot_time += M;
            }

            // Asignar trabajo a los robots disponibles
            for (int i = 0; i < robots; ++i) {
                work_queue.push(total_time + S + W);
            }

            // Procesar trabajos completados
            while (!work_queue.empty() && work_queue.top() <= total_time) {
                work_queue.pop();
                total_resource += C;
            }

            total_time++;
        }

        cout << total_time << endl;
    }
    return 0;
}