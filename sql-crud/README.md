# SQL CRUD

## Part 1: Restaurant finder
1. the SQL code to create the required tables:

```
CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY,
    restaurant_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price_tier TEXT NOT NULL,
    neighborhood TEXT NOT NULL,
    opening_time TEXT NOT NULL,
    closing_time TEXT NOT NULL,
    average_rating REAL NOT NULL,
    good_for_kids TEXT NOT NULL
);
```

```
CREATE TABLE reviews (
    restaurant_id INTEGER PRIMARY KEY,
    review TEXT NOT NULL
);
```

2. the link to the practice CSV data files in the data directory: [restaurants.csv](data/restaurants.csv), [reviews.csv](data/reviews.csv)
3. the SQLite code to import the practice CSV data files into the tables:

```
.mode csv
.import C:/Users/Herry/Desktop/DDI/sql-crud-ryqherry/data/restaurants.csv restaurants --skip 1
.import C:/Users/Herry/Desktop/DDI/sql-crud-ryqherry/data/reviews.csv reviews --skip 1
```

4. the SQL queries that solve each of the tasks you were asked to do:
   
- 1.Find all cheap restaurants in a particular neighborhood (pick any neighborhood as an example).

```   
select * from restaurants where price_tier = "cheap" and neighborhood = "SoHo";
```

   - 2.Find all restaurants in a particular genre (pick any genre as an example) with 3 stars or more, ordered by the number of stars in descending order.

```
select * from restaurants where category = "Chinese" and average_rating >= 3 order by average_rating desc;
```

   - 3.Find all restaurants that are open now (see hint below).

```
select * from restaurants where opening_time <= strftime('%H:%M', 'now')and strftime('%H:%M', 'now') <= closing_time;
```

   - 4.Leave a review for a restaurant (pick any restaurant as an example).

```
insert into reviews (restaurant_id, review) values ("1", "Good food!");
```

   - 5.Delete all restaurants that are not good for kids.

```
delete from restaurants where good_for_kids = "FALSE”;
```

   - 6.Find the number of restaurants in each NYC neighborhood.

```
select neighborhood, count(id) from restaurants group by neighborhood;
```

## Part 2: Social media app
1. the SQL code to create the required tables:

```
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);
```

```
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    post_type TEXT NOT NULL,
    content TEXT NOT NULL,
    sender TEXT NOT NULL,
    recipient TEXT NOT NULL,
    post_time DATETIME,
    visible TEXT NOT NULL
);
```

2. the link to the practice CSV data files in the data directory: [posts.csv](data/posts.csv), [users.csv](data/users.csv)
3. the SQLite code to import the practice CSV data files into the tables:

```
.mode csv
.import C:/Users/Herry/Desktop/DDI/sql-crud-ryqherry/data/users.csv users --skip 1
.import C:/Users/Herry/Desktop/DDI/sql-crud-ryqherry/data/psts.csv posts --skip 1
```

4. the SQL queries that solve each of the tasks you were asked to do:
   
- 1.Register a new User.

```
insert into users (username, email, password) values ("CoulsonL", "cl1234@nyu.edu", "123456");
```

   - 2.Create a new Message sent by a particular User to a particular User (pick any two Users for example).

```
insert into posts (post_type, content, sender, recipient, post_time, visible) values ("Message", "When shall we meet?", "1", "2", "2023-02-26 22:00:00", "TRUE");
```

   - 3.Create a new Story by a particular User (pick any User for example).

```
insert into posts (post_type, content, sender, recipient, post_time, visible) values ("Story", "This is a story with one sentence.", "1", "all", "2023-02-26 22:00:00", "TRUE");
```

   - 4.Show the 10 most recent visible Messages and Stories, in order of recency.

```
select * from posts where visible = "TRUE" order by post_time desc limit 10;
```

   - 5.Show the 10 most recent visible Messages sent by a particular User to a particular User (pick any two Users for example), in order of recency.

```
select * from posts where sender = "110" and recipient = "956" and visible = "TRUE" order by post_time desc limit 10;
```

   - 6.Make all Stories that are more than 24 hours old invisible.

```
update posts set visible = "FALSE" where ROUND((JULIANDAY('now') - JULIANDAY(post_time)) * 24) > 24 and post_type = "Story";
```

   - 7.Show all invisible Messages and Stories, in order of recency.

```
select * from posts where visible = "FALSE" order by post_time desc;
```

   - 8.Show the number of posts by each User.

```
select sender, count(sender) from posts group by sender;
```

   - 9.Show the post text and email address of all posts and the User who made them within the last 24 hours.

```
select posts.post_content, users.email, users.username from posts inner join users on posts.sender = users.id where ROUND((JULIANDAY('now') - JULIANDAY(posts.post_time)) * 24) < 24;
```

   - 10.Show the email addresses of all Users who have not posted anything yet.

```
select users.email from users left join posts on posts.From_user = users.id WHERE posts.sender IS NULL;
```