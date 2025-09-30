-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.62 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.1.0.4867
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
-- Dumping data for table 12a.login: ~13 rows (approximately)
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` (`USERNAME`, `PWD`, `PHONE`) VALUES
	('NETHRA', 'QWERTY', '987654321'),
	('bbg@121', 'asdfg', '987654321'),
	('qwerty', 'qwerty', '987654321'),
	('supraja', 'suppu', '9820744997'),
	('RAVIN', 'nirvana', '9820744997'),
	('maheshwari', '12345', '8450981722'),
	('sowmya_1112', 'asd123', '9769538138'),
	('user123', 'qwerty', '9989785982'),
	('hpv', 'charizad', '9789993156'),
	('maheshravin17', 'mahesh17', '9820744007'),
	('shankar.12', 'shankar12', '7768756431'),
	('gk', 'gth', '9149311060'),
	('aarti', 'aarti', '1234578901');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;

-- Dumping data for table 12a.scoreboard: ~13 rows (approximately)
/*!40000 ALTER TABLE `scoreboard` DISABLE KEYS */;
INSERT INTO `scoreboard` (`username`, `score`) VALUES
	('NETHRA', 72000),
	('bbg@121', 19000),
	('maheshwari17', 0),
	('qwerty', 0),
	('supraja', 0),
	('RAVIN', 25000),
	('sowmya_1112', 1000),
	('user123', 0),
	('hpv', 4000),
	('maheshravin17', 0),
	('shankar.12', 0),
	('gk', 1000),
	('aarti', 6000);
/*!40000 ALTER TABLE `scoreboard` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
