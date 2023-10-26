#include <iostream>
#include <vector>

// 定义游戏板
std::vector<std::vector<char> > board(3, std::vector<char>(3, ' '));


// 函数声明
void printBoard();
bool makeMove(char player, int row, int col);
bool checkWin(char player);
bool checkDraw();

int main() {
    char currentPlayer = 'X';
    bool gameWon = false;
    int row, col;

    std::cout << "欢迎来到井字游戏！" << std::endl;

    while (!gameWon && !checkDraw()) {
        printBoard();

        // 获取玩家输入
        std::cout << "玩家 " << currentPlayer << "，请输入行和列（例如：1 2）: ";
        std::cin >> row >> col;

        // 检查是否有效移动
        if (row < 0 || row >= 3 || col < 0 || col >= 3 || board[row][col] != ' ') {
            std::cout << "无效的移动，请重试。" << std::endl;
            continue;
        }

        // 执行玩家的移动
        if (!makeMove(currentPlayer, row, col)) {
            std::cout << "无效的移动，请重试。" << std::endl;
            continue;
        }

        // 检查是否获胜
        if (checkWin(currentPlayer)) {
            printBoard();
            std::cout << "玩家 " << currentPlayer << " 获胜！恭喜！" << std::endl;
            gameWon = true;
        } else {
            // 切换玩家
            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }
    }

    if (!gameWon) {
        printBoard();
        std::cout << "游戏平局。" << std::endl;
    }

    return 0;
}

// 打印游戏板
void printBoard() {
    std::cout << "  0 1 2" << std::endl;
    for (int i = 0; i < 3; i++) {
        std::cout << i << " ";
        for (int j = 0; j < 3; j++) {
            std::cout << board[i][j];
            if (j < 2) {
                std::cout << "|";
            }
        }
        std::cout << std::endl;
        if (i < 2) {
            std::cout << "  -+-+-" << std::endl;
        }
    }
}

// 执行玩家的移动
bool makeMove(char player, int row, int col) {
    if (board[row][col] == ' ') {
        board[row][col] = player;
        return true;
    }
    return false;
}

// 检查是否获胜
bool checkWin(char player) {
    // 检查行和列
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
            return true;
        }
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) {
            return true;
        }
    }

    // 检查对角线
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) {
        return true;
    }
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) {
        return true;
    }

    return false;
}

// 检查是否平局
bool checkDraw() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') {
                return false; // 存在空格，游戏尚未平局
            }
        }
    }
    return true; // 所有格子都被占满，游戏平局
}
