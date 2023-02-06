-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2023 at 05:40 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `customer`
--

-- --------------------------------------------------------

--
-- Table structure for table `buy`
--

CREATE TABLE `buy` (
  `CID` int(11) NOT NULL,
  `PID` int(11) NOT NULL,
  `QUAN` int(11) NOT NULL,
  `IS_PAID` char(10) DEFAULT NULL,
  `PURCHASE_DATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buy`
--

INSERT INTO `buy` (`CID`, `PID`, `QUAN`, `IS_PAID`, `PURCHASE_DATE`) VALUES
(5, 2, 9, 'PAID', '2023-01-23'),
(5, 1, 45, 'PAID', '2023-01-23'),
(5, 5, 10, 'PAID', '2023-01-23'),
(5, 8, 9, 'PAID', '2023-01-23'),
(2, 3, 78, 'PAID', '2023-01-23'),
(3, 2, 5, 'NOT PAID', '2027-01-23'),
(3, 6, 34, 'NOT PAID', '2027-01-23'),
(3, 14, 45, 'NOT PAID', '2027-01-23'),
(12, 15, 2, 'PAID', '2027-01-23'),
(12, 14, 1, 'PAID', '2027-01-23'),
(12, 13, 1, 'PAID', '2027-01-23');

-- --------------------------------------------------------

--
-- Table structure for table `dummy`
--

CREATE TABLE `dummy` (
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `time` time NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dummy`
--

INSERT INTO `dummy` (`name`, `email`, `date`, `time`) VALUES
('ram', 'ram@gmail.com', '2023-01-23', '11:31:23');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `PID` int(11) DEFAULT NULL,
  `PNAME` char(100) DEFAULT NULL,
  `PQUAN` varchar(20) DEFAULT NULL,
  `PRICE` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`PID`, `PNAME`, `PQUAN`, `PRICE`) VALUES
(1, 'Aashirvaad Atta with Multigrains', '1kg', 1094),
(2, 'Tata Salt', '1kg', 28),
(3, 'Tata Tea Gold Leaf Pouch', '1500gm', 250),
(4, 'Harpic Powerplus Toilet Cleaner Original', '1ltr', 289),
(5, 'Dabur Honey', '1bottle', 396),
(6, 'Rin Advanced Detergent Powder', '7kg', 672),
(7, 'Potato', '1kg', 25),
(8, 'Jaggery', '1kg', 30),
(9, 'Pencil', '1box', 45),
(10, 'Eraser', '1box', 25),
(11, 'BLUE-Ink pot', '1box', 50),
(12, 'ARASAN Soap', '1SOAP', 38),
(13, 'MARGO Soap', '1SOAP', 27),
(14, 'MYSORE SANDAL Soap', '1SOAP', 55),
(15, 'MIRANDA', '1ltr', 68);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
