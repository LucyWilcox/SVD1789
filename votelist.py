import glob
import os

# house_2015_votes = []
# os.chdir("/home/lucy/SVD1789/house2015")
# for file in glob.glob("*.csv"):
# 	house_2015_votes.append(file)

# senate_2015_votes = []
# os.chdir("/home/lucy/SVD1789/senate2015")
# for file in glob.glob("*.csv"):
# 	senate_2015_votes.append(file)



house_2015_votes = ['congress_votes_114-2015_h155.csv', 'congress_votes_114-2015_h164.csv', 'congress_votes_114-2015_h147.csv', 'congress_votes_114-2015_h140.csv', 'congress_votes_114-2015_h142.csv', 'congress_votes_114-2015_h165.csv', 'congress_votes_114-2015_h148.csv', 'congress_votes_114-2015_h137.csv', 'congress_votes_114-2015_h150.csv', 'congress_votes_114-2015_h157.csv', 'congress_votes_114-2015_h160.csv', 'congress_votes_114-2015_h156.csv', 'congress_votes_114-2015_h144.csv', 'congress_votes_114-2015_h151.csv', 'congress_votes_114-2015_h161.csv', 'congress_votes_114-2015_h145.csv', 'congress_votes_114-2015_h146.csv', 'congress_votes_114-2015_h136.csv', 'congress_votes_114-2015_h167.csv', 'congress_votes_114-2015_h143.csv', 'congress_votes_114-2015_h168.csv', 'congress_votes_114-2015_h166.csv', 'congress_votes_114-2015_h159.csv', 'congress_votes_114-2015_h139.csv', 'congress_votes_114-2015_h138.csv', 'congress_votes_114-2015_h149.csv', 'congress_votes_114-2015_h154.csv', 'congress_votes_114-2015_h163.csv', 'congress_votes_114-2015_h158.csv', 'congress_votes_114-2015_h152.csv', 'congress_votes_114-2015_h169.csv', 'congress_votes_114-2015_h162.csv', 'congress_votes_114-2015_h141.csv', 'congress_votes_114-2015_h170.csv']
senate_2015_votes = ['congress_votes_114-2015_s84.csv', 'congress_votes_114-2015_s113.csv', 'congress_votes_114-2015_s121.csv', 'congress_votes_114-2015_s145.csv', 'congress_votes_114-2015_s85.csv', 'congress_votes_114-2015_s135.csv', 'congress_votes_114-2015_s90.csv', 'congress_votes_114-2015_s161.csv', 'congress_votes_114-2015_s127.csv', 'congress_votes_114-2015_s114.csv', 'congress_votes_114-2015_s103.csv', 'congress_votes_114-2015_s146.csv', 'congress_votes_114-2015_s111.csv', 'congress_votes_114-2015_s120.csv', 'congress_votes_114-2015_s117.csv', 'congress_votes_114-2015_s98.csv', 'congress_votes_114-2015_s94.csv', 'congress_votes_114-2015_s151.csv', 'congress_votes_114-2015_s159.csv', 'congress_votes_114-2015_s126.csv', 'congress_votes_114-2015_s107.csv', 'congress_votes_114-2015_s131.csv', 'congress_votes_114-2015_s142.csv', 'congress_votes_114-2015_s160.csv', 'congress_votes_114-2015_s104.csv', 'congress_votes_114-2015_s158.csv', 'congress_votes_114-2015_s156.csv', 'congress_votes_114-2015_s88.csv', 'congress_votes_114-2015_s123.csv', 'congress_votes_114-2015_s162.csv', 'congress_votes_114-2015_s149.csv', 'congress_votes_114-2015_s124.csv', 'congress_votes_114-2015_s157.csv', 'congress_votes_114-2015_s95.csv', 'congress_votes_114-2015_s144.csv', 'congress_votes_114-2015_s112.csv', 'congress_votes_114-2015_s154.csv', 'congress_votes_114-2015_s134.csv', 'congress_votes_114-2015_s153.csv', 'congress_votes_114-2015_s108.csv', 'congress_votes_114-2015_s89.csv', 'congress_votes_114-2015_s97.csv', 'congress_votes_114-2015_s101.csv', 'congress_votes_114-2015_s148.csv', 'congress_votes_114-2015_s82.csv', 'congress_votes_114-2015_s96.csv', 'congress_votes_114-2015_s93.csv', 'congress_votes_114-2015_s83.csv', 'congress_votes_114-2015_s116.csv', 'congress_votes_114-2015_s100.csv', 'congress_votes_114-2015_s110.csv', 'congress_votes_114-2015_s119.csv', 'congress_votes_114-2015_s150.csv', 'congress_votes_114-2015_s132.csv', 'congress_votes_114-2015_s133.csv', 'congress_votes_114-2015_s99.csv', 'congress_votes_114-2015_s163.csv', 'congress_votes_114-2015_s91.csv', 'congress_votes_114-2015_s87.csv', 'congress_votes_114-2015_s130.csv', 'congress_votes_114-2015_s115.csv', 'congress_votes_114-2015_s152.csv', 'congress_votes_114-2015_s128.csv', 'congress_votes_114-2015_s118.csv', 'congress_votes_114-2015_s122.csv', 'congress_votes_114-2015_s105.csv', 'congress_votes_114-2015_s106.csv', 'congress_votes_114-2015_s109.csv', 'congress_votes_114-2015_s147.csv', 'congress_votes_114-2015_s143.csv', 'congress_votes_114-2015_s129.csv', 'congress_votes_114-2015_s155.csv', 'congress_votes_114-2015_s81.csv', 'congress_votes_114-2015_s86.csv', 'congress_votes_114-2015_s125.csv', 'congress_votes_114-2015_s102.csv', 'congress_votes_114-2015_s92.csv']


