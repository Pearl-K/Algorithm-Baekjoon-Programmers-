#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

struct Album {
    string name; // 현재 앨범 이름
    set<string> photos; // 사진 저장 (사전순 정렬, 중복 방지)
    map<string, Album*> subAlbums; // 하위 앨범 저장 (사전순 정렬)
    Album* parent; // 상위 앨범 (nullptr 이면 최상위 앨범)

    // 생성자
    Album(string name, Album* parent = nullptr)
            : name(name), parent(parent) {}

    // 소멸자
    ~Album() {
        for (auto& [_, album] : subAlbums) {
            delete album; // 하위 앨범 메모리 해제
        }
    }
};

struct AlbumManager {
    Album* root;
    Album* current;

    // 생성자: 최상위 앨범 생성
    AlbumManager() {
        root = new Album("album");
        current = root;
    }

    // 소멸자: 최상위 앨범 메모리 해제
    ~AlbumManager() {
        delete root;
    }

    void mkalb(const string& name) {
        if (current->subAlbums.count(name)) {
            cout << "duplicated album name\n";
            return;
        }
        current->subAlbums[name] = new Album(name, current);
    }

    void rmalb(const string& name) {
        if (name == "-1" || name == "0" || name == "1") {
            rmalbByOrder(name);
            return;
        }

        auto it = current->subAlbums.find(name);
        if (it == current->subAlbums.end()) {
            cout << "0 0\n";
            return;
        }

        int albumCount = 0, photoCount = 0;
        countAlbumAndPhotos(it->second, albumCount, photoCount);

        delete it->second;
        current->subAlbums.erase(it);
        cout << albumCount << " " << photoCount << "\n";
    }

    void insert(const string& name) {
        if (current->photos.count(name)) {
            cout << "duplicated photo name\n";
            return;
        }
        current->photos.insert(name);
    }

    void deletePhoto(const string& name) {
        if (name == "-1" || name == "0" || name == "1") {
            deletePhotoByOrder(name);
            return;
        }

        auto it = current->photos.find(name);
        if (it == current->photos.end()) {
            cout << "0\n";
            return;
        }
        current->photos.erase(it);
        cout << "1\n";
    }

    void ca(const string& name) {
        if (name == "/") {
            current = root;
        } else if (name == "..") {
            if (current->parent) {
                current = current->parent;
            }
        } else {
            auto it = current->subAlbums.find(name);
            if (it != current->subAlbums.end()) {
                current = it->second;
            }
        }
        cout << current->name << "\n";
    }

    void countAlbumAndPhotos(Album* album, int& albumCount, int& photoCount) {
        albumCount++;
        photoCount += album->photos.size();

        for (auto& [_, subAlbum] : album->subAlbums) {
            countAlbumAndPhotos(subAlbum, albumCount, photoCount);
        }
    }

    void rmalbByOrder(const string& order) {
        if (current->subAlbums.empty()) {
            cout << "0 0\n";
            return;
        }

        Album* target = nullptr;
        if (order == "-1") {
            target = current->subAlbums.begin()->second;
        } else if (order == "1") {
            target = current->subAlbums.rbegin()->second;
        } else if (order == "0") {
            int totalAlbums = 0, totalPhotos = 0;
            for (auto& [_, album] : current->subAlbums) {
                countAlbumAndPhotos(album, totalAlbums, totalPhotos);
                delete album;
            }
            current->subAlbums.clear();
            cout << totalAlbums << " " << totalPhotos << "\n";
            return;
        }

        int albumCount = 0, photoCount = 0;
        countAlbumAndPhotos(target, albumCount, photoCount);

        current->subAlbums.erase(target->name);
        delete target;

        cout << albumCount << " " << photoCount << "\n";
    }

    void deletePhotoByOrder(const string& order) {
        if (current->photos.empty()) {
            cout << "0\n";
            return;
        }

        if (order == "-1") {
            current->photos.erase(current->photos.begin());
        } else if (order == "1") {
            current->photos.erase(prev(current->photos.end()));
        } else if (order == "0") {
            int photoCount = current->photos.size();
            current->photos.clear();
            cout << photoCount << "\n";
            return;
        }
        cout << "1\n";
    }
};

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int N;
    cin >> N;

    AlbumManager manager;

    while (N--) {
        string comm, arg;
        cin >> comm;
        
        if (comm == "mkalb" || comm == "rmalb" || comm == "insert" || comm == "delete" || comm == "ca") {
            cin >> arg;
            if (comm == "mkalb") manager.mkalb(arg);
            else if (comm == "rmalb") manager.rmalb(arg);
            else if (comm == "insert") manager.insert(arg);
            else if (comm == "delete") manager.deletePhoto(arg);
            else if (comm == "ca") manager.ca(arg);
        }
    }
    
    return 0;
}