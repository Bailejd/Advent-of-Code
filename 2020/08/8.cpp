#include <iostream>
#include <string>
#include <fstream>

class Node {
public:
    std::string op;
    std::string sign;
    int num;
    int times_exe;
    struct Node* prev;
    struct Node* next;
};

void print_list(Node *head) {
    Node* temp = head;
    while(temp != NULL) {
        std::cout << temp->op << " " << temp->sign << temp->num << " " << temp->times_exe << std::endl;
        temp = temp->next;
    }
    std::cout << "NULL" << std::endl;
}

int part_one(Node *head) {
    int acc = 0;
    Node* temp = head;

    while(temp != NULL) {
        if(temp->times_exe < 1) {
            if(temp->op == "nop") {
                temp->times_exe += 1;
                temp = temp->next;
            }
            else if(temp->op == "jmp") {
                std::string sign = temp->sign;
                int num = temp->num;
                temp->times_exe += 1;
                for(int i = 0; i < num; i++) {
                    if(sign == "+") {
                        temp = temp->next;
                    }
                    else if(sign == "-") {
                        temp = temp->prev;
                    }
                    else {
                        // Error
                        std::cout << "No sign(jmp)" << std::endl;
                    }
                }
            }
            else if(temp->op == "acc") {
                temp->times_exe += 1;
                if(temp->sign == "+") {
                    acc += temp->num;
                }
                else if(temp->sign == "-") {
                    acc -= temp->num;
                }
                else {
                    // Error
                    std::cout << "No sign(acc)" << std::endl;
                }
                temp = temp->next;
            }
        }
        else {
            return acc;
        }
    }

    return 1;
}

int part_two(Node *head) {
    int acc = 0;
    Node* temp = head;
    Node* swtch = head;

    while(swtch != NULL) {
        // Swap a jmp or nop
        bool changed = false;
        if(swtch->op == "jmp") {
            swtch->op = "nop";
            changed = true;
        }
        else if(swtch->op == "nop") {
            swtch->op = "jmp";
            changed = true;
        }

        // Check if valid
        while(temp != NULL && changed) {
            if(temp->times_exe < 1) {
                if(temp->op == "nop") {
                    temp->times_exe += 1;
                    temp = temp->next;
                }
                else if(temp->op == "jmp") {
                    std::string sign = temp->sign;
                    int num = temp->num;
                    temp->times_exe += 1;
                    for(int i = 0; i < num; i++) {
                        if(sign == "+") {
                            temp = temp->next;
                        }
                        else if(sign == "-") {
                            temp = temp->prev;
                        }
                        else {
                            std::cout << "Error" << std::endl;
                        }
                    }
                }
                else if(temp->op == "acc") {
                    if(temp->sign == "+") {
                        acc += temp->num;
                    }
                    else if(temp->sign == "-") {
                        acc -= temp->num;
                    }
                    else {
                        std::cout << "Error" << std::endl;
                    }
                    temp = temp->next;
                }
                else if(temp->op == "eof") {
                    return  acc;
                }
            }
            else {
                temp = NULL;
            }
        }

        // Swap back
        if(swtch->op == "jmp") {
            swtch->op = "nop";
        }
        else if(swtch->op == "nop") {
            swtch->op = "jmp";
        }

        // Move swtch
        swtch = swtch->next;

        // Reset
        temp = head;
        while(temp != NULL) {
            temp->times_exe = 0;
            temp = temp->next;
        }
        temp = head;
        acc = 0;
    }

    return 1;
}

int main() {
    std::ifstream infile("./input.txt");
    Node* head = NULL;
    Node* last = NULL;
    
    std::string line;
    while(getline(infile, line)) {
        Node* new_node = (Node*)malloc(sizeof(Node));
        std::string temp_op = line.substr(0,3);
        std::string temp_sign = line.substr(4,1);
        int temp_num = stoi(line.substr(5));
        new_node->op = temp_op;
        new_node->sign = temp_sign;
        new_node->num = temp_num;
        new_node->times_exe = 0;

        if(head == NULL) {
            new_node->next = NULL;
            new_node->prev = NULL;
            head = new_node;
            last = new_node;
        }
        else {
            last->next = new_node;
            new_node->next = NULL;
            new_node->prev = last;
            last = new_node;
        }

    }

    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->op = "eof";
    last->next = new_node;
    new_node->next = NULL;
    new_node->prev = last;
    last = new_node;

    int result1 = part_one(head);
    std::cout << "Part 1: " << result1 << std::endl;

    int result2 = part_two(head);
    std::cout << "Part 2: " << result2 << std::endl;

    return 0;
}
