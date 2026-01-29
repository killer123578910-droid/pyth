#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;cin>>t;
    while(t--){
        char s1,s2;
        cin>>s1>>s2;
        string num1, num2;
        cin>>num1>>num2;
        int minn=INT_MAX,maxx=INT_MIN;
        if(s1>s2){
            swap(s1,s2);
        }
        string temp1,temp2;
        temp1=num1;
        temp2=num2;
        for(char &x:temp1){
            if(x==s2){
                x=s1;
            }
        }
         for(char &x:temp2){
            if(x==s2){
                x=s1;
            }
        }
        minn=stoi(temp1)+stoi(temp2);
        temp1=num1;
        temp2=num2;
        for(char &x:temp1){
            if(x==s1){
                x=s2;
            }
        }
         for(char &x:temp2){
            if(x==s1){
                x=s2;
            }
        }
        maxx=stoi(temp1)+stoi(temp2);
        cout<<minn<<" "<<maxx<<endl;
    }
    return 0;
}