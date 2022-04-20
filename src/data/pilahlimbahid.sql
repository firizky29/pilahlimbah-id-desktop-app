
create table if not exists region (
	region_id INT PRIMARY KEY AUTO_INCREMENT,
	region VARCHAR(500) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(5) NOT NULL
);

create table if not exists bank (
    bank_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(100) NOT NULL,
    region_id INT,
    FOREIGN KEY (region_id)
    REFERENCES region(region_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

create table if not exists user(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fullname VARCHAR(100) NOT NULL,
    birthdate DATE NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    roles VARCHAR(50)
);

create table if not exists account (
	account_id INT PRIMARY KEY AUTO_INCREMENT,
	user_id INT,
	account_number VARCHAR(16) UNIQUE NOT NULL,
	security_code VARCHAR(100),
	bank_id INT,
	amount DECIMAL(15,2),
    FOREIGN KEY (bank_id)
    REFERENCES bank(bank_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (user_id)
    REFERENCES user(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

drop table if exists orderlist;
create table orderlist (
    orderlist_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    order_date datetime NOT NULL,
    deadline_date datetime NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (account_id)
    REFERENCES account(account_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

create table if not exists admin(
    admin_id INT PRIMARY KEY,
    FOREIGN KEY (admin_id)
    REFERENCES user(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

create table if not exists member(
    member_id INT PRIMARY KEY,
    region_id INT NOT NULL,
    FOREIGN KEY (member_id)
    REFERENCES user(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (region_id)
    REFERENCES region(region_id)
);


create table if not exists guest(
    guest_id INT PRIMARY KEY,
    region_id INT,
    FOREIGN KEY (guest_id)
    REFERENCES user(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (region_id)
    REFERENCES region(region_id)
    ON DELETE SET NULL
);

create table if not exists task(
    task_date DATE,
    task_id INT,
    task_name VARCHAR(100),
    description TEXT,
    PRIMARY KEY (task_date, task_id)
);

create table if not exists activity(
    activity_date DATE,
    task_id INT, 
    member_id INT,
    time_completed datetime NOT NULL,
    PRIMARY KEY(activity_date, task_id, member_id),
    FOREIGN KEY (member_id)
    REFERENCES member(member_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (activity_date, task_id)
    REFERENCES task(task_date, task_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

create table if not exists transactions(
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_time datetime, 
    account_id INT, 
    amount DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (account_id)
    REFERENCES account(account_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

create table if not exists content(
    content_id INT PRIMARY KEY AUTO_INCREMENT,
    content_title TEXT,
    content_text TEXT
);

delimiter //
CREATE TRIGGER insert_order AFTER INSERT ON orderlist
    FOR EACH ROW
    BEGIN
        INSERT INTO transactions(
          transaction_time, account_id, amount  
        ) values(
            NEW.order_date, NEW.account_id, NEW.amount
        );
        UPDATE account SET amount = amount - NEW.amount;
    END;//
delimiter ;

delimiter //
CREATE TRIGGER insert_guest AFTER INSERT ON guest
    FOR EACH ROW
    BEGIN
        UPDATE user SET roles = 'Guest'
        WHERE user_id = NEW.guest_id;
    END;//
delimiter ;

delimiter //
CREATE TRIGGER delete_guest AFTER DELETE ON guest
    FOR EACH ROW
    BEGIN
        UPDATE user SET roles = NULL
        WHERE user_id = OLD.guest_id;
    END;//
delimiter ;

delimiter //
CREATE TRIGGER delete_member AFTER DELETE ON member
    FOR EACH ROW
    BEGIN
        INSERT INTO guest (guest_id, region_id) VALUES (OLD.member_id, OLD.region_id);
    END;//
delimiter ;

delimiter //
CREATE TRIGGER insert_member AFTER INSERT ON member
    FOR EACH ROW
    BEGIN
        DELETE FROM guest WHERE guest_id = NEW.member_id;
        UPDATE user SET roles = 'Member'
        WHERE user_id = NEW.member_id;
    END;//
delimiter ;



INSERT INTO region(region_id, region, city, country, postal_code) VALUES
(1, '3153 Church Lane', 'English', 'Nepal', '16153'),
(2, '3417 East Lake Ct', 'Zuni', 'Kenya', '08545'),
(3, '616 SE Riverside Ln', 'Coalgate', 'Kuwait', '07564'),
(4, '841 Fox Hill Ln', 'Harrold', 'Paraguay', '17759'),
(5, '592 New Market St', 'Sea Cliff', 'Sierra Leone', '38357'),
(6, '872 White Rushwood Ct', 'Lake Villa', 'Iceland', '54611'),
(7, '1953 Fox Hill Lane', 'Mio', 'Guatemala', '43408'),
(8, '2256 SW Prospect Hill Ln', 'Palo', 'Mauritius', '89927'),
(9, '3894 E Rock Hill Lane', 'Russell', 'Pakistan', '34510'),
(10, '67 Highland Drive', 'Palo Alto', 'Moldova', '27379'),
(11, '95 Cedar Tree Rd', 'Russell Springs', 'Sri Lanka', '05932'),
(12, '1108 NW Monument Blvd', 'Lake Village', 'Panama', '08756'),
(13, '645 North Rose Hill St', 'Bingen', 'Romania', '53246'),
(14, '69 Ski Hill Parkway', 'Mira Loma', 'Ghana', '47420'),
(15, '1381 South Rose Hill Hwy', 'Englishtown', 'Israel', '14585'),
(16, '957 North Buttonwood Loop', 'Trabuco Canyon', 'Yemen', '91266'),
(17, '825 Hunting Hill Circle', 'Sea Girt', 'Spain', '03732'),
(18, '2728 East Hunting Hill Hwy', 'Tracy', 'Ghana', '39158'),
(19, '3640 S Sharp Hill Pkwy', 'Harsens Island', 'Mauritius', '79960'),
(20, '160 White Front Pkwy', 'Palo Cedro', 'Italy', '73960'),
(21, '579 E Monument Parkway', 'Enid', 'Ireland', '77891'),
(22, '143 Waterview Avenue', 'Lake Wales', 'United Kingdom', '12971'),
(23, '3384 Highland Street', 'Miramonte', 'Mauritania', '81470'),
(24, '153 Rose Hill Pkwy', 'Lake Worth', 'Iraq', '84567'),
(25, '776 W Prospect Hill Hwy', 'Russellton', 'Turkey', '28421'),
(26, '368 West Beachwood Ct', 'Hart', 'Georgia', '43101'),
(27, '3083 S Front Circle', 'Miranda', 'Colombia', '67522'),
(28, '1562 Deepwood Ln', 'Lake Zurich', 'South Africa', '68850'),
(29, '255 Chapel Hill Hwy', 'Sea Isle City', 'Estonia', '01366'),
(30, '1870 North Sharp Hill Court', 'Palo Pinto', 'Mexico', '43314'),
(31, '3781 South Hunting Hill Parkway', 'Enigma', 'India', '06621'),
(32, '2466 Rock Hill Circle', 'Misenheimer', 'Pakistan', '06849'),
(33, '3309 Hidden Parkwood Ct', 'Tracyton', 'Uganda', '63370'),
(34, '2470 1st Hwy', 'Lakefield', 'Namibia', '02933'),
(35, '93 East Deepwood Road', 'Coalinga', 'Austria', '69192'),
(36, '1667 NE Social Avenue', 'Binger', 'Peru', '42679'),
(37, '851 Deepwood Road', 'Russellville', 'Ghana', '07851'),
(38, '1743 Red Cedar Tree Hwy', 'Coalmont', 'Sweden', '01685'),
(39, '1334 Prospect Hill Road', 'Hartford', 'South Africa', '59890'),
(40, '1124 Old Hunting Hill Pkwy', 'Mishawaka', 'Austria', '71572'),
(41, '787 Hidden Edgewood Ln', 'Lakehurst', 'Chile', '55848'),
(42, '46 Glenwood Ct', 'Enka', 'Philippines', '30158'),
(43, '3143 Red Prospect Hill Avenue', 'Palo Verde', 'Lithuania', '73551'),
(44, '64 S Meadowview Ln', 'Bingham', 'United Kingdom', '18648'),
(45, '1327 W Mount Drive', 'Mishicot', 'Nepal', '39804'),
(46, '583 Market Ln', 'Russia', 'Brazil', '30248'),
(47, '473 New Social Lane', 'Coalton', 'Gambia', '30134'),
(48, '3353 Ironwood Ct', 'Lakeland', 'Argentina', '94055'),
(49, '2798 West Parkwood Loop', 'Seabrook', 'Indonesia', '72440'),
(50, '28 Riverview Way', 'Mission', 'Ghana', '58278');

--
-- Inserting data into table bank
--
INSERT INTO bank(bank_id, branch_name, region_id) VALUES
(1, 'Smart Solar Power Corporation', 35),
(2, 'Home Space Research Corp.', 50),
(3, 'Home Entertainment Inc.', 46),
(4, 'Special Space Explore Inc.', 22),
(5, 'United Media Corporation', 5),
(6, 'West Wind Power Co.', 11),
(7, 'Union Engineering Corporation', 24),
(8, 'International High-Technologies Group', 49),
(9, 'Beyond Space Explore Co.', 17),
(10, 'Special High-Technologies Group', 12),
(11, 'Federal L-Mobile Group', 18),
(12, 'Australian W-Mobile Group', 30),
(13, 'Australian Space Research Group', 6),
(14, 'Creative Technologies Corp.', 41),
(15, 'WorldWide Travel Group', 1),
(16, 'General Green Resources Corp.', 47),
(17, 'Creative Research Group', 25),
(18, 'General Software Group', 36),
(19, 'Canadian Nuclear Power Inc.', 7),
(20, 'General W-Mobile Corp.', 42),
(21, 'South Transport Inc.', 45),
(22, 'West Coast Q-Mobile Corporation', 37),
(23, 'Global Insurance Corporation', 31),
(24, 'Federal High-Technologies Co.', 2),
(25, 'Smart D-Mobile Corp.', 43),
(26, 'WorldWide Renewable Energy Corporation', 8),
(27, 'North 6D Electronic Inc.', 48),
(28, 'South High-Technologies Group', 3),
(29, 'International High-Technologies Group', 26),
(30, 'Creative Nuclear Power Co.', 13),
(31, 'Canadian Solar Energy Inc.', 19),
(32, 'Special Optics Inc.', 14),
(33, 'Australian Space Explore Inc.', 20),
(34, 'Smart High-Technologies Group', 38),
(35, 'American U-Mobile Corp.', 9),
(36, 'Flexible Natural Gas Energy Group', 4),
(37, 'Domestic 5G Wireless Group', 32),
(38, 'City Trust Inc.', 27),
(39, 'North Q-Mobile Inc.', 33),
(40, 'Advanced Devices Inc.', 10),
(41, 'Smart Automotive Corporation', 28),
(42, 'Professional 5G Wireless Corporation', 15),
(43, 'Global Mobile Corp.', 44),
(44, 'American High-Technologies Corporation', 21),
(45, 'Home Space Research Corporation', 23),
(46, 'Home 3G Wireless Group', 29),
(47, 'Professional Wave Energy Co.', 16),
(48, 'Flexible Optics Inc.', 39),
(49, 'International Business Corp.', 34),
(50, 'International Industry Co.', 40);


-- dummy account
insert into user values (1, 'pilahlimbahid', '08552d6b6d5545af73e9b14af205e832340ae4aca0d334f3ea52c3aae8c6ae58', 'pilahlimbah@sampah.id', 'Pilah Limbah', '2020-03-15', 'Male', NULL);
insert into account values (1, 1, '1234567890123456', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 1, 100000000.0);


insert into task (task_date, task_id, task_name, description) values ('2021-04-17', 1, 'Pilah Sampah', 'Bypass Left Femoral Artery to Left Femoral Artery with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-17', 2, 'Pilah Sampah', 'Extirpation of Matter from Cervix, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-17', 3, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Bladder, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-04-20', 1, 'Bakar Sampah', 'Occlusion of Large Intestine, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-20', 2, 'Bakar Sampah', 'Release Right Parotid Gland, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-20', 3, 'Pilah Sampah', 'Repair Right Axillary Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-23', 1, 'Bakar Sampah', 'Extraction of Right Cornea, External Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-04-23', 2, 'Pilah Sampah', 'Repair Right Femoral Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-23', 3, 'Bakar Sampah', 'Reposition Nasal Bone, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-26', 1, 'Buang Sampah', 'Fluoroscopy of Kidneys, Ureters and Bladder using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-04-26', 2, 'Bakar Sampah', 'Drainage of Right Lower Extremity Bursa and Ligament with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-26', 3, 'Pilah Sampah', 'Packing of Left Upper Arm using Packing Material');
insert into task (task_date, task_id, task_name, description) values ('2021-04-29', 1, 'Pilah Sampah', 'Excision of Left Internal Mammary Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-29', 2, 'Bakar Sampah', 'Inspection of Uterus and Cervix, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-04-29', 3, 'Pilah Sampah', 'Bypass Jejunum to Anus with Autologous Tissue Substitute, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2021-05-02', 1, 'Buang Sampah', 'Sensory Awareness-Processing-Integrity Assessment of Neurological System - Whole Body using Other Equipment');
insert into task (task_date, task_id, task_name, description) values ('2021-05-02', 2, 'Buang Sampah', 'Drainage of Female Perineum with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-02', 3, 'Bakar Sampah', 'Inspection of Right Lower Extremity, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-05', 1, 'Buang Sampah', 'Release Left Mandible, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-05', 2, 'Bakar Sampah', 'Supplement Lower Esophagus with Nonautologous Tissue Substitute, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2021-05-05', 3, 'Buang Sampah', 'Removal of Synthetic Substitute from Right Finger Phalangeal Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-08', 1, 'Buang Sampah', 'Reposition Right Tarsal with Internal Fixation Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-08', 2, 'Buang Sampah', 'Drainage of Cul-de-sac with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-08', 3, 'Buang Sampah', 'Inspection of Right Acromioclavicular Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-11', 1, 'Bakar Sampah', 'Drainage of Right Hand Muscle, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-11', 2, 'Buang Sampah', 'Extirpation of Matter from Right External Auditory Canal, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-05-11', 3, 'Bakar Sampah', 'Revision of Synthetic Substitute in Uterus and Cervix, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-14', 1, 'Bakar Sampah', 'Transfer Right Abdomen Muscle, Transverse Rectus Abdominis Myocutaneous Flap, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-14', 2, 'Pilah Sampah', 'Insertion of Pacemaker, Dual Chamber into Chest Subcutaneous Tissue and Fascia, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-14', 3, 'Bakar Sampah', 'Replacement of Right Lower Femur with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-17', 1, 'Buang Sampah', 'Dilation of Middle Colic Artery, Bifurcation, with Drug-eluting Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-17', 2, 'Bakar Sampah', 'Drainage of Left Internal Mammary Lymphatic, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-17', 3, 'Bakar Sampah', 'Bypass Jejunum to Ascending Colon with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-20', 1, 'Pilah Sampah', 'Excision of Bilateral Lungs, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-05-20', 2, 'Bakar Sampah', 'Repair Right Upper Leg Skin, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-20', 3, 'Pilah Sampah', 'Drainage of Left Main Bronchus with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-23', 1, 'Bakar Sampah', 'Bypass Right Kidney Pelvis to Left Ureter with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-23', 2, 'Pilah Sampah', 'Removal of Nonautologous Tissue Substitute from Right Acetabulum, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-23', 3, 'Pilah Sampah', 'Resection of Accessory Sinus, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-26', 1, 'Buang Sampah', 'Repair Right Metatarsal-Tarsal Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-26', 2, 'Bakar Sampah', 'Introduction of Anti-inflammatory into Eye, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-05-26', 3, 'Pilah Sampah', 'Replacement of Right Temporal Bone with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-29', 1, 'Bakar Sampah', 'Transplantation of Endocrine System into Products of Conception, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-29', 2, 'Buang Sampah', 'Drainage of Accessory Nerve with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-05-29', 3, 'Bakar Sampah', 'Revision of Synthetic Substitute in Spinal Canal, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-01', 1, 'Pilah Sampah', 'Removal of Synthetic Substitute from Left Carpal, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-01', 2, 'Bakar Sampah', 'Destruction of Head and Neck Bursa and Ligament, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-01', 3, 'Pilah Sampah', 'Dilation of Pulmonary Trunk with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-04', 1, 'Pilah Sampah', 'Supplement Thoracolumbar Vertebral Disc with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-04', 2, 'Bakar Sampah', 'Supplement Left Atrium with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-04', 3, 'Buang Sampah', 'Drainage of Acoustic Nerve, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-06-07', 1, 'Buang Sampah', 'Inspection of Left Sternoclavicular Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-07', 2, 'Bakar Sampah', 'Drainage of Left Orbit with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-07', 3, 'Pilah Sampah', 'Supplement Left Metacarpophalangeal Joint with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-10', 1, 'Buang Sampah', 'Drainage of Right Neck Muscle with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-10', 2, 'Buang Sampah', 'Insertion of Internal Fixation Device into Left Zygomatic Bone, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-10', 3, 'Bakar Sampah', 'Fusion of Left Sternoclavicular Joint with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-13', 1, 'Buang Sampah', 'Reattachment of Urethra, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-13', 2, 'Buang Sampah', 'Bypass Right Hepatic Duct to Stomach with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-13', 3, 'Pilah Sampah', 'Revision of Spacer in Left Toe Phalangeal Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-16', 1, 'Bakar Sampah', 'Plain Radiography of Right Internal Mammary Bypass Graft using High Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-06-16', 2, 'Bakar Sampah', 'Insertion of Stimulator Lead into Bladder, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-16', 3, 'Bakar Sampah', 'Revision of Spacer in Thoracic Vertebral Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-19', 1, 'Pilah Sampah', 'Revision of Other Device in Left Upper Extremity, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-19', 2, 'Pilah Sampah', 'Plain Radiography of Left Hand');
insert into task (task_date, task_id, task_name, description) values ('2021-06-19', 3, 'Buang Sampah', 'Dilation of Left Popliteal Artery, Bifurcation, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-22', 1, 'Bakar Sampah', 'Extirpation of Matter from Right Brachial Artery, Bifurcation, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-22', 2, 'Pilah Sampah', 'Removal of Feeding Device from Upper Intestinal Tract, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-22', 3, 'Bakar Sampah', 'Dilation of Coronary Artery, Four or More Arteries with Two Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-25', 1, 'Buang Sampah', 'Dilation of Right Ulnar Artery, Bifurcation, with Three Drug-eluting Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-25', 2, 'Buang Sampah', 'Extirpation of Matter from Left Acromioclavicular Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-25', 3, 'Pilah Sampah', 'Map Medulla Oblongata, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-28', 1, 'Buang Sampah', 'Drainage of Large Intestine, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-28', 2, 'Pilah Sampah', 'Robotic Assisted Procedure of Upper Extremity, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-06-28', 3, 'Pilah Sampah', 'Dilation of Left Anterior Tibial Artery with Three Drug-eluting Intraluminal Devices, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-01', 1, 'Pilah Sampah', 'Revision of Radioactive Element in Upper Jaw, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-01', 2, 'Buang Sampah', 'Release Multiple Parathyroid Glands, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-01', 3, 'Bakar Sampah', 'Replacement of Right Knee Joint, Femoral Surface with Synthetic Substitute, Cemented, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-04', 1, 'Bakar Sampah', 'Supplement Aortic Valve with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-04', 2, 'Bakar Sampah', 'Bypass Transverse Colon to Cutaneous, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-04', 3, 'Bakar Sampah', 'Restriction of Right Vertebral Artery with Bioactive Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-07', 1, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Left Ulna, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-07', 2, 'Pilah Sampah', 'Destruction of Right Renal Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-07', 3, 'Pilah Sampah', 'Immobilization of Left Foot using Other Device');
insert into task (task_date, task_id, task_name, description) values ('2021-07-10', 1, 'Bakar Sampah', 'Release Sacral Plexus, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-10', 2, 'Pilah Sampah', 'Replacement of Right Knee Joint with Synthetic Substitute, Uncemented, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-10', 3, 'Buang Sampah', 'Dilation of Right Lacrimal Duct with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-13', 1, 'Pilah Sampah', 'Revision of External Fixation Device in Left Humeral Head, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-13', 2, 'Bakar Sampah', 'Restriction of Right Colic Artery with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-13', 3, 'Bakar Sampah', 'Dilation of Right Internal Iliac Artery, Bifurcation, with Two Drug-eluting Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-16', 1, 'Pilah Sampah', 'Transfer Face Subcutaneous Tissue and Fascia with Skin, Subcutaneous Tissue and Fascia, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-16', 2, 'Bakar Sampah', 'Removal of Radioactive Element from Right Lower Extremity, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-16', 3, 'Bakar Sampah', 'Alteration of Right Upper Arm with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-19', 1, 'Bakar Sampah', 'Repair Left Subclavian Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-19', 2, 'Pilah Sampah', 'Hearing Screening Assessment using Occupational Hearing Equipment');
insert into task (task_date, task_id, task_name, description) values ('2021-07-19', 3, 'Pilah Sampah', 'Bypass Right Basilic Vein to Upper Vein with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-22', 1, 'Bakar Sampah', 'Restriction of Left External Carotid Artery with Bioactive Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-22', 2, 'Buang Sampah', 'Removal of Drainage Device from Scrotum and Tunica Vaginalis, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-22', 3, 'Pilah Sampah', 'Insertion of Infusion Device into Colic Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-25', 1, 'Buang Sampah', 'Repair Other Body System in Products of Conception with Other Device, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-07-25', 2, 'Bakar Sampah', 'Excision of Bilateral Testes, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-07-25', 3, 'Pilah Sampah', 'Reposition Left Greater Saphenous Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-28', 1, 'Pilah Sampah', 'Excision of Accessory Nerve, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-28', 2, 'Bakar Sampah', 'Excision of Pancreatic Duct, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2021-07-28', 3, 'Pilah Sampah', 'Replacement of Coccyx with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-31', 1, 'Bakar Sampah', 'Excision of Radial Nerve, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-07-31', 2, 'Buang Sampah', 'Alteration of Bilateral Breast, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-07-31', 3, 'Pilah Sampah', 'Bypass Superior Vena Cava to Pulmonary Trunk with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-03', 1, 'Buang Sampah', 'Dilation of Right Axillary Artery with Three Drug-eluting Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-03', 2, 'Bakar Sampah', 'Revision of Infusion Device in Lower Jaw, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-03', 3, 'Buang Sampah', 'Bypass Jejunum to Rectum with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-06', 1, 'Pilah Sampah', 'Extirpation of Matter from Left Trunk Bursa and Ligament, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-06', 2, 'Pilah Sampah', 'Ultrasonography of Penile Arteries');
insert into task (task_date, task_id, task_name, description) values ('2021-08-06', 3, 'Pilah Sampah', 'Drainage of Right Internal Mammary Artery with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-09', 1, 'Pilah Sampah', 'Supplement Right Ankle Tendon with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-09', 2, 'Buang Sampah', 'Revision of Synthetic Substitute in Penis, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-08-09', 3, 'Bakar Sampah', 'Supplement Buccal Mucosa with Synthetic Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-12', 1, 'Buang Sampah', 'Extirpation of Matter from Right Basilic Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-12', 2, 'Bakar Sampah', 'Magnetic Resonance Imaging (MRI) of Left Elbow');
insert into task (task_date, task_id, task_name, description) values ('2021-08-12', 3, 'Pilah Sampah', 'Transfer Training Treatment using Mechanical Equipment');
insert into task (task_date, task_id, task_name, description) values ('2021-08-15', 1, 'Buang Sampah', 'Destruction of Head Muscle, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-15', 2, 'Pilah Sampah', 'Drainage of Multiple Parathyroid Glands, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-08-15', 3, 'Bakar Sampah', 'Revision of Autologous Tissue Substitute in Lumbar Vertebral Disc, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-18', 1, 'Pilah Sampah', 'Dilation of Innominate Artery, Bifurcation, with Three Drug-eluting Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-18', 2, 'Pilah Sampah', 'Extirpation of Matter from Thoracic Spinal Cord, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-18', 3, 'Pilah Sampah', 'Drainage of Left Axilla, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-21', 1, 'Pilah Sampah', 'Bypass Right Common Iliac Vein to Lower Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-21', 2, 'Buang Sampah', 'Removal of Autologous Tissue Substitute from Left Pelvic Bone, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-21', 3, 'Buang Sampah', 'Bypass Esophageal Vein to Lower Vein with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-24', 1, 'Bakar Sampah', 'Fusion of Thoracic Vertebral Joint with Synthetic Substitute, Posterior Approach, Anterior Column, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-24', 2, 'Pilah Sampah', 'Revision of Monitoring Device in Gallbladder, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-24', 3, 'Bakar Sampah', 'Replacement of Bilateral Breast with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-27', 1, 'Bakar Sampah', 'Beam Radiation of Oropharynx using Photons 1 - 10 MeV');
insert into task (task_date, task_id, task_name, description) values ('2021-08-27', 2, 'Bakar Sampah', 'Introduction of Nutritional Substance into Products of Conception, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-08-27', 3, 'Pilah Sampah', 'Destruction of Left Tympanic Membrane, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-30', 1, 'Pilah Sampah', 'Transfusion of Nonautologous Fibrinogen into Products of Conception, Circulatory, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-08-30', 2, 'Pilah Sampah', 'Insertion of Intraluminal Device into Right External Iliac Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-08-30', 3, 'Pilah Sampah', 'Release Right Ethmoid Bone, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-02', 1, 'Buang Sampah', 'Replacement of Pulmonary Trunk with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-02', 2, 'Bakar Sampah', 'Repair Left Common Iliac Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-02', 3, 'Pilah Sampah', 'Removal of Synthetic Substitute from Right Tarsal, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-05', 1, 'Buang Sampah', 'Replacement of Right Patella with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-05', 2, 'Pilah Sampah', 'Drainage of Epidural Space, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-05', 3, 'Pilah Sampah', 'Excision of Left Vocal Cord, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-09-08', 1, 'Pilah Sampah', 'Supplement Right Thumb Phalanx with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-08', 2, 'Bakar Sampah', 'Beam Radiation of Tongue using Neutrons');
insert into task (task_date, task_id, task_name, description) values ('2021-09-08', 3, 'Bakar Sampah', 'Map Thalamus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-11', 1, 'Buang Sampah', 'Change Drainage Device in Epididymis and Spermatic Cord, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-11', 2, 'Buang Sampah', 'Drainage of Right Hip Bursa and Ligament, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-11', 3, 'Pilah Sampah', 'Introduction of Other Anti-infective into Respiratory Tract, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-14', 1, 'Pilah Sampah', 'Drainage of Right Lens, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-09-14', 2, 'Bakar Sampah', 'Restriction of Left Kidney Pelvis, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-14', 3, 'Buang Sampah', 'Drainage of Spinal Meninges with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-17', 1, 'Bakar Sampah', 'Drainage of Gastric Artery with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-17', 2, 'Bakar Sampah', 'Destruction of Upper Esophagus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-17', 3, 'Bakar Sampah', 'Bypass Right Internal Iliac Artery to Foot Artery with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-20', 1, 'Pilah Sampah', 'Fusion of Cervical Vertebral Joint with Nonautologous Tissue Substitute, Posterior Approach, Anterior Column, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-20', 2, 'Bakar Sampah', 'Revision of Synthetic Substitute in Lumbosacral Disc, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-20', 3, 'Pilah Sampah', 'Replacement of Superior Mesenteric Artery with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-23', 1, 'Pilah Sampah', 'Removal of Infusion Device from Pelvic Cavity, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-23', 2, 'Pilah Sampah', 'Repair Pons, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-23', 3, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Thoracic Vertebral Disc, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-26', 1, 'Buang Sampah', 'Transfer Right Lower Arm and Wrist Muscle with Skin and Subcutaneous Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-26', 2, 'Buang Sampah', 'Drainage of Left Rib, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-26', 3, 'Pilah Sampah', 'Bypass Right Renal Vein to Lower Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-29', 1, 'Bakar Sampah', 'Bypass Right External Iliac Artery to Bilateral Internal Iliac Arteries with Autologous Arterial Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-09-29', 2, 'Pilah Sampah', 'Stereotactic Gamma Beam Radiosurgery of Abdomen');
insert into task (task_date, task_id, task_name, description) values ('2021-09-29', 3, 'Pilah Sampah', 'Plain Radiography of Right Parotid Gland using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-10-02', 1, 'Buang Sampah', 'Bypass Left Hypogastric Vein to Lower Vein with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-02', 2, 'Buang Sampah', 'Insertion of Monitoring Device into Thoracic Aorta, Descending, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-02', 3, 'Pilah Sampah', 'Removal of Reservoir from Trunk Subcutaneous Tissue and Fascia, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-05', 1, 'Bakar Sampah', 'Occlusion of Ductus Arteriosus with Extraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-05', 2, 'Bakar Sampah', 'Ultrasonography of Bilateral Upper Extremity Veins');
insert into task (task_date, task_id, task_name, description) values ('2021-10-05', 3, 'Pilah Sampah', 'Drainage of Bone Marrow with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-08', 1, 'Bakar Sampah', 'Release Right Parietal Bone, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-08', 2, 'Pilah Sampah', 'Repair Left Thumb, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-08', 3, 'Buang Sampah', 'Reposition Left Tympanic Membrane, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2021-10-11', 1, 'Buang Sampah', 'Plain Radiography of Right Epididymis using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-10-11', 2, 'Buang Sampah', 'Release Left Upper Femur, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-11', 3, 'Bakar Sampah', 'Dilation of Left Popliteal Artery with Four or More Drug-eluting Intraluminal Devices, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-14', 1, 'Bakar Sampah', 'Removal of Brace on Abdominal Wall');
insert into task (task_date, task_id, task_name, description) values ('2021-10-14', 2, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Right Thumb Phalanx, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-14', 3, 'Buang Sampah', 'Dilation of Left Axillary Artery with Drug-eluting Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-17', 1, 'Bakar Sampah', 'Gastrointestinal System, Dilation');
insert into task (task_date, task_id, task_name, description) values ('2021-10-17', 2, 'Bakar Sampah', 'Revision of Internal Fixation Device in Left Elbow Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-17', 3, 'Bakar Sampah', 'Removal of Infusion Device from Endocrine Gland, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-20', 1, 'Pilah Sampah', 'Resection of Left Fallopian Tube, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-20', 2, 'Bakar Sampah', 'Revision of Drainage Device in Trachea, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-20', 3, 'Buang Sampah', 'Introduction of Local Anesthetic into Products of Conception, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-10-23', 1, 'Buang Sampah', 'Repair Appendix, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-10-23', 2, 'Pilah Sampah', 'Insertion of Internal Fixation Device into Right Humeral Head, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-23', 3, 'Bakar Sampah', 'Bypass Coronary Artery, Four or More Arteries from Abdominal Artery with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-26', 1, 'Buang Sampah', 'Abortion of Products of Conception, Abortifacient, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-10-26', 2, 'Pilah Sampah', 'Plain Radiography of Portal and Splanchnic Veins using High Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-10-26', 3, 'Buang Sampah', 'Bypass Abdominal Aorta to Right External Iliac Artery with Autologous Arterial Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-29', 1, 'Buang Sampah', 'Bypass Abdominal Aorta to Left External Iliac Artery with Autologous Arterial Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-29', 2, 'Pilah Sampah', 'Release Left Pulmonary Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-10-29', 3, 'Bakar Sampah', 'Alteration of Right Upper Leg with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-01', 1, 'Bakar Sampah', 'Alteration of Upper Back with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-01', 2, 'Bakar Sampah', 'Introduction of Monoclonal Antibody into Peripheral Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-01', 3, 'Buang Sampah', 'Low Dose Rate (LDR) Brachytherapy of Pineal Body using Iodine 125 (I-125)');
insert into task (task_date, task_id, task_name, description) values ('2021-11-04', 1, 'Buang Sampah', 'Repair Left Fallopian Tube, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-04', 2, 'Buang Sampah', 'Removal of Intraluminal Device from Larynx, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-04', 3, 'Bakar Sampah', 'Insertion of Endobronchial Valve into Right Main Bronchus, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-07', 1, 'Pilah Sampah', 'Stereotactic Gamma Beam Radiosurgery of Parathyroid Glands');
insert into task (task_date, task_id, task_name, description) values ('2021-11-07', 2, 'Pilah Sampah', 'Excision of Left Internal Carotid Artery, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-11-07', 3, 'Bakar Sampah', 'Removal of Intraluminal Device from Kidney, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-10', 1, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Left Extraocular Muscle, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-10', 2, 'Bakar Sampah', 'Repair Pharynx, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-10', 3, 'Pilah Sampah', 'Reposition Left Lesser Saphenous Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-13', 1, 'Pilah Sampah', 'Placement, Anatomical Orifices, Packing');
insert into task (task_date, task_id, task_name, description) values ('2021-11-13', 2, 'Pilah Sampah', 'Dilation of Right Axillary Artery with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-13', 3, 'Buang Sampah', 'Repair Left Femoral Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-16', 1, 'Pilah Sampah', 'Insertion of External Fixation Device into Left Carpal, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-16', 2, 'Bakar Sampah', 'Inspection of Penis, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-16', 3, 'Buang Sampah', 'Revision of Synthetic Substitute in Thoracic Vertebral Disc, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-19', 1, 'Pilah Sampah', 'Drainage of Celiac Artery with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-19', 2, 'Buang Sampah', 'Repair Right Thumb Phalanx, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-19', 3, 'Bakar Sampah', 'Resection of Right Extraocular Muscle, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-22', 1, 'Pilah Sampah', 'Excision of Prepuce, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-22', 2, 'Buang Sampah', 'Computerized Tomography (CT Scan) of Right Pelvic (Iliac) Veins using Low Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-11-22', 3, 'Buang Sampah', 'Supplement Left Hand Muscle with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-25', 1, 'Pilah Sampah', 'Removal of Radioactive Element from Left Upper Extremity, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-25', 2, 'Buang Sampah', 'Fluoroscopy of Right Fallopian Tube using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-11-25', 3, 'Pilah Sampah', 'Bypass Left Axillary Artery to Bilateral Lower Leg Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-28', 1, 'Bakar Sampah', 'Bypass Left Kidney Pelvis to Colocutaneous with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-28', 2, 'Pilah Sampah', 'Revision of Drainage Device in Right Lung, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-11-28', 3, 'Buang Sampah', 'Fusion of Left Knee Joint with External Fixation Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-01', 1, 'Pilah Sampah', 'Insertion of Monitoring Device into Urethra, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2021-12-01', 2, 'Pilah Sampah', 'Bypass Bilateral Vas Deferens to Right Epididymis with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-01', 3, 'Bakar Sampah', 'Replacement of Left Lacrimal Duct with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-04', 1, 'Pilah Sampah', 'Insertion of Radioactive Element into Pancreatic Duct, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-04', 2, 'Pilah Sampah', 'Release Left Seminal Vesicle, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-04', 3, 'Pilah Sampah', 'Occlusion of Cystic Duct with Extraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-07', 1, 'Bakar Sampah', 'Excision of Right Parotid Gland, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-12-07', 2, 'Bakar Sampah', 'Restriction of Right Ureter with Extraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-07', 3, 'Buang Sampah', 'Extirpation of Matter from Left Lens, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-10', 1, 'Pilah Sampah', 'Bypass Left Common Iliac Artery to Lower Artery with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-10', 2, 'Pilah Sampah', 'Plain Radiography of Right Hand-Finger Joint using High Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-12-10', 3, 'Pilah Sampah', 'Bypass Right Hepatic Duct to Caudate Hepatic Duct with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-13', 1, 'Buang Sampah', 'Drainage of Left Axilla, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-13', 2, 'Buang Sampah', 'Tomographic (Tomo) Nuclear Medicine Imaging of Right Upper Extremity using Technetium 99m (Tc-99m)');
insert into task (task_date, task_id, task_name, description) values ('2021-12-13', 3, 'Bakar Sampah', 'Revision of Bone Growth Stimulator in Lower Bone, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-16', 1, 'Pilah Sampah', 'Insertion of Internal Fixation Device into Right Lower Femur, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-16', 2, 'Pilah Sampah', 'Transfer Left Thorax Bursa and Ligament, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-16', 3, 'Bakar Sampah', 'Release Innominate Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-19', 1, 'Buang Sampah', 'Drainage of Bilateral Breast, Via Natural or Artificial Opening, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-12-19', 2, 'Pilah Sampah', 'Insertion of Infusion Device into Pancreatic Duct, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-19', 3, 'Buang Sampah', 'Computerized Tomography (CT Scan) of Hepatobiliary System, All using Low Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2021-12-22', 1, 'Buang Sampah', 'Repair Cisterna Chyli, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-22', 2, 'Bakar Sampah', 'Destruction of Left Humeral Shaft, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-22', 3, 'Bakar Sampah', 'Excision of Right Eustachian Tube, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-25', 1, 'Buang Sampah', 'Extirpation of Matter from Head and Neck Sympathetic Nerve, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-25', 2, 'Pilah Sampah', 'Drainage of Bladder Neck, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-12-25', 3, 'Buang Sampah', 'Dilation of Left Internal Mammary Artery with Four or More Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-28', 1, 'Buang Sampah', 'Reposition Left Hand Tendon, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-28', 2, 'Bakar Sampah', 'Drainage of Nose, External Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-12-28', 3, 'Buang Sampah', 'Dilation of Face Artery with Two Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-31', 1, 'Pilah Sampah', 'Excision of Buccal Mucosa, External Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2021-12-31', 2, 'Buang Sampah', 'Excision of Right Humeral Head, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2021-12-31', 3, 'Buang Sampah', 'Fragmentation in Common Bile Duct, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-03', 1, 'Buang Sampah', 'Chiropractic Manipulation of Pelvis, Long Lever Specific Contact');
insert into task (task_date, task_id, task_name, description) values ('2022-01-03', 2, 'Buang Sampah', 'Drainage of Stomach, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-01-03', 3, 'Buang Sampah', 'Drainage of Right Internal Iliac Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-06', 1, 'Bakar Sampah', 'Occlusion of Right External Iliac Vein with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-06', 2, 'Pilah Sampah', 'Drainage of Left Maxillary Sinus, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-06', 3, 'Buang Sampah', 'Removal of Radioactive Element from Pleura, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-09', 1, 'Buang Sampah', 'Drainage of Ileocecal Valve, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-09', 2, 'Buang Sampah', 'Excision of Pulmonary Valve, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-01-09', 3, 'Buang Sampah', 'Computerized Tomography (CT Scan) of Colon using High Osmolar Contrast, Unenhanced and Enhanced');
insert into task (task_date, task_id, task_name, description) values ('2022-01-12', 1, 'Pilah Sampah', 'Revision of Drainage Device in Occipital-cervical Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-12', 2, 'Bakar Sampah', 'Alteration of Head with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-12', 3, 'Pilah Sampah', 'Bypass Right Common Iliac Artery to Bilateral Internal Iliac Arteries with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-15', 1, 'Pilah Sampah', 'Dilation of Left Anterior Tibial Artery, Bifurcation, with Two Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-15', 2, 'Buang Sampah', 'Revision of Drainage Device in Bone Marrow, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-15', 3, 'Pilah Sampah', 'Drainage of Right Toe Phalanx with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-18', 1, 'Pilah Sampah', 'Drainage of Trachea, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-01-18', 2, 'Bakar Sampah', 'Revision of Internal Fixation Device in Left Finger Phalangeal Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-18', 3, 'Buang Sampah', 'Revision of Nonautologous Tissue Substitute in Lower Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-21', 1, 'Buang Sampah', 'Replacement of Bladder Neck with Autologous Tissue Substitute, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-01-21', 2, 'Pilah Sampah', 'Extirpation of Matter from Accessory Sinus, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-21', 3, 'Buang Sampah', 'Revision of Radioactive Element in Uterus and Cervix, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-01-24', 1, 'Pilah Sampah', 'Drainage of Spinal Canal, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-01-24', 2, 'Pilah Sampah', 'High Dose Rate (HDR) Brachytherapy of Oropharynx using Iodine 125 (I-125)');
insert into task (task_date, task_id, task_name, description) values ('2022-01-24', 3, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Urethra, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-01-27', 1, 'Bakar Sampah', 'Revision of Nonautologous Tissue Substitute in Left Auditory Ossicle, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-01-27', 2, 'Buang Sampah', 'Extirpation of Matter from Left Basilic Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-27', 3, 'Bakar Sampah', 'Destruction of Right Lower Femur, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-30', 1, 'Buang Sampah', 'Removal of Internal Fixation Device from Right Elbow Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-01-30', 2, 'Buang Sampah', 'Restriction of Ileum, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-01-30', 3, 'Pilah Sampah', 'Drainage of Portal Vein with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-02', 1, 'Bakar Sampah', 'Fluoroscopy of Left Ureter using Low Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-02-02', 2, 'Pilah Sampah', 'Revision of Monitoring Device in Heart, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-02', 3, 'Pilah Sampah', 'Drainage of Uterus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-05', 1, 'Buang Sampah', 'Insertion of Hybrid External Fixation Device into Left Ulna, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-05', 2, 'Pilah Sampah', 'Planar Nuclear Medicine Imaging of Chest using Iodine 123 (I-123)');
insert into task (task_date, task_id, task_name, description) values ('2022-02-05', 3, 'Pilah Sampah', 'Revision of Infusion Device in Tracheobronchial Tree, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-08', 1, 'Bakar Sampah', 'Drainage of Lower Gingiva, External Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-02-08', 2, 'Buang Sampah', 'Destruction of Bilateral Spermatic Cords, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-08', 3, 'Buang Sampah', 'Revision of Intraluminal Device in Ureter, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-11', 1, 'Bakar Sampah', 'Dilation of Left Radial Artery, Bifurcation, with Four or More Drug-eluting Intraluminal Devices, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-11', 2, 'Buang Sampah', 'Destruction of Right Maxilla, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-11', 3, 'Buang Sampah', 'Insertion of Ring External Fixation Device into Right Humeral Shaft, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-14', 1, 'Pilah Sampah', 'Supplement Bilateral External Ear with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-14', 2, 'Pilah Sampah', 'Excision of Right Upper Extremity Lymphatic, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-14', 3, 'Pilah Sampah', 'Computerized Tomography (CT Scan) of Neck using Low Osmolar Contrast, Unenhanced and Enhanced');
insert into task (task_date, task_id, task_name, description) values ('2022-02-17', 1, 'Buang Sampah', 'Revision of Intraluminal Device in Esophagus, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-02-17', 2, 'Pilah Sampah', 'Replacement of Hepatic Artery with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-17', 3, 'Pilah Sampah', 'Repair Hypothalamus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-20', 1, 'Pilah Sampah', 'Computerized Tomography (CT Scan) of Left Lower Extremity using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-02-20', 2, 'Pilah Sampah', 'Dilation of Gastric Artery with Four or More Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-20', 3, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Upper Muscle, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-23', 1, 'Buang Sampah', 'Drainage of Right Cornea, External Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-02-23', 2, 'Buang Sampah', 'Revision of Nonautologous Tissue Substitute in Right Breast, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-23', 3, 'Bakar Sampah', 'Replacement of Right Atrium with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-26', 1, 'Buang Sampah', 'Release Lumbosacral Disc, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-26', 2, 'Pilah Sampah', 'Release Left Lobe Liver, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-02-26', 3, 'Pilah Sampah', 'Upper Veins, Bypass');
insert into task (task_date, task_id, task_name, description) values ('2022-03-01', 1, 'Pilah Sampah', 'Insertion of Radioactive Element into Cervix, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-01', 2, 'Pilah Sampah', 'Introduction of Nonautologous Pancreatic Islet Cells into Biliary and Pancreatic Tract, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-03-01', 3, 'Pilah Sampah', 'Map Pons, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-04', 1, 'Buang Sampah', 'Excision of Lumbosacral Disc, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-03-04', 2, 'Buang Sampah', 'Release Sternum, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-04', 3, 'Bakar Sampah', 'Resection of Right Metacarpal, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-07', 1, 'Pilah Sampah', 'Removal of External Fixation Device from Right Metatarsal-Phalangeal Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-07', 2, 'Bakar Sampah', 'Removal of Autologous Tissue Substitute from Upper Tendon, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-07', 3, 'Bakar Sampah', 'Plain Radiography of Vasa Vasorum using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-03-10', 1, 'Pilah Sampah', 'Restriction of Left Internal Iliac Artery with Extraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-10', 2, 'Bakar Sampah', 'Insertion of Monitoring Device into Stomach, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-03-10', 3, 'Buang Sampah', 'Release Left Hip Muscle, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-13', 1, 'Pilah Sampah', 'Insertion of Airway into Mouth and Throat, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-03-13', 2, 'Bakar Sampah', 'Excision of Uvula, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-13', 3, 'Pilah Sampah', 'Repair Head Lymphatic, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-16', 1, 'Bakar Sampah', 'Supplement Left Shoulder Muscle with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-16', 2, 'Bakar Sampah', 'Destruction of Left Subclavian Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-16', 3, 'Pilah Sampah', 'Destruction of Superior Mesenteric Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-19', 1, 'Buang Sampah', 'Reposition Right Knee Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-19', 2, 'Bakar Sampah', 'Replacement of Left Temporal Artery with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-19', 3, 'Pilah Sampah', 'Removal of Synthetic Substitute from Cervical Vertebral Disc, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-22', 1, 'Pilah Sampah', 'Release Right Metatarsal, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-22', 2, 'Buang Sampah', 'Insertion of Infusion Device into Gastric Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-22', 3, 'Bakar Sampah', 'Drainage of Right Ovary with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-25', 1, 'Pilah Sampah', 'Drainage of Right Lower Arm, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-03-25', 2, 'Buang Sampah', 'Reattachment of Left Shoulder Bursa and Ligament, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-25', 3, 'Pilah Sampah', 'Fusion of Left Elbow Joint with Internal Fixation Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-28', 1, 'Bakar Sampah', 'Extirpation of Matter from Right Internal Iliac Artery, Bifurcation, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-28', 2, 'Bakar Sampah', 'Hearing and Related Disorderlists Counseling Treatment');
insert into task (task_date, task_id, task_name, description) values ('2022-03-28', 3, 'Bakar Sampah', 'Dilation of Right Hepatic Duct with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-31', 1, 'Buang Sampah', 'High Dose Rate (HDR) Brachytherapy of Thyroid using Californium 252 (Cf-252)');
insert into task (task_date, task_id, task_name, description) values ('2022-03-31', 2, 'Buang Sampah', 'Revision of Other Device in Right Lower Extremity, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-03-31', 3, 'Pilah Sampah', 'Dilation of Left Common Carotid Artery, Bifurcation, with Two Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-03', 1, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Left Metacarpocarpal Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-03', 2, 'Bakar Sampah', 'Dilation of Duodenum, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-04-03', 3, 'Buang Sampah', 'Reposition Left Thyroid Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-06', 1, 'Buang Sampah', 'Drainage of Clitoris, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-06', 2, 'Pilah Sampah', 'Alteration of Right Wrist Region with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-06', 3, 'Bakar Sampah', 'Supplement Inferior Mesenteric Artery with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-09', 1, 'Pilah Sampah', 'Beam Radiation of Prostate using Neutrons');
insert into task (task_date, task_id, task_name, description) values ('2022-04-09', 2, 'Bakar Sampah', 'Repair Left Acetabulum, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-09', 3, 'Buang Sampah', 'Fluoroscopy of Right Pulmonary Vein using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-04-12', 1, 'Bakar Sampah', 'Destruction of Left Ethmoid Sinus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-12', 2, 'Pilah Sampah', 'Insertion of Diaphragmatic Pacemaker Lead into Right Diaphragm, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-12', 3, 'Pilah Sampah', 'Reposition Left Peroneal Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-15', 1, 'Bakar Sampah', 'Extirpation of Matter from Left Hip Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-15', 2, 'Bakar Sampah', 'Replacement of Left Vocal Cord with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-15', 3, 'Pilah Sampah', 'Revision of Radioactive Element in Lower Jaw, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-18', 1, 'Buang Sampah', 'Drainage of Right Epididymis, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-18', 2, 'Bakar Sampah', 'Dilation of Coronary Artery, Two Arteries, Bifurcation, with Two Drug-eluting Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-18', 3, 'Bakar Sampah', 'Drainage of Left Foot Vein with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-21', 1, 'Pilah Sampah', 'Supplement Epiglottis with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-21', 2, 'Pilah Sampah', 'Drainage of Right Palatine Bone with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-21', 3, 'Pilah Sampah', 'Drainage of Right Testis, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-24', 1, 'Bakar Sampah', 'Fusion of Sacrococcygeal Joint with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-24', 2, 'Pilah Sampah', 'Bypass Right Internal Iliac Artery to Left Femoral Artery with Autologous Arterial Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-24', 3, 'Bakar Sampah', 'Drainage of Bilateral Epididymis, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-04-27', 1, 'Buang Sampah', 'Restriction of Right Subclavian Vein with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-27', 2, 'Bakar Sampah', 'Supplement Buccal Mucosa with Synthetic Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-27', 3, 'Buang Sampah', 'Replacement of Left Lower Eyelid with Nonautologous Tissue Substitute, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-30', 1, 'Buang Sampah', 'Excision of Right Wrist Bursa and Ligament, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-04-30', 2, 'Pilah Sampah', 'Extirpation of Matter from Hypothalamus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-04-30', 3, 'Bakar Sampah', 'Insertion of Infusion Device into Left Radial Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-03', 1, 'Bakar Sampah', 'Fluoroscopy of Lower Extremity');
insert into task (task_date, task_id, task_name, description) values ('2022-05-03', 2, 'Bakar Sampah', 'Insertion of Infusion Device into Tracheobronchial Tree, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-03', 3, 'Buang Sampah', 'Insertion of Internal Fixation Device into Left Clavicle, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-06', 1, 'Bakar Sampah', 'Repair Left Ankle Bursa and Ligament, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-06', 2, 'Buang Sampah', 'Removal of Stimulator Lead from Upper Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-06', 3, 'Pilah Sampah', 'Beam Radiation of Oropharynx using Neutrons');
insert into task (task_date, task_id, task_name, description) values ('2022-05-09', 1, 'Buang Sampah', 'Low Dose Rate (LDR) Brachytherapy of Abdomen using Iodine 125 (I-125)');
insert into task (task_date, task_id, task_name, description) values ('2022-05-09', 2, 'Buang Sampah', 'Revision of Nonautologous Tissue Substitute in Left Hip Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-09', 3, 'Pilah Sampah', 'Drainage of Epiglottis with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-12', 1, 'Bakar Sampah', 'Destruction of Penis, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-12', 2, 'Bakar Sampah', 'Supplement Left Trunk Tendon with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-12', 3, 'Pilah Sampah', 'Repair Right Hand Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-15', 1, 'Bakar Sampah', 'Destruction of Right Thyroid Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-15', 2, 'Buang Sampah', 'Drainage of Right Hip Bursa and Ligament, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-15', 3, 'Bakar Sampah', 'Fusion of Right Elbow Joint with Synthetic Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-18', 1, 'Bakar Sampah', 'Removal of Synthetic Substitute from Right Knee Joint, Tibial Surface, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-18', 2, 'Pilah Sampah', 'Resection of Left Shoulder Muscle, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-18', 3, 'Bakar Sampah', 'Fusion of Right Metacarpocarpal Joint with External Fixation Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-21', 1, 'Pilah Sampah', 'Extirpation of Matter from Right Radial Artery, Bifurcation, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-21', 2, 'Buang Sampah', 'Insertion of Internal Fixation Device into Hyoid Bone, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-21', 3, 'Buang Sampah', 'Supplement Perineum Tendon with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-24', 1, 'Buang Sampah', 'Fluoroscopy of Bilateral Temporomandibular Joints using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-05-24', 2, 'Pilah Sampah', 'Drainage of Left Main Bronchus, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-24', 3, 'Buang Sampah', 'Insertion of Intraluminal Device into Right Colic Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-27', 1, 'Bakar Sampah', 'Control Bleeding in Male Perineum, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-27', 2, 'Bakar Sampah', 'Alteration of Right Lower Extremity, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-27', 3, 'Bakar Sampah', 'Bypass Left Internal Iliac Artery to Left External Iliac Artery with Autologous Arterial Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-30', 1, 'Bakar Sampah', 'Bypass Splenic Vein to Lower Vein with Autologous Arterial Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-30', 2, 'Bakar Sampah', 'Reposition Left Femoral Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-05-30', 3, 'Pilah Sampah', 'Supplement Right Occipital Bone with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-02', 1, 'Bakar Sampah', 'Motor Function Treatment of Musculoskeletal System - Upper Back - Upper Extremity using Orthosis');
insert into task (task_date, task_id, task_name, description) values ('2022-06-02', 2, 'Bakar Sampah', 'Control Bleeding in Left Lower Extremity, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-02', 3, 'Buang Sampah', 'Laser Interstitial Thermal Therapy of Stomach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-05', 1, 'Pilah Sampah', 'Dilation of Left Internal Mammary Artery with Three Drug-eluting Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-05', 2, 'Pilah Sampah', 'Removal of Drainage Device from Right Wrist Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-05', 3, 'Pilah Sampah', 'Revision of Other Device in Left Pleural Cavity, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-08', 1, 'Pilah Sampah', 'Insertion of Ring External Fixation Device into Left Ulna, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-08', 2, 'Buang Sampah', 'Plain Radiography of Lumbar Facet Joint(s) using Low Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-06-08', 3, 'Buang Sampah', 'Dilation of Innominate Artery with Three Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-11', 1, 'Buang Sampah', 'Excision of Left Peroneal Artery, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-06-11', 2, 'Pilah Sampah', 'Dilation of Left Thyroid Artery, Bifurcation, with Three Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-11', 3, 'Bakar Sampah', 'Drainage of Brachial Plexus, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-06-14', 1, 'Bakar Sampah', 'Removal of Infusion Device from Cisterna Chyli, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-14', 2, 'Bakar Sampah', 'Supplement Left Brachial Vein with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-14', 3, 'Buang Sampah', 'Repair Left Shoulder Region, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-17', 1, 'Bakar Sampah', 'Evoked Otoacoustic Emissions, Screening Assessment');
insert into task (task_date, task_id, task_name, description) values ('2022-06-17', 2, 'Buang Sampah', 'Magnetic Resonance Imaging (MRI) of Sacrum and Coccyx using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-06-17', 3, 'Bakar Sampah', 'Reposition Cervical Vertebral Joint with Internal Fixation Device, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-20', 1, 'Bakar Sampah', 'Supplement Cerebral Meninges with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-20', 2, 'Pilah Sampah', 'Supplement Left Humeral Shaft with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-20', 3, 'Bakar Sampah', 'Release Left Ulna, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-23', 1, 'Pilah Sampah', 'Revision of Drainage Device in Upper Tendon, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-23', 2, 'Pilah Sampah', 'Insertion of Radioactive Element into Head, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-23', 3, 'Buang Sampah', 'Supplement Right Upper Arm Muscle with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-26', 1, 'Buang Sampah', 'Computerized Tomography (CT Scan) of Abdominal Aorta using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-06-26', 2, 'Pilah Sampah', 'Tomographic (Tomo) Nuclear Medicine Imaging of Upper Extremity using Fluorine 18 (F-18)');
insert into task (task_date, task_id, task_name, description) values ('2022-06-26', 3, 'Buang Sampah', 'Excision of Left Thorax Tendon, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-29', 1, 'Buang Sampah', 'Drainage of Thoracic Duct with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-29', 2, 'Pilah Sampah', 'Transfusion of Autologous Serum Albumin into Peripheral Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-06-29', 3, 'Buang Sampah', 'Dilation of Left Hepatic Duct with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-02', 1, 'Bakar Sampah', 'Division of Left Zygomatic Bone, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-02', 2, 'Bakar Sampah', 'Low Dose Rate (LDR) Brachytherapy of Testis using Iodine 125 (I-125)');
insert into task (task_date, task_id, task_name, description) values ('2022-07-02', 3, 'Buang Sampah', 'Removal of Synthetic Substitute from Mediastinum, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-05', 1, 'Buang Sampah', 'Revision of Infusion Device in Right Sternoclavicular Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-05', 2, 'Buang Sampah', 'Revision of Nonautologous Tissue Substitute in Lower Muscle, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-05', 3, 'Pilah Sampah', 'Drainage of Right Trunk Bursa and Ligament, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-07-08', 1, 'Buang Sampah', 'Supplement Left Elbow Bursa and Ligament with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-08', 2, 'Bakar Sampah', 'Replacement of Left Ventricle with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-08', 3, 'Buang Sampah', 'Removal of Synthetic Substitute from Sacrum, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-11', 1, 'Buang Sampah', 'Extirpation of Matter from Left Superior Parathyroid Gland, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-11', 2, 'Bakar Sampah', 'Plain Radiography of Left Hand-Finger Joint');
insert into task (task_date, task_id, task_name, description) values ('2022-07-11', 3, 'Buang Sampah', 'Excision of Left Sphenoid Bone, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-14', 1, 'Bakar Sampah', 'Dilation of Left Internal Carotid Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-14', 2, 'Buang Sampah', 'Repair Skin in Products of Conception, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-07-14', 3, 'Pilah Sampah', 'Reposition Left Toe Phalangeal Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-17', 1, 'Buang Sampah', 'Supplement Left Ulna with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-17', 2, 'Pilah Sampah', 'Restriction of Colic Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-17', 3, 'Bakar Sampah', 'Excision of Right Lower Arm, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-20', 1, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Right Ulna, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-20', 2, 'Bakar Sampah', 'Bypass Right Lacrimal Duct to Nasal Cavity, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-20', 3, 'Pilah Sampah', 'Insertion of Infusion Device into Uterus and Cervix, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-07-23', 1, 'Bakar Sampah', 'Supplement Left Glenoid Cavity with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-23', 2, 'Bakar Sampah', 'Drainage of Left Pleura, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-23', 3, 'Pilah Sampah', 'Monitoring of Venous Flow, Peripheral, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-26', 1, 'Bakar Sampah', 'Repair Respiratory System in Products of Conception with Other Device, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-07-26', 2, 'Bakar Sampah', 'Revision of Nonautologous Tissue Substitute in Left Eye, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-26', 3, 'Buang Sampah', 'Dilation of Right Subclavian Artery, Bifurcation, with Four or More Drug-eluting Intraluminal Devices, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-29', 1, 'Bakar Sampah', 'Drainage of Upper Jaw, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-07-29', 2, 'Pilah Sampah', 'Replacement of Right Conjunctiva with Autologous Tissue Substitute, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-07-29', 3, 'Pilah Sampah', 'Muscle Performance Treatment of Neurological System - Whole Body using Prosthesis');
insert into task (task_date, task_id, task_name, description) values ('2022-08-01', 1, 'Pilah Sampah', 'Resection of Right Superior Parathyroid Gland, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-01', 2, 'Buang Sampah', 'Bypass Right Common Iliac Artery to Left Renal Artery with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-01', 3, 'Bakar Sampah', 'Bypass Right External Iliac Artery to Bilateral Femoral Arteries with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-04', 1, 'Pilah Sampah', 'Reposition Right Parotid Duct, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-04', 2, 'Bakar Sampah', 'Removal of Extraluminal Device from Kidney, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-08-04', 3, 'Bakar Sampah', 'Occlusion of Left Basilic Vein with Extraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-07', 1, 'Bakar Sampah', 'Insertion of Infusion Device into Left Face Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-07', 2, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Right Thumb Phalanx, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-07', 3, 'Buang Sampah', 'Insertion of External Fixation Device into Skull, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-10', 1, 'Pilah Sampah', 'Drainage of Right Ulnar Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-10', 2, 'Pilah Sampah', 'Alteration of Upper Jaw, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-10', 3, 'Bakar Sampah', 'Supplement Right Renal Vein with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-13', 1, 'Bakar Sampah', 'Transfer Left Upper Leg Tendon, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-13', 2, 'Bakar Sampah', 'Stereotactic Other Photon Radiosurgery of Head and Neck');
insert into task (task_date, task_id, task_name, description) values ('2022-08-13', 3, 'Buang Sampah', 'Insertion of Infusion Device into Left Foot, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-16', 1, 'Pilah Sampah', 'Dilation of Right Common Carotid Artery, Bifurcation, with Drug-eluting Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-16', 2, 'Buang Sampah', 'Ventilation, Respiration and Circulation Assessment of Respiratory System - Upper Back - Upper Extremity using Mechanical Equipment');
insert into task (task_date, task_id, task_name, description) values ('2022-08-16', 3, 'Bakar Sampah', 'Destruction of Right Toe Phalangeal Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-19', 1, 'Pilah Sampah', 'Release Right Sphenoid Sinus, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-19', 2, 'Bakar Sampah', 'Bypass Left Radial Artery to Lower Arm Vein with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-19', 3, 'Pilah Sampah', 'Excision of Bilateral Breast, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-22', 1, 'Pilah Sampah', 'Drainage of Left Foot Tendon with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-22', 2, 'Pilah Sampah', 'Subcutaneous Tissue and Fascia, Division');
insert into task (task_date, task_id, task_name, description) values ('2022-08-22', 3, 'Buang Sampah', 'Occlusion of Pancreatic Duct with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-25', 1, 'Pilah Sampah', 'Removal of Autologous Tissue Substitute from Upper Intestinal Tract, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-25', 2, 'Bakar Sampah', 'Dilation of Right External Carotid Artery with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-25', 3, 'Buang Sampah', 'Drainage of Right Tunica Vaginalis with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-28', 1, 'Bakar Sampah', 'Extirpation of Matter from Right Foot Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-28', 2, 'Buang Sampah', 'Control Bleeding in Right Shoulder Region, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-28', 3, 'Buang Sampah', 'Extirpation of Matter from Epiglottis, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-31', 1, 'Pilah Sampah', 'Destruction of Medulla Oblongata, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-31', 2, 'Buang Sampah', 'Excision of Uterine Supporting Structure, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-08-31', 3, 'Pilah Sampah', 'Drainage of Ampulla of Vater with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-03', 1, 'Bakar Sampah', 'Revision of Extraluminal Device in Left Eye, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-03', 2, 'Buang Sampah', 'Change Drainage Device in Lymphatic, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-03', 3, 'Pilah Sampah', 'Removal of External Fixation Device from Left Radius, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-06', 1, 'Buang Sampah', 'Restriction of Bladder Neck with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-06', 2, 'Bakar Sampah', 'Transfusion of Nonautologous Plasma Cryoprecipitate into Central Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-06', 3, 'Buang Sampah', 'Insertion of Neurostimulator Lead into Left Innominate Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-09', 1, 'Bakar Sampah', 'Restriction of Right Internal Carotid Artery with Bioactive Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-09', 2, 'Bakar Sampah', 'Bypass Left Axillary Artery to Bilateral Lower Arm Artery with Autologous Arterial Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-09', 3, 'Pilah Sampah', 'Insertion of External Fixation Device into Right Finger Phalanx, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-12', 1, 'Buang Sampah', 'Dilation of Right Axillary Artery, Bifurcation, with Two Drug-eluting Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-12', 2, 'Pilah Sampah', 'Dilation of Left Renal Vein with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-12', 3, 'Bakar Sampah', 'Repair Musculoskeletal System in Products of Conception, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-09-15', 1, 'Pilah Sampah', 'Drainage of Esophageal Vein, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-09-15', 2, 'Pilah Sampah', 'Resection of Right Ovary, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-15', 3, 'Pilah Sampah', 'Bypass Abdominal Aorta to Right External Iliac Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-18', 1, 'Bakar Sampah', 'Inspection of Head, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-18', 2, 'Bakar Sampah', 'Removal of Drainage Device from Lymphatic, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-18', 3, 'Buang Sampah', 'Resection of Products of Conception, Ectopic, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2022-09-21', 1, 'Buang Sampah', 'Revision of Autologous Tissue Substitute in Left Finger Phalangeal Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-21', 2, 'Buang Sampah', 'Insertion of Internal Fixation Device into Right Elbow Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-21', 3, 'Pilah Sampah', 'Fusion of Left Carpal Joint with External Fixation Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-24', 1, 'Pilah Sampah', 'Fusion of Left Tarsal Joint with Synthetic Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-24', 2, 'Pilah Sampah', 'Replacement of Right Tibia with Synthetic Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-24', 3, 'Buang Sampah', 'Release Coccygeal Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-27', 1, 'Buang Sampah', 'Excision of Left External Auditory Canal, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-27', 2, 'Pilah Sampah', 'Dilation of Right Subclavian Vein with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-27', 3, 'Pilah Sampah', 'Supplement Left Orbit with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-30', 1, 'Bakar Sampah', 'Alteration of Lower Jaw with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-30', 2, 'Buang Sampah', 'Replacement of Left Sphenoid Bone with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-09-30', 3, 'Buang Sampah', 'Drainage of Left Subclavian Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-03', 1, 'Pilah Sampah', 'Supplement Right Lower Extremity with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-03', 2, 'Bakar Sampah', 'Insertion of Infusion Device into Cervical Vertebral Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-03', 3, 'Buang Sampah', 'Reposition Left Frontal Bone, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-06', 1, 'Pilah Sampah', 'Replacement of Abdomen Skin with Autologous Tissue Substitute, Partial Thickness, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-06', 2, 'Bakar Sampah', 'Insertion of Monitoring Device into Small Intestine, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-06', 3, 'Pilah Sampah', 'Bypass Left Axillary Artery to Left Extracranial Artery with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-09', 1, 'Buang Sampah', 'Removal of Monitoring Device from Lower Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-09', 2, 'Bakar Sampah', 'Destruction of Thalamus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-09', 3, 'Bakar Sampah', 'Inspection of Lumbosacral Disc, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-12', 1, 'Pilah Sampah', 'Fusion of Left Metacarpophalangeal Joint with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-12', 2, 'Pilah Sampah', 'Release Right Lower Arm and Wrist Tendon, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-12', 3, 'Pilah Sampah', 'Insertion of Intraluminal Device into Left Cephalic Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-15', 1, 'Bakar Sampah', 'Repair Right Mandible, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-15', 2, 'Bakar Sampah', 'Dilation of Right Hand Artery, Bifurcation, with Two Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-15', 3, 'Buang Sampah', 'Dilation of Right Brachial Artery with Drug-eluting Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-18', 1, 'Buang Sampah', 'Supplement Right Foot Tendon with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-18', 2, 'Buang Sampah', 'Revision of Nonautologous Tissue Substitute in Face, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-18', 3, 'Pilah Sampah', 'Repair Left Ankle Region, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-21', 1, 'Bakar Sampah', 'Occlusion of Aortic Lymphatic with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-21', 2, 'Buang Sampah', 'Occlusion of Thorax Lymphatic with Extraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-21', 3, 'Buang Sampah', 'Destruction of Thyroid Gland, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-24', 1, 'Buang Sampah', 'Physical Rehabilitation and Diagnostic Audiology, Rehabilitation, Activities of Daily Living Treatment');
insert into task (task_date, task_id, task_name, description) values ('2022-10-24', 2, 'Pilah Sampah', 'Resection of Right Superior Parathyroid Gland, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-24', 3, 'Buang Sampah', 'Plain Radiography of Right Breast');
insert into task (task_date, task_id, task_name, description) values ('2022-10-27', 1, 'Bakar Sampah', 'Reattachment of Left Ring Finger, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-27', 2, 'Buang Sampah', 'Release Left Renal Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-27', 3, 'Bakar Sampah', 'High Dose Rate (HDR) Brachytherapy of Hard Palate using Californium 252 (Cf-252)');
insert into task (task_date, task_id, task_name, description) values ('2022-10-30', 1, 'Buang Sampah', 'Repair Cerebral Hemisphere, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-30', 2, 'Buang Sampah', 'Bypass Left Basilic Vein to Upper Vein with Autologous Venous Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-10-30', 3, 'Pilah Sampah', 'Extirpation of Matter from Left Finger Phalangeal Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-02', 1, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Male Perineum, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-02', 2, 'Bakar Sampah', 'Supplement Right Toe Phalanx with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-02', 3, 'Buang Sampah', 'Caregiver Training in Application, Proper Use and Care of Devices using Assistive, Adaptive, Supportive or Protective Equipment');
insert into task (task_date, task_id, task_name, description) values ('2022-11-05', 1, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Right Upper Extremity, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-05', 2, 'Bakar Sampah', 'Excision of Peroneal Nerve, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2022-11-05', 3, 'Buang Sampah', 'Dilation of Coronary Artery, Three Arteries, Bifurcation, with Four or More Drug-eluting Intraluminal Devices, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-08', 1, 'Pilah Sampah', 'Change Traction Apparatus on Right Toe');
insert into task (task_date, task_id, task_name, description) values ('2022-11-08', 2, 'Pilah Sampah', 'Repair Right Lower Lobe Bronchus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-08', 3, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Lumbar Vertebra, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-11', 1, 'Buang Sampah', 'Inspection of Lumbar Vertebral Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-11', 2, 'Buang Sampah', 'Supplement Right External Jugular Vein with Synthetic Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-11', 3, 'Pilah Sampah', 'Extirpation of Matter from Rectum, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-11-14', 1, 'Buang Sampah', 'Revision of Autologous Tissue Substitute in Brain, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-14', 2, 'Pilah Sampah', 'Removal of Infusion Device from Female Perineum, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-14', 3, 'Buang Sampah', 'Bypass Right Subclavian Artery to Right Pulmonary Artery with Autologous Venous Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-17', 1, 'Pilah Sampah', 'Release Anus, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-17', 2, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Upper Muscle, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-17', 3, 'Bakar Sampah', 'Drainage of Right Brachial Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-20', 1, 'Bakar Sampah', 'Drainage of Right Upper Extremity Lymphatic with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-20', 2, 'Buang Sampah', 'Repair Left Choroid, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-20', 3, 'Bakar Sampah', 'Auditory Processing Assessment using Other Equipment');
insert into task (task_date, task_id, task_name, description) values ('2022-11-23', 1, 'Buang Sampah', 'Introduction of Destructive Agent into Pericardial Cavity, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-23', 2, 'Pilah Sampah', 'Destruction of Left Metatarsal, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-23', 3, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Sacrum, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-26', 1, 'Pilah Sampah', 'Insertion of Limb Lengthening External Fixation Device into Right Lower Femur, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-26', 2, 'Pilah Sampah', 'Repair Coronary Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-26', 3, 'Pilah Sampah', 'Supplement Right Sternoclavicular Joint with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-29', 1, 'Buang Sampah', 'Replacement of Right Carpal with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-29', 2, 'Pilah Sampah', 'Destruction of Right Main Bronchus, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-11-29', 3, 'Pilah Sampah', 'Insertion of Monitoring Device into Endocrine Gland, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-02', 1, 'Buang Sampah', 'Introduction of Autologous Somatic Stem Cells into Cranial Cavity and Brain, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-02', 2, 'Pilah Sampah', 'Bypass Abdominal Aorta to Lower Artery with Autologous Arterial Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-02', 3, 'Buang Sampah', 'Revision of Drainage Device in Upper Bursa and Ligament, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-05', 1, 'Pilah Sampah', 'Extirpation of Matter from Left Trunk Tendon, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-05', 2, 'Buang Sampah', 'Excision of Right Shoulder Muscle, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-05', 3, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Right Carpal, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-08', 1, 'Buang Sampah', 'Lower Arteries, Extirpation');
insert into task (task_date, task_id, task_name, description) values ('2022-12-08', 2, 'Bakar Sampah', 'Radiation Therapy, Male Reproductive System, Stereotactic Radiosurgery');
insert into task (task_date, task_id, task_name, description) values ('2022-12-08', 3, 'Pilah Sampah', 'Computerized Tomography (CT Scan) of Left Toe(s) using Low Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2022-12-11', 1, 'Buang Sampah', 'Upper Veins, Dilation');
insert into task (task_date, task_id, task_name, description) values ('2022-12-11', 2, 'Buang Sampah', 'Occlusion of Right Innominate Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-11', 3, 'Buang Sampah', 'Revision of Infusion Device in Pericardial Cavity, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-14', 1, 'Bakar Sampah', 'Destruction of Right Lung, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-14', 2, 'Pilah Sampah', 'Supplement Right Renal Vein with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-14', 3, 'Buang Sampah', 'Resection of Right Hand Muscle, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-17', 1, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Right Humeral Shaft, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-17', 2, 'Pilah Sampah', 'Drainage of Right Radial Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-17', 3, 'Bakar Sampah', 'Extirpation of Matter from Right Axillary Artery, Bifurcation, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-20', 1, 'Buang Sampah', 'Dilation of Right Kidney Pelvis with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-20', 2, 'Pilah Sampah', 'Bypass Ileum to Descending Colon, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-12-20', 3, 'Pilah Sampah', 'Reposition Right Sphenoid Bone with Internal Fixation Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-23', 1, 'Pilah Sampah', 'Monitoring of Lymphatic Pressure, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-23', 2, 'Buang Sampah', 'Replacement of Right Hip Joint with Synthetic Substitute, Uncemented, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-23', 3, 'Bakar Sampah', 'Drainage of Carina with Drainage Device, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2022-12-26', 1, 'Pilah Sampah', 'Bypass Accessory Pancreatic Duct to Duodenum with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-26', 2, 'Buang Sampah', 'Removal of Infusion Device from Left Metatarsal-Phalangeal Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-26', 3, 'Buang Sampah', 'Removal of Synthetic Substitute from Bladder, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-29', 1, 'Pilah Sampah', 'Excision of Left Colic Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-29', 2, 'Bakar Sampah', 'Dilation of Coronary Artery, One Artery with Radioactive Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2022-12-29', 3, 'Buang Sampah', 'Dilation of Descending Colon with Intraluminal Device, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2023-01-01', 1, 'Buang Sampah', 'Occlusion of Left Hand Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-01', 2, 'Buang Sampah', 'Drainage of Sacrum, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-01-01', 3, 'Buang Sampah', 'Resection of Left Shoulder Muscle, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-04', 1, 'Bakar Sampah', 'Release Right Pulmonary Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-04', 2, 'Bakar Sampah', 'Release Right Hand Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-04', 3, 'Pilah Sampah', 'Drainage of Left Abdomen Muscle, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-01-07', 1, 'Bakar Sampah', 'Replacement of Right Finger Phalanx with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-07', 2, 'Bakar Sampah', 'Range of Motion and Joint Integrity Assessment of Musculoskeletal System - Upper Back - Upper Extremity');
insert into task (task_date, task_id, task_name, description) values ('2023-01-07', 3, 'Pilah Sampah', 'Supplement Right Iris with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-10', 1, 'Buang Sampah', 'Drainage of Bilateral Seminal Vesicles, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-01-10', 2, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Trunk Subcutaneous Tissue and Fascia, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-10', 3, 'Buang Sampah', 'Revision of Intraluminal Device in Upper Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-13', 1, 'Pilah Sampah', 'Repair Right Upper Arm Tendon, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-13', 2, 'Bakar Sampah', 'Individual Counseling for Substance Abuse Treatment, Vocational');
insert into task (task_date, task_id, task_name, description) values ('2023-01-13', 3, 'Pilah Sampah', 'Bypass Right Common Iliac Artery to Bilateral Internal Iliac Arteries with Autologous Arterial Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-16', 1, 'Pilah Sampah', 'Insertion of Monoplanar External Fixation Device into Left Upper Femur, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-16', 2, 'Bakar Sampah', 'Drainage of Lumbar Sympathetic Nerve, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-01-16', 3, 'Buang Sampah', 'Ultrasonography of Inferior Vena Cava, Guidance');
insert into task (task_date, task_id, task_name, description) values ('2023-01-19', 1, 'Bakar Sampah', 'Excision of Female Perineum, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-01-19', 2, 'Buang Sampah', 'Release Innominate Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-19', 3, 'Bakar Sampah', 'Introduction of Monoclonal Antibody into Eye, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-22', 1, 'Pilah Sampah', 'Drainage of Peritoneal Cavity with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-22', 2, 'Buang Sampah', 'Bypass Left Popliteal Artery to Lower Extremity Artery with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-22', 3, 'Buang Sampah', 'Destruction of Left Spermatic Cord, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-25', 1, 'Buang Sampah', 'Tendons, Destruction');
insert into task (task_date, task_id, task_name, description) values ('2023-01-25', 2, 'Pilah Sampah', 'Alteration of Left Elbow Region with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-25', 3, 'Pilah Sampah', 'Inspection of Right Knee Region, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-28', 1, 'Buang Sampah', 'Transfer Abducens Nerve to Vagus Nerve, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-28', 2, 'Pilah Sampah', 'Repair Right Elbow Region, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-28', 3, 'Buang Sampah', 'Drainage of Right Upper Arm Tendon, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-01-31', 1, 'Pilah Sampah', 'Supplement Left Thorax Muscle with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-31', 2, 'Buang Sampah', 'Replacement of Right Scapula with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-01-31', 3, 'Bakar Sampah', 'Restriction of Right Anterior Tibial Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-03', 1, 'Buang Sampah', 'Occlusion of Left Basilic Vein with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-03', 2, 'Bakar Sampah', 'Release Nasal Bone, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-03', 3, 'Buang Sampah', 'Repair Bladder, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-06', 1, 'Buang Sampah', 'Transfer Left Ankle Tendon, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-06', 2, 'Pilah Sampah', 'Resection of Left Lower Arm and Wrist Tendon, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-06', 3, 'Bakar Sampah', 'Removal of Internal Fixation Device from Right Radius, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-09', 1, 'Pilah Sampah', 'Insertion of Intramedullary Internal Fixation Device into Left Radius, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-09', 2, 'Bakar Sampah', 'Drainage of Abducens Nerve with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-09', 3, 'Buang Sampah', 'Revision of Intraluminal Device in Great Vessel, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-12', 1, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Left Radius, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-12', 2, 'Buang Sampah', 'Replacement of Epiglottis with Nonautologous Tissue Substitute, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2023-02-12', 3, 'Bakar Sampah', 'Supplement Common Bile Duct with Synthetic Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-15', 1, 'Bakar Sampah', 'Drainage of Sternum with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-15', 2, 'Bakar Sampah', 'Caregiver Training in Bed Mobility using Orthosis');
insert into task (task_date, task_id, task_name, description) values ('2023-02-15', 3, 'Pilah Sampah', 'Occlusion of Left Fallopian Tube with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-18', 1, 'Pilah Sampah', 'Creation of Mitral Valve from Common Atrioventricular Valve using Zooplastic Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-18', 2, 'Buang Sampah', 'Replacement of Left Metatarsal with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-18', 3, 'Pilah Sampah', 'Insertion of Radioactive Element into Left Knee Region, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-21', 1, 'Pilah Sampah', 'Extirpation of Matter from Pulmonary Trunk, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-21', 2, 'Buang Sampah', 'Excision of Buccal Mucosa, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-02-21', 3, 'Pilah Sampah', 'Supplement Left Thorax Tendon with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-24', 1, 'Pilah Sampah', 'Drainage of Right Lower Extremity Bursa and Ligament, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-02-24', 2, 'Buang Sampah', 'Ultrasonography of Lower Extremity');
insert into task (task_date, task_id, task_name, description) values ('2023-02-24', 3, 'Buang Sampah', 'Excision of Right Hand Subcutaneous Tissue and Fascia, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-27', 1, 'Pilah Sampah', 'Bypass Ileum to Anus with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-27', 2, 'Bakar Sampah', 'Transfusion of Autologous Frozen Plasma into Central Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-02-27', 3, 'Buang Sampah', 'Bypass Left Common Iliac Artery to Right Renal Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-02', 1, 'Bakar Sampah', 'Dilation of Right Radial Artery, Bifurcation, with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-02', 2, 'Bakar Sampah', 'Insertion of Defibrillator Lead into Left Ventricle, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-02', 3, 'Buang Sampah', 'Insertion of Intraluminal Device into Colic Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-05', 1, 'Buang Sampah', 'Fluoroscopy of Portal and Splanchnic Veins using High Osmolar Contrast, Guidance');
insert into task (task_date, task_id, task_name, description) values ('2023-03-05', 2, 'Buang Sampah', 'Drainage of Right Foot Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-05', 3, 'Buang Sampah', 'Insertion of Internal Fixation Device into Right Finger Phalangeal Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-08', 1, 'Pilah Sampah', 'Revision of Spacer in Left Metatarsal-Tarsal Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-08', 2, 'Bakar Sampah', 'Filtered Speech Assessment using Audiovisual Equipment');
insert into task (task_date, task_id, task_name, description) values ('2023-03-08', 3, 'Bakar Sampah', 'Low Dose Rate (LDR) Brachytherapy of Stomach using Other Isotope');
insert into task (task_date, task_id, task_name, description) values ('2023-03-11', 1, 'Pilah Sampah', 'Removal of Radioactive Element from Left Eye, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-11', 2, 'Buang Sampah', 'Removal of Drainage Device from Pleura, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-11', 3, 'Buang Sampah', 'Stereotactic Other Photon Radiosurgery of Thorax Lymphatics');
insert into task (task_date, task_id, task_name, description) values ('2023-03-14', 1, 'Pilah Sampah', 'Dilation of Ileocecal Valve with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-14', 2, 'Pilah Sampah', 'Bypass Superior Vena Cava to Right Pulmonary Vein with Autologous Arterial Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-14', 3, 'Buang Sampah', 'Resection of Right Ankle Bursa and Ligament, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-17', 1, 'Bakar Sampah', 'Transfusion of Autologous White Cells into Central Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-17', 2, 'Bakar Sampah', 'Bypass Bilateral Vas Deferens to Right Vas Deferens with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-17', 3, 'Pilah Sampah', 'Repair Left Ovary, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-20', 1, 'Bakar Sampah', 'Excision of Brachial Plexus, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-03-20', 2, 'Buang Sampah', 'Computerized Tomography (CT Scan) of Colon using Low Osmolar Contrast, Unenhanced and Enhanced');
insert into task (task_date, task_id, task_name, description) values ('2023-03-20', 3, 'Buang Sampah', 'Fusion of Right Sternoclavicular Joint with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-23', 1, 'Pilah Sampah', 'Excision of Left Fallopian Tube, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-03-23', 2, 'Buang Sampah', 'Fragmentation in Right Pleural Cavity, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-23', 3, 'Pilah Sampah', 'Transfer Buccal Mucosa, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-26', 1, 'Buang Sampah', 'Extraction of Sacral Sympathetic Nerve, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-26', 2, 'Buang Sampah', 'Removal of Intermittent Pressure Device on Left Thumb');
insert into task (task_date, task_id, task_name, description) values ('2023-03-26', 3, 'Buang Sampah', 'Drainage of Cul-de-sac with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-29', 1, 'Pilah Sampah', 'Removal of Splint on Face');
insert into task (task_date, task_id, task_name, description) values ('2023-03-29', 2, 'Buang Sampah', 'Detachment at Left Hindquarter, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-03-29', 3, 'Pilah Sampah', 'Gait Training-Functional Ambulation Treatment using Other Equipment');
insert into task (task_date, task_id, task_name, description) values ('2023-04-01', 1, 'Buang Sampah', 'Drainage of Oral Cavity and Throat, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-01', 2, 'Buang Sampah', 'Division of Left Hand Muscle, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-01', 3, 'Bakar Sampah', 'Respiratory System, Extraction');
insert into task (task_date, task_id, task_name, description) values ('2023-04-04', 1, 'Pilah Sampah', 'Drainage of Left Mandible, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-04-04', 2, 'Bakar Sampah', 'Removal of Drainage Device from Lower Bone, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-04', 3, 'Buang Sampah', 'Supplement Right Abdomen Bursa and Ligament with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-07', 1, 'Pilah Sampah', 'Excision of Esophagogastric Junction, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-04-07', 2, 'Bakar Sampah', 'Fusion of Left Metatarsal-Phalangeal Joint with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-07', 3, 'Buang Sampah', 'Removal of Nonautologous Tissue Substitute from Left Tibia, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-10', 1, 'Buang Sampah', 'Removal of Infusion Device from Pancreatic Duct, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-10', 2, 'Buang Sampah', 'Release Left Lacrimal Duct, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-10', 3, 'Buang Sampah', 'Removal of Cast on Neck');
insert into task (task_date, task_id, task_name, description) values ('2023-04-13', 1, 'Buang Sampah', 'Therapeutic Exercise Treatment of Integumentary System - Whole Body using Assistive, Adaptive, Supportive or Protective Equipment');
insert into task (task_date, task_id, task_name, description) values ('2023-04-13', 2, 'Buang Sampah', 'Drainage of Left Shoulder Muscle, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-13', 3, 'Buang Sampah', 'Dilation of Right Femoral Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-16', 1, 'Bakar Sampah', 'Removal of Spacer from Right Metatarsal-Tarsal Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-16', 2, 'Bakar Sampah', 'Coordination-Dexterity Treatment of Neurological System - Whole Body using Other Equipment');
insert into task (task_date, task_id, task_name, description) values ('2023-04-16', 3, 'Pilah Sampah', 'Alteration of Male Perineum with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-19', 1, 'Bakar Sampah', 'Fusion of Right Elbow Joint with Autologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-19', 2, 'Bakar Sampah', 'Revision of Internal Fixation Device in Right Finger Phalanx, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-19', 3, 'Bakar Sampah', 'Alteration of Right Lower Extremity with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-22', 1, 'Buang Sampah', 'Occlusion of Left Uterine Artery with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-22', 2, 'Pilah Sampah', 'Occlusion of Intracranial Vein with Extraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-22', 3, 'Bakar Sampah', 'Insertion of Infusion Device into Right Lower Arm, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-25', 1, 'Bakar Sampah', 'Reposition Jejunum, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-25', 2, 'Pilah Sampah', 'Removal of Nonautologous Tissue Substitute from Epididymis and Spermatic Cord, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-25', 3, 'Bakar Sampah', 'Supplement Left Lower Leg Tendon with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-28', 1, 'Pilah Sampah', 'Revision of Autologous Tissue Substitute in Right Hip Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-28', 2, 'Buang Sampah', 'Occlusion of Pelvis Lymphatic with Extraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-04-28', 3, 'Pilah Sampah', 'Transfer Right Upper Leg Muscle with Skin and Subcutaneous Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-01', 1, 'Bakar Sampah', 'Revision of Monitoring Device in Right Lung, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-05-01', 2, 'Pilah Sampah', 'Dilation of Right Renal Artery, Bifurcation, with Four or More Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-01', 3, 'Pilah Sampah', 'Fusion of Right Tarsal Joint with Internal Fixation Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-04', 1, 'Bakar Sampah', 'Repair Left Tympanic Membrane, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-05-04', 2, 'Pilah Sampah', 'Replacement of Right Hip Joint, Femoral Surface with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-04', 3, 'Bakar Sampah', 'Insertion of Radioactive Element into Mediastinum, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-07', 1, 'Pilah Sampah', 'Removal of Intraluminal Device from Stomach, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-07', 2, 'Buang Sampah', 'Extirpation of Matter from Para-aortic Body, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-07', 3, 'Bakar Sampah', 'Bypass Right Subclavian Artery to Right Lower Arm Artery with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-10', 1, 'Bakar Sampah', 'Inspection of Upper Tendon, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-10', 2, 'Bakar Sampah', 'Removal of Synthetic Substitute from Left Tibia, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-10', 3, 'Pilah Sampah', 'Reposition Left Iris, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-13', 1, 'Buang Sampah', 'Revision of Autologous Tissue Substitute in Left Hip Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-13', 2, 'Buang Sampah', 'Replacement of Chordae Tendineae with Zooplastic Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-13', 3, 'Pilah Sampah', 'Revision of External Fixation Device in Right Knee Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-16', 1, 'Bakar Sampah', 'Restriction of Cisterna Chyli with Extraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-16', 2, 'Bakar Sampah', 'Extirpation of Matter from Lingula Bronchus, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2023-05-16', 3, 'Pilah Sampah', 'Drainage of Right Hip Muscle with Drainage Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-19', 1, 'Buang Sampah', 'Dilation of Inferior Mesenteric Artery, Bifurcation, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-19', 2, 'Buang Sampah', 'Excision of Right Elbow Bursa and Ligament, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-19', 3, 'Bakar Sampah', 'Drainage of Right Ureter with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-22', 1, 'Pilah Sampah', 'Plaque Radiation of Stomach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-22', 2, 'Bakar Sampah', 'Dilation of Right Common Iliac Artery with Four or More Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-22', 3, 'Bakar Sampah', 'Excision of Right Pulmonary Artery, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-05-25', 1, 'Pilah Sampah', 'Occlusion of Left Pulmonary Vein with Extraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-25', 2, 'Buang Sampah', 'Revision of Intraluminal Device in Urethra, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2023-05-25', 3, 'Pilah Sampah', 'Destruction of Left Subclavian Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-28', 1, 'Buang Sampah', 'Supplement Left Lower Eyelid with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-28', 2, 'Pilah Sampah', 'Division of Right Glenoid Cavity, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-28', 3, 'Buang Sampah', 'Gastrointestinal System, Reattachment');
insert into task (task_date, task_id, task_name, description) values ('2023-05-31', 1, 'Bakar Sampah', 'Revision of Spacer in Right Sternoclavicular Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-31', 2, 'Pilah Sampah', 'Destruction of Left Lower Lung Lobe, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-05-31', 3, 'Pilah Sampah', 'Replacement of Right Zygomatic Bone with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-03', 1, 'Pilah Sampah', 'Feeding-Eating Treatment using Other Equipment');
insert into task (task_date, task_id, task_name, description) values ('2023-06-03', 2, 'Bakar Sampah', 'Removal of Autologous Tissue Substitute from Heart, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-03', 3, 'Bakar Sampah', 'Occlusion of Right Face Vein with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-06', 1, 'Pilah Sampah', 'Release Accessory Sinus, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-06', 2, 'Buang Sampah', 'Supplement Left Neck Lymphatic with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-06', 3, 'Bakar Sampah', 'Drainage of Left Axillary Vein, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-06-09', 1, 'Buang Sampah', 'Control Bleeding in Lower Back, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-09', 2, 'Bakar Sampah', 'Supplement Left Atrium with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-09', 3, 'Bakar Sampah', 'Excision of Jejunum, Via Natural or Artificial Opening Endoscopic, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-06-12', 1, 'Bakar Sampah', 'Excision of Right Trunk Tendon, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-06-12', 2, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Brain, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-12', 3, 'Bakar Sampah', 'Occlusion of Right Vertebral Vein with Extraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-15', 1, 'Bakar Sampah', 'Release Small Intestine, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-15', 2, 'Bakar Sampah', 'Drainage of Esophageal Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-15', 3, 'Buang Sampah', 'Control Bleeding in Left Femoral Region, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-18', 1, 'Bakar Sampah', 'Insertion of Infusion Device into Oral Cavity and Throat, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-18', 2, 'Pilah Sampah', 'Dilation of Right Femoral Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-18', 3, 'Buang Sampah', 'Reposition Right Elbow Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-21', 1, 'Buang Sampah', 'Supplement Right Elbow Bursa and Ligament with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-21', 2, 'Buang Sampah', 'Removal of Drainage Device from Female Perineum, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-21', 3, 'Pilah Sampah', 'Removal of Bandage on Neck');
insert into task (task_date, task_id, task_name, description) values ('2023-06-24', 1, 'Bakar Sampah', 'Fusion of Left Knee Joint with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-24', 2, 'Pilah Sampah', 'Insertion of Pedicle-Based Spinal Stabilization Device into Cervical Vertebral Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-24', 3, 'Buang Sampah', 'Integumentary Integrity Assessment of Musculoskeletal System - Whole Body');
insert into task (task_date, task_id, task_name, description) values ('2023-06-27', 1, 'Bakar Sampah', 'Dilation of Right Radial Artery with Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-27', 2, 'Bakar Sampah', 'Drainage of Left Trunk Bursa and Ligament, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-06-27', 3, 'Buang Sampah', 'Reflex Integrity Assessment of Neurological System - Lower Back - Lower Extremity');
insert into task (task_date, task_id, task_name, description) values ('2023-06-30', 1, 'Bakar Sampah', 'Fragmentation in Pelvic Cavity, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-30', 2, 'Bakar Sampah', 'Fusion of Lumbosacral Joint with Synthetic Substitute, Anterior Approach, Anterior Column, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-06-30', 3, 'Bakar Sampah', 'Insertion of Intraluminal Device into Left Brachial Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-03', 1, 'Buang Sampah', 'Drainage of Occipital-cervical Joint, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-07-03', 2, 'Bakar Sampah', 'Revision of Drainage Device in Left Eye, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-03', 3, 'Bakar Sampah', 'Insertion of Infusion Device into Left Metatarsal-Phalangeal Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-06', 1, 'Pilah Sampah', 'Gait and-or Balance Assessment');
insert into task (task_date, task_id, task_name, description) values ('2023-07-06', 2, 'Buang Sampah', 'Bypass Left Atrium to Pulmonary Trunk with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-06', 3, 'Pilah Sampah', 'Dilation of Lingula Bronchus with Intraluminal Device, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2023-07-09', 1, 'Bakar Sampah', 'Drainage of Left Fallopian Tube, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-09', 2, 'Bakar Sampah', 'Dilation of Right Axillary Artery, Bifurcation, with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-09', 3, 'Bakar Sampah', 'Replacement of Right Lacrimal Bone with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-12', 1, 'Bakar Sampah', 'Release Aortic Body, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-12', 2, 'Bakar Sampah', 'Drainage of Right Femoral Shaft, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-12', 3, 'Buang Sampah', 'Plain Radiography of Cervico-Cerebral Arch using High Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2023-07-15', 1, 'Bakar Sampah', 'Reattachment of Right Diaphragm, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-15', 2, 'Bakar Sampah', 'Dilation of Superior Mesenteric Artery, Bifurcation, with Drug-eluting Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-15', 3, 'Bakar Sampah', 'Removal of Other Device from Lower Back, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-18', 1, 'Buang Sampah', 'Excision of Left Elbow Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-18', 2, 'Bakar Sampah', 'Dilation of Celiac Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-18', 3, 'Buang Sampah', 'Bypass Right Internal Iliac Artery to Right External Iliac Artery, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-21', 1, 'Bakar Sampah', 'Dilation of Left Anterior Tibial Artery, Bifurcation, with Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-21', 2, 'Buang Sampah', 'Repair Right Sublingual Gland, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-21', 3, 'Bakar Sampah', 'Replacement of Left Mandible with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-24', 1, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Vagina and Cul-de-sac, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-24', 2, 'Bakar Sampah', 'Replacement of Left Ureter with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-24', 3, 'Pilah Sampah', 'Occlusion of Left Vertebral Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-27', 1, 'Pilah Sampah', 'Extirpation of Matter from Lumbosacral Plexus, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-27', 2, 'Bakar Sampah', 'Excision of Left Occipital Bone, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-07-27', 3, 'Pilah Sampah', 'Inspection of Products of Conception, Ectopic, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-30', 1, 'Pilah Sampah', 'Excision of Right Adrenal Gland, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-07-30', 2, 'Pilah Sampah', 'Beam Radiation of Sternum using Electrons');
insert into task (task_date, task_id, task_name, description) values ('2023-07-30', 3, 'Bakar Sampah', 'Supplement Left Occipital Bone with Autologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-02', 1, 'Bakar Sampah', 'Removal of Internal Fixation Device from Left Thumb Phalanx, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-02', 2, 'Buang Sampah', 'Revision of Diaphragmatic Pacemaker Lead in Diaphragm, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-02', 3, 'Buang Sampah', 'Ultrasonography of Left Fallopian Tube using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2023-08-05', 1, 'Bakar Sampah', 'High Dose Rate (HDR) Brachytherapy of Uterus using Californium 252 (Cf-252)');
insert into task (task_date, task_id, task_name, description) values ('2023-08-05', 2, 'Pilah Sampah', 'Removal of Synthetic Substitute from Left Elbow Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-05', 3, 'Bakar Sampah', 'Supplement Papillary Muscle with Zooplastic Tissue, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-08', 1, 'Pilah Sampah', 'Restriction of Lingula Bronchus, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-08', 2, 'Pilah Sampah', 'Fusion of Left Hip Joint with Autologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-08', 3, 'Pilah Sampah', 'Drainage of Pelvic Region Subcutaneous Tissue and Fascia, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-11', 1, 'Bakar Sampah', 'Repair Left Upper Extremity Lymphatic, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-11', 2, 'Pilah Sampah', 'Drainage of Left Internal Carotid Artery, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-11', 3, 'Bakar Sampah', 'Revision of Autologous Tissue Substitute in Small Intestine, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-14', 1, 'Pilah Sampah', 'Revision of Internal Fixation Device in Cervical Vertebral Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-14', 2, 'Bakar Sampah', 'Revision of External Fixation Device in Right Metacarpocarpal Joint, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-14', 3, 'Pilah Sampah', 'Drainage of Anal Sphincter, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-08-17', 1, 'Bakar Sampah', 'Occlusion of Esophageal Vein with Extraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-17', 2, 'Pilah Sampah', 'Occlusion of Left Hand Vein, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-17', 3, 'Pilah Sampah', 'Supplement Right Nipple with Synthetic Substitute, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-20', 1, 'Buang Sampah', 'Plain Radiography of Lumbar Disc(s) using Other Contrast');
insert into task (task_date, task_id, task_name, description) values ('2023-08-20', 2, 'Buang Sampah', 'Monitoring of Venous Saturation, Central, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-20', 3, 'Bakar Sampah', 'Restriction of Ampulla of Vater with Intraluminal Device, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-08-23', 1, 'Buang Sampah', 'Bypass Abdominal Aorta to Celiac Artery with Autologous Venous Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-23', 2, 'Bakar Sampah', 'Reposition Upper Tooth, Multiple, with External Fixation Device, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-23', 3, 'Pilah Sampah', 'Revision of Feeding Device in Lower Intestinal Tract, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-26', 1, 'Buang Sampah', 'Drainage of Right Upper Femur, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-26', 2, 'Buang Sampah', 'Resection of Nose, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-26', 3, 'Pilah Sampah', 'Repair Thalamus, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-29', 1, 'Bakar Sampah', 'Computerized Tomography (CT Scan) of Nasopharynx-Oropharynx using Low Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2023-08-29', 2, 'Pilah Sampah', 'Excision of Left Trunk Muscle, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-08-29', 3, 'Buang Sampah', 'Replacement of Left Axillary Artery with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-01', 1, 'Bakar Sampah', 'Dilation of Right Common Iliac Artery, Bifurcation, with Drug-eluting Intraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-01', 2, 'Bakar Sampah', 'Bypass Left Popliteal Artery to Lower Extremity Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-01', 3, 'Bakar Sampah', 'Revision of Nonautologous Tissue Substitute in Nose, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-04', 1, 'Pilah Sampah', 'Insertion of Internal Fixation Device into Right Scapula, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-04', 2, 'Bakar Sampah', 'Fluoroscopy of Left Kidney');
insert into task (task_date, task_id, task_name, description) values ('2023-09-04', 3, 'Pilah Sampah', 'Fusion of Right Finger Phalangeal Joint with External Fixation Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-07', 1, 'Buang Sampah', 'Reposition Right Main Bronchus, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-07', 2, 'Buang Sampah', 'Change Drainage Device in Upper Bursa and Ligament, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-07', 3, 'Buang Sampah', 'Dilation of Intracranial Artery with Drug-eluting Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-10', 1, 'Buang Sampah', 'Removal of Drainage Device from Upper Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-10', 2, 'Buang Sampah', 'Beam Radiation of Skull using Photons 1 - 10 MeV');
insert into task (task_date, task_id, task_name, description) values ('2023-09-10', 3, 'Pilah Sampah', 'Bithermal, Binaural Caloric Irrigation Assessment using Vestibular - Balance Equipment');
insert into task (task_date, task_id, task_name, description) values ('2023-09-13', 1, 'Pilah Sampah', 'Revision of Nonautologous Tissue Substitute in Right Upper Extremity, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-13', 2, 'Pilah Sampah', 'Insertion of Infusion Device into Right Internal Carotid Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-13', 3, 'Pilah Sampah', 'Revision of Drainage Device in Pleura, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-09-16', 1, 'Bakar Sampah', 'Replacement of Left Knee Joint with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-16', 2, 'Buang Sampah', 'Removal of Monitoring Device from Diaphragm, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-16', 3, 'Buang Sampah', 'Removal of Drainage Device from Bone Marrow, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-19', 1, 'Bakar Sampah', 'Drainage of Right Knee Bursa and Ligament with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-19', 2, 'Buang Sampah', 'Extirpation of Matter from Optic Nerve, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-19', 3, 'Buang Sampah', 'Transfer Tibial Nerve to Peroneal Nerve, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-22', 1, 'Bakar Sampah', 'Ultrasonography of Inferior Mesenteric Artery, Intravascular');
insert into task (task_date, task_id, task_name, description) values ('2023-09-22', 2, 'Buang Sampah', 'Resection of Right Inguinal Lymphatic, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-22', 3, 'Buang Sampah', 'Reattachment of Left Shoulder Bursa and Ligament, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-25', 1, 'Bakar Sampah', 'Removal of Nonautologous Tissue Substitute from Epididymis and Spermatic Cord, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-09-25', 2, 'Buang Sampah', 'Excision of Bilateral Epididymis, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-25', 3, 'Pilah Sampah', 'Release Right Sphenoid Bone, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-28', 1, 'Buang Sampah', 'Drainage of Left Metatarsal, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-28', 2, 'Pilah Sampah', 'Monitoring of Central Nervous Electrical Activity, Intraoperative, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-09-28', 3, 'Bakar Sampah', 'Bypass Left Renal Vein to Lower Vein with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-01', 1, 'Bakar Sampah', 'Removal of Internal Fixation Device from Left Knee Joint, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-01', 2, 'Bakar Sampah', 'Transfer Right Upper Arm Subcutaneous Tissue and Fascia, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-01', 3, 'Buang Sampah', 'Environmental, Home and Work Barriers Assessment using Orthosis');
insert into task (task_date, task_id, task_name, description) values ('2023-10-04', 1, 'Pilah Sampah', 'Repair Right Metacarpocarpal Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-04', 2, 'Pilah Sampah', 'Extirpation of Matter from Nasopharynx, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-04', 3, 'Bakar Sampah', 'Supplement Right Inguinal Lymphatic with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-07', 1, 'Pilah Sampah', 'Removal of Synthetic Substitute from Skull, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-07', 2, 'Bakar Sampah', 'Reattachment of Chest Skin, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-07', 3, 'Pilah Sampah', 'Occlusion of Left Axillary Lymphatic with Extraluminal Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-10', 1, 'Pilah Sampah', 'Insertion of Spacer into Right Temporomandibular Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-10', 2, 'Bakar Sampah', 'Insertion of Infusion Device into Lymphatic, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-10', 3, 'Pilah Sampah', 'Excision of Gastric Vein, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-10-13', 1, 'Bakar Sampah', 'Excision of Bilateral Lungs, Via Natural or Artificial Opening Endoscopic, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-10-13', 2, 'Bakar Sampah', 'Supplement Head and Neck Bursa and Ligament with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-13', 3, 'Buang Sampah', 'Replacement of Accessory Pancreatic Duct with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-16', 1, 'Bakar Sampah', 'Revision of Monitoring Device in Heart, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-16', 2, 'Pilah Sampah', 'Occlusion of Mesenteric Lymphatic with Extraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-16', 3, 'Pilah Sampah', 'Drainage of Left Hepatic Duct, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2023-10-19', 1, 'Pilah Sampah', 'Repair Pancreatic Duct, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-10-19', 2, 'Buang Sampah', 'Bypass Left Internal Iliac Artery to Right Femoral Artery with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-19', 3, 'Bakar Sampah', 'Revision of Drainage Device in Cerebral Ventricle, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-22', 1, 'Pilah Sampah', 'Bypass Left Subclavian Artery to Right Lower Leg Artery with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-22', 2, 'Pilah Sampah', 'Drainage of Thymus with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-22', 3, 'Bakar Sampah', 'Dilation of Right Ulnar Artery with Three Drug-eluting Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-25', 1, 'Bakar Sampah', 'Excision of Left Clavicle, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-25', 2, 'Bakar Sampah', 'Inspection of Right Lower Leg, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-25', 3, 'Bakar Sampah', 'Computerized Tomography (CT Scan) of Left Forearm using Low Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2023-10-28', 1, 'Pilah Sampah', 'Fluoroscopy of Lumbar Arteries using High Osmolar Contrast');
insert into task (task_date, task_id, task_name, description) values ('2023-10-28', 2, 'Bakar Sampah', 'Reposition Left Femoral Shaft with Intramedullary Internal Fixation Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-28', 3, 'Buang Sampah', 'Drainage of Left Foot Artery with Drainage Device, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-31', 1, 'Buang Sampah', 'Bypass Left Ulnar Artery to Left Lower Arm Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-31', 2, 'Pilah Sampah', 'Dilation of Abdominal Aorta, Bifurcation, with Two Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-10-31', 3, 'Buang Sampah', 'Irrigation of Female Reproductive using Irrigating Substance, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-03', 1, 'Buang Sampah', 'Division of Right Upper Leg Tendon, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-03', 2, 'Pilah Sampah', 'Revision of Synthetic Substitute in Right Auditory Ossicle, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-03', 3, 'Bakar Sampah', 'Plain Radiography of Nasopharynx-Oropharynx');
insert into task (task_date, task_id, task_name, description) values ('2023-11-06', 1, 'Bakar Sampah', 'Drainage of Right Large Intestine, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-06', 2, 'Bakar Sampah', 'Destruction of Left Temporal Bone, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-06', 3, 'Pilah Sampah', 'Destruction of Left Lacrimal Gland, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-09', 1, 'Pilah Sampah', 'Revision of Other Device in Face, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-09', 2, 'Buang Sampah', 'Excision of Left Lower Leg Muscle, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-09', 3, 'Buang Sampah', 'Transfer Back Subcutaneous Tissue and Fascia, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-12', 1, 'Buang Sampah', 'Bypass Esophagus to Cutaneous with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-12', 2, 'Pilah Sampah', 'Removal of Synthetic Substitute from Right Patella, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-12', 3, 'Bakar Sampah', 'Insertion of Other Device into Genitourinary Tract, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-15', 1, 'Pilah Sampah', 'Extraction of Optic Nerve, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-15', 2, 'Buang Sampah', 'Bypass Right Atrium to Pulmonary Trunk with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-15', 3, 'Bakar Sampah', 'Inspection of Lower Back, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-18', 1, 'Pilah Sampah', 'Removal of Splint on Right Toe');
insert into task (task_date, task_id, task_name, description) values ('2023-11-18', 2, 'Buang Sampah', 'Revision of Infusion Device in Right Knee Joint, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-18', 3, 'Buang Sampah', 'Revision of Synthetic Substitute in Right Knee Joint, Patellar Surface, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-21', 1, 'Buang Sampah', 'Release Pudendal Nerve, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-21', 2, 'Bakar Sampah', 'Drainage of Face, Open Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-11-21', 3, 'Bakar Sampah', 'Supplement Left Metatarsal-Tarsal Joint with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-24', 1, 'Pilah Sampah', 'Supplement Ileum with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-24', 2, 'Buang Sampah', 'Extraction of Sciatic Nerve, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-24', 3, 'Pilah Sampah', 'Release Right Maxilla, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-27', 1, 'Buang Sampah', 'Bypass Left Pulmonary Artery from Carotid with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-27', 2, 'Bakar Sampah', 'Revision of Nonautologous Tissue Substitute in Bladder, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-27', 3, 'Bakar Sampah', 'Excision of Upper Back, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-30', 1, 'Pilah Sampah', 'Beam Radiation of Femur using Photons <1 MeV');
insert into task (task_date, task_id, task_name, description) values ('2023-11-30', 2, 'Buang Sampah', 'Occlusion of Right Internal Carotid Artery with Bioactive Intraluminal Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-11-30', 3, 'Bakar Sampah', 'Bypass Left Ureter to Right Ureter, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-03', 1, 'Buang Sampah', 'Insertion of Limb Lengthening External Fixation Device into Right Tibia, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-03', 2, 'Bakar Sampah', 'Introduction of Monoclonal Antibody into Nose, Via Natural or Artificial Opening');
insert into task (task_date, task_id, task_name, description) values ('2023-12-03', 3, 'Bakar Sampah', 'Repair Inferior Mesenteric Vein, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-06', 1, 'Pilah Sampah', 'Repair Right Hand, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-06', 2, 'Bakar Sampah', 'Dilation of Left Common Iliac Artery, Bifurcation, with Two Intraluminal Devices, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-06', 3, 'Bakar Sampah', 'Immobilization of Face using Wire');
insert into task (task_date, task_id, task_name, description) values ('2023-12-09', 1, 'Buang Sampah', 'Supplement Left Abdomen Tendon with Synthetic Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-09', 2, 'Pilah Sampah', 'Range of Motion and Joint Mobility Treatment of Integumentary System - Head and Neck using Orthosis');
insert into task (task_date, task_id, task_name, description) values ('2023-12-09', 3, 'Buang Sampah', 'Drainage of Right Hand Artery with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-12', 1, 'Pilah Sampah', 'Repair Optic Nerve, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-12', 2, 'Buang Sampah', 'Inspection of Lower Vein, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-12', 3, 'Buang Sampah', 'Excision of Left Hand Bursa and Ligament, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-15', 1, 'Buang Sampah', 'Extirpation of Matter from Left Foot Bursa and Ligament, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-15', 2, 'Bakar Sampah', 'Drainage of Right Trunk Bursa and Ligament with Drainage Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-15', 3, 'Buang Sampah', 'Reposition Right Humeral Head with Ring External Fixation Device, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-18', 1, 'Buang Sampah', 'Bypass Right Common Iliac Artery to Lower Extremity Artery with Autologous Arterial Tissue, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-18', 2, 'Pilah Sampah', 'Monitoring of Peripheral Nervous Conductivity, Sensory, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-18', 3, 'Bakar Sampah', 'Excision of Left Hip Tendon, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-21', 1, 'Pilah Sampah', 'Excision of Right Hand Subcutaneous Tissue and Fascia, Percutaneous Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2023-12-21', 2, 'Buang Sampah', 'Replacement of Cervicothoracic Vertebral Disc with Nonautologous Tissue Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-21', 3, 'Bakar Sampah', 'Extirpation of Matter from Right Lung, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-12-24', 1, 'Buang Sampah', 'Supplement of Left Upper Leg Subcutaneous Tissue and Fascia with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-24', 2, 'Pilah Sampah', 'Release Left Ethmoid Bone, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-24', 3, 'Pilah Sampah', 'Destruction of Left Breast, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-12-27', 1, 'Bakar Sampah', 'Fusion of Right Elbow Joint with External Fixation Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-27', 2, 'Buang Sampah', 'Replacement of Left Orbit with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-27', 3, 'Pilah Sampah', 'Reattachment of Left Lower Leg Tendon, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-30', 1, 'Pilah Sampah', 'Revision of Autologous Tissue Substitute in Uterus and Cervix, Via Natural or Artificial Opening Endoscopic');
insert into task (task_date, task_id, task_name, description) values ('2023-12-30', 2, 'Pilah Sampah', 'Dilation of Left Popliteal Artery, Bifurcation, with Two Intraluminal Devices, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2023-12-30', 3, 'Pilah Sampah', 'Dilation of Left Temporal Artery with Intraluminal Device, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-02', 1, 'Pilah Sampah', 'Supplement Right Wrist Joint with Nonautologous Tissue Substitute, Percutaneous Endoscopic Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-02', 2, 'Buang Sampah', 'Replacement of Left Hand Skin with Synthetic Substitute, Full Thickness, External Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-02', 3, 'Bakar Sampah', 'Insertion of Monitoring Device into Right Pulmonary Artery, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-05', 1, 'Bakar Sampah', 'Drainage of Right Lower Leg Tendon, Percutaneous Endoscopic Approach, Diagnostic');
insert into task (task_date, task_id, task_name, description) values ('2024-01-05', 2, 'Buang Sampah', 'Repair Adenoids, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-05', 3, 'Buang Sampah', 'Alteration of Abdominal Wall with Nonautologous Tissue Substitute, Percutaneous Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-08', 1, 'Bakar Sampah', 'Supplement Left Hand Vein with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-08', 2, 'Pilah Sampah', 'Revision of Spacer in Right Ankle Joint, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-08', 3, 'Pilah Sampah', 'Supplement Left Cephalic Vein with Synthetic Substitute, Open Approach');
insert into task (task_date, task_id, task_name, description) values ('2024-01-11', 1, 'Buang Sampah', 'Revision of Autologous Tissue Substitute in Left Humeral Head, External Approach');

insert into content (content_title, content_text) values ("Tentang SDG", "Sustainable Development Goal adalah program aksi\nyang dilakukan PBB untuk mengakhiri kemisikinan,\nmenjaga bumi, dan menjamin semua orang hidup\ndalam kedamaian dan kesejahteraan di tahun 2030.")