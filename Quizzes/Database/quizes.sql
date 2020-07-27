-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 27, 2020 at 09:05 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quizes`
--

-- --------------------------------------------------------

--
-- Table structure for table `aptitude`
--

CREATE TABLE `aptitude` (
  `QID` int(11) NOT NULL,
  `Question` varchar(250) NOT NULL,
  `Image` varchar(50) DEFAULT NULL,
  `A` varchar(20) NOT NULL,
  `B` varchar(20) NOT NULL,
  `C` varchar(20) NOT NULL,
  `D` varchar(20) NOT NULL,
  `Answer` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `aptitude`
--

INSERT INTO `aptitude` (`QID`, `Question`, `Image`, `A`, `B`, `C`, `D`, `Answer`) VALUES
(1, 'The profit obtained  by  selling  an  article  for  Rs.  56  is  the  same  as  the  loss  obtained  by  selling  it  for  Rs.  42.  What  is  the  cost  price  of  the  article?', NULL, 'Rs. 40', 'Rs. 50', 'Rs. 49', 'None of these', 'C'),
(2, 'An  article  is sold  at  a  certain  price.  By  selling it  at  2/3  of  that  price  one  loses  10%.  Find  the  gain  percent  at  original  price.', NULL, '15%', '35%', '25%', '50%', 'B'),
(3, 'A  man  bought  a  horse  and  a  carriage  for  Rs.  3000.  He  sold   the  horse  at  a  gain  of  20%  and  the  carriage  at  a  loss  of  10%,  thereby  gaining  2%  on  the  whole.  Find  the  cost  of  the  horse.', NULL, '2200', '1800', '1200', '1000', 'C'),
(4, 'The  price  of  a  jewel,  passing  through  three  hands, rises  on  the  whole  by  65%.  If  the  first  and  second  sellers  earned  20%  and  25%  profit  respectively,  find  the  percentage  profit  earned  by  the  third  seller.', NULL, '10%', '22%', '18%', '12%', 'A'),
(5, 'At  what  percentage  above  the  C.P  must  an  article  be  marked   so  as  to  gain  33%  after  allowing  a  customer  a  discount  of  5%?', NULL, '38%', '40%', '43%', '48%', 'B'),
(6, 'A  grocer  purchased  80  kg  of  rice  at  Rs.  13.50  per  kg  and  mixed  it  with  120  kg  rice  at Rs. 16  per  kg.  At  what  rate  per  kg  should  he  sell  the  mixture  to  gain  16%?', NULL, 'Rs. 19', 'Rs. 20.5', 'Rs. 17.4', 'Rs. 21.6', 'C'),
(7, 'On  an  article ,the  manufacturer  gains 10%,  the   wholesale   dealer   15%,  and  the  retailer  25%,  If  its  retail  price   is  1265,  what  is  the  cost  of  its  production?', NULL, '1000', '800', '1100', '900', 'B'),
(8, 'A  dealer  professing  to  sell  his  goods  at  cost  price,  uses  900gm  weight  for  1 kg.  His  gain  percent  is', NULL, '13%', '37/3%', '100/9%', '10%', 'C'),
(9, 'A  trader  has  50 kg  of  rice,  a  part  of  which  he  sells  at  14%  profit  and  rest  at  6%  loss.  On  the  whole  his  loss  is  4% .  What  is  the  quantity  sold  at  14%  profit   and  that  at  6%  loss?', NULL, '5 and 45 kg', '10 and 40 kg', '15 and 35 kg', '20 and 30 kg', 'A'),
(10, 'The  cost  price  of  two  types  of  tea  are  Rs.  180  per kg  and  Rs.  200       per  kg  respectively. On mixing  them  in  the  ratio  5:3, the  mixture is  sold  at  Rs. 210  per  kg .  In  the  whole  transaction,  the  gain  percent  is', NULL, '10%', '11%', '12%', '13%', 'C');

-- --------------------------------------------------------

--
-- Table structure for table `cprogramming`
--

CREATE TABLE `cprogramming` (
  `QID` int(11) NOT NULL,
  `Question` varchar(250) NOT NULL,
  `Image` varchar(50) DEFAULT NULL,
  `A` varchar(20) NOT NULL,
  `B` varchar(20) NOT NULL,
  `C` varchar(20) NOT NULL,
  `D` varchar(20) NOT NULL,
  `Answer` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cprogramming`
--

