class Solution {
public:
    // 2, 3, 5의 소수만으로 이루어진 수를 찾아야한다.
    bool ans[1690];
    void Eratos(int n)
    {
        if (n <= 1) return;
	    for (int i = 2; i * i <= n; i++)
	    {
		    if (ans[i]==false)
			    for (int j = i * 2; j <= n; j += i) {
                    if(j >= 1690)
                        break;
			        ans[j] = true;
                }
	    }
        return;
    }
    void che(int s, int val, bool turn) {
        while(s < 1690) {
            ans[s] = turn;
            s += val;
        }
        return;
    }
    int nthUglyNumber(int n) {
        for(int i = 0; i < 1690; ++i)
            ans[i] = false;
        Eratos(1690);
        che(2, 2, false);
        che(3, 3, false);
        che(5, 5, false);
        int cnt = 0;
        for(int i = 1; i < 1690; i++) {
            if(ans[i]==false) {
                cnt++;
                cout << i << endl;
            }
            if(cnt == n)
                return i;
        }
        return -1;
    }
};
