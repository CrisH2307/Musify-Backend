
/* Drop all tables [in reverse order]
DROP TABLE Customer_Accounts;
DROP TABLE Employee_Accounts;
DROP TABLE Transactions;
DROP TABLE Employees;
DROP TABLE Locations;
DROP TABLE Role;
DROP TABLE Customers;
*/

BEGIN 
    EXECUTE IMMEDIATE 'DROP TABLE Customers CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE Role CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE Locations CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE Employees CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE Account CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE Transactions CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE Customer_Accounts CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE Employee_Accounts CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;


/* New table creation */

-- Create the CUSTOMERS table
PROMPT '******* Create CUSTOMERS table';
CREATE TABLE Customers(
    LASTNAME VARCHAR(50),
    FIRSTNAME VARCHAR(50),
    ADDRESS VARCHAR(255),
    CITY VARCHAR(255),
    CUSTOMERNUMBER NUMBER(38,0),
    PRIMARY KEY(CUSTOMERNUMBER)
)

-- Create the ROLE table
CREATE TABLE Role (
    RoleID INT PRIMARY KEY,
    RoleName VARCHAR(50)
);

-- Create the Locations table
PROMPT '******* Create Locations table';
CREATE TABLE Locations (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Address VARCHAR(100),
    Phone VARCHAR(15)
    );
-- Insert data into the Locations table
INSERT ALL
 INTO Locations (LocationID, LocationName, Address, Phone) VALUES (1, 'Main Branch', '123 Main St', '123-456-7890')
 INTO Locations (LocationID, LocationName, Address, Phone) VALUES (2, 'Downtown Branch', '456 Elm St', '987-654-3210')
 INTO Locations (LocationID, LocationName, Address, Phone) VALUES (3, 'West End Branch', '789 Oak St', '555-555-5555')
 INTO Locations (LocationID, LocationName, Address, Phone) VALUES (4, 'North Branch', '101 Maple St', '888-888-8888')
 INTO Locations (LocationID, LocationName, Address, Phone) VALUES (5, 'South Branch', '555 Birch St', '999-999-9999')
SELECT * FROM DUAL;
COMMIT;


--Insert data into the Customer table
INSERT INTO Customers (LASTNAME, FIRSTNAME, ADDRESS, CITY, CUSTOMERNUMBER)
VALUES ('Smith', 'John', '123 Main Street', 'New York', 1);

-- Insert Customer 2
INSERT INTO Customers (LASTNAME, FIRSTNAME, ADDRESS, CITY, CUSTOMERNUMBER)
VALUES ('Johnson', 'Mary', '456 Elm Street', 'Los Angeles', 2);

-- Insert Customer 3
INSERT INTO Customers (LASTNAME, FIRSTNAME, ADDRESS, CITY, CUSTOMERNUMBER)
VALUES ('Brown', 'David', '789 Oak Avenue', 'Chicago', 3);

-- Insert Customer 4
INSERT INTO Customers (LASTNAME, FIRSTNAME, ADDRESS, CITY, CUSTOMERNUMBER)
VALUES ('Davis', 'Linda', '101 Pine Road', 'Houston', 4);

-- Insert Customer 5
INSERT INTO Customers (LASTNAME, FIRSTNAME, ADDRESS, CITY, CUSTOMERNUMBER)
VALUES ('Wilson', 'Susan', '555 Cedar Lane', 'Miami', 5);
SELECT * FROM DUAL;
COMMIT;

--Insert data into the Role Table
INSERT INTO Role (RoleID, RoleName)
VALUES (1, 'Customer');
INSERT INTO Role (RoleID, RoleName)
VALUES (2, 'Bank Teller');
INSERT INTO Role (RoleID, RoleName)
VALUES (3, 'Branch Manager');
INSERT INTO Role (RoleID, RoleName)
VALUES (4, 'Loan Officer');
INSERT INTO Role (RoleID, RoleName)
VALUES (5, 'Financial Advisor');
SELECT * FROM DUAL;
COMMIT;

--Insert data into the account table
-- Insert example account records
INSERT INTO ACCOUNT (AccountID, ACCOUNTTYPE, BALANCE, OPENDATE, CLOSEDATE)
VALUES (1, 'Savings', 1000.00, TO_DATE('2023-01-15', 'YYYY-MM-DD'), NULL);

INSERT INTO ACCOUNT (AccountID, ACCOUNTTYPE, BALANCE, OPENDATE, CLOSEDATE)
VALUES (2, 'Checking', 500.50, TO_DATE('2023-02-10', 'YYYY-MM-DD'), NULL);

INSERT INTO ACCOUNT (AccountID, ACCOUNTTYPE, BALANCE, OPENDATE, CLOSEDATE)
VALUES (3, 'Loan', -5000.00, TO_DATE('2022-12-05', 'YYYY-MM-DD'), TO_DATE('2023-03-20', 'YYYY-MM-DD'));

INSERT INTO ACCOUNT (AccountID, ACCOUNTTYPE, BALANCE, OPENDATE, CLOSEDATE)
VALUES (4, 'Credit Card', -1000.00, TO_DATE('2023-01-25', 'YYYY-MM-DD'), NULL);

INSERT INTO ACCOUNT (AccountID, ACCOUNTTYPE, BALANCE, OPENDATE, CLOSEDATE)
VALUES (5, 'Investment', 75000.00, TO_DATE('2023-03-01', 'YYYY-MM-DD'), NULL);
SELECT * FROM DUAL;
COMMIT;

-- Create the Employees  table
PROMPT '******* Create Employees table';
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Role INT, -- e.g., Customer Service, Branch Manager, IT Support
    Salary DECIMAL(10, 2),
    HireDate DATE,
    LocationID INT,
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID),
    FOREIGN KEY (Role) REFERENCES Role(RoleID)
);

-- Create the ACCOUNT table
PROMPT '******* Create ACCOUNT table';
CREATE TABLE ACCOUNT (
    AccountID NUMBER(38, 0) PRIMARY KEY,
    ACCOUNTTYPE VARCHAR(50),
    BALANCE DECIMAL(15, 2),
    OPENDATE DATE,
    CLOSEDATE DATE
);

PROMPT '******* Create CUSTOMER_ACCOUNTS table';
CREATE TABLE Customer_Accounts (
    CustomerID INT,
    AccountID INT,
    PRIMARY KEY (CustomerID, AccountID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CUSTOMERNUMBER),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
)

PROMPT '******* Create EMPLOYEE_ACCOUNTS table';
CREATE TABLE Employee_Accounts (
    EmployeeID INT,
    AccountID INT,
    PRIMARY KEY (EmployeeID, AccountID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);

PROMPT '******* Create Transactions table';
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT,
    TransactionType VARCHAR(20), -- e.g., Deposit, Withdrawal, Transfer
    Amount DECIMAL(15, 2),
    TransactionDate DATE,
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);
