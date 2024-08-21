#include <iostream>
#include <vector>
#include <string>
#include <sstream> 

using namespace std;

bool puedeMover(const string &carta1, const string &carta2) {
    return carta1[0] == carta2[0] || carta1[1] == carta2[1];
}
void jugar(vector<string> &cartas) {
    vector<vector<string>> pilas;
    
    for (const string &carta : cartas) {
        pilas.push_back({carta});
    }

    bool movido;
    do {
        movido = false;
        for ( int i = 0; i < pilas.size(); ++i) {
            if (i >= 3 && puedeMover(pilas[i].back(), pilas[i - 3].back())) {
                pilas[i - 3].push_back(pilas[i].back());
                pilas[i].pop_back();
                if (pilas[i].empty()) {
                    pilas.erase(pilas.begin() + i);
                }
                movido = true;
                break;
            } else if (i >= 1 && puedeMover(pilas[i].back(), pilas[i - 1].back())) {
                pilas[i - 1].push_back(pilas[i].back());
                pilas[i].pop_back();
                if (pilas[i].empty()) {
                    pilas.erase(pilas.begin() + i);
                }
                movido = true;
                break;
            }
        }
    } while (movido);

    cout << pilas.size() << " piles"  << " remaining" << ":";
    for (const auto &pila : pilas) {
        cout << " " << pila.size();
    }
    cout << endl;
}

int main() {
    string linea;
    while (getline(cin, linea) && linea[0] != '#') {
        vector<string> cartas;
        string carta;
        
        for (int i = 0; i < 2; ++i) {
            istringstream iss(linea);
            while (iss >> carta) {
                cartas.push_back(carta);
            }
            if (i == 0) {
                getline(cin, linea);
            }
        }
        jugar(cartas);
    }
    return 0;
}
