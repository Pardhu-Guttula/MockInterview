create database mockinterview;
use mockinterview;
drop database mockinterview;
-- Fact Tables
CREATE TABLE InterviewFact (
    interviewID VARCHAR(255) PRIMARY KEY,
    interviewerID VARCHAR(255),   -- References Interviewer
    intervieweeID VARCHAR(255),   -- References Interviewee
    adminID VARCHAR(255),         -- Optionally References Admin
    slotID VARCHAR(255),
    performanceScore DOUBLE,
    time DATETIME NOT NULL,
    FOREIGN KEY (interviewerID) REFERENCES UserDim(userID),
    FOREIGN KEY (intervieweeID) REFERENCES UserDim(userID),
    FOREIGN KEY (adminID) REFERENCES UserDim(userID), -- Optional
    FOREIGN KEY (slotID) REFERENCES SlotDim(slotID)
);



CREATE TABLE SupportFact (
    supportID VARCHAR(255) PRIMARY KEY,
    raisedByID VARCHAR(255),
    status ENUM('Open', 'Resolved') NOT NULL,
    issue VARCHAR(255) NOT NULL,
    time DATETIME NOT NULL,
    FOREIGN KEY (raisedByID) REFERENCES UserDim(userID)
);


-- Dimension Tables
CREATE TABLE UserDim (
    userID VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    role ENUM('Interviewer', 'Interviewee', 'Admin') NOT NULL, -- Added Admin as a role option
    performanceScore DOUBLE
);


CREATE TABLE SlotDim (
    slotID VARCHAR(255) PRIMARY KEY,
    techRole VARCHAR(255) NOT NULL,
    level ENUM('Mock', 'Basic', 'Intermediate') NOT NULL,
    time DATETIME NOT NULL,
    status ENUM('Available', 'Accepted', 'Cancelled') NOT NULL
);


CREATE TABLE AdminDim (
    adminID VARCHAR(255) PRIMARY KEY,
    userID VARCHAR(255),
    FOREIGN KEY (userID) REFERENCES UserDim(userID)
);


select * from interviewfact;
insert into InterviewFact (interviewID, interviewerID, intervieweeID, adminID, slotID, performanceScore, time ) values
("INT-001", "INTWEE-001", "INTVWER-001", "A-001", 'SLOT-001', 80, '2024-10-19 12:30:00' );

INSERT INTO UserDim (userID, username, email, role, performanceScore)
VALUES
('INTWEE-001', 'John Doe', 'johndoe@example.com', 'Interviewee', NULL),
('INTVWER-001', 'Jane Smith', 'janesmith@example.com', 'Interviewer', 85.5),
('A-001', 'Admin User', 'admin@example.com', 'Admin', NULL);

INSERT INTO SlotDim (slotID, techRole, level, time, status)
VALUES
('SLOT-001', 'Frontend Developer', 'Basic', '2024-10-19 12:30:00', 'Available'),
('SLOT-002', 'Backend Developer', 'Intermediate', '2024-10-19 15:00:00', 'Accepted'),
('SLOT-003', 'Full Stack Developer', 'Mock', '2024-10-20 10:00:00', 'Cancelled');
