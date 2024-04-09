-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 31, 2024 at 11:07 PM
-- Server version: 8.0.36-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `iudi`
--

-- --------------------------------------------------------

--
-- Table structure for table `CommentFavorite`
--

CREATE TABLE `CommentFavorite` (
  `CommentFavoriteID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `CommentID` int DEFAULT NULL,
  `FavoriteType` tinyint(1) DEFAULT NULL,
  `FavoriteTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `CommentPhotos`
--

CREATE TABLE `CommentPhotos` (
  `PhotoID` int NOT NULL,
  `CommentID` int DEFAULT NULL,
  `PhotoURL` varchar(255) NOT NULL,
  `UploadTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Favorite`
--

CREATE TABLE `Favorite` (
  `FavoriteID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `PostID` int DEFAULT NULL,
  `FavoriteType` tinyint(1) DEFAULT NULL,
  `FavoriteTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Favorite`
--

INSERT INTO `Favorite` (`FavoriteID`, `UserID`, `PostID`, `FavoriteType`, `FavoriteTime`) VALUES
(1, 1, 2, 0, '2024-01-31 17:12:05');

-- --------------------------------------------------------

--
-- Table structure for table `ForumPhotos`
--

CREATE TABLE `ForumPhotos` (
  `PhotoID` int NOT NULL,
  `PostID` int DEFAULT NULL,
  `PhotoURL` varchar(255) NOT NULL,
  `UploadTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ForumPhotos`
--

INSERT INTO `ForumPhotos` (`PhotoID`, `PostID`, `PhotoURL`, `UploadTime`) VALUES
(1, 2, 'image4.jpg', '2024-01-31 17:02:35'),
(2, 2, 'image5.jpg', '2024-01-31 17:02:35'),
(3, 2, 'image6.jpg', '2024-01-31 17:02:35'),
(4, 3, 'image4.jpg', '2024-01-31 17:02:54'),
(5, 3, 'image5.jpg', '2024-01-31 17:02:54'),
(6, 3, 'image6.jpg', '2024-01-31 17:02:54'),
(7, 4, 'image4.jpg', '2024-01-31 17:03:01'),
(8, 4, 'image5.jpg', '2024-01-31 17:03:01'),
(9, 4, 'image6.jpg', '2024-01-31 17:03:01');

-- --------------------------------------------------------

--
-- Table structure for table `ForumPosts`
--

CREATE TABLE `ForumPosts` (
  `PostID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `GroupID` int DEFAULT NULL,
  `Title` text,
  `Content` text,
  `PostTime` datetime DEFAULT NULL,
  `IPPosted` varchar(45) DEFAULT NULL,
  `PostLatitude` decimal(10,8) DEFAULT NULL,
  `PostLongitude` decimal(11,8) DEFAULT NULL,
  `UpdatePostAt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ForumPosts`
--

INSERT INTO `ForumPosts` (`PostID`, `UserID`, `GroupID`, `Title`, `Content`, `PostTime`, `IPPosted`, `PostLatitude`, `PostLongitude`, `UpdatePostAt`) VALUES
(2, 1, 1, 'Gà', 'Có rất nhiều con gà trong đàn ag cozzn', '2024-01-31 17:02:35', '192.168.88.1', '40.00000000', '50.00000000', '2024-01-31 17:02:35'),
(3, 1, 1, 'Một con Chó conzzzz', 'Có rất nhiều con chó trong đàn mèo cozzn', '2024-01-31 17:02:54', '192.168.88.1', '40.00000000', '50.00000000', '2024-01-31 17:02:54'),
(4, 1, 1, 'Một con mèo conzzzz', 'Có rất nhiều con chó trong đàn mèo cozzn', '2024-01-31 17:03:01', '192.168.88.1', '40.00000000', '50.00000000', '2024-01-31 17:03:00');

-- --------------------------------------------------------

--
-- Table structure for table `Groups`
--

CREATE TABLE `Groups` (
  `GroupID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `GroupName` varchar(50) NOT NULL,
  `CreateAt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Groups`
--

INSERT INTO `Groups` (`GroupID`, `UserID`, `GroupName`, `CreateAt`) VALUES
(1, 1, 'Xuân Đỉnh', '2024-01-31 17:01:54'),
(2, 1, 'Thanh Xuân', '2024-01-31 17:02:04'),
(3, 1, 'Hoàng mai', '2024-01-31 17:02:08'),
(4, 1, 'ALoha', '2024-01-31 17:02:19');

-- --------------------------------------------------------

--
-- Table structure for table `Locations`
--

CREATE TABLE `Locations` (
  `LocationID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `Latitude` decimal(10,8) DEFAULT NULL,
  `Longitude` decimal(11,8) DEFAULT NULL,
  `Type` enum('registration','login','current') DEFAULT NULL,
  `UpdateTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Locations`
--

INSERT INTO `Locations` (`LocationID`, `UserID`, `Latitude`, `Longitude`, `Type`, `UpdateTime`) VALUES
(1, 3, '27.00000000', '40.00000000', 'registration', '2024-01-31 16:53:33'),
(2, 3, '27.00000000', '40.00000000', 'login', '2024-01-31 16:53:33'),
(3, 3, '27.00000000', '40.00000000', 'current', '2024-01-31 16:53:33');

-- --------------------------------------------------------

--
-- Table structure for table `MessagePhotos`
--

CREATE TABLE `MessagePhotos` (
  `PhotoID` int NOT NULL,
  `MessageID` int DEFAULT NULL,
  `PhotoURL` varchar(255) NOT NULL,
  `UploadTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Messages`
--

CREATE TABLE `Messages` (
  `MessageID` int NOT NULL,
  `SenderID` int DEFAULT NULL,
  `ReceiverID` int DEFAULT NULL,
  `Content` text,
  `MessageTime` datetime DEFAULT NULL,
  `IsSeen` smallint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `PostComments`
--

CREATE TABLE `PostComments` (
  `CommentID` int NOT NULL,
  `PostID` int DEFAULT NULL,
  `UserID` int DEFAULT NULL,
  `Content` text,
  `CommentTime` datetime DEFAULT NULL,
  `CommentUpdateTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Provinces`
--

CREATE TABLE `Provinces` (
  `ProvinceID` int NOT NULL,
  `ProvinceName` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Provinces`
--

INSERT INTO `Provinces` (`ProvinceID`, `ProvinceName`) VALUES
(6, 'An Giang'),
(7, 'Bà Rịa - Vũng Tàu'),
(8, 'Bắc Giang'),
(9, 'Bắc Kạn'),
(10, 'Bạc Liêu'),
(11, 'Bắc Ninh'),
(12, 'Bến Tre'),
(13, 'Bình Định'),
(14, 'Bình Dương'),
(15, 'Bình Phước'),
(16, 'Bình Thuận'),
(17, 'Cà Mau'),
(5, 'Cần Thơ'),
(18, 'Cao Bằng'),
(3, 'Đà Nẵng'),
(19, 'Đắk Lắk'),
(20, 'Đắk Nông'),
(21, 'Điện Biên'),
(22, 'Đồng Nai'),
(23, 'Đồng Tháp'),
(24, 'Gia Lai'),
(25, 'Hà Giang'),
(26, 'Hà Nam'),
(1, 'Hà Nội'),
(27, 'Hà Tĩnh'),
(28, 'Hải Dương'),
(4, 'Hải Phòng'),
(29, 'Hậu Giang'),
(2, 'Hồ Chí Minh'),
(30, 'Hòa Bình'),
(31, 'Hưng Yên'),
(32, 'Khánh Hòa'),
(33, 'Kiên Giang'),
(34, 'Kon Tum'),
(35, 'Lai Châu'),
(36, 'Lâm Đồng'),
(37, 'Lạng Sơn'),
(38, 'Lào Cai'),
(39, 'Long An'),
(40, 'Nam Định'),
(41, 'Nghệ An'),
(42, 'Ninh Bình'),
(43, 'Ninh Thuận'),
(44, 'Phú Thọ'),
(45, 'Quảng Bình'),
(46, 'Quảng Nam'),
(47, 'Quảng Ngãi'),
(48, 'Quảng Ninh'),
(49, 'Quảng Trị'),
(50, 'Sóc Trăng'),
(51, 'Sơn La'),
(52, 'Tây Ninh'),
(53, 'Thái Bình'),
(54, 'Thái Nguyên'),
(55, 'Thanh Hóa'),
(56, 'Thừa Thiên Huế'),
(57, 'Tiền Giang'),
(58, 'Trà Vinh'),
(59, 'Tuyên Quang'),
(60, 'Vĩnh Long'),
(61, 'Vĩnh Phúc'),
(62, 'Yên Bái');

-- --------------------------------------------------------

--
-- Table structure for table `Relationships`
--

CREATE TABLE `Relationships` (
  `RelationshipID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `RelatedUserID` int DEFAULT NULL,
  `RelationshipType` enum('block','other','favorite') NOT NULL,
  `CreateTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `UserPhotos`
--

CREATE TABLE `UserPhotos` (
  `PhotoID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `PhotoURL` varchar(255) NOT NULL,
  `UploadTime` datetime DEFAULT NULL,
  `SetAsAvatar` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `UserID` int NOT NULL,
  `FullName` varchar(50) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Gender` enum('Nam','Nữ','Đồng tính nữ','Đồng tính nam') DEFAULT NULL,
  `BirthDate` date DEFAULT NULL,
  `BirthTime` time DEFAULT NULL,
  `ProvinceID` int DEFAULT NULL,
  `IsAnonymous` smallint DEFAULT NULL,
  `RegistrationIP` varchar(45) DEFAULT NULL,
  `LastLoginIP` varchar(45) DEFAULT NULL,
  `LastActivityTime` datetime DEFAULT NULL,
  `IsLoggedIn` tinyint(1) DEFAULT NULL,
  `Role` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`UserID`, `FullName`, `Username`, `Password`, `Email`, `Phone`, `Gender`, `BirthDate`, `BirthTime`, `ProvinceID`, `IsAnonymous`, `RegistrationIP`, `LastLoginIP`, `LastActivityTime`, `IsLoggedIn`, `Role`) VALUES
(1, 'Phap dep chai', 'admin', '$pbkdf2-sha256$29000$BuA8Z2wtxdi7N4bwnrN2jg$4zUx3bgLkDEcmRpPf7J0wvndwTjPkguo/OI70ks8TAY', 'pxlphap@gmail.com', '0383848623', 'Nam', '2001-05-13', '00:00:00', 1, 0, '192.168.88.1', NULL, NULL, 0, 1),
(2, 'Phap dep chai', 'admin2', '$pbkdf2-sha256$29000$07o3hlCqtXbuPceYc67V2g$PSAYt/BKEGTAV7s9xVR8k2.EhK/coBQ2r2lK6rxKsGc', 'pxlphapz@gmail.com', NULL, NULL, NULL, NULL, NULL, 0, '192.168.88.1', NULL, NULL, 0, 0),
(3, 'Phap dep chai', 'admin3', '$pbkdf2-sha256$29000$AOAcg/A.5xwD4ByDsPZ.rw$9hXpwXsKR1XQ7jea/Z0ozTaaIkoY47T8XumPTpoaheg', 'pxlphapzz@gmail.com', NULL, NULL, NULL, NULL, NULL, 0, '192.168.88.1', NULL, NULL, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CommentFavorite`
--
ALTER TABLE `CommentFavorite`
  ADD PRIMARY KEY (`CommentFavoriteID`),
  ADD KEY `UserID` (`UserID`),
  ADD KEY `CommentID` (`CommentID`);

--
-- Indexes for table `CommentPhotos`
--
ALTER TABLE `CommentPhotos`
  ADD PRIMARY KEY (`PhotoID`),
  ADD KEY `CommentID` (`CommentID`);

--
-- Indexes for table `Favorite`
--
ALTER TABLE `Favorite`
  ADD PRIMARY KEY (`FavoriteID`),
  ADD KEY `UserID` (`UserID`),
  ADD KEY `PostID` (`PostID`);

--
-- Indexes for table `ForumPhotos`
--
ALTER TABLE `ForumPhotos`
  ADD PRIMARY KEY (`PhotoID`),
  ADD KEY `PostID` (`PostID`);

--
-- Indexes for table `ForumPosts`
--
ALTER TABLE `ForumPosts`
  ADD PRIMARY KEY (`PostID`),
  ADD KEY `UserID` (`UserID`),
  ADD KEY `GroupID` (`GroupID`);

--
-- Indexes for table `Groups`
--
ALTER TABLE `Groups`
  ADD PRIMARY KEY (`GroupID`),
  ADD UNIQUE KEY `GroupName` (`GroupName`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `Locations`
--
ALTER TABLE `Locations`
  ADD PRIMARY KEY (`LocationID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `MessagePhotos`
--
ALTER TABLE `MessagePhotos`
  ADD PRIMARY KEY (`PhotoID`),
  ADD KEY `MessageID` (`MessageID`);

--
-- Indexes for table `Messages`
--
ALTER TABLE `Messages`
  ADD PRIMARY KEY (`MessageID`),
  ADD KEY `SenderID` (`SenderID`),
  ADD KEY `ReceiverID` (`ReceiverID`);

--
-- Indexes for table `PostComments`
--
ALTER TABLE `PostComments`
  ADD PRIMARY KEY (`CommentID`),
  ADD KEY `PostID` (`PostID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `Provinces`
--
ALTER TABLE `Provinces`
  ADD PRIMARY KEY (`ProvinceID`),
  ADD UNIQUE KEY `ProvinceName` (`ProvinceName`);

--
-- Indexes for table `Relationships`
--
ALTER TABLE `Relationships`
  ADD PRIMARY KEY (`RelationshipID`),
  ADD KEY `UserID` (`UserID`),
  ADD KEY `RelatedUserID` (`RelatedUserID`);

--
-- Indexes for table `UserPhotos`
--
ALTER TABLE `UserPhotos`
  ADD PRIMARY KEY (`PhotoID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `Username` (`Username`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD KEY `ProvinceID` (`ProvinceID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CommentFavorite`
--
ALTER TABLE `CommentFavorite`
  MODIFY `CommentFavoriteID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CommentPhotos`
--
ALTER TABLE `CommentPhotos`
  MODIFY `PhotoID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Favorite`
--
ALTER TABLE `Favorite`
  MODIFY `FavoriteID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ForumPhotos`
--
ALTER TABLE `ForumPhotos`
  MODIFY `PhotoID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `ForumPosts`
--
ALTER TABLE `ForumPosts`
  MODIFY `PostID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Groups`
--
ALTER TABLE `Groups`
  MODIFY `GroupID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Locations`
--
ALTER TABLE `Locations`
  MODIFY `LocationID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `MessagePhotos`
--
ALTER TABLE `MessagePhotos`
  MODIFY `PhotoID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Messages`
--
ALTER TABLE `Messages`
  MODIFY `MessageID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PostComments`
--
ALTER TABLE `PostComments`
  MODIFY `CommentID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Provinces`
--
ALTER TABLE `Provinces`
  MODIFY `ProvinceID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `Relationships`
--
ALTER TABLE `Relationships`
  MODIFY `RelationshipID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `UserPhotos`
--
ALTER TABLE `UserPhotos`
  MODIFY `PhotoID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `UserID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `CommentFavorite`
--
ALTER TABLE `CommentFavorite`
  ADD CONSTRAINT `CommentFavorite_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`),
  ADD CONSTRAINT `CommentFavorite_ibfk_2` FOREIGN KEY (`CommentID`) REFERENCES `PostComments` (`CommentID`);

--
-- Constraints for table `CommentPhotos`
--
ALTER TABLE `CommentPhotos`
  ADD CONSTRAINT `CommentPhotos_ibfk_1` FOREIGN KEY (`CommentID`) REFERENCES `PostComments` (`CommentID`);

--
-- Constraints for table `Favorite`
--
ALTER TABLE `Favorite`
  ADD CONSTRAINT `Favorite_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`),
  ADD CONSTRAINT `Favorite_ibfk_2` FOREIGN KEY (`PostID`) REFERENCES `ForumPosts` (`PostID`);

--
-- Constraints for table `ForumPhotos`
--
ALTER TABLE `ForumPhotos`
  ADD CONSTRAINT `ForumPhotos_ibfk_1` FOREIGN KEY (`PostID`) REFERENCES `ForumPosts` (`PostID`);

--
-- Constraints for table `ForumPosts`
--
ALTER TABLE `ForumPosts`
  ADD CONSTRAINT `ForumPosts_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`),
  ADD CONSTRAINT `ForumPosts_ibfk_2` FOREIGN KEY (`GroupID`) REFERENCES `Groups` (`GroupID`);

--
-- Constraints for table `Groups`
--
ALTER TABLE `Groups`
  ADD CONSTRAINT `Groups_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `Locations`
--
ALTER TABLE `Locations`
  ADD CONSTRAINT `Locations_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `MessagePhotos`
--
ALTER TABLE `MessagePhotos`
  ADD CONSTRAINT `MessagePhotos_ibfk_1` FOREIGN KEY (`MessageID`) REFERENCES `Messages` (`MessageID`);

--
-- Constraints for table `Messages`
--
ALTER TABLE `Messages`
  ADD CONSTRAINT `Messages_ibfk_1` FOREIGN KEY (`SenderID`) REFERENCES `Users` (`UserID`),
  ADD CONSTRAINT `Messages_ibfk_2` FOREIGN KEY (`ReceiverID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `PostComments`
--
ALTER TABLE `PostComments`
  ADD CONSTRAINT `PostComments_ibfk_1` FOREIGN KEY (`PostID`) REFERENCES `ForumPosts` (`PostID`),
  ADD CONSTRAINT `PostComments_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `Relationships`
--
ALTER TABLE `Relationships`
  ADD CONSTRAINT `Relationships_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`),
  ADD CONSTRAINT `Relationships_ibfk_2` FOREIGN KEY (`RelatedUserID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `UserPhotos`
--
ALTER TABLE `UserPhotos`
  ADD CONSTRAINT `UserPhotos_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `Users` (`UserID`);

--
-- Constraints for table `Users`
--
ALTER TABLE `Users`
  ADD CONSTRAINT `Users_ibfk_1` FOREIGN KEY (`ProvinceID`) REFERENCES `Provinces` (`ProvinceID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
