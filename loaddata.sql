CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Categories ('label') VALUES ('Movies')

INSERT INTO Categories (label) VALUES ('News');
INSERT INTO Categories (label) VALUES ('Movies');
INSERT INTO Categories (label) VALUES ('Sports');
INSERT INTO Categories (label) VALUES ('Music');
INSERT INTO Categories (label) VALUES ('Technology');


SELECT * 
FROM Categories

INSERT INTO "Posts" ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (1, 2, "My First Post", "2023-05-12", "https://example.com/image1.jpg", "This is my first post!", 1);

INSERT INTO "Posts" ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (2, 3, "Another Post", "2023-05-11", "https://example.com/image2.jpg", "Here's another post for you to enjoy.", 0);

INSERT INTO "Posts" ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (3, 1, "A Third Post", "2023-05-10", "https://example.com/image3.jpg", "This is the third post on my blog.", 1);

INSERT INTO "Posts" ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (2, 2, "My Favorite Things", "2023-05-09", "https://example.com/image4.jpg", "These are a few of my favorite things.", 1);


INSERT INTO Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active)
VALUES ('John', 'Doe', 'john.doe@email.com', 'I am a software engineer', 'johndoe', 'password123', 'https://example.com/profile.jpg', '2023-05-11', 1);

INSERT INTO Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active)
VALUES ('Jane', 'Doe', 'jane.doe@email.com', 'I am a web developer', 'janedoe', 'password456', 'https://example.com/profile.jpg', '2023-05-11', 1);

INSERT INTO Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active)
VALUES ('Alice', 'Smith', 'alice.smith@email.com', 'I am a graphic designer', 'alicesmith', 'password789', 'https://example.com/profile.jpg', '2023-05-11', 1);

INSERT INTO Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active)
VALUES ('Bob', 'Johnson', 'bob.johnson@email.com', 'I am a data analyst', 'bobjohnson', 'password101112', 'https://example.com/profile.jpg', '2023-05-11', 1);
