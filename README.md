## Mini-Project

### Title: Goodbooks
This project contains index, login, search and logout method. As name suggest index is a home page, login requires username and password which would query from Cassandra table running on different container, search works with a parameter "such as book name" and fetch first 20 titles and finally logout which shutdown the cluster.

#### API's: Goodreads [www.goodreads.com/api]
The Goodreads API allows developers access to Goodreads data in order to help websites or applications that deal with books. Most API methods will require you to register for a developer key. There is my personal key in the Goodbooks.py file. (only for assessment)
#### Technologies 
Python, 
Cassandra, 
Docker and
Amazon web services
#### Launch
This application has been designed to run on containers therefore be able to run it successufully blow steps must be fallowed.
First of all create an container with Cassandra table. The code has been provided in cassandra_code.txt.
Secondly, create another container for python file. (Goodbooks.py). In order to login successfully user need to enter username and password thus a set of credentials has provided username= sultan and password= cloud (hashed with md5 and salt).

