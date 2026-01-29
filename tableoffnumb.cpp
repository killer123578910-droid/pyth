#include <bits/stdc++.h>
using namespace std;
void check(){
    int n,h,l;
    cin >> n >> h >> l;
    int demh=0;
    int deml=0;
    int cahai=0;
    for(int i=0; i<n; i++){
        int a; cin >> a;
        if(a<=h && a<=l) cahai++;
        else if(a<=h) demh++;
        else if(a<=l) deml++;
    }
    int tong=0;
    int layh= min(cahai, demh);
    tong +=layh;
    cahai-=layh;
    int layl = min(cahai,deml);
    tong +=layl;
    cahai-=layl;

    tong +=cahai/2;
    cout << tong << endl;

}
int main(){
    int t; cin >> t;
    while(t--){
        check();
    }
}