CREATE DATABASE IF NOT EXISTS atm_demo;
USE atm_demo;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_name VARCHAR(50),
    balance DECIMAL(12,2)
);

CREATE TABLE cards (
    card_no CHAR(16) PRIMARY KEY,
    account_id INT,
    pin_hash CHAR(64),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE transactions (
    tx_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    card_no CHAR(16),
    atm_id INT,
    tx_type VARCHAR(20),
    amount DECIMAL(12,2),
    balance_after DECIMAL(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO accounts (owner_name, balance) VALUES ('Nguyen Van A', 2000000);
INSERT INTO cards (card_no, account_id, pin_hash)
VALUES ('1234567890123456', 1, SHA2('1234', 256));

-- Get-Content "D:\cnpm\BaiTapLab1\labs\lab07\atm_demo.sql" | & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
