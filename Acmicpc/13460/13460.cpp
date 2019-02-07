/*
 * ToDo
 * visited 배열을 활용하지 못하고 있음
 * R, B에 관계없이 bfs를 활용할 것
 */
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int Y, X;
vector<vector<char> > board;
vector<vector<bool> > visited;
queue<pair<int, int> > redQ;
queue<pair<int, int> > blueQ;

// 상 하 좌 우
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

int move(pair<int, int>& one, pair<int, int>& two, int dir) {
    int oneY = one.first;
    int oneX = one.second;
    bool finishOne = false;
    while(true) {
        int nextOneY = oneY + dy[dir];
        int nextOneX = oneX + dx[dir];
        // 범위를 벗어나면 탈락
        if(nextOneY < 0 || nextOneX < 0 || nextOneY >=Y || nextOneX >= X)
            break;
        // One이 골인을 했을 경우
        if(board[nextOneY][nextOneX] == 'O') {
            finishOne = true;
            break;
        }
        // .일 경우에만 이동 if(board[nextOneY][nextOneX] != '.')
        if(board[nextOneY][nextOneX] != '.')
            break;
        oneY = nextOneY;
        oneX = nextOneX;
    }

    // Two가 오지 못하도록 벽을 세운다.
    if(!finishOne)
        board[oneY][oneX] = 'X';

    int twoY = two.first;
    int twoX = two.second;
    bool finishTwo = false;

    while(true) {
        int nextTwoY = twoY + dy[dir];
        int nextTwoX = twoX + dx[dir];
        if(nextTwoY < 0 || nextTwoX < 0 || nextTwoY >=Y || nextTwoX >= X)
            break;
        if(board[nextTwoY][nextTwoX] == 'O') {
            finishTwo = true;
            break;
        }
        if(board[nextTwoY][nextTwoX] != '.')
            break;
        twoY = nextTwoY;
        twoX = nextTwoX;
    }
    //one을 원래대로 되돌린다
    if(!finishOne)
        board[oneY][oneX] = '.';

    if(finishOne && finishTwo)
        return -1;

    if(finishOne)
        return 1;

    if(finishTwo)
        return 2;

    // 이동 성공
    visited[oneY][oneX] = true;
    visited[twoY][twoX] = true;
    one.first = oneY;
    one.second = oneX;
    two.first = twoY;
    two.second = twoX;
    return 0;
}

void bfs() {
    // 굴리는 횟수가 10번이 넘어가면 실패로 처리한다.
    int cnt = 0;
    while(true) {
        int size = redQ.size();
        cnt++;
        if(cnt > 10) {
            cout << -1 << endl;
            return;
        }
        if(size==0) break;

        while(size) {
            pair<int, int> redP = redQ.front();
            redQ.pop();
            pair<int, int> blueP = blueQ.front();
            blueQ.pop();
            // 상하좌우로 R과 B를 굴려본다.
            int bestStatus = 0;
            for(int i = 0; i < 4; ++i) {
                // R와 B의 경우 같은 라인에 있다면 먼저 앞선 방향에 있는 공을 먼저 굴려야한다.
                pair<int, int> nextRedP = redP;
                pair<int, int> nextBlueP = blueP;
                int status;
                char one = 'B';

                if(i == 0 && redP.first > blueP.first)
                    status = move(nextBlueP, nextRedP, i);
                else if(i == 1 && redP.first < blueP.first)
                    status = move(nextBlueP, nextRedP, i);
                else if(i == 2 && redP.second > blueP.second)
                    status = move(nextBlueP, nextRedP, i);
                else if(i == 3 && redP.second < blueP.second)
                    status = move(nextBlueP, nextRedP, i);
                else {
                    status = move(nextRedP, nextBlueP, i);
                    one = 'R';
                }
                if((one == 'R' && status == 1) || (one == 'B' && status == 2)) {
                    cout << cnt << endl;
                    return;
                }
                else if (status == 0) {
                    redQ.push(nextRedP);
                    blueQ.push(nextBlueP);
                }
            }
            size--;
        }
    }
    cout << -1 << endl;
}

int main(void) {
    cin >> Y >> X;
    board.resize(Y, vector<char>(X));
    visited.resize(Y, vector<bool>(X, false));

    for(int y = 0; y < Y; ++y)
        for(int x = 0; x < X; ++x) {
            cin >> board[y][x];
            if(board[y][x] == 'R') {
                redQ.push(make_pair(y, x));
                visited[y][x] = true;
                board[y][x] = '.';
            }
            else if(board[y][x] == 'B') {
                blueQ.push(make_pair(y, x));
                visited[y][x] = true;
                board[y][x] = '.';
            }
        }

    bfs();

    return 0;
}