house_votes = ['congress_votes_1-1_h35.csv', 'congress_votes_1-1_h33.csv', 'congress_votes_1-1_h34.csv', 'congress_votes_1-1_h32.csv', 'congress_votes_1-1_h31.csv', 'congress_votes_1-1_h30.csv', 'congress_votes_1-1_h29.csv', 'congress_votes_1-1_h28.csv', 'congress_votes_1-1_h27.csv', 'congress_votes_1-1_h26.csv', 'congress_votes_1-1_h25.csv', 'congress_votes_1-1_h24.csv', 'congress_votes_1-1_h16.csv', 'congress_votes_1-1_h21.csv', 'congress_votes_1-1_h20.csv', 'congress_votes_1-1_h14.csv', 'congress_votes_1-1_h23.csv', 'congress_votes_1-1_h17.csv', 'congress_votes_1-1_h22.csv', 'congress_votes_1-1_h18.csv', 'congress_votes_1-1_h19.csv', 'congress_votes_1-1_h15.csv', 'congress_votes_1-1_h13.csv', 'congress_votes_1-1_h8.csv', 'congress_votes_1-1_h9.csv', 'congress_votes_1-1_h11.csv', 'congress_votes_1-1_h10.csv', 'congress_votes_1-1_h12.csv', 'congress_votes_1-1_h7.csv', 'congress_votes_1-1_h32.csv', 'congress_votes_1-1_h6.csv', 'congress_votes_1-1_h5.csv', 'congress_votes_1-1_h4.csv', 'congress_votes_1-1_h3.csv', 'congress_votes_1-1_h2.csv', 'congress_votes_1-1_h1.csv']
senate_votes = ['congress_votes_1-1_s21.csv', 'congress_votes_1-1_s20.csv', 'congress_votes_1-1_s17.csv', 'congress_votes_1-1_s19.csv', 'congress_votes_1-1_s18.csv', 'congress_votes_1-1_s16.csv', 'congress_votes_1-1_s15.csv', 'congress_votes_1-1_s14.csv', 'congress_votes_1-1_s10.csv', 'congress_votes_1-1_s8.csv', 'congress_votes_1-1_s11.csv', 'congress_votes_1-1_s12.csv', 'congress_votes_1-1_s13.csv', 'congress_votes_1-1_s9.csv', 'congress_votes_1-1_s7.csv', 'congress_votes_1-1_s6.csv', 'congress_votes_1-1_s1.csv', 'congress_votes_1-1_s2.csv', 'congress_votes_1-1_s3.csv', 'congress_votes_1-1_s5.csv', 'congress_votes_1-1_s4.csv']


