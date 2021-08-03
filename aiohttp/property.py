# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         # self.gotmarks = self.name + self.marks
#     @property
#     def gotmarks(self):
#         return self.name + self.marks
#     def print_str(self):
#         return self.name + self.marks

# st = Student("trung", '22')
# st.name = 'lim'
# print(st.gotmarks)
# print(st.print_str())

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     @property
#     def gotmarks(self):
#         return self.name + self.marks
    
#     @gotmarks.setter
#     def gotmarks(self, sentence):
#         name, rand, marks = sentence.split(' ')
#         self.name = name
#         self.marks = marks
# st = Student('trung', '22')
# print(st.name)
# st.name = 'lan'
# print(st.name)