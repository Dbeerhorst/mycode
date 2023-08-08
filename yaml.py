---
- name: Tuesday Challenge
  hosts: planet express
  gather_facts: no

  tasks:
   - name: creating a file
     copy:
        dest: challenge/challengefile.txt
        content: "Success!"
       
   - name: create a directory
     file:
       path: challenge
       state: directory

