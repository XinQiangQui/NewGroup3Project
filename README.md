# NewGroup3Project
TA scheduling app

Each year the computer science department hires graduate students as TAs to help teach its courses. Some courses have many lab sections to which the TAs must be assigned. All TAs should have contact information and, if appropriate for their role, office hours. The department secretary and other administrators need to have access to this information to update the schedule of classes, and also during the semester to contact the TA.

Currently, TAs fill out a paper form with their contact information when they are hired. This information is often out of date for TAs who have been at UWM for several years. Each semester the department chair assigns TAs to courses via email. Instructors of those courses work out who is handling each lab section, then email lab section assignments to the department secretary. Finally the department secretary enters lab instructor information into the schedule of classes.

We would like to replace this ad hoc system with a web application written in Python. The users of the application will have 3 roles:

Supervisor/Administrator (department chair)
create courses
create accounts
delete accounts
edit accounts
send out notifications to users via UWM email
access all data in the system
assign instructors to courses
assign TAs to courses (usually specifying number of labs, or grader status)
assign TAs to particular lab sections
Instructor
edit their own contact information (not course assignments)
view course assignments
view TA assignments (for all TAs)
send out notifications to their TAs via UWM email
assign their TAs to particular lab sections
read public contact information of all users
TA
edit their own contact information (not course assignments)
view TA assignments (for all TAs)
read public contact information of all users
Public information: the personal phone number or home address of a TA or instructor is private information. The administrator and supervisor need to have access to it, but it is not available to other users.
