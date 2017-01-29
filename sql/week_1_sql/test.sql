-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `ip_adress` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`blogs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`blogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `blog_name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`admins` (
  `user_id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_blogs_blogs1_idx` (`blog_id` ASC),
  INDEX `fk_users_has_blogs_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_users_has_blogs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_blogs_blogs1`
    FOREIGN KEY (`blog_id`)
    REFERENCES `mydb`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `blog_id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  `post` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_blogs1_idx` (`blog_id` ASC),
  INDEX `fk_posts_admins1_idx` (`admin_id` ASC),
  CONSTRAINT `fk_posts_blogs1`
    FOREIGN KEY (`blog_id`)
    REFERENCES `mydb`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `mydb`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `blog_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  `comment` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_blogs_idx` (`blog_id` ASC),
  INDEX `fk_comments_posts1_idx` (`post_id` ASC),
  INDEX `fk_comments_admins1_idx` (`admin_id` ASC),
  CONSTRAINT `fk_comments_blogs`
    FOREIGN KEY (`blog_id`)
    REFERENCES `mydb`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `mydb`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `mydb`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`files`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`files` (
  `admin_id` INT NOT NULL,
  `blogs_id` INT NOT NULL,
  `files` TEXT NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  INDEX `fk_admins_has_blogs_blogs1_idx` (`blogs_id` ASC),
  INDEX `fk_admins_has_blogs_admins1_idx` (`admin_id` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_admins_has_blogs_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `mydb`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_admins_has_blogs_blogs1`
    FOREIGN KEY (`blogs_id`)
    REFERENCES `mydb`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user_viewing`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_viewing` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  `time_viewing` TIMESTAMP NOT NULL,
  `time_stayed` TIME NOT NULL,
  `user_viewingcol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_blogs_blogs2_idx` (`blog_id` ASC),
  INDEX `fk_users_has_blogs_users2_idx` (`user_id` ASC),
  CONSTRAINT `fk_users_has_blogs_users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_blogs_blogs2`
    FOREIGN KEY (`blog_id`)
    REFERENCES `mydb`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
