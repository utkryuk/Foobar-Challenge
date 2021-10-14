#include <bits/stdc++.h>
using namespace std;

// in-short-use macros

#define all(c) (c).begin(),(c).end()
#define ll long long int
#define ld long double
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define mod 1000000007
#define PI 3.14159265
#define sizes 1000010
//main function here

vector<vector<int> > dp(205, vector<int>(205));

int staircase(int prevhighest, int left){
    if(left == 0){
        return 1;
    }
    if (dp[prevhighest][left]){
        return dp[prevhighest][left];
    }
    int ans = 0;
    for(int i = prevhighest + 1; i <= left + 1; i++){
        ans += stair(i, left - 1);
    }
    dp[prevhighest][left] = ans;
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("C:/Users/saura/Desktop/cp/input.txt", "r", stdin);
    freopen("C:/Users/saura/Desktop/cp/output.txt", "w", stdout);
    #endif
    int n;
    cin>>n;
    cout << staircase(0, n) - 1;
    return 0;
}