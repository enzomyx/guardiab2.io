-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mer 29 Janvier 2025 à 10:47
-- Version du serveur :  5.6.20-log
-- Version de PHP :  5.4.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `ecole`
--

-- --------------------------------------------------------

--
-- Structure de la table `notes`
--

CREATE TABLE IF NOT EXISTS `notes` (
`ID` int(11) NOT NULL,
  `Prénom Prof` varchar(100) NOT NULL,
  `Nom Prof` varchar(100) NOT NULL,
  `Date` date NOT NULL,
  `Nom Eleve` varchar(100) NOT NULL,
  `Prénom Eleve` varchar(100) NOT NULL,
  `Classe` varchar(100) NOT NULL,
  `Matière` varchar(100) NOT NULL,
  `Contrôle` varchar(100) NOT NULL,
  `Note` varchar(100) NOT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `notes`
--

INSERT INTO `notes` (`ID`, `Prénom Prof`, `Nom Prof`, `Date`, `Nom Eleve`, `Prénom Eleve`, `Classe`, `Matière`, `Contrôle`, `Note`) VALUES
(1, 'Phillippe', 'Kaadi', '2025-01-28', 'Test', 'Antony', 'GSC', 'Français', 'Dictée', '14/20'),
(2, 'Phillippe', 'Kaadi', '2025-01-28', 'Test', 'Antony', 'GSC', 'Français', 'Figures de styles', '9/20');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
`ID` int(255) NOT NULL,
  `Prénom` varchar(100) NOT NULL,
  `Nom` varchar(100) NOT NULL,
  `Matière` varchar(100) NOT NULL,
  `Classe` varchar(100) NOT NULL,
  `Identifiant` varchar(100) NOT NULL,
  `Mot de passe` varchar(100) NOT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `users`
--

INSERT INTO `users` (`ID`, `Prénom`, `Nom`, `Matière`, `Classe`, `Identifiant`, `Mot de passe`) VALUES
(1, 'Antony', 'Test', '', 'GSC', 'Antony', 'test1'),
(2, 'Phillippe', 'Kaadi', 'Français', '', 'Phillipe', 'test2'),
(3, 'Orane', 'Mainville', '', 'GSC', 'Orane', 'test3');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `notes`
--
ALTER TABLE `notes`
 ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
 ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `notes`
--
ALTER TABLE `notes`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
MODIFY `ID` int(255) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
