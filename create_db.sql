-- Create Student table
-- DROP TABLE IF EXISTS Student;
CREATE TABLE Student (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT
);

-- Create Course table
-- DROP TABLE IF EXISTS Course;
CREATE TABLE Course (
    CourseID INTEGER PRIMARY KEY,
    Name TEXT,
    Professor TEXT
);

-- Create Student Courses table with foreign key reference to Student table
-- DROP TABLE IF EXISTS StudentCourses;
CREATE TABLE StudentCourses (
    StudentID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    PRIMARY KEY (StudentID, CourseID)
);

-- Create Course Gradable table
-- DROP TABLE IF EXISTS CourseGradeables;
CREATE TABLE CourseGradeables (
    AssignmentID INTEGER PRIMARY KEY,
    CourseID INTEGER,
    AssignmentType TEXT CHECK (AssignmentType IN ('test', 'quiz', 'essay', 'presentation', 'assignment')),
    DueDate DATE,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- Create Student Performance table with foreign key references to Student, Course Gradable tables
-- DROP TABLE IF EXISTS StudentPerformance;
CREATE TABLE StudentPerformance (
    StudentID INTEGER,
    AssignmentID INTEGER,
    TimeManagementFeedback TEXT CHECK (TimeManagementFeedback IN ('too much', 'too little', 'just enough')),
    Grade INTEGER,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (AssignmentID) REFERENCES CourseGradeables(AssignmentID),
    PRIMARY KEY (StudentID, AssignmentID)
);