house_voters = ['Abiel Foster', 'Abraham Baldwin', 'Aedanus Burke', 'Alexander White', 'Andrew Moore', 'Benjamin Bourne', 'Benjamin Contee', 'Benjamin Goodhue', 'Benjamin Huntington', 'Daniel Carroll', 'Daniel Hiester', 'Daniel Huger', 'Egbert Benson', 'Elbridge Gerry', 'Elias Boudinot', 'Fisher Ames', 'Frederick Muhlenberg', 'George Clymer', 'George Gale', 'George Leonard', 'George Mathews', 'George Partridge', 'George Thatcher', 'Henry Wynkoop', 'Hugh Williamson', 'Isaac Coles', 'James Jackson', 'James Madison', 'James Schureman', 'Jeremiah Van', 'Jeremiah Wadsworth', 'John Ashe', 'John Brown', 'John Hathorn', 'John Laurance', 'John Muhlenberg', 'John Page', 'John Sevier', 'John Steele', 'John Vining', 'Jonathan Grout', 'Jonathan Sturges', 'Jonathan Trumbull', 'Joshua Seney', 'Josiah Parker', 'Lambert Cadwalader', 'Michael Stone', 'Nicholas Gilman', 'Peter Silvester', 'Richard Lee', 'Roger Sherman', 'Samuel Griffin', 'Samuel Livermore', 'Theodore Sedgwick', 'Theodorick Bland', 'Thomas Fitzsimons', 'Thomas Hartley', 'Thomas Scott', 'Thomas Sinnickson', 'Thomas Sumter', 'Thomas Tucker', 'Timothy Bloodworth', 'William Floyd', 'William Smith']
senate_voters = ['Caleb Strong', 'Charles \xe2\x80\x9cof', 'George Read', 'James Gunn', 'John Henry', 'John Langdon', 'Jonathan Elmer', 'Oliver Ellsworth', 'Paine Wingate', 'Philip Schuyler','Pierce Butler', 'Ralph Izard', 'Richard Bassett', 'Richard Lee', 'Robert Morris', 'Rufus King','Tristram Dalton', 'William Few', 'William Grayson', 'William Johnson', 'William Maclay', 'William Paterson']

