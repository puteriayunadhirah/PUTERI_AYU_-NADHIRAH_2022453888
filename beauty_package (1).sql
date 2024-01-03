-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 08:06 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `beauty_package`
--

-- --------------------------------------------------------

--
-- Table structure for table `beauty package`
--

CREATE TABLE `beauty package` (
  `treatment_type` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `packs` int(3) NOT NULL,
  `cust_name` varchar(20) NOT NULL,
  `cust_age` int(2) NOT NULL,
  `cust_contact` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `beauty package`
--

INSERT INTO `beauty package` (`treatment_type`, `price`, `packs`, `cust_name`, `cust_age`, `cust_contact`) VALUES
('Treatment A', 540, 6, 'Dahlia', 29, 154326781),
('Combo Treatment', 240, 1, 'sara adelia', 20, 1323234567),
('Treatment B', 300, 2, 'NAFIZ', 30, 1154327896),
('Treatment B', 300, 2, 'NAFIZ', 30, 1154327896),
('Combo Treatment', 240, 1, 'Puteri Ayu Nadhirah', 35, 113426782),
('Treatment A', 180, 2, 'Luth', 17, 113457652),
('Combo Treatment', 1200, 5, 'hanim', 41, 115668764),
('Treatment A', 90, 1, 'hajar', 11, 223688798);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
