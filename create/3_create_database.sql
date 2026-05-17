\c cs415

-- WebUser
INSERT INTO WebUser
(web_user_id,first_name,last_name,email,password,created_date,is_active,last_login)
VALUES
(1,'Main','User','muser@email.com','12345',CURRENT_TIMESTAMP,true,CURRENT_TIMESTAMP),
(2,'Willie','Nelson','willie.nelson@email.com','12345',CURRENT_TIMESTAMP,true,CURRENT_TIMESTAMP);

ALTER SEQUENCE WebUser_web_user_id_seq RESTART WITH 100;

-- AddressType
INSERT INTO AddressType(address_type_id,address_type)
VALUES
(1,'Home'),
(2,'Work'),
(3,'Billing'),
(4,'Shipping');

ALTER SEQUENCE AddressType_address_type_id_seq RESTART WITH 6;

-- UserAddress
INSERT INTO UserAddress
(user_address_id,web_user_id,street_1,street_2,city,st,zip,country,address_type_id,created_date)
VALUES
(1,1,'100 Fake St','','Fake City','UT','84032','United States',1,CURRENT_TIMESTAMP),
(2,1,'200 Fake Ave','','Faker City','UT','84033','United States',3,CURRENT_TIMESTAMP),
(3,2,'200 Fake Ave','','Fakie City','UT','84033','United States',1,CURRENT_TIMESTAMP);

-- PhoneType
INSERT INTO PhoneType(phone_type_id,phone_type)
VALUES
(1,'Mobile'),
(2,'Home'),
(3,'Work'),
(4,'Emergency');

-- UserPhone
INSERT INTO UserPhone
(user_phone_id,web_user_id,phone_type_id,phone_number)
VALUES
(1,1,1,'801-111-1111'),
(2,1,2,'801-222-2222'),
(3,2,1,'801-333-3333'),
(4,2,4,'801-444-4444');

-- UserInfo
INSERT INTO UserInfo
(user_info_id,web_user_id,profile_bio,profile_picture,created_date)
VALUES
(1,1,'Main user bio',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTYZ4AiSTOD6IbZ-zuTTghcjbMr15XMj1XSQ&s',
CURRENT_TIMESTAMP),

(2,2,'Willie bio',
'https://is1-ssl.mzstatic.com/image/thumb/Features125/v4/b4/c2/9a/b4c29a1e-3b45-2b60-be65-dbb96d21e42a/mza_1383128222591135178.png/375x375bb.jpg',
CURRENT_TIMESTAMP);

-- PageData
INSERT INTO PageData
(page_data_id,week,title,description,image_url,page_name)
VALUES
(1,'Week 1','Overview and Setup',
'Create the GitHub repositories.',
'https://yt3.googleusercontent.com/vtckU0sW8j7MgqC6SnO4Ed3yaG0t-fFwhUEir-9SMTOuYBIXPkfSx3fzD3YrwUj8PI46fw1Le9o=s160-c-k-c0x00ffffff-no-rj',
'Week 1 - Overview and Setup'),

(2,'Week 2','Database Container and API',
'Install PostgreSQL in a container and access the data.',
'https://miro.medium.com/v2/resize:fit:720/format:webp/0*prut14lFoArZnPK5.jpg',
'Week 2 - Postres DB, Django API');