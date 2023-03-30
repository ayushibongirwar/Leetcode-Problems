struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const{
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ hash2 ;
    }
};

class Solution {
    typedef pair<int,int> pii;
public:
    int maxPoints(vector<vector<int>>& p) {
        int n = p.size(), mx,my,x2,y2 ,ans = 0;
        for(int i = 0;i<n;i++){
            unordered_map<pii,int, hash_pair> mp;
            for(int j = 0;j<n;j++){
                if(i==j) continue;
                my = p[j][1]-p[i][1], mx = p[j][0]-p[i][0];
                int x = __gcd(my,mx);
                ans = max(ans,++mp[{my/x,mx/x}]);
            }
        }
        return ans+1;
    }
};