house_2015_voters = ['Ken Calvert', 'Sean Duffy', 'Robert Aderholt', 'Randy Neugebauer', 'Tim Ryan', 'Todd Rokita', 'Joaquin Castro', 'Peter Visclosky', 'Ron Kind', 'Mike Quigley', 'Rodney Davis', 'Ed Whitfield', 'Roger Williams', 'Karen Bass', 'Mark Amodei', 'Julia Brownley', 'Dennis Ross', 'Brenda Lawrence', 'Lacy Clay', 'Loretta Sanchez', 'Louise Slaughter', 'Carolyn Maloney', 'Thomas Massie', 'Tom Graves', 'David Jolly', 'Frank Pallone', "Beto O'Rourke", 'Brendan Boyle', 'Mo Brooks', 'Tim Walberg', 'David Scott', 'Dana Rohrabacher', 'Mario Diaz-Balart', 'John Yarmuth', 'Theodore Deutch', 'James \xe2\x80\x9cJim\xe2\x80\x9d', 'Marsha Blackburn', 'Al Green', 'Zoe Lofgren', 'Michael Fitzpatrick', 'Juan Vargas', 'Marshall \xe2\x80\x9cMark\xe2\x80\x9d', 'Jerrold Nadler', 'Lynn Westmoreland', 'Duncan Hunter', 'Luke Messer', 'Henry Cuellar', 'David Young', 'Collin Peterson', 'Marc Veasey', 'Jackie Walorski', 'Tom MacArthur', 'Adam Kinzinger', 'Gerald Connolly', 'Daniel Lipinski', 'Brad Ashford', 'Brian Higgins', 'Lois Capps', 'Rick Allen', 'John Carter', 'Paul Tonko', 'Jeff Fortenberry', 'Alcee Hastings', 'Jaime Herrera', 'Garret Graves', 'Mike Thompson', 'Tom Cole', 'Tammy Duckworth', 'Michael Burgess', 'Tom Price', 'Richard Hudson', 'Marcy Kaptur', 'Paul Ryan', 'Jerry McNerney', 'Kathleen Rice', 'Dan Newhouse', 'Trent Franks', 'Jeb Hensarling', 'Steny Hoyer', 'Jim Bridenstine', 'Nita Lowey', 'Katherine Clark', 'Bob Goodlatte', 'Cathy McMorris', 'Elise Stefanik', 'Blake Farenthold', 'David Valadao', 'Louie Gohmert', 'Alan Lowenthal', 'Ami Bera', 'Martha McSally', 'Mike Rogers', 'Glenn Thompson', 'Brad Wenstrup', 'Patrick Murphy', 'Anna Eshoo', 'Michelle Lujan', 'John Kline', 'Steve Russell', 'Vicky Hartzler', 'Yvette Clarke', 'Sean Maloney', 'Tim Huelskamp', 'Chris Collins', 'David Schweikert', 'Doris Matsui', 'Danny Davis', 'Kenny Marchant', 'Charles \xe2\x80\x9cChuck\xe2\x80\x9d', 'Ken Buck', 'Adrian Smith', 'Robert Hurt', 'Jody Hice', 'Tom Emmer', 'Bill Posey', 'Darrell Issa', 'Michael Capuano', 'Mark DeSaulnier', 'Eliot Engel', 'Bob Dold', 'Scott DesJarlais', 'Diane Black', 'Jim Jordan', 'Donna Edwards', 'Peter Roskam', 'Joe Courtney', 'Suzanne Bonamici', 'William Keating', 'Betty McCollum', 'John Conyers', 'Will Hurd', 'Steve Cohen', 'Marcia Fudge', 'Virginia Foxx', 'Kathy Castor', 'Robert Brady', 'Mick Mulvaney', 'Andr\xc3\xa9 Carson', 'Adam Smith', 'Chris Van', 'Todd Young', 'Michael Conaway', 'Janice \xe2\x80\x9cJan\xe2\x80\x9d', 'Robin Kelly', 'Randy Forbes', 'John Fleming', 'Jason Smith', 'Garland \xe2\x80\x9cAndy\xe2\x80\x9d', 'Blaine Luetkemeyer', 'Chaka Fattah', 'Peter \xe2\x80\x9cPete\xe2\x80\x9d', 'Corrine Brown', 'Gwen Graham', 'Sander Levin', 'Frank LoBiondo', 'Mike Kelly', 'Ted Poe', 'Xavier Becerra', 'Ron DeSantis', 'John Katko', 'Mike Coffman', 'Tulsi Gabbard', 'Niki Tsongas', 'Daniel Webster', 'Rob Woodall', 'Nydia Vel\xc3\xa1zquez', 'Steve Israel', 'John Larson', 'Randy Hultgren', 'Billy Long', 'Bonnie Watson', 'Devin Nunes', 'Filemon Vela', 'Donald Norcross', 'Justin Amash', 'Bradley Walker', 'Robert \xe2\x80\x9cBobby\xe2\x80\x9d', 'Kyrsten Sinema', 'Kevin Brady', 'James Sensenbrenner', 'Tom Rice', 'Seth Moulton', 'Richard Nugent', 'Thomas Rooney', 'French Hill', 'Adam Schiff', 'Steven Palazzo', 'Lamar Smith', 'David \xe2\x80\x9cPhil\xe2\x80\x9d', 'Frank Lucas', 'Brett Guthrie', 'John Shimkus', 'Alma Adams', 'Tony C\xc3\xa1rdenas', 'Matthew Cartwright', 'Edward \xe2\x80\x9cEd\xe2\x80\x9d', 'Lynn Jenkins', 'Carlos Curbelo', 'Trey Gowdy', 'Barry Loudermilk', 'Cedric Richmond', 'Michael McCaul', 'Hakeem Jeffries', 'Michael Turner', 'Patrick McHenry', 'Peter Welch', 'Edward \xe2\x80\x9cScott\xe2\x80\x9d', 'Terri Sewell', 'Janice Hahn', 'Stephen Fincher', 'Joyce Beatty', 'Scott Peters', 'Judy Chu', 'Ander Crenshaw', 'Glenn Grothman', 'Sheila Jackson', 'Elizabeth Esty', 'Donald Payne', 'Emanuel Cleaver', 'Rodney Frelinghuysen', 'Gus Bilirakis', 'Kristi Noem', 'Ra\xc3\xbal Labrador', 'John Garamendi', 'Derek Kilmer', 'Martha Roby', 'Debbie Wasserman', 'James Himes', 'Charles Dent', 'Gwen Moore', 'Mike Pompeo', 'Pete Olson', 'Alex Mooney', 'Ann Kuster', 'David Price', 'Jeff Duncan', 'Stephen Lynch', 'Joseph Heck', 'Timothy Walz', 'Bradley Byrne', 'Tom Reed', 'Mark Takano', 'Tom McClintock', 'Keith Ellison', 'John Delaney', 'Erik Paulsen', 'Brian Babin', 'Walter Jones', 'Steve Knight', 'Rub\xc3\xa9n Hinojosa', 'Rick Larsen', 'Grace Meng', 'Nancy Pelosi', 'Ed Perlmutter', 'Bill Flores', 'Dina Titus', 'Susan Brooks', 'Maxine Waters', 'Bill Johnson', 'David Loebsack', 'Doug Lamborn', 'Charles \xe2\x80\x9cCharlie\xe2\x80\x9d', 'Pete Aguilar', 'Austin Scott', 'Brad Sherman', 'John Culberson', 'Jared Huffman', 'Gary Palmer', 'Ryan Costello', 'Harold \xe2\x80\x9cHal\xe2\x80\x9d', 'Lou Barletta', 'John Sarbanes', 'Kurt Schrader', 'Ted Yoho', 'Cheri Bustos', 'Ralph Abraham', 'Scott Perry', 'Luis Guti\xc3\xa9rrez', 'Keith Rothfus', 'Morgan Griffith', 'Bill Pascrell', 'Richard Neal', 'Joe Wilson', 'Don Young', 'Christopher Gibson', 'David \xe2\x80\x9cDave\xe2\x80\x9d', 'Jackie Speier', 'Marlin Stutzman', 'Michael \xe2\x80\x9cMike\xe2\x80\x9d', 'Scott Garrett', 'Jos\xc3\xa9 Serrano', 'Earl Blumenauer', 'Bill Shuster', 'Jared Polis', 'Ann Wagner', 'Joseph Pitts', 'Norma Torres', 'Henry \xe2\x80\x9cHank\xe2\x80\x9d', 'Leonard Lance', 'Tom Marino', 'Ileana Ros-Lehtinen', 'George \xe2\x80\x9cG.K.\xe2\x80\x9d', 'Buddy Carter', 'Jim Cooper', 'Debbie Dingell', 'Jeff Miller', 'Joseph Crowley', 'Lucille Roybal-Allard', 'Kevin Yoder', 'Barbara Comstock', 'John Ratcliffe', 'Donald Beyer', 'Larry Bucshon', 'John \xe2\x80\x9cJimmy\xe2\x80\x9d', 'Pete Sessions', 'Mia Love', 'Joseph Kennedy', 'Jim Costa', 'Jim McDermott', 'John Moolenaar', 'Peter DeFazio', 'Bobby Rush', 'Doug Collins', 'Markwayne Mullin', 'John Mica', 'Daniel Kildee', 'Evan Jenkins', 'Denny Heck', 'Cresent Hardy', 'Richard Hanna', 'Randy Weber', 'Frank Guinta', 'Bill Foster', 'Mac Thornberry', 'Elijah Cummings', 'John Lewis', 'David Joyce', 'Bruce Poliquin', 'Tim Murphy', 'Dan Benishek', 'Frederica Wilson', 'Paul Cook', 'Steve Scalise', 'Curtis \xe2\x80\x9cCurt\xe2\x80\x9d', 'Robert Wittman', 'Matt Salmon', 'Steve Chabot', 'Robert Latta', 'Steve Stivers', 'Gene Green', 'Susan Davis', 'Barbara Lee', 'Gregory Meeks', 'Albio Sires', 'Jeff Denham', 'Mark Pocan', 'Sanford Bishop', 'Raul Ruiz', 'Patrick Meehan', 'Mark Meadows', 'Rosa DeLauro', 'Kay Granger', 'Greg Walden', 'Mimi Walters', 'Reid Ribble', 'Ann Kirkpatrick', 'Rob Bishop', 'Candice Miller', 'Patrick \xe2\x80\x9cPat\xe2\x80\x9d', 'Bob Gibbs', 'Bill Huizenga', 'Rod Blum', 'Vern Buchanan', 'Ryan Zinke', 'Suzan DelBene', 'Diana DeGette', 'Linda S\xc3\xa1nchez', 'Steve King', 'James Renacci', 'Charles Boustany', 'Kevin McCarthy', 'Sam Farr', 'Bennie Thompson', 'Mike Bost', 'Cynthia Lummis', 'Bruce Westerman', 'Kevin Cramer', 'Robert Pittenger', 'David McKinley', 'Stevan \xe2\x80\x9cSteve\xe2\x80\x9d', 'Fred Upton', 'Eric Swalwell', 'Chris Stewart', 'David Cicilline', 'Ruben Gallego', 'Ben Luj\xc3\xa1n', 'Andy Harris', 'A. Dutch', 'David Reichert', 'Eddie Johnson', 'Lois Frankel', 'Eric \xe2\x80\x9cRick\xe2\x80\x9d', 'Lee Zeldin', 'Ted Lieu', 'Richard Nolan', 'Scott Tipton', 'Steve Womack', 'Sam Graves', 'Dave Trott', 'John Carney', 'Grace Napolitano', 'Chellie Pingree', 'Ra\xc3\xbal Grijalva', 'Jason Chaffetz', 'Christopher \xe2\x80\x9cChris\xe2\x80\x9d', 'Sam Johnson', 'Joe Barton', 'David Rouzer', 'Alan Grayson', 'Renee Ellmers', 'George Holding', 'Doug LaMalfa', 'Gregg Harper', 'Mike Bishop', 'Mark Takai', 'Paul Gosar', 'Lloyd Doggett']
senate_2015_voters =['Jeff Merkley', 'Kelly Ayotte', 'Lisa Murkowski', 'Jon Tester', 'Sheldon Whitehouse', 'Amy Klobuchar', 'John McCain', 'Shelley Capito', 'Robert \xe2\x80\x9cBob\xe2\x80\x9d', 'Tom Cotton', 'Thomas Carper', 'Orrin Hatch', 'Michael Crapo', 'Mazie Hirono', 'Christopher Murphy', 'Dan Sullivan', 'Benjamin Sasse', 'Tammy Baldwin', 'Richard Durbin', 'Joe Donnelly', 'Debbie Stabenow', 'Susan Collins', 'Deb Fischer', 'Steve Daines', 'Richard Burr', 'Kirsten Gillibrand', 'John Hoeven', 'Jeff Flake', 'Lamar Alexander', 'Mike Rounds', 'Chris Coons', 'Jeanne Shaheen', 'James \xe2\x80\x9cJim\xe2\x80\x9d', 'Bill Cassidy', 'Bernard \xe2\x80\x9cBernie\xe2\x80\x9d', 'Patrick Leahy', 'Elizabeth Warren', 'John Boozman', 'David Vitter', 'Dean Heller', 'Thad Cochran', 'Pat Roberts', 'Patrick \xe2\x80\x9cPat\xe2\x80\x9d', 'Barbara Mikulski', 'Lindsey Graham', 'Cory Booker', 'Ron Johnson', 'Cory Gardner', 'Sherrod Brown', 'Patty Murray', 'Ron Wyden', 'Claire McCaskill', 'Jerry Moran', 'Maria Cantwell', 'John \xe2\x80\x9cJack\xe2\x80\x9d', 'John Barrasso', 'Mark Warner', 'Thom Tillis', 'Roger Wicker', 'Daniel Coats', 'Benjamin Cardin', 'Ted Cruz', 'Robert \xe2\x80\x9cRob\xe2\x80\x9d', 'Bob Corker', 'Richard Shelby', 'Roy Blunt', 'Alan \xe2\x80\x9cAl\xe2\x80\x9d', 'Harry Reid', 'Bill Nelson', 'Dianne Feinstein', 'Gary Peters', 'Edward \xe2\x80\x9cEd\xe2\x80\x9d', 'John Cornyn', 'Joni Ernst', 'Jefferson \xe2\x80\x9cJeff\xe2\x80\x9d', 'John \xe2\x80\x9cJohnny\xe2\x80\x9d', 'Rand Paul', 'Mark Kirk', 'Timothy Kaine', 'Tim Scott', 'John Thune', 'Mike Lee', 'Michael Enzi', 'Marco Rubio', 'Joe Manchin', 'Mitch McConnell', 'Martin Heinrich', 'Michael Bennet', 'Barbara Boxer', 'David Perdue', 'Angus King', 'Heidi Heitkamp', 'Charles \xe2\x80\x9cChuck\xe2\x80\x9d', 'James Lankford', 'James Risch', 'Richard Blumenthal', 'Brian Schatz', 'Tom Udall']