#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        int w;cin>>w;
        vector<int> weig(n+1),val(n+1);
        for(int i=1;i<=n;i++){
            int x,y;
            cin>>x>>y;
            weig[i]=x;
            val[i]=y;
        }
        vector<int> dp(w+1,0);
        for(int i=1;i<=n;i++){
            for(int j=w;j>=weig[i];j--){
                dp[j]=max(dp[j],val[i]+dp[j-weig[i]]);
            }
        }
        cout<<dp[w]<<endl;
    }
    return 0;
}