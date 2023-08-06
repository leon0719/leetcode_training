#include <iostream>
using namespace std;


struct Node {
    int data;
    Node* next;
};

int main() {
    // 创建链表
    Node* head = new Node;
    head->data = 1;

    Node* node1 = new Node;
    node1->data = 2;

    Node* node2 = new Node;
    node2->data = 3;

    head->next = node1;
    node1->next = node2;
    node2->next = nullptr;

    // 使用指针遍历链表
    Node* current = head;
    while (current != nullptr) {
        cout << current->data << " ";
        current = current->next;
    }

    // 释放链表的内存
    while (head != nullptr) {
        Node* temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}
