# library_manager_system

# 关系模式
1、用户（学号，姓名，密码，是否为管理员，联系方式）

2、书籍（书名，书号（ISBN），作者，分类，出版社，出版日期，库存，剩余可借，预约数量）

3、用户借阅（学号，书号，借出时间，归还时间，借出状态，预约排队）

# E-R图构建
![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/ER.png)
# 设计流程图
### 1、管理员总流程图
![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/admin.png)
1. 添加书籍
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/add_book.png)
2. 删除书籍
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/delete_book.png)
3. 添加学生
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/add_user.png)
4. 编辑学生信息
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/edit_user.png)
5. 删除学生
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/delete_user.png)

### 2、学生总流程图
![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/user.png)
1. 借阅书籍
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/borrow.png)
2. 归还书籍
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/return.png)
3. 预约书籍
   ![image](https://github.com/sasukeCP3/library_manager_system/blob/main/graph/booking.png)





