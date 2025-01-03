#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
int N, M, Q;

struct Folder {
    string fName;
    Folder *parent;
    unordered_set<Folder*> cFolders;
    unordered_set<string> files;

    Folder() {
        fName = "";
        cFolders.clear();
        files.clear();
    }

    Folder(string name) {
        fName = name;
        parent = nullptr;
    }

    ~Folder() {
        cFolders.clear();
        files.clear();
        fName.clear();
        parent = nullptr;
    }
};

Folder *root = new Folder("main");
unordered_map<string, Folder*> DB;

// 1. addFolder
// DB map에 존재 여부 확인 후 추가
// 부모, 자식 폴더 사이의 pointer, set 관계 연결
void addFolder(string parentName, string nowName) {
    Folder *folder = nullptr;
    if(DB.find(nowName) == DB.end()) {
        folder = new Folder(nowName);
        DB[nowName] = folder;
    }
    folder = DB[nowName];

    Folder *parentFolder = nullptr;
    if(DB.find(parentName) == DB.end()) {
        parentFolder = new Folder(parentName);
        DB[parentName] = parentFolder;
    }
    parentFolder = DB[parentName];

    folder->parent = parentFolder;
    parentFolder->cFolders.insert(folder);

}

// 2. addFile
// 현재 folderName이 DB에 존재하는지 확인
// 확인 후, DB 포인터 연결 + set에 추가
void addFile(string folderName, string fileName) {
    Folder *folder = nullptr;
    if(DB.find(folderName) == DB.end()) {
        folder = new Folder(folderName);
        DB[folderName] = folder;
    }
    folder = DB[folderName];
    folder->files.insert(fileName);
}

// 결과 출력을 위한 dfs & printRet 함수
void dfs(Folder *cur, unordered_map<string, int> &ret) {
    for(string fileName: cur->files) ret[fileName]++;
    for(Folder* nxt: cur->cFolders) dfs(nxt, ret);
}

pii printRet(string name) {
    Folder *folder = DB[name];
    unordered_map<string, int> ret;
    dfs(folder, ret);

    int sum =0;
    for (auto [key, cnt]: ret) sum += cnt;
    return make_pair(ret.size(), sum);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> M;
    string P, F;
    int C;

    for(int i=0; i<N+M; ++i) {
        cin >> P >> F >> C;
        if(C==1) addFolder(P, F);
        else addFile(P, F);
    }

    cin >> Q;
    for(int i=0; i<Q; ++i) {
        string q;
        cin >> q;

        istringstream iss(q);
        string buf;
        while(getline(iss, buf, '/')){}

        pii ret = printRet(buf);
        cout << ret.first << " " << ret.second << "\n";
    }
    return 0;
}