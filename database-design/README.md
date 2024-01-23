# Data Normalization and Entity-Relationship Diagramming

## The Original Data Set

| assignment_id | student_id | due_date | professor | assignment_topic                | classroom | grade | relevant_reading    | professor_email   |
| :------------ | :--------- | :------- | :-------- | :------------------------------ | :-------- | :---- | :------------------ | :---------------- |
| 1             | 1          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 80    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 2             | 7          | 18.11.21 | Logston   | Single table queries            | 60FA 314  | 25    | Dümmlers Chapter 11 | e.logston@foo.edu |
| 1             | 4          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 75    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 5             | 2          | 05.05.21 | Logston   | Python and pandas               | 60FA 314  | 92    | Dümmlers Chapter 14 | e.logston@foo.edu |
| 4             | 2          | 04.07.21 | Nevarez   | Spreadsheet aggregate functions | WWH 201   | 65    | Zehnder Page 87     | i.nevarez@foo.edu |
| ...           | ...        | ...      | ...       | ...                             | ...       | ...   | ...                 | ...               |

## What Makes the Original Data Set Not Compliant with 4NF

Let `assignment_id` be the primary key, then:
- `grade`is a fact of `student_id`, thus a non-key field is a fact about another non-key field, violating 4NF.
- `professor_email` is a fact of `professor`, thus a non-key field is a fact about another non-key field, violating 4NF.
- `classroom` is not a fact of `assignment_id`, thus a non-key field does not provide a fact about the entity uniquely identified by the primary key, violating 4NF.

## Tables Containing the 4NF-Compliant Version of the Data Set

### Table 1

| assignment_id | due_date | assignment_topic                | section_id | relevant_reading    |
| :------------ | :------- | :------------------------------ | :--------- | :------------------ |
| 1             | 23.02.21 | Data normalization              | 1          | Deumlich Chapter 3  |
| 2             | 18.11.21 | Single table queries            | 2          | Dümmlers Chapter 11 |
| 5             | 05.05.21 | Python and pandas               | 3          | Dümmlers Chapter 14 |
| 4             | 04.07.21 | Spreadsheet aggregate functions | 4          | Zehnder Page 87     |
| ...           | ...      | ...                             | ...        | ...                 |

### Table 2

| student_id | assignment_id | grade |
| :--------- | :------------ | :---- |
| 1          | 1             | 80    |
| 7          | 2             | 25    |
| 4          | 1             | 75    |
| 2          | 5             | 92    |
| 2          | 4             | 65    |
| ...        | ...           | ...   |

### Table 3

| professor_id | professor | professor_email   |
| :----------- | :-------- | :---------------- |
| 1            | Melvin    | l.melvin@foo.edu  |
| 2            | Logston   | e.logston@foo.edu |
| 3            | Nevarez   | i.nevarez@foo.edu |
| ...          | ...       | ...               |

### Table 4

| section_id | classroom | professor_id |
| :--------- | :-------- | :----------- |
| 1          | WWH 101   | 1            |
| 2          | 60FA 314  | 2            |
| 3          | 60FA 314  | 2            |
| 4          | WWH 201   | 3            |
| ...        | ...       | ...          |

## The ER Diagram of the 4NF-Compliant Version of the Data Set

![er diagram](./images/er-diagram.drawio.svg)

## What Changes I Made and How these Changes Make the Data 4NF-Compliant
- I split the original table into four smaller tables, with four different kinds of entities: assignments, students, professors, and sections.
- For table 1, I set `assignment_id` as the primary key, and set non-key fields: `due_date`, `assignment_topic`, `section_id`, and `relevant_reading`, which are all facts of assignment and they are not facts of each other. Then, this table is compliant with 4NF.
- For table 2, I set `student_id` and `assignment_id` as the compound primary key, and set a non-key field: `grade`, which is a fact of the entity uniquely identified by the compound primary key. Then, this table is clearly compliant with 4NF.
- For table 3, I set `professor_id` as the primary key, and set non-key fields: `professor`, and `professor_email`, which are two facts of professor and they are not facts of each other. And clearly, this is compliant with 4NF.
- For table 4, I set `section_id` as the primary key, and set non-key fields: `classroom`, and `professor_id`, which are two facts of serction and they are not facts of each other. Thus, this is compliant with 4NF as well. 
- Altogether, the original table has been transformed into four samller tables, and become compliant with 4NF.