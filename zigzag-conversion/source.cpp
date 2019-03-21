class Solution {
public:
    string convert(string s, int numRows) {
        vector<vector<int> > zigzag;
        zigzag.resize(numRows);

        int step = 0, maxIndex = numRows - 1;
        bool booho = true;
        string ans;

        for(int i = 0; i < s.length(); ++i) {
            zigzag[step].push_back(s[i]);

            // numRows가 1인 경우는 증가하면 안됨.
            if (booho && step < maxIndex)
                step++;
            else if (!booho && step > 0)
                step--;

            // 끝에 도달했다면, 부호를 변경
            if (step == 0 || step == maxIndex)
                booho = !booho;
        }

        for(int i = 0; i < zigzag.size(); ++i) {
            for(int j = 0; j < zigzag[i].size(); ++j)
                ans += zigzag[i][j];
        }
        return ans;
    }
};
