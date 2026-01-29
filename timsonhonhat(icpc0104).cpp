#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; 
    cin >> t;
    while(t--) {
        string s;
        cin >> s;

        int minnum = INT_MAX;
        string temp = "";

        for(int i = 0; i < s.size(); i++) {
            if(isdigit(s[i])) {
                temp += s[i];
            } else {
                if(!temp.empty()) {
                    minnum = min(minnum, stoi(temp));
                    temp.clear();
                }
            }
        }

        // xử lý số ở cuối chuỗi
        if(!temp.empty()) {
            minnum = min(minnum, stoi(temp));
        }

        cout << minnum << endl;
    }
    return 0;
}
