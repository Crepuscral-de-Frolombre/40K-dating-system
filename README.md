## 40K-dating-system
A python program converting gregorian dates into imperial ones (from warhammer 40K) and the other way.

#For the ones unfamiliar with warhammer 40 000 or the imperial dating system:
imperial dates are a special format of dates made to be able to tell the moment of the year, whenever you are: space, earth, mars, proxima centauri, cadia...

It consist of 3 part: reference, year and year fraction.

The two first are very simple, it's the last one that get complicated.
reference say how confident your date is. 0 or 1 mean the event was on Earth and 9 mean that you clearly don't know for sure if it's 2022 or 1987.
The year is not like a regular year. It's divided between the millenium and the year of that millenium. 
For exemple, 2022 is 022.M3 because it's the 22th year of the 3nd millenium.

The most complicated part is the year fraction. 
Let's say that you're on a planet that take 2 earth year to make full revolution, and 1 year on this planet is divided between 27 seasons and 46 months.
How can you tell, on a Earthling perspective, that today is the middle of the year of that planet ?
Well don't worry, the year fraction is here for you.
It's a number between 000 and 999 that tell you were in the year you are.

How do we calculate this thing?
You will need the month, day and hour of the date. Let's say were the 06 may 2022 at 15 h 26 (don't use the american date for the calculations).
First you take the month: may, and turn it into days. For 2022, the 1st of may is 31 + 28 + 31 + 30 = 120 days apart from the 1st day of the year.
Secondly you add the days of the current month to the number: 120 + 06 = 126.
Then you turn that into hours: 126 * 26 = 3024 hours.
To that you add the current hour: 3024 + 15 = 3039.
  If you're a psycho like me and like perfection, you can put the minutes and seconds to that: minute / 60 and second / 6000.
  By doing so, minutes will be 2 number after the decimal and second 4 number after the decimal. And also turned into hundredth: 0-60 -> 0-100
Then you multiply this thing by 0.11407955 : 3039 * 0,11407955 = 346,6877
You take the integer of that: 346,... -> 346
And voilà ! You have a imperial year fraction.

So 06 may 2022 at 15 h 26 on Earth is 1346.022.M3
  the year fraction and the reference are glued together for whatever reasons, i'm not the one who made this shit.

Turning gregorian dates into imperial ones is a piece of cake, but the other way is much more complicated.
If you're a mathematician, you'll need to use a system with Gauss pivot or even use complex algebra you don't want to learn.
And for the lazy ones, you juste need to make multiple divisions.

However, this as a terrible problem: the hours is clearly not precise, and i don't talk about minutes and second.
For exemple: 06/05/2022 - 00 H 00 M 00 S -> 344
             06/05/2022 - 23 H 59 M 59 S -> 347
So basically, a day is 003 year fraction long. So it will be hard to find the right hour.

I tried it and failed miserably. So please help me improve my ugly code and then find a solution to this problem.