INSERT INTO `cprogramming` (`QID`, `Question`, `Image`, `A`, `B`, `C`, `D`, `Answer`) VALUES
(1, 'C99 standard guarantees uniqueness of __________ characters for internal names.', NULL, '31', '63', '12', '14', 'B'),
(2, 'Which of the following is not a valid variable name declaration?', NULL, 'int__a3;', 'int__3a;', 'int__A3', 'None of these', 'C'),
(3, 'All keywords in C are in ____________', NULL, 'LowerCase letters', 'UpperCase letters', 'CamelCase letters', 'None of these', 'A'),
(4, 'Variable name resolution (number of significant characters for the uniqueness of variable) depends on ___________', NULL, 'Compiler and linker ', 'Assemblers and loade', 'C language', 'None of these', 'A'),
(5, 'Which of the following is not a valid C variable name?', NULL, 'int number;', 'float rate;', 'int vaiable_count;', 'int $main;', 'D'),
(6, 'Which is valid C expression?', NULL, 'int my_num = 100,000', 'int my_num = 100000;', 'int my num = 1000;', 'int $my_num = 10000;', 'B'),
(7, 'Which of the following is not a valid variable name declaration?', NULL, 'float PI = 3.14;', 'double PI = 3.14;', 'int PI = 3.14;', '#define PI 3.14', 'D'),
(8, 'Which of the following cannot be a variable name in C?', NULL, 'volatile', 'true', 'friend', 'export', 'A'),
(9, 'The format identifier ‘%i’ is also used for _____ data type.', NULL, 'char', 'int', 'float', 'double', 'B'),
(10, ' Which data type is most suitable for storing a number 65000 in a 32-bit system?', NULL, 'signed short', 'unsigned short', 'long', 'int', 'B');

-- --------------------------------------------------------

--
-- Table structure for table `resoning`
--

CREATE TABLE `resoning` (
  `QID` int(11) NOT NULL,
  `Question` varchar(250) NOT NULL,
  `Image` varchar(50) DEFAULT NULL,
  `A` varchar(20) NOT NULL,
  `B` varchar(20) NOT NULL,
  `C` varchar(20) NOT NULL,
  `D` varchar(20) NOT NULL,
  `Answer` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resoning`
--

INSERT INTO `resoning` (`QID`, `Question`, `Image`, `A`, `B`, `C`, `D`, `Answer`) VALUES
(1, 'Look at this series: 12, 11, 13, 12, 14, 13, … What number should come next?', NULL, '10', '16', '13', '15', 'D'),
(2, 'Which word does NOT belong with the others?', NULL, 'index', 'glossary', 'chapter', 'book', 'D'),
(3, 'CUP : LIP :: BIRD : ?', NULL, 'GRASS', 'FOREST', 'BREAK', 'BUSH', 'C'),
(4, 'Pointing to a photograph, a man said, \"I have no brother, and that man\'s father is my father\'s son.\" Whose photograph was it?', NULL, 'His Son', 'His Own', 'His Father', 'His Nephew', 'A'),
(5, 'Find the next number in the sequence: 3, 6, 9, 30, 117......', NULL, '192', '352', '388', '588', 'D'),
(6, 'John has more coins than Sonu. Sonu has fewer coins than Danish. Danish has more coins than John. If the first two statements are true, the third statement is', NULL, 'True', 'False', 'Uncertain', 'None of these', 'B'),
(7, 'Statements: A > B, B ≥ C, C < D Conclusions:  \r\nI. A > C  \r\nII. A = C', NULL, 'Only I is true', 'Only II is true', 'Either I and II true', 'Neither I and II tru', 'A'),
(8, 'SCD, TEF, UGH, ____, WKL', NULL, 'CMN', 'UJI', 'VIJ', 'IJT', 'C'),
(9, 'FAG, GAF, HAI, IAH, ____', NULL, 'JAK', 'HAL', 'HAK', 'JAI', 'A'),
(10, 'ELFA, GLHA, ILJA, _____, MLNA', NULL, 'OLPA', 'KLMA', 'LLMA', 'KLLA', 'D');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aptitude`
--
ALTER TABLE `aptitude`
  ADD PRIMARY KEY (`QID`);

--
-- Indexes for table `cprogramming`
--
ALTER TABLE `cprogramming`
  ADD PRIMARY KEY (`QID`);

--
-- Indexes for table `resoning`
--
ALTER TABLE `resoning`
  ADD PRIMARY KEY (`QID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
