#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>

using namespace std;

struct Node {
  string dir;
  Node* parent;
  unordered_map<string, Node*> children;
  unordered_map<string, int> files;
  int dirSize = 0;
  Node(string dir, Node* parent) : dir(dir), parent(parent) {}
};

int computeDirSize(Node* node) {
  int dirSize = 0;
  for (auto& it : node->files) dirSize += it.second;
  for (auto& it : node->children) dirSize += computeDirSize(it.second);
  node->dirSize = dirSize;
  return dirSize;
}

Node* readFileSystem() {
  string line;
  ifstream file("../data/7.in");

  auto root = new Node("/", nullptr);
  auto curr = root;

  while (getline(file, line)) {
    auto prefix = line.substr(0, 4);
    if (prefix == "$ cd") {
      auto dir = line.substr(5);
      if (dir == "..") {
        curr = curr->parent;
      } else if (dir != "/") {
        curr->children[dir] = new Node(dir, curr);
        curr = curr->children[dir];
      }
    } else if (isdigit(line[0])) {
      auto bytes = stoi(line.substr(0, line.find(" ")));
      auto filename = line.substr(line.find(" ") + 1);
      curr->files[filename] = bytes;
    }
  }
  file.close();
  computeDirSize(root);
  return root;
}

int totalSizeSmallDirs(const Node* node) {
  int size = 0;
  for (auto& it : node->children) {
    size += totalSizeSmallDirs(it.second);
  }
  return size + (node->dirSize <= 100000 ? node->dirSize : 0);
}

int dirToDelete(const Node* root) {
  int needsToFree = root->dirSize - 40000000;
  const Node* best = nullptr;
  queue<const Node*> q;
  q.push(root);
  while (!q.empty()) {
    auto curr = q.front();
    q.pop();
    for (auto& it : curr->children) q.push(it.second);
    if (curr->dirSize >= needsToFree) {
      if (best == nullptr || curr->dirSize < best->dirSize) {
        best = curr;
      }
    }
  }
  return best->dirSize;
}

int main() {
  auto root = readFileSystem();
  cout << "Part 1: " << totalSizeSmallDirs(root) << endl;
  cout << "Part 2: " << dirToDelete(root) << endl;
}