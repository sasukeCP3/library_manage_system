/*
 Navicat Premium Data Transfer

 Source Server         : zsy
 Source Server Type    : MySQL
 Source Server Version : 80035 (8.0.35)
 Source Host           : localhost:3306
 Source Schema         : lib_manage_sys

 Target Server Type    : MySQL
 Target Server Version : 80035 (8.0.35)
 File Encoding         : 65001

 Date: 12/11/2023 17:46:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `BookName` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '书名',
  `BookId` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '书号',
  `Auth` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '作者',
  `Category` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '分类',
  `Publisher` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '出版社',
  `PublishTime` date NULL DEFAULT NULL COMMENT '出版时间',
  `NumStorage` int NULL DEFAULT 0 COMMENT '库存数量',
  `NumCanBorrow` int NULL DEFAULT 0 COMMENT '剩余可借',
  `NumBookinged` int NULL DEFAULT 0 COMMENT '预约数量'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('高等数学1', '0000', '武忠祥', '教育', '西安交通大学出版社', '1999-01-01', 20, 20, 0);
INSERT INTO `book` VALUES ('高等数学2', '0001', '武忠祥', '教育', '西安交通大学出版社', '1999-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('高等数学3', '0002', '武忠祥', '教育', '西安交通大学出版社', '1999-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('高等数学4', '0003', '武忠祥', '教育', '西安交通大学出版社', '1999-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('高等数学5', '0004', '武忠祥', '教育', '西安交通大学出版社', '1999-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('高等数学6', '0005', '武忠祥', '教育', '西安交通大学出版社', '1999-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('高等数学7', '0006', '武忠祥', '教育', '西安交通大学出版社', '1999-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('线性代数1', '0007', '李永乐', '教育', '西安交通大学出版社', '2001-02-28', 30, 3, 3);
INSERT INTO `book` VALUES ('线性代数2', '0008', '李永乐', '教育', '高等教育', '2001-02-28', 30, 30, 0);
INSERT INTO `book` VALUES ('线性代数3', '0009', '李永乐', '教育', '高等教育', '2001-02-28', 30, 30, 0);
INSERT INTO `book` VALUES ('线性代数4', '0010', '李永乐', '教育', '高等教育', '2001-02-28', 30, 30, 0);
INSERT INTO `book` VALUES ('线性代数5', '0011', '李永乐', '教育', '高等教育', '2001-02-28', 30, 30, 0);
INSERT INTO `book` VALUES ('数据库原理与技术1', '0012', '刘帅', '教育', '西安交通大学出版社', '2010-01-01', 100, 3, 3);
INSERT INTO `book` VALUES ('数据库原理与技术2', '0013', '刘帅', '教育', '西安交通大学出版社', '2010-01-01', 100, 100, 0);
INSERT INTO `book` VALUES ('数据库原理与技术3', '0014', '刘帅', '教育', '西安交通大学出版社', '2010-01-01', 100, 100, 0);
INSERT INTO `book` VALUES ('数据库原理与技术4', '0015', '刘帅', '教育', '西安交通大学出版社', '2010-01-01', 100, 100, 0);
INSERT INTO `book` VALUES ('哈利波特1', '0016', 'J.K.罗琳', '艺术', '布鲁姆斯伯里出版社', '1998-03-08', 20, 19, 0);
INSERT INTO `book` VALUES ('哈利波特2', '0017', 'J.K.罗琳', '艺术', '布鲁姆斯伯里出版社', '1998-03-08', 20, 20, 0);
INSERT INTO `book` VALUES ('哈利波特3', '0018', 'J.K.罗琳', '艺术', '布鲁姆斯伯里出版社', '1998-03-08', 20, 20, 0);
INSERT INTO `book` VALUES ('哈利波特4', '0019', 'J.K.罗琳', '艺术', '布鲁姆斯伯里出版社', '1998-03-08', 20, 20, 0);
INSERT INTO `book` VALUES ('哈利波特5', '0020', 'J.K.罗琳', '艺术', '布鲁姆斯伯里出版社', '1998-03-08', 20, 20, 0);
INSERT INTO `book` VALUES ('哈利波特6', '0021', 'J.K.罗琳', '艺术', '布鲁姆斯伯里出版社', '1998-03-08', 20, 20, 0);
INSERT INTO `book` VALUES ('哈利波特7', '0022', 'J.K.罗琳', '艺术', '布鲁姆斯伯里出版社', '1998-03-08', 20, 20, 0);
INSERT INTO `book` VALUES ('西游记', '0023', '吴承恩', '文化', '人民文学出版社', '2011-12-01', 10, 1, 0);
INSERT INTO `book` VALUES ('三国演义', '0024', '罗贯中', '文化', '人民文学出版社', '2011-04-01', 10, 10, 0);
INSERT INTO `book` VALUES ('水浒传', '0025', '施耐庵', '文化', '人民文学出版社', '2016-05-01', 10, 10, 0);
INSERT INTO `book` VALUES ('红楼梦', '0026', '曹雪芹', '文化', '人民文学出版社', '2021-02-01', 10, 10, 0);
INSERT INTO `book` VALUES ('我的区长父亲1', '0027', '袁华', '社会科学', '中国青年出版社', '2011-05-01', 666, 666, 0);
INSERT INTO `book` VALUES ('我的区长父亲2', '0028', '袁华', '社会科学', '中国青年出版社', '2011-05-05', 666, 666, 0);
INSERT INTO `book` VALUES ('Navicat教程', '0029', '郑重', '教育', '中国科学技术大学', '2011-05-01', 5, 1, 0);
INSERT INTO `book` VALUES ('细胞学', '0030', '佚名', '生物学', '中国科学技术大学', '2011-05-01', 5, 5, 0);
INSERT INTO `book` VALUES ('生物医学学', '0031', '佚名', '生物学', '中国科学技术大学', '2011-05-01', 5, 5, 0);
INSERT INTO `book` VALUES ('道德经', '0032', '老子', '哲学', '人民文学出版社', '2016-06-15', 5, 4, 0);
INSERT INTO `book` VALUES ('喀斯特地貌详解1', '0035', '佚名', '地理', '高等教育出版社', '2012-01-01', 44, 44, 0);
INSERT INTO `book` VALUES ('亮剑', '0034', '都梁', '军事', '人民出版社', '1998-01-01', 44, 44, 0);
INSERT INTO `book` VALUES ('喀斯特地貌详解1', '0033', '佚名', '地理', '高等教育出版社', '2012-01-01', 44, 44, 0);
INSERT INTO `book` VALUES ('三国志', '0036', '陈寿', '历史', '人民文学出版社', '2000-06-30', 58, 58, 0);
INSERT INTO `book` VALUES ('金克拉使用指南', '0037', '佚名', '农业', '中国农业出版社', '2015-07-17', 58, 58, 0);
INSERT INTO `book` VALUES ('篮球', '0038', 'Lebron James', '体育', '博尔达出版社', '2023-11-15', 58, 7, 0);
INSERT INTO `book` VALUES ('篮球进阶', '0039', 'Lebron James', '体育', '博尔达出版社', '2023-11-17', 58, 58, 0);
INSERT INTO `book` VALUES ('法外狂徒王五', '0042', '罗翔', '法律', '武汉大学出版社', '2011-10-26', 23, 23, 0);
INSERT INTO `book` VALUES ('法外狂徒李四', '0041', '罗翔', '法律', '武汉大学出版社', '2011-10-26', 23, 23, 0);
INSERT INTO `book` VALUES ('法外狂徒张三', '0040', '罗翔', '法律', '武汉大学出版社', '2011-10-26', 23, 23, 0);
INSERT INTO `book` VALUES ('语文', '0098', 'zzz', '语言文字', '人民出版社', '1999-10-11', 50, 50, 0);
INSERT INTO `book` VALUES ('语文', '1234', 'ggs', '语言文字', '人民出版社', '2005-05-01', 40, 40, 0);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `StudentId` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学号',
  `Name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '姓名',
  `Password` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '密码',
  `IsAdmin` int NULL DEFAULT 0 COMMENT '是否为管理员',
  `tel` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '联系方式'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', '1', 1, '18180022722');
INSERT INTO `user` VALUES ('111', 'james', '111', 0, '110');
INSERT INTO `user` VALUES ('222', '张三', '222', 0, '120');
INSERT INTO `user` VALUES ('12345678', '王小华', '12345678', 0, '110119120');
INSERT INTO `user` VALUES ('987654321', '李华', '987654321', 0, '911369');
INSERT INTO `user` VALUES ('147258369', '小明', '147258369', 0, '963852741');
INSERT INTO `user` VALUES ('2555', 'ijij', '1234', 0, '852852852');

-- ----------------------------
-- Table structure for user_book
-- ----------------------------
DROP TABLE IF EXISTS `user_book`;
CREATE TABLE `user_book`  (
  `StudentId` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学号',
  `BookId` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '书号',
  `BorrowTime` date NULL DEFAULT NULL COMMENT '借出时间',
  `ReturnTime` date NULL DEFAULT NULL COMMENT '归还时间',
  `BorrowState` bit(1) NULL DEFAULT b'0' COMMENT '借出状态',
  `BookingState` int NULL DEFAULT 0 COMMENT '预约排队'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user_book
-- ----------------------------
INSERT INTO `user_book` VALUES ('111', '0023', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('111', '0032', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('111', '0007', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('111', '0029', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('222', '0023', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('222', '0029', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('222', '0007', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('222', '0038', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('12345678', '0029', '2023-11-03', '2023-11-05', b'0', 0);
INSERT INTO `user_book` VALUES ('12345678', '0007', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('12345678', '0012', '2023-11-01', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('12345678', '0029', '2023-11-04', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('987654321', '0029', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('987654321', '0016', '2023-11-02', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('987654321', '0007', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('987654321', '0012', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('222', '0012', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('987654321', '0029', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('12345678', '0029', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('12345678', '0029', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('12345678', '0029', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('12345678', '0017', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('12345678', '0012', '2023-11-10', NULL, b'1', 0);
INSERT INTO `user_book` VALUES ('12345678', '0036', '2023-11-10', '2023-11-10', b'0', 0);
INSERT INTO `user_book` VALUES ('2555', '0007', '2023-11-10', NULL, b'1', 0);

SET FOREIGN_KEY_CHECKS = 1;
